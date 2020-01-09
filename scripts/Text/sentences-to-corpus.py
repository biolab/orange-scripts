"""
input: Corpus preprocessed with Preprocess Text. Tokenizer is set to Sentences.
output: Corpus where sentences are now documents.
requires: Text add-on
"""

import numpy as np
from Orange.data import Domain, StringVariable
from orangecontrib.text.corpus import Corpus

tokens = in_data.tokens
title = [i for i in in_data.domain.metas if "title" in i.attributes][0]
new_domain = Domain(attributes=[], metas=[StringVariable('Sentences'),
                                          title)

titles = []
content = []


for i, doc in enumerate(tokens):
    for t in doc:
        titles.append(in_data[i][title.name].value)
        content.append(t)

metas = np.column_stack((content, titles))
out_data = Corpus.from_numpy(domain=new_domain, X=np.empty((len(content), 0)),
                             metas=metas)
out_data.set_text_features([StringVariable('Sentences')])
out_data.set_title_variable(title)