from rosalind.solutions.q3e import q3e
from rosalind.solutions.q3d import q3d


def test_debruijn_text():
    ans = q3d("bioinformatics/tests/data/rosalind/iq3d.txt", None).strip().split("\n")
    assert len(ans) == 8


def test_debruijn_kmer():
    ans = q3e("bioinformatics/tests/data/rosalind/iq3e.txt", None).strip().split("\n")
    assert len(ans) == 5
