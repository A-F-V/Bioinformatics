
from algorithms.sequencing_graph import DeBruijn_Graph, Graph
from algorithms.eulerian_cycle import eulerian_path
from algorithms.reconstruct_genome_string import reconstruct_from_kmers
from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion


def distortion_rosalind(rows):
    params = rows[0].split()
    k, dim = int(params[0]), int(params[1])
    centres = parse_rows_of_vectors(rows[1:k+1])
    points = parse_rows_of_vectors(rows[k+2:])
    return distortion(points, centres)


def q8b(i="bioinformatics/rosalind/io/i8b.txt", o="bioinformatics/rosalind/io/o8b.txt"):
    return rosalind_solve(i, o, distortion_rosalind)
