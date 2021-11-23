from rosalind.q3f import q3f
from rosalind.q3g import q3g


def test_eulerian_simple_cycle():
    x = q3f("bioinformatics/tests/data/rosalind/iq3f.txt", None).split("->")
    assert x[0] == x[-1]
    assert len(x) == 13


def test_eulerian_path_cycle():
    x = q3g("bioinformatics/tests/data/rosalind/iq3g.txt", None).split("->")
    assert len(x) == 11
