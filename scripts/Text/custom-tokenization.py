"""
input: Corpus.
output: Corpus with tokens.
requires: Text add-on
"""

from gensim.corpora import Dictionary

tokens = []
for doc in in_data.documents:
    tokens.append([token.strip(' ').lower() for token in doc.split(';')])

dictionary = Dictionary(tokens)
dictionary.filter_extremes(keep_n = 100)


tokens = [[token for token in doc if token in dictionary.token2id.keys() and token != '?'] for doc in tokens]

out = in_data.copy()
out.store_tokens(tokens)
out_data = out