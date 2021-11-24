from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans, soft_kmeans
from algorithms.trie import create_trie, Trie, create_suffix_trie


def shortest_non_shared_substring_trie(text):
    tree_text = text[1]
    trie = create_suffix_trie(tree_text, False)
    text = text[0]
    best = None
    for i in range(len(text)):
        attempt = trie.shortest_non_substring(text[i:])
        print(attempt)
        if "(M)" not in attempt and (best is None or len(attempt) < len(best)):
            best = attempt
    return best


def q9f(i="bioinformatics/rosalind/io/i9f.txt", o="bioinformatics/rosalind/io/o9f.txt"):
    return rosalind_solve(i, o, shortest_non_shared_substring_trie)
