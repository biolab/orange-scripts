"""
This script filters columns with low bag-of-words count or tf-idf

input: Corpus with bag-of-words counts.
output: Corpus with bag-of-words counts with removed columns/values lower than
    CUT_VALUE.
requires: Text add-on
"""

from Orange.data import Domain
from orangecontrib.text.corpus import Corpus

CUT_VALUE = 10

"""
Remove columns that do not have any value above CUT_VALUE
"""
print("Num values in original data:", len(in_data.X.data))
print("Num attributes in original data:", len(in_data.domain.attributes))

column_max = in_data.X.max(axis=0).toarray().flatten()
attributes_mask = column_max > CUT_VALUE

out_data = Corpus(Domain(
    [a for a, inc in zip(in_data.domain.attributes, attributes_mask) if inc],
    in_data.domain.class_var, in_data.domain.metas),
    in_data.X[:, attributes_mask], Y=in_data.Y, metas=in_data.metas,
    text_features=in_data.text_features
)

print("Num values after removing columns:", len(out_data.X.data))

"""
This part is optional:
Remove values that are not above CUT_VALUE
"""
cx = out_data.X.tocoo()
for i, j, v in zip(cx.row, cx.col, cx.data):
    if v <= CUT_VALUE:
        out_data.X[i, j] = 0
out_data.X.eliminate_zeros()

print("Num values in output data:", len(out_data.X.data))
print("Num attributes in output data:", len(out_data.domain.attributes))
