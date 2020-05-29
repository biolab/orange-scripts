"""
input: Corpus with pre-computed bag of words data (document-term matrix).
output: Corpus with sparse matrix and token property. Can be used with Topic Modelling and Word Cloud.
requires: Text add-on
"""

import numpy as np
from scipy.sparse import csr_matrix

# build tokens
tokens = []
for doc in in_data.X:
    temp = []
    for i, token in enumerate(doc):
        if token != 0.0 and not np.isnan(token):
            temp.append(in_data.domain.attributes[i].name)
    tokens.append(temp)
    
out = in_data.copy()

# tag variables as bow features
for var in out.domain.attributes:
    var.attributes.update({'bow-feature': True})

out.store_tokens(tokens)
out.X = csr_matrix(out.X)
out_data = out