from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans


def lloyd_rosalind(rows):
    params = rows[0].split()
    k, dim = int(params[0]), int(params[1])
    points = parse_rows_of_vectors(rows[1:])
    centres = lloyd_kmeans(points, k)
    return list(map(vector_to_row, centres))


def q8c(i="bioinformatics/rosalind/io/i8c.txt", o="bioinformatics/rosalind/io/o8c.txt"):
    return rosalind_solve(i, o, lloyd_rosalind)
