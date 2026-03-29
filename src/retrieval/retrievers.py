"""
Retrieval strategies for dependency tree similarity.
Implements TF-IDF, structural, and morphological retrievers.
"""

from collections import Counter, defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_sentence_text(sentence):
    """Extract text from a parsed CoNLL-U sentence."""
    return " ".join([t[1] for t in sentence if isinstance(t, list)])


def get_pos_sequence(sentence):
    """Extract POS tag sequence."""
    return [t[3] for t in sentence if isinstance(t, list)]


def get_tree_depth(sentence):
    """Calculate maximum depth of dependency tree."""
    children = defaultdict(list)
    for i, token in enumerate(sentence):
        if isinstance(token, list):
            try:
                head = int(token[6]) if token[6] != '_' else 0
                children[head].append(i + 1)
            except ValueError:
                pass

    def dfs(node, depth=0):
        if not children[node]:
            return depth
        return max(dfs(child, depth + 1) for child in children[node])

    return dfs(0)


def get_morpho_features(sentence):
    """Extract morphological features (POS|FEATS per token)."""
    features = []
    for token in sentence:
        if isinstance(token, list):
            pos = token[3]
            feats = token[5] if token[5] != '_' else ''
            features.append(f"{pos}|{feats}")
    return features


def _get_ngrams(seq, n):
    """Get n-grams from a sequence."""
    return Counter(tuple(seq[i:i + n]) for i in range(len(seq) - n + 1))


def _jaccard(counter1, counter2):
    """Jaccard similarity for counters."""
    if not counter1 or not counter2:
        return 0.0
    intersection = sum((counter1 & counter2).values())
    union = sum((counter1 | counter2).values())
    return intersection / union if union > 0 else 0.0


class TFIDFRetriever:
    """Baseline TF-IDF retriever (word-based cosine similarity)."""

    def __init__(self, sentences):
        self.sentences = sentences
        corpus = [get_sentence_text(s) for s in sentences]
        self.vectorizer = TfidfVectorizer(max_features=5000, stop_words=None)
        self.X = self.vectorizer.fit_transform(corpus)

    def retrieve(self, query_sent, k=5):
        query_text = get_sentence_text(query_sent)
        query_vec = self.vectorizer.transform([query_text])
        sims = cosine_similarity(query_vec, self.X).flatten()
        top_k_idx = sims.argsort()[-k:][::-1]
        return [(idx, sims[idx]) for idx in top_k_idx]


class StructuralRetriever:
    """Retriever based on sentence length and POS n-gram similarity (Eq. 1 in paper)."""

    def __init__(self, sentences):
        self.sentences = sentences
        self.features = []
        for sent in sentences:
            pos_seq = get_pos_sequence(sent)
            self.features.append({
                'length': len(pos_seq),
                'pos_bigrams': _get_ngrams(pos_seq, 2),
                'pos_trigrams': _get_ngrams(pos_seq, 3),
            })

    def _similarity(self, feat1, feat2):
        """Weighted combination: length + POS bigrams + POS trigrams."""
        len_sim = 1.0 - abs(feat1['length'] - feat2['length']) / max(feat1['length'], feat2['length'], 1)
        bigram_sim = _jaccard(feat1['pos_bigrams'], feat2['pos_bigrams'])
        trigram_sim = _jaccard(feat1['pos_trigrams'], feat2['pos_trigrams'])
        return 0.33 * len_sim + 0.33 * bigram_sim + 0.34 * trigram_sim

    def retrieve(self, query_sent, k=5):
        query_pos = get_pos_sequence(query_sent)
        query_feat = {
            'length': len(query_pos),
            'pos_bigrams': _get_ngrams(query_pos, 2),
            'pos_trigrams': _get_ngrams(query_pos, 3),
        }
        sims = [self._similarity(query_feat, feat) for feat in self.features]
        top_k_idx = np.argsort(sims)[-k:][::-1]
        return [(idx, sims[idx]) for idx in top_k_idx]


class MorphologicalRetriever:
    """Retriever based on TF-IDF over POS+morphological features."""

    def __init__(self, sentences):
        self.sentences = sentences
        corpus = [" ".join(get_morpho_features(s)) for s in sentences]
        self.vectorizer = TfidfVectorizer(max_features=3000)
        self.X = self.vectorizer.fit_transform(corpus)

    def retrieve(self, query_sent, k=5):
        query_morpho = " ".join(get_morpho_features(query_sent))
        query_vec = self.vectorizer.transform([query_morpho])
        sims = cosine_similarity(query_vec, self.X).flatten()
        top_k_idx = sims.argsort()[-k:][::-1]
        return [(idx, sims[idx]) for idx in top_k_idx]
