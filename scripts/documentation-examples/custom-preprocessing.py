print('Running Preprocessing ...')
tokens = [doc.split(' ') for doc in in_data.documents]
print('Tokens:', tokens)
out_data = in_data.copy()
out_data.store_tokens(tokens)