from rosalind.rosalind import rosalind_solve, parse_rows_of_vectors, vector_to_row
from algorithms.trie import create_suffix_trie
from algorithms.suffix_array import create_suffix_array


def suffix_array_pattern_match(text):
    sarray = create_suffix_array(text[0], False)
    indices = []
    for pattern in text[1:]:
        indices.extend(sarray.find_matching_pattern(pattern))
    return " ".join(map(str, (sorted(indices))))


def q9h(i="bioinformatics/rosalind/io/i9h.txt", o="bioinformatics/rosalind/io/o9h.txt"):
    return rosalind_solve(i, o, suffix_array_pattern_match)
