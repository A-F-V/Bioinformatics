from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans, soft_kmeans
from algorithms.trie import create_trie, Trie, create_suffix_trie


def shared_substring_trie(text):
    tree_text = text[0]
    trie = create_suffix_trie(tree_text, False)
    text = text[1]
    best = ""
    for i in range(len(text)):
        attempt = trie.longest_substring_match(text[i:])
        print(attempt)
        if len(attempt) > len(best):
            best = attempt
    return best


def q9e(i="bioinformatics/rosalind/io/i9e.txt", o="bioinformatics/rosalind/io/o9e.txt"):
    return rosalind_solve(i, o, shared_substring_trie)
