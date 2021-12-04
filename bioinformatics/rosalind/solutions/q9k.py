from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from algorithms.burrows_wheeler import inverse_bwt, number_letters, first_col_from_bwt, index_list


def last_to_first_rosalind(text):
    bwt = text[0]
    i = int(text[1])
    f_col = number_letters(first_col_from_bwt(bwt))
    l_col = number_letters(bwt)
    indexed_f_col = index_list(f_col)
    return indexed_f_col[l_col[i]]


def q9k(i="bioinformatics/rosalind/io/i.txt", o="bioinformatics/rosalind/io/o.txt"):
    return rosalind_solve(i, o, last_to_first_rosalind)
