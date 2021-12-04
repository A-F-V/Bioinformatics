from algorithms.burrows_wheeler import bwt, inverse_bwt, bwt_matching_all
from rosalind.solutions.q9k import last_to_first_rosalind


def test_bwt_transform():
    assert bwt("GCGTGCCTGGTCA$") == "ACTGGCT$TGCGGC"


def test_inverse_bwt():
    assert inverse_bwt("TTCCTAACG$A") == "TACATCACGT$"


def test_last_to_first():
    assert last_to_first_rosalind(["T$GACCA", "3"]) == 1


def test_bwmatching():
    bwt = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
    patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]
    counts = list(map(lambda x: x[1]-x[0], bwt_matching_all(bwt, patterns)))
    assert counts == [2, 1, 1, 0, 1]
