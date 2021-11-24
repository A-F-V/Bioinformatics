from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans, soft_kmeans
from algorithms.trie import create_trie, Trie, create_suffix_trie


def subString_with_trie_rosalind(text):
    text = text[0]
    trie = create_suffix_trie(text, False)
    return trie.get_longest_repeat_string()


def q9d(i="bioinformatics/rosalind/io/i9d.txt", o="bioinformatics/rosalind/io/o9d.txt"):
    return rosalind_solve(i, o, subString_with_trie_rosalind)
