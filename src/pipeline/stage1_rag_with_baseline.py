"""
THIVLVC Stage 1: RAG-augmented LLM refinement of UDPipe baseline parses.

Given an input sentence, retrieves similar examples from the CIRCSE treebank,
then prompts an LLM to refine the baseline parse using the retrieved examples
and UD annotation guidelines.

Supports any model via OpenRouter, or local models via Ollama/vLLM.

Usage:
    # OpenRouter (any model)
    python stage1_rag_with_baseline.py --provider openrouter --model google/gemini-2.0-flash-001 ...

    # Local Ollama
    python stage1_rag_with_baseline.py --provider local --model qwen3:72b ...
"""

import argparse
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.conllu_utils import (
    parse_conllu, format_conllu, fix_cycles, fix_roots, clean_mwts, fix_mwt_heads
)
from utils.llm_client import LLMClient, extract_conllu
from retrieval.retrievers import StructuralRetriever


SYSTEM_PROMPT = (
    "You are the Latin Chief Annotator. "
    "Refine and improve the syntax (HEAD/DEPREL) of the Input Sentence using best practices."
)


def build_prompt(sentence, latinpipe_sent, examples, guidelines_text):
    """Build the refinement prompt."""
    conllu_str = format_conllu(sentence)
    latinpipe_str = format_conllu(latinpipe_sent) if latinpipe_sent else "N/A"

    example_str = ""
    for i, ex in enumerate(examples):
        example_str += f"--- Example {i + 1} ---\n{format_conllu(ex)}\n\n"

    prompt = ""
    if guidelines_text:
        prompt += f"=== OFFICIAL ANNOTATION GUIDELINES ===\n{guidelines_text}\n======================================\n\n"

    prompt += f"""Here are 5 SIMILAR examples from the training data.
{example_str}

--- BASELINE (from automatic parser) ---
{latinpipe_str}

--- Input Sentence ---
{conllu_str}

Task:
1. Compare the baseline parse with the examples and guidelines
2. Identify any improvements needed in HEAD/DEPREL
3. Output your refined version
4. If uncertain, add a comment line # needs_council = true

Output ONLY the CoNLL-U block for the Input Sentence (not the baseline)."""

    return prompt


def parse_response(text):
    """Parse CoNLL-U from LLM response text."""
    text = extract_conllu(text)
    new_sent = []
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('```'):
            continue
        if line.startswith('#'):
            new_sent.append(line)
            continue
        parts = line.split('\t')
        if len(parts) == 10:
            new_sent.append(parts)
    return new_sent


def refine_sentence(client, sentence, latinpipe_sent, examples, guidelines_text, idx):
    """Refine a single sentence using the LLM."""
    prompt = build_prompt(sentence, latinpipe_sent, examples, guidelines_text)

    try:
        response = client.complete(prompt, system=SYSTEM_PROMPT, temperature=0.0)
        new_sent = parse_response(response)

        if new_sent:
            new_sent = fix_cycles(new_sent)
            new_sent = fix_roots(new_sent)
            new_sent = clean_mwts(new_sent)
            new_sent = fix_mwt_heads(new_sent)
            print(f"  [{idx + 1}] Refined")
            return new_sent

        print(f"  [{idx + 1}] Empty response, keeping baseline")
        return latinpipe_sent if latinpipe_sent else sentence

    except Exception as e:
        print(f"  [{idx + 1}] Error: {e}, keeping baseline")
        return latinpipe_sent if latinpipe_sent else sentence


def main():
    parser = argparse.ArgumentParser(description="THIVLVC: RAG + LLM Refinement")
    parser.add_argument("--input_file", required=True, help="Input CoNLL-U file")
    parser.add_argument("--latinpipe_file", required=True, help="UDPipe baseline file")
    parser.add_argument("--kb_file", required=True, help="Knowledge base (CIRCSE train)")
    parser.add_argument("--output_file", required=True, help="Output file")
    parser.add_argument("--guidelines_file", default=None, help="UD guidelines file")
    parser.add_argument("--max_sentences", type=int, default=None)
    parser.add_argument("--concurrency", type=int, default=10)

    # LLM configuration
    parser.add_argument("--provider", default="openrouter",
                        choices=["openrouter", "local"],
                        help="LLM provider: openrouter (any model) or local (Ollama/vLLM)")
    parser.add_argument("--model", default=None,
                        help="Model ID (e.g. google/gemini-2.0-flash-001, qwen3:72b)")
    parser.add_argument("--base_url", default=None,
                        help="Override API endpoint (e.g. http://localhost:11434/v1)")

    args = parser.parse_args()

    # Load files
    print("Loading files...")
    input_sents = parse_conllu(args.input_file)
    latinpipe_sents = parse_conllu(args.latinpipe_file)
    print(f"  Input: {len(input_sents)} sentences")
    print(f"  Baseline: {len(latinpipe_sents)} sentences")

    if len(input_sents) != len(latinpipe_sents):
        print(f"  WARNING: sentence count mismatch ({len(input_sents)} vs {len(latinpipe_sents)})")

    guidelines_text = ""
    if args.guidelines_file and os.path.exists(args.guidelines_file):
        with open(args.guidelines_file) as f:
            guidelines_text = f.read()
        print(f"  Guidelines: {len(guidelines_text)} chars")

    if args.max_sentences:
        input_sents = input_sents[:args.max_sentences]
        latinpipe_sents = latinpipe_sents[:args.max_sentences]

    # Initialize retriever
    print(f"Loading knowledge base: {args.kb_file}")
    kb_sents = parse_conllu(args.kb_file)
    retriever = StructuralRetriever(kb_sents)
    print(f"  KB: {len(kb_sents)} sentences")

    # Initialize LLM client
    client = LLMClient(
        provider=args.provider,
        model=args.model,
        base_url=args.base_url,
    )
    print(f"  LLM: {client.provider} / {client.model}")

    # Process sentences with thread pool
    print(f"Processing {len(input_sents)} sentences (concurrency={args.concurrency})...")

    refined = [None] * len(input_sents)

    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = {}
        for idx, (inp, lp) in enumerate(zip(input_sents, latinpipe_sents)):
            results = retriever.retrieve(inp, k=5)
            examples = [kb_sents[r[0]] for r in results]
            fut = executor.submit(
                refine_sentence, client, inp, lp, examples, guidelines_text, idx
            )
            futures[fut] = idx

        for fut in as_completed(futures):
            idx = futures[fut]
            try:
                refined[idx] = fut.result()
            except Exception as e:
                print(f"  [{idx + 1}] Exception: {e}")
                refined[idx] = input_sents[idx]

    # Write output
    print(f"Writing {len(refined)} sentences to {args.output_file}...")
    os.makedirs(os.path.dirname(args.output_file) or '.', exist_ok=True)
    with open(args.output_file, 'w') as f:
        for sent in refined:
            for line in sent:
                if isinstance(line, str):
                    f.write(line + '\n')
                else:
                    f.write('\t'.join(line) + '\n')
            f.write('\n')

    # Print stats
    stats = client.get_stats()
    print(f"Done! {stats['requests']} API calls, "
          f"{stats['input_tokens']} input tokens, {stats['output_tokens']} output tokens")


if __name__ == "__main__":
    main()
