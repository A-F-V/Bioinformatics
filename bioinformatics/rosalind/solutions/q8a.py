
from algorithms.sequencing_graph import DeBruijn_Graph, Graph
from algorithms.eulerian_cycle import eulerian_path
from algorithms.reconstruct_genome_string import reconstruct_from_kmers
from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import farthest_first_clustering


def farthest_first_rosalind(rows):
    params = rows[0].split()
    k, dim = int(params[0]), int(params[1])
    points = parse_rows_of_vectors(rows[1:])
    o = farthest_first_clustering(points, k)
    return list(map(vector_to_row, o))


def q8a(i="bioinformatics/rosalind/io/i8a.txt", o="bioinformatics/rosalind/io/o8a.txt"):
    return rosalind_solve(i, o, farthest_first_rosalind)
