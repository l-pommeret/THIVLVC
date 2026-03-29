#!/usr/bin/env python3
"""
Prepare evaluation data for blind gold vs IA comparison.
Reads gold and IA CoNLL-U files, finds disagreements, outputs JSON for web_eval.
"""

import json
import sys
from pathlib import Path
from collections import OrderedDict


def parse_conllu(filepath):
    """Parse a CoNLL-U file into a list of sentences.
    Each sentence is a dict with 'sent_id', 'text', 'conllu' (raw string), 'tokens' (list of dicts).
    """
    sentences = []
    current_lines = []
    current_meta = {}

    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("# sent_id"):
                current_meta["sent_id"] = line.split("=", 1)[1].strip()
                current_lines.append(line)
            elif line.startswith("# text"):
                current_meta["text"] = line.split("=", 1)[1].strip()
                current_lines.append(line)
            elif line.startswith("#"):
                current_lines.append(line)
            elif line.strip() == "":
                # End of sentence
                if current_lines and "sent_id" in current_meta:
                    tokens = []
                    conllu_str = "\n".join(current_lines)
                    for l in current_lines:
                        if l.startswith("#") or l.strip() == "":
                            continue
                        parts = l.split("\t")
                        if len(parts) >= 10:
                            # Skip multiword tokens (e.g., "1-2")
                            if "-" in parts[0] or "." in parts[0]:
                                continue
                            tokens.append({
                                "id": parts[0],
                                "form": parts[1],
                                "lemma": parts[2],
                                "upos": parts[3],
                                "xpos": parts[4],
                                "feats": parts[5],
                                "head": parts[6],
                                "deprel": parts[7],
                                "deps": parts[8],
                                "misc": parts[9],
                            })
                    sentences.append({
                        "sent_id": current_meta.get("sent_id", ""),
                        "text": current_meta.get("text", ""),
                        "conllu": conllu_str,
                        "tokens": tokens,
                    })
                current_lines = []
                current_meta = {}
            else:
                current_lines.append(line)

        # Handle last sentence if file doesn't end with blank line
        if current_lines and "sent_id" in current_meta:
            tokens = []
            conllu_str = "\n".join(current_lines)
            for l in current_lines:
                if l.startswith("#") or l.strip() == "":
                    continue
                parts = l.split("\t")
                if len(parts) >= 10:
                    if "-" in parts[0] or "." in parts[0]:
                        continue
                    tokens.append({
                        "id": parts[0],
                        "form": parts[1],
                        "lemma": parts[2],
                        "upos": parts[3],
                        "xpos": parts[4],
                        "feats": parts[5],
                        "head": parts[6],
                        "deprel": parts[7],
                        "deps": parts[8],
                        "misc": parts[9],
                    })
            sentences.append({
                "sent_id": current_meta.get("sent_id", ""),
                "text": current_meta.get("text", ""),
                "conllu": conllu_str,
                "tokens": tokens,
            })

    return sentences


def find_disagreements(gold_sent, ia_sent):
    """Compare two sentences token by token, return list of disagreements."""
    disagreements = []
    gold_tokens = {t["id"]: t for t in gold_sent["tokens"]}
    ia_tokens = {t["id"]: t for t in ia_sent["tokens"]}

    for token_id in gold_tokens:
        if token_id not in ia_tokens:
            continue
        gt = gold_tokens[token_id]
        it = ia_tokens[token_id]

        if gt["head"] != it["head"] or gt["deprel"] != it["deprel"]:
            disagreements.append({
                "token_id": token_id,
                "form": gt["form"],
                "gold": {"head": gt["head"], "deprel": gt["deprel"]},
                "ia": {"head": it["head"], "deprel": it["deprel"]},
            })

    return disagreements


def main():
    base = Path(__file__).parent.parent / "data" / "final"

    files = {
        "poetry": {
            "gold": base / "EvaLatin_2026_Syntactic_Parsing_test_data_gold" / "EvaLatin_2026_poetry_gold.conllu",
            "ia": base / "poetry_IA.conllu",
        },
        "prose": {
            "gold": base / "EvaLatin_2026_Syntactic_Parsing_test_data_gold" / "EvaLatin_2026_prose_gold.conllu",
            "ia": base / "prose_IA.conllu",
        },
    }

    result = OrderedDict()
    total_sentences = 0
    total_disagreements = 0

    for genre, paths in files.items():
        print(f"\n=== {genre.upper()} ===")
        gold_sents = parse_conllu(paths["gold"])
        ia_sents = parse_conllu(paths["ia"])

        print(f"  Gold sentences: {len(gold_sents)}")
        print(f"  IA sentences:   {len(ia_sents)}")

        # Index by sent_id
        gold_by_id = {s["sent_id"]: s for s in gold_sents}
        ia_by_id = {s["sent_id"]: s for s in ia_sents}

        genre_data = []
        genre_disagreements = 0

        for sent_id in gold_by_id:
            if sent_id not in ia_by_id:
                print(f"  WARNING: sent_id {sent_id} not in IA file, skipping")
                continue

            gold_sent = gold_by_id[sent_id]
            ia_sent = ia_by_id[sent_id]

            disagreements = find_disagreements(gold_sent, ia_sent)
            if not disagreements:
                continue

            genre_data.append({
                "sent_id": sent_id,
                "text": gold_sent["text"],
                "gold_conllu": gold_sent["conllu"],
                "ia_conllu": ia_sent["conllu"],
                "disagreements": disagreements,
            })
            genre_disagreements += len(disagreements)

        result[genre] = genre_data
        total_sentences += len(genre_data)
        total_disagreements += genre_disagreements
        print(f"  Sentences with disagreements: {len(genre_data)}")
        print(f"  Total disagreements: {genre_disagreements}")

    print(f"\n=== TOTAL ===")
    print(f"  Sentences with disagreements: {total_sentences}")
    print(f"  Total disagreements: {total_disagreements}")

    # Write output
    output_path = Path(__file__).parent / "data" / "eval_gold_vs_ia.json"
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\nOutput written to {output_path}")


if __name__ == "__main__":
    main()
