from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans, soft_kmeans
from algorithms.trie import create_trie, Trie


def trie_rosalind(words):
    return str(create_trie(words))


def q9a(i="bioinformatics/rosalind/io/i9a.txt", o="bioinformatics/rosalind/io/o9a.txt"):
    return rosalind_solve(i, o, trie_rosalind)
