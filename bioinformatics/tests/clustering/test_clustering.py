from rosalind.solutions.q8a import q8a
from rosalind.solutions.q8b import q8b
from rosalind.solutions.q8c import q8c
from rosalind.solutions.q8d import q8d


def test_farthest_centre():
    x = q8a("bioinformatics/tests/data/rosalind/iq8a.txt", None)
    assert len(x) == 3
    assert "0.0 5.0" in x


def test_distortion():
    x = q8b("bioinformatics/tests/data/rosalind/iq8b.txt", None)
    assert abs(x-18.246) < 0.001


def test_lloyd():
    x = q8c("bioinformatics/tests/data/rosalind/iq8c.txt", None)
    assert abs(float(x[0].split(' ')[0])-1.8) < 0.001


def test_soft_clustering():
    x = q8d("bioinformatics/tests/data/rosalind/iq8d.txt", None)
    assert abs(float(x[0].split(' ')[0])-1.662) < 0.001
