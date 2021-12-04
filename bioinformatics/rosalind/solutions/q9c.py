from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans
from algorithms.trie import create_trie, Trie, create_suffix_trie


def suffix_trie_rosalind(text):
    text = text[0]
    trie = create_suffix_trie(text)
    output = []
    for frm in trie.edges:
        for edge in trie.edges[frm]:
            output.append(edge[1])
    return '\n'.join(output)


def q9c(i="bioinformatics/rosalind/io/i9c.txt", o="bioinformatics/rosalind/io/o.txt"):
    return rosalind_solve(i, o, suffix_trie_rosalind)
