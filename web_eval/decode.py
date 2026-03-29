#!/usr/bin/env python3
"""
Décode les annotations aveugles (A/B) en gold/ia.
Gère plusieurs formats d'export :
  - Format serveur : {practice: [...], evaluation: [...]}
  - Format localStorage brut : {eval2_responses: "...", eval2_practice_responses: "..."}
  - Ancien format (winner déjà en gold/ia)
  - Nouveau format (winner en a/b, à décoder avec la clé)

Usage:
    python3 decode.py annotateur1.json
    python3 decode.py annotateur1.json annotateur2.json
"""

import json
import sys
import argparse
from collections import Counter


def get_ab_assignment(flat_idx):
    """Même hash que le JavaScript : ((flatIdx * 2654435761) >>> 0) % 2 === 0"""
    h = ((flat_idx * 2654435761) & 0xFFFFFFFF) % 2
    return h == 0  # True = gold est A


def decode_winner(winner, is_gold_a):
    """Convertit 'a'/'b' en 'gold'/'ia'."""
    if winner == 'a':
        return 'gold' if is_gold_a else 'ia'
    elif winner == 'b':
        return 'ia' if is_gold_a else 'gold'
    else:
        return winner


def load_file(path):
    """Charge un fichier d'annotations, gère tous les formats."""
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    # Format localStorage brut (clés eval2_*)
    if isinstance(data, dict) and 'eval2_responses' in data:
        responses = json.loads(data['eval2_responses']) if isinstance(data['eval2_responses'], str) else data['eval2_responses']
        practice = json.loads(data['eval2_practice_responses']) if isinstance(data.get('eval2_practice_responses', '[]'), str) else data.get('eval2_practice_responses', [])
        return practice, responses

    # Format serveur {practice, evaluation}
    if isinstance(data, dict) and 'evaluation' in data:
        return data.get('practice', []), data.get('evaluation', [])

    # Format liste simple
    if isinstance(data, list):
        return [], data

    return [], []


def decode_responses(responses):
    """Décode une liste de réponses. Détecte automatiquement le format."""
    decoded = []
    for r in responses:
        flat_idx = r['flatIdx']
        winner = r.get('winner', '')

        # Ancien format : winner déjà en gold/ia → pas besoin de décoder
        if winner in ('gold', 'ia', 'both_wrong', 'undecidable', 'dunno'):
            decoded.append({
                **r,
                'winner_decoded': winner,
                'gold_was': '(ancien format)',
            })
        # Nouveau format : winner en a/b → décoder avec la clé
        elif winner in ('a', 'b'):
            is_gold_a = get_ab_assignment(flat_idx)
            decoded.append({
                **r,
                'winner_decoded': decode_winner(winner, is_gold_a),
                'gold_was': 'A' if is_gold_a else 'B',
            })
        else:
            decoded.append({**r, 'winner_decoded': winner, 'gold_was': '?'})

    return decoded


def compute_stats(decoded):
    total = len(decoded)
    if total == 0:
        return None
    return {
        'total': total,
        'gold_wins': sum(1 for r in decoded if r['winner_decoded'] == 'gold'),
        'ia_wins': sum(1 for r in decoded if r['winner_decoded'] == 'ia'),
        'both_wrong': sum(1 for r in decoded if r['winner_decoded'] == 'both_wrong'),
        'undecidable': sum(1 for r in decoded if r['winner_decoded'] == 'undecidable'),
        'dunno': sum(1 for r in decoded if r['winner_decoded'] == 'dunno'),
    }


def print_stats(stats, label=""):
    if not stats:
        print(f"  {label}: aucune réponse")
        return
    t = stats['total']
    if label:
        print(f"\n  --- {label} ({t} annotations) ---")
    print(f"  Gold (humain) :  {stats['gold_wins']:4d}  ({stats['gold_wins']/t*100:.1f}%)")
    print(f"  IA            :  {stats['ia_wins']:4d}  ({stats['ia_wins']/t*100:.1f}%)")
    print(f"  Les deux tort :  {stats['both_wrong']:4d}  ({stats['both_wrong']/t*100:.1f}%)")
    print(f"  Indécidable   :  {stats['undecidable']:4d}  ({stats['undecidable']/t*100:.1f}%)")
    print(f"  Je ne sais pas:  {stats['dunno']:4d}  ({stats['dunno']/t*100:.1f}%)")


