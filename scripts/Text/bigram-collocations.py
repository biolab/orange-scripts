"""
input: Corpus with tokens.
output: Table of bigrams and their scores.
requires: Text add-on
"""

import nltk.collocations
from Orange.data import Domain, StringVariable, ContinuousVariable, Table
import numpy as np

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = nltk.BigramCollocationFinder.from_documents(in_data.tokens)
finder.apply_freq_filter(5)

print("\nBest 50 bigrams according to PMI:", finder.nbest(bigram_measures.pmi, 50))

bigram = []
score = []

for word_tup, scores in finder.score_ngrams(bigram_measures.pmi):
    first, second = word_tup
    bigram.append(first + ' ' + second)
    score.append(scores)
    
bigram = np.array(bigram)[:, None]
score = np.array(score)[:, None]

meta_attrs = [StringVariable('bigram')]
cont_attrs = [ContinuousVariable('score')]
domain = Domain(attributes=cont_attrs, metas=meta_attrs)

out_data = Table.from_numpy(domain, X=score, metas=bigram)
