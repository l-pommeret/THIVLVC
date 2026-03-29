"""
Utilities for parsing, formatting, and validating CoNLL-U files.
"""


def parse_conllu(file_path):
    """Parse a CoNLL-U file into a list of sentences.
    Each sentence is a list of items: comment strings or 10-field token lists.
    """
    sentences = []
    current_sentence = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                if current_sentence:
                    sentences.append(current_sentence)
                    current_sentence = []
                continue
            if line.startswith('#'):
                current_sentence.append(line)
                continue
            fields = line.split('\t')
            if len(fields) == 10:
                current_sentence.append(fields)
        if current_sentence:
            sentences.append(current_sentence)
    return sentences


def format_conllu(sentence):
    """Format a sentence back to CoNLL-U string."""
    lines = []
    for fields in sentence:
        if isinstance(fields, list):
            lines.append('\t'.join(fields))
        else:
            lines.append(fields)
    return '\n'.join(lines)


def sentence_to_text(sentence):
    """Extract plain text from a parsed sentence."""
    return ' '.join([fields[1] for fields in sentence if isinstance(fields, list)])


def fix_cycles(sentence_data):
    """Detect and fix dependency cycles by attaching cycle nodes to root."""
    nodes = {}
    for line in sentence_data:
        if isinstance(line, list) and line[0].isdigit():
            nodes[line[0]] = line

    visited = set()

    def has_cycle(node_id, path):
        if node_id == '0':
            return None
        if node_id in path:
            cycle_start = path.index(node_id)
            return path[cycle_start:] + [node_id]
        if node_id in visited:
            return None
        visited.add(node_id)
        path.append(node_id)
        if node_id not in nodes:
            path.pop()
            return None
        head_id = nodes[node_id][6]
        if not head_id.isdigit():
            path.pop()
            return None
        cycle = has_cycle(head_id, path)
        if cycle:
            return cycle
        path.pop()
        return None

    for tid in list(nodes.keys()):
        cycle = has_cycle(tid, [])
        if cycle:
            node_to_fix = cycle[-2]
            target = nodes[node_to_fix]
            target[6] = '0'
            target[7] = 'root'
            return fix_cycles(sentence_data)

    return sentence_data


def fix_roots(sentence_data):
    """Ensure exactly one root (HEAD=0) in the sentence."""
    roots = []
    for idx, line in enumerate(sentence_data):
        if isinstance(line, list) and len(line) >= 7 and line[0].isdigit():
            if line[6] == '0':
                roots.append(idx)

    if len(roots) > 1:
        main_root_id = sentence_data[roots[0]][0]
        for r_idx in roots[1:]:
            sentence_data[r_idx][6] = main_root_id
            sentence_data[r_idx][7] = "parataxis"
    elif len(roots) == 0:
        for line in sentence_data:
            if isinstance(line, list) and len(line) >= 7 and line[0].isdigit():
                line[6] = '0'
                line[7] = 'root'
                break

    return sentence_data


def clean_mwts(sentence_data):
    """Clean Multi-Word Token lines: set HEAD and DEPREL to underscore."""
    for line in sentence_data:
        if isinstance(line, list) and '-' in line[0]:
            line[6] = '_'
            line[7] = '_'
    return sentence_data


def fix_mwt_heads(sentence_data):
    """Fix tokens whose HEAD points to an MWT range."""
    range_map = {}
    for line in sentence_data:
        if isinstance(line, list) and '-' in line[0]:
            start, _ = line[0].split('-')
            range_map[line[0]] = start

    for line in sentence_data:
        if isinstance(line, list) and line[6] in range_map:
            line[6] = range_map[line[6]]
    return sentence_data


def fix_out_of_bounds(sentence):
    """Fix tokens with HEAD pointing outside the sentence."""
    tokens = [line for line in sentence if isinstance(line, list)
              and '-' not in line[0] and '.' not in line[0]]
    L = len(tokens)
    token_ids = {t[0] for t in tokens}

    root_id = "1"
    for tok in tokens:
        if tok[6] == '0':
            root_id = tok[0]
            break

    for tok in tokens:
        try:
            head = int(tok[6])
        except ValueError:
            continue
        if head < 0 or head > L:
            if str(head) not in token_ids:
                tok[6] = root_id
                tok[7] = "dep"

    return sentence


def validate_structure(sentence_data):
    """Return a list of structural errors found in the sentence."""
    errors = []
    nodes = {}
    tokens = []
    for line in sentence_data:
        if isinstance(line, list) and line[0].isdigit():
            nodes[line[0]] = line
            tokens.append(line)

    if not tokens:
        return ["Sentence has no tokens."]

    roots = [t for t in tokens if t[6] == '0']
    if len(roots) == 0:
        errors.append("No root found (HEAD=0 missing).")
    elif len(roots) > 1:
        errors.append(f"Multiple roots found ({len(roots)} tokens have HEAD=0).")

    token_ids = set(nodes.keys())
    for t in tokens:
        if t[6] != '0' and t[6] not in token_ids:
            errors.append(f"Token {t[0]} has head {t[6]} which is out of bounds.")

    visited = set()

    def check_cycle(node_id, path):
        if node_id == '0':
            return None
        if node_id in path:
            return path[path.index(node_id):] + [node_id]
        if node_id in visited:
            return None
        visited.add(node_id)
        path.append(node_id)
        if node_id in nodes:
            head_id = nodes[node_id][6]
            if head_id.isdigit() or head_id == '0':
                res = check_cycle(head_id, path)
                if res:
                    return res
        path.pop()
        return None

    for tid in nodes:
        cycle = check_cycle(tid, [])
        if cycle:
            errors.append(f"Cycle detected: {' -> '.join(cycle)}")
            break

    return errors
