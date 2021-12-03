from algorithms.reconstruct_genome_string import construct_k_universal_circular_string
from rosalind.solutions.q3b import q3b
from rosalind.solutions.q3h import q3h
from rosalind.solutions.q3j import q3j


def test_reconstruction_simple():
    ans = q3b("bioinformatics/tests/data/rosalind/iq3b.txt", None)
    assert ans == "ACCGAAGCT"


def test_reconstruction_from_just_kmers():
    ans = q3h("bioinformatics/tests/data/rosalind/iq3h.txt", None)
    assert ans == "GGCTTACCA"


def test_construct_universal():
    ans = construct_k_universal_circular_string(4)
    assert len(ans) == len("0000110010111101")


def test_reconstruction_from_just_kmer_pairs():
    ans = q3j("bioinformatics/tests/data/rosalind/iq3j.txt", None)
    assert ans == "GTGGTCGTGAGATGTTGA"
