from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans, soft_kmeans
from algorithms.trie import create_trie, Trie, create_suffix_trie
from algorithms.suffix_array import create_suffix_array


def suffix_array(text):
    return ", ".join(map(str, create_suffix_array(text[0]).indices))


def q9g(i="bioinformatics/rosalind/io/i9g.txt", o="bioinformatics/rosalind/io/o9g.txt"):
    return rosalind_solve(i, o, suffix_array)
