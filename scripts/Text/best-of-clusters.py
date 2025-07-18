"""
input: Scores output of Annotated Corpus Map

output: Ranking table with, for each cluster, all the words below a specified p-value
and above a specified score (default 0.05 for both thresholds), one word per row,
with ranking of the word within the cluster, score and p-value.

Use case: if there is a need to do further processing with the words shown as cluster
labels (or even more of them than the default maximum of 5 words)

Suggested use: to get a table with, for each cluster, the top-n words concatenated:
connect output to Select Rows, condition "Rank is at most n",
followed by Group-by -> cluster number, word | concatenate

requires: Text add-on
"""

from Orange.data import Domain, Table, ContinuousVariable, StringVariable

# Create a copy of the input data
out_data = in_data.copy()

# Clear any previous data by reinitializing the output data structure
output_data = []

# Define domain with correct types: cluster number and rank as continuous, word as string, score and p-value as continuous
cluster_var = ContinuousVariable("cluster number")
rank_var = ContinuousVariable("rank")
word_var = StringVariable("word")
score_var = ContinuousVariable("score")
p_value_var = ContinuousVariable("p-value")

output_domain = Domain([cluster_var, rank_var, score_var, p_value_var], metas=[word_var])

# Recalculate the number of clusters based on the current data
nclusters = sum(1 for var in out_data.domain if var.name.startswith('Score(C'))

nrows = len(out_data)

# Iterate over each cluster
for n in range(1, nclusters + 1):
    score = f'Score(C{n})'
    p_value = f'p_value(C{n})'
    
    if score in out_data.domain:
        # Create a list of tuples containing (word, rounded score, p_value) for each word in the cluster
        cluster_words = [
            (out_data[i, 'Words'], round(out_data[i, score], 6), out_data[i, p_value])
            for i in range(nrows)
            # change threshold for p value and score below as needed
            if out_data[i, p_value] <= 0.05 and out_data[i, score] > 0.05
        ]
        
        # Sort the words by rounded score in descending order and by p-value in ascending order
        cluster_words_sorted = sorted(cluster_words, key=lambda x: (-x[1], x[2]))
        
        # Assign ranks and add them to the output data
        for rank, (word, score_value, p_value_value) in enumerate(cluster_words_sorted, start=1):
            output_data.append([n, rank, score_value, p_value_value, word])

# Create an Orange Table with the output data
out_table = Table.from_list(output_domain, output_data)

out_data = out_table
