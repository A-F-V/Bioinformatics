from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans, soft_kmeans
from algorithms.trie import create_trie, Trie, match_text_to_patterns


def trie_matching_rosalind(words):
    text = words[0]
    patterns = words[1:]
    return " ".join(map(str, match_text_to_patterns(text, patterns)))


def q9b(i="bioinformatics/rosalind/io/i9b.txt", o="bioinformatics/rosalind/io/o9b.txt"):
    return rosalind_solve(i, o, trie_matching_rosalind)
