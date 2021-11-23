from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from data_processors.adj_to_graph import agg_adj_to_graph
from algorithms.clustering import distortion, lloyd_kmeans, soft_kmeans


def soft_rosalind(rows):
    params = rows[0].split()
    k, dim = int(params[0]), int(params[1])
    beta = float(rows[1])
    points = parse_rows_of_vectors(rows[2:])
    centres = soft_kmeans(points, k, beta)
    return list(map(vector_to_row, centres))


def q8d(i="bioinformatics/rosalind/io/i8d.txt", o="bioinformatics/rosalind/io/o8d.txt"):
    return rosalind_solve(i, o, soft_rosalind)
