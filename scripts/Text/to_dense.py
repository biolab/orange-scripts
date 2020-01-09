"""
input: Corpus.
output: Dense representation of attributes.
requires: Text add-on
"""

from orangecontrib.text import Corpus

out_data = Corpus.to_dense(in_data.copy())