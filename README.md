# Orange Scripts

Scripts for the Python Script Orange widget.

## Orange

- log-attributes.py: Log-transform the data.

## Documentation examples
- batch-filtering.py: Filter variables on condition.
- custom-preprocessing.py: Custom preprocessing for text data (requires Text add-on).
- gaussian-noise.py: Introduce Gaussian noise.
- round-values.py: Round feature values.

## Text add-on

- bigram-collocations.py: Compute and output a table of bigrams from the input corpus.
- custom-tokenization.py: Tokenize data by splitting by semicolon and keep the most frequent 100 tokens.
- extract-url.py: Find url in the text and add it as an additional column.
- filter-pos-tags.py: Keep only certain POS tags in tokens.
- sentence-to-corpus.py: Use sentences as documents and output the new corpus.
- to_dense.py: Transform sparse data to dense.
- remove_low_tfidf_values.py: Filters columns with low bag-of-words count or tf-idf
- bow-to-sparse.py: Transforms an existing bow matrix (document-term), builds tokens, and turns it into sparse matrix.

## Timeseries add-on

- timeseries-alignment.py: align timeseries at value n.
