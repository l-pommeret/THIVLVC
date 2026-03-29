#!/usr/bin/env python3
"""
Compare retrieval strategies for dependency tree similarity.
Evaluates TF-IDF, structural, and morphological retrievers on CIRCSE data.

Usage:
    python scripts/test_rag_strategies.py \
        --kb_file data/UD_Latin-CIRCSE/la_circse-ud-train.conllu \
        --test_file data/test.conllu
"""

import argparse
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.utils.conllu_utils import parse_conllu
from src.retrieval.retrievers import (
    TFIDFRetriever, StructuralRetriever, MorphologicalRetriever,
    get_sentence_text, get_pos_sequence, get_tree_depth
)


def strip_annotations(sentence):
    """Remove HEAD and DEPREL for fair retrieval testing."""
    stripped = []
    for item in sentence:
        if isinstance(item, str):
            stripped.append(item)
        else:
            token = list(item)
            token[6] = '_'
            token[7] = '_'
            stripped.append(token)
    return stripped


def evaluate_retrieval(retriever, test_sentences, kb_sentences, name, k=5):
    """Evaluate retrieval quality with length difference and POS overlap metrics."""
    print(f"\n{'=' * 60}")
    print(f"Evaluating: {name}")
    print(f"{'=' * 60}")

    length_diffs = []
    pos_overlaps = []

    for test_sent in test_sentences:
        stripped = strip_annotations(test_sent)
        results = retriever.retrieve(stripped, k=k)

        test_length = len(get_pos_sequence(test_sent))
        test_pos = set(get_pos_sequence(test_sent))

        for idx, score in results:
            retrieved = kb_sentences[idx]
            ret_length = len(get_pos_sequence(retrieved))
            ret_pos = set(get_pos_sequence(retrieved))

            length_diffs.append(abs(test_length - ret_length))
            overlap = len(test_pos & ret_pos) / len(test_pos | ret_pos) if test_pos | ret_pos else 0
            pos_overlaps.append(overlap)

    print(f"  Length Difference: {np.mean(length_diffs):.2f} +/- {np.std(length_diffs):.2f}")
    print(f"  POS Overlap:      {np.mean(pos_overlaps):.4f} +/- {np.std(pos_overlaps):.4f}")

    return {
        'name': name,
        'avg_length_diff': float(np.mean(length_diffs)),
        'std_length_diff': float(np.std(length_diffs)),
        'avg_pos_overlap': float(np.mean(pos_overlaps)),
        'std_pos_overlap': float(np.std(pos_overlaps)),
    }


def main():
    parser = argparse.ArgumentParser(description="Compare RAG strategies")
    parser.add_argument("--kb_file", default="data/UD_Latin-CIRCSE/la_circse-ud-train.conllu")
    parser.add_argument("--test_file", required=True)
    parser.add_argument("--max_test", type=int, default=None)
    parser.add_argument("--k", type=int, default=5)
    parser.add_argument("--output", default="outputs/rag_evaluation.json")
    args = parser.parse_args()

    kb = parse_conllu(args.kb_file)
    test = parse_conllu(args.test_file)
    if args.max_test:
        test = test[:args.max_test]

    print(f"KB: {len(kb)} sentences, Test: {len(test)} sentences")

    retrievers = {
        'TF-IDF': TFIDFRetriever(kb),
        'Structural': StructuralRetriever(kb),
        'Morphological': MorphologicalRetriever(kb),
    }

    results = []
    for name, ret in retrievers.items():
        r = evaluate_retrieval(ret, test, kb, name, k=args.k)
        results.append(r)

    print(f"\n{'=' * 70}")
    print(f"{'Strategy':<25} {'Length Diff':<20} {'POS Overlap':<20}")
    print(f"{'-' * 70}")
    for r in results:
        print(f"{r['name']:<25} {r['avg_length_diff']:.2f} +/- {r['std_length_diff']:.2f}     "
              f"{r['avg_pos_overlap']:.4f} +/- {r['std_pos_overlap']:.4f}")

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
