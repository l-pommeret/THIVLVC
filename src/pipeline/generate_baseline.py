"""
Generate UDPipe baseline parses via the Lindat API.
"""

import argparse
import time
import requests

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.conllu_utils import parse_conllu, format_conllu

API_URL = "http://lindat.mff.cuni.cz/services/udpipe/api/process"
DEFAULT_MODEL = "latin-circse-ud-2.17-251125"


def strip_annotations(sentence):
    """Keep only ID and FORM, clear other columns."""
    stripped = []
    for line in sentence:
        if isinstance(line, list):
            stripped.append([line[0], line[1]] + ["_"] * 8)
        else:
            stripped.append(line)
    return stripped


def parse_conllu_string(text):
    """Parse CoNLL-U from a string."""
    sentences = []
    current = []
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            if current:
                sentences.append(current)
                current = []
            continue
        if line.startswith('#'):
            current.append(line)
            continue
        fields = line.split('\t')
        if len(fields) == 10:
            current.append(fields)
    if current:
        sentences.append(current)
    return sentences


def generate_baseline(input_path, output_path, model=DEFAULT_MODEL):
    """Generate baseline parses for all sentences in input file."""
    print(f"Reading {input_path}...")
    sentences = parse_conllu(input_path)
    print(f"Generating baseline for {len(sentences)} sentences using {model}...")

    results = []
    chunk_size = 50

    for i in range(0, len(sentences), chunk_size):
        chunk = sentences[i:i + chunk_size]
        stripped = [strip_annotations(s) for s in chunk]
        chunk_text = "\n\n".join([format_conllu(s) for s in stripped])

        payload = {
            'model': model,
            'tagger': '',
            'parser': '',
            'data': chunk_text,
            'input': 'conllu'
        }

        for attempt in range(3):
            try:
                resp = requests.post(API_URL, data=payload)
                if resp.status_code == 429:
                    time.sleep(2 ** attempt)
                    continue
                resp.raise_for_status()
                parsed = parse_conllu_string(resp.json()['result'])
                results.extend(parsed)
                print(f"  Chunk {i // chunk_size + 1}/{len(sentences) // chunk_size + 1}")
                break
            except Exception as e:
                print(f"Error on chunk {i}: {e}")
                time.sleep(1)

    print(f"Writing {len(results)} sentences to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        for sent in results:
            f.write(format_conllu(sent) + "\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate UDPipe baseline parses")
    parser.add_argument("--input", required=True, help="Input CoNLL-U file")
    parser.add_argument("--output", required=True, help="Output CoNLL-U file")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="UDPipe model name")
    args = parser.parse_args()
    generate_baseline(args.input, args.output, args.model)