def print_coverage(decoded, label=""):
    """Affiche la couverture et les sauts."""
    idxs = sorted(r['flatIdx'] for r in decoded)
    if not idxs:
        return
    gaps = []
    for i in range(len(idxs) - 1):
        if idxs[i + 1] - idxs[i] > 1:
            gaps.append((idxs[i], idxs[i + 1], idxs[i + 1] - idxs[i] - 1))
    print(f"  Plage : {idxs[0]} → {idxs[-1]}")
    if gaps:
        print(f"  Sauts :")
        for start, end, size in gaps:
            print(f"    {start} → {end} ({size} items sautés)")


def decode_single(input_path, output_path=None):
    practice, responses = load_file(input_path)
    decoded_practice = decode_responses(practice)
    decoded = decode_responses(responses)

    print(f"\n{'='*48}")
    print(f"  RÉSULTATS DÉCODÉS")
    print(f"{'='*48}")

    if decoded_practice:
        stats_p = compute_stats(decoded_practice)
        print_stats(stats_p, "Entraînement")

    stats = compute_stats(decoded)
    print_stats(stats, "Évaluation")
    print()
    print_coverage(decoded, "Évaluation")
    print(f"{'='*48}\n")

    if output_path is None:
        output_path = input_path.replace('.json', '_decoded.json')

    result = {
        'stats': stats,
        'practice_stats': compute_stats(decoded_practice),
        'responses': decoded,
        'practice_responses': decoded_practice,
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  Sauvegardé : {output_path}")


def decode_multi(input_paths, output_path=None):
    all_decoded = {}
    all_stats = {}

    print(f"\n{'='*48}")
    print(f"  RÉSULTATS DÉCODÉS – {len(input_paths)} ANNOTATEURS")
    print(f"{'='*48}")

    for path in input_paths:
        name = path.rsplit('/', 1)[-1].replace('.json', '')
        _, responses = load_file(path)
        decoded = decode_responses(responses)
        all_decoded[name] = decoded
        stats = compute_stats(decoded)
        all_stats[name] = stats
        print_stats(stats, label=name)
        print_coverage(decoded)

    # Accord inter-annotateurs
    print(f"\n{'='*48}")
    print(f"  ACCORD INTER-ANNOTATEURS")
    print(f"{'='*48}")

    by_idx = {}
    for name, decoded in all_decoded.items():
        by_idx[name] = {r['flatIdx']: r['winner_decoded'] for r in decoded}

    names = list(all_decoded.keys())
    common_idxs = set.intersection(*(set(by_idx[n].keys()) for n in names))
    print(f"\n  Items annotés par tous : {len(common_idxs)}")

    if len(common_idxs) > 0 and len(names) >= 2:
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                n1, n2 = names[i], names[j]
                agree = sum(1 for idx in common_idxs
                            if by_idx[n1][idx] == by_idx[n2][idx])
                pct = agree / len(common_idxs) * 100
                print(f"  {n1} vs {n2} : {agree}/{len(common_idxs)} ({pct:.1f}%)")

        unanimous = sum(1 for idx in common_idxs
                        if len(set(by_idx[n][idx] for n in names)) == 1)
        pct = unanimous / len(common_idxs) * 100
        print(f"\n  Accord unanime : {unanimous}/{len(common_idxs)} ({pct:.1f}%)")

        # Détail des désaccords
        disagreements = []
        for idx in sorted(common_idxs):
            votes = {n: by_idx[n][idx] for n in names}
            if len(set(votes.values())) > 1:
                item = next(r for r in all_decoded[names[0]] if r['flatIdx'] == idx)
                disagreements.append({
                    'flatIdx': idx,
                    'word': item.get('word', '?'),
                    'bench': item.get('bench', '?'),
                    'votes': votes,
                })

        if disagreements:
            print(f"\n  --- Désaccords ({len(disagreements)}) ---")
            for d in disagreements[:30]:
                votes_str = ", ".join(f"{n}={v}" for n, v in d['votes'].items())
                print(f"    #{d['flatIdx']} [{d['bench']}] {d['word']}: {votes_str}")
            if len(disagreements) > 30:
                print(f"    ... et {len(disagreements) - 30} autres")

    print(f"\n{'='*48}\n")

    if output_path is None:
        output_path = 'resultats_combines.json'

    result = {
        'annotateurs': {name: {'stats': all_stats[name], 'responses': decoded}
                        for name, decoded in all_decoded.items()},
        'accord': {'items_communs': len(common_idxs)},
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  Sauvegardé : {output_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Décode les annotations aveugles EvaLatin 2026')
    parser.add_argument('input', nargs='+', help='Fichier(s) JSON des annotations')
    parser.add_argument('-o', '--output', help='Fichier de sortie')
    args = parser.parse_args()

    if len(args.input) == 1:
        decode_single(args.input[0], args.output)
    else:
        decode_multi(args.input, args.output)
