"""
input: Corpus.
output: Corpus with an additional feature containing url.
requires: Text add-on
"""

from Orange.data import Domain, StringVariable
from orangecontrib.text import Corpus
import re

new_feature = []
new_attr = StringVariable('url')
# the script assumes the text feature is called Content
for d in in_data.get_column_view('Content')[0]:
        if re.search(r"(https?://\S+)", str(d)):
            new_feature.append([re.findall(r"(https?://\S+)", str(d))[-1]])
        else:
            new_feature.append([''])

new_domain = Domain(in_data.domain.attributes, in_data.domain.class_vars, in_data.domain.metas + (new_attr,))

out_data = in_data.transform(new_domain)
out_data[:, new_attr] = new_feature
