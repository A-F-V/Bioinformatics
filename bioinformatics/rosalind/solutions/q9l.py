from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from algorithms.burrows_wheeler import bwt_matching_all


def bwmatching_rosalind(text):
    bwt = text[0]
    patterns = text[1].split(" ")
    return " ".join(map(lambda x: str(x[1]-x[0]), bwt_matching_all(bwt, patterns)))


def q9l(i="bioinformatics/rosalind/io/i.txt", o="bioinformatics/rosalind/io/o.txt"):
    return rosalind_solve(i, o, bwmatching_rosalind)
