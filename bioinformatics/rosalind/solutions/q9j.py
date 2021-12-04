from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from algorithms.burrows_wheeler import inverse_bwt


def inverse_bwt_rosalind(text):
    return inverse_bwt(text[0])


def q9j(i="bioinformatics/rosalind/io/i9j.txt", o="bioinformatics/rosalind/io/o9j.txt"):
    return rosalind_solve(i, o, inverse_bwt_rosalind)
