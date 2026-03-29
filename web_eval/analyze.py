#!/usr/bin/env python3
"""
Analyse taxonomique des accords inter-annotateurs.
Extrait les cas unanimes, classifie les erreurs Gold vs IA.

Usage:
    python3 web_eval/analyze.py web_eval/data/annotation_jules.json web_eval/data/annotations_thibault.json
"""

import json
import sys
import argparse
from collections import Counter


def get_ab_assignment(flat_idx):
    return ((flat_idx * 2654435761) & 0xFFFFFFFF) % 2 == 0


def decode_winner(winner, flat_idx):
    if winner in ('gold', 'ia', 'both_wrong', 'undecidable', 'dunno'):
        return winner
    is_gold_a = get_ab_assignment(flat_idx)
    if winner == 'a':
        return 'gold' if is_gold_a else 'ia'
    if winner == 'b':
        return 'ia' if is_gold_a else 'gold'
    return winner


def load_file(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict) and 'eval2_responses' in data:
        raw = data['eval2_responses']
        return json.loads(raw) if isinstance(raw, str) else raw
    if isinstance(data, dict) and 'evaluation' in data:
        return data['evaluation']
    if isinstance(data, list):
        return data
    return []


def classify_error(item):
    same_head = item['gold_head'] == item['ia_head']
    g = item['gold_deprel']
    i = item['ia_deprel']
    g_base = g.split(':')[0]
    i_base = i.split(':')[0]

    if same_head and g_base == i_base and g != i:
        return 'Sous-type (même base)'
    elif same_head and g != i:
        return 'Mauvaise relation (même tête)'
    elif not same_head and g == i:
        return 'Mauvaise tête (même relation)'
    elif not same_head and g_base == i_base:
        return 'Tête + sous-type'
    elif not same_head:
        return 'Tête + relation'
    else:
        return 'Autre'


