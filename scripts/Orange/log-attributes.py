"""
input: Data.
output: Log-transformed data.
"""

import numpy as np
from Orange.data import Table

new_X = np.log(in_data.X)
out_data = Table.from_table(in_data.domain, new_X, in_data.Y, in_data.metas)
