"""
input: Corpus with Bag of Words and POS tags.
output: Corpus with filtered attributes.
requires: Text add-on
"""

from Orange.data import Domain

condition = "_NN"

attrs = [attr for attr in in_data.domain.attributes if condition not in attr.name]
new_domain = Domain(attrs, in_data.domain.class_vars, in_data.domain.metas)
out_data = in_data.transform(new_domain)