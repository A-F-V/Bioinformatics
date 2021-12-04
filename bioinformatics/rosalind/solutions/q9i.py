from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from algorithms.burrows_wheeler import bwt


def bwt_rosalind(text):
    return bwt(text[0])


def q9i(i="bioinformatics/rosalind/io/i9i.txt", o="bioinformatics/rosalind/io/o9i.txt"):
    return rosalind_solve(i, o, bwt_rosalind)