def main():
    parser = argparse.ArgumentParser(
        description='Analyse taxonomique des annotations EvaLatin 2026')
    parser.add_argument('input', nargs='+', help='Fichiers JSON des annotateurs')
    parser.add_argument('--data', default='web_eval/data/eval_gold_vs_ia.json',
                        help='Fichier de données (défaut: web_eval/data/eval_gold_vs_ia.json)')
    parser.add_argument('-o', '--output', default='web_eval/data/consensus_analysis.json',
                        help='Fichier de sortie JSON')
    args = parser.parse_args()

    # Load evaluation data
    with open(args.data, encoding='utf-8') as f:
        eval_data = json.load(f)

    # Build flat list
    flat_items = []
    for bench in eval_data:
        for si, sent in enumerate(eval_data[bench]):
            for di, dis in enumerate(sent['disagreements']):
                flat_items.append({
                    'bench': bench, 'si': si, 'di': di,
                    'sent': sent, 'dis': dis
                })

    # Load and decode all annotators
    annotators = {}
    for path in args.input:
        name = path.rsplit('/', 1)[-1].replace('.json', '')
        responses = load_file(path)
        annotators[name] = {
            r['flatIdx']: decode_winner(r['winner'], r['flatIdx'])
            for r in responses
        }

    names = list(annotators.keys())

    # Find unanimous agreements
    common = set.intersection(*(set(a.keys()) for a in annotators.values()))
    agreements = []
    for idx in sorted(common):
        votes = [annotators[n][idx] for n in names]
        if len(set(votes)) == 1:
            item = flat_items[idx]
            dis = item['dis']
            agreements.append({
                'flatIdx': idx,
                'bench': item['bench'],
                'sent_id': item['sent']['sent_id'],
                'text': item['sent']['text'],
                'word': dis['form'],
                'token_id': dis['token_id'],
                'gold_head': dis['gold']['head'],
                'gold_deprel': dis['gold']['deprel'],
                'ia_head': dis['ia']['head'],
                'ia_deprel': dis['ia']['deprel'],
                'verdict': votes[0],
            })

    gold_wins = [d for d in agreements if d['verdict'] == 'gold']
    ia_wins = [d for d in agreements if d['verdict'] == 'ia']
    both_wrong = [d for d in agreements if d['verdict'] == 'both_wrong']
    undecidable = [d for d in agreements if d['verdict'] == 'undecidable']
    dunno = [d for d in agreements if d['verdict'] == 'dunno']

    # === PRINT REPORT ===
    W = 60
    print("\n" + "=" * W)
    print("  ANALYSE DES ACCORDS UNANIMES")
    print("=" * W)
    print(f"  Items annotés par tous  : {len(common)}")
    print(f"  Accords unanimes        : {len(agreements)} ({len(agreements)/len(common)*100:.0f}%)")
    print(f"  IA meilleur que Gold    : {len(ia_wins)}")
    print(f"  Gold meilleur que IA    : {len(gold_wins)}")
    print(f"  Les deux ont tort       : {len(both_wrong)}")
    print(f"  Indécidable             : {len(undecidable)}")
    print(f"  Je ne sais pas          : {len(dunno)}")

    decided = len(gold_wins) + len(ia_wins)
    if decided > 0:
        print(f"\n  Sur les {decided} cas tranchés :")
        print(f"    Gold : {len(gold_wins)} ({len(gold_wins)/decided*100:.1f}%)")
        print(f"    IA   : {len(ia_wins)} ({len(ia_wins)/decided*100:.1f}%)")

    # --- TYPE DE DIFFÉRENCE ---
    print("\n" + "=" * W)
    print("  TYPE DE DIFFÉRENCE")
    print("=" * W)

    def error_type(item):
        same_head = item['gold_head'] == item['ia_head']
        same_rel = item['gold_deprel'] == item['ia_deprel']
        if not same_head and not same_rel:
            return 'head+deprel'
        elif not same_head:
            return 'head seul'
        else:
            return 'deprel seul'

    for label, items in [("Erreurs Gold (IA raison)", ia_wins),
                         ("Erreurs IA (Gold raison)", gold_wins)]:
        print(f"\n  --- {label} ---")
        for t, c in Counter(error_type(i) for i in items).most_common():
            print(f"    {t}: {c}")

    # --- TAXONOMIE ---
    print("\n" + "=" * W)
    print("  TAXONOMIE DES ERREURS")
    print("=" * W)

    print("\n  Erreurs du Gold:")
    for cat, c in Counter(classify_error(i) for i in ia_wins).most_common():
        print(f"    {cat}: {c}")

    print("\n  Erreurs de l'IA:")
    for cat, c in Counter(classify_error(i) for i in gold_wins).most_common():
        print(f"    {cat}: {c}")

    # --- RELATIONS ---
    print("\n" + "=" * W)
    print("  RELATIONS OÙ GOLD SE TROMPE (verdict=ia)")
    print("=" * W)
    for rel, c in Counter(i['gold_deprel'] for i in ia_wins).most_common(15):
        print(f"    {rel}: {c}")

    print("\n" + "=" * W)
    print("  RELATIONS OÙ IA SE TROMPE (verdict=gold)")
    print("=" * W)
    for rel, c in Counter(i['ia_deprel'] for i in gold_wins).most_common(15):
        print(f"    {rel}: {c}")

    # --- CONFUSIONS ---
    print("\n" + "=" * W)
    print("  CONFUSIONS FRÉQUENTES")
    print("=" * W)

    print("\n  Gold se trompe (gold_rel -> ia_rel correct):")
    conf_g = Counter()
    for item in ia_wins:
        if item['gold_deprel'] != item['ia_deprel']:
            conf_g[(item['gold_deprel'], item['ia_deprel'])] += 1
    for (g, i), c in conf_g.most_common(15):
        print(f"    {g} -> {i}: {c}")

    print("\n  IA se trompe (ia_rel -> gold_rel correct):")
    conf_i = Counter()
    for item in gold_wins:
        if item['ia_deprel'] != item['gold_deprel']:
            conf_i[(item['ia_deprel'], item['gold_deprel'])] += 1
    for (i, g), c in conf_i.most_common(15):
        print(f"    {i} -> {g}: {c}")

    # --- PAR GENRE ---
    print("\n" + "=" * W)
    print("  PAR GENRE")
    print("=" * W)
    for bench in ['poetry', 'prose']:
        ia_w = sum(1 for d in ia_wins if d['bench'] == bench)
        gold_w = sum(1 for d in gold_wins if d['bench'] == bench)
        total = ia_w + gold_w
        if total > 0:
            print(f"  {bench}: Gold={gold_w} ({gold_w/total*100:.0f}%) | IA={ia_w} ({ia_w/total*100:.0f}%) | total={total}")

    # --- ATTACHEMENT ---
    print("\n" + "=" * W)
    print("  ERREURS D'ATTACHEMENT (HEAD)")
    print("=" * W)
    head_err_gold = sum(1 for i in ia_wins if i['gold_head'] != i['ia_head'])
    head_err_ia = sum(1 for i in gold_wins if i['gold_head'] != i['ia_head'])
    print(f"  Gold se trompe de tête: {head_err_gold}/{len(ia_wins)} ({head_err_gold/max(len(ia_wins),1)*100:.0f}%)")
    print(f"  IA se trompe de tête:   {head_err_ia}/{len(gold_wins)} ({head_err_ia/max(len(gold_wins),1)*100:.0f}%)")

    print("\n" + "=" * W + "\n")

    # --- SAVE ---
    output = {
        'summary': {
            'common_items': len(common),
            'agreements': len(agreements),
            'gold_wins': len(gold_wins),
            'ia_wins': len(ia_wins),
            'both_wrong': len(both_wrong),
            'undecidable': len(undecidable),
            'dunno': len(dunno),
        },
        'agreements': agreements,
    }
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"  Sauvegardé : {args.output}")


if __name__ == '__main__':
    main()
