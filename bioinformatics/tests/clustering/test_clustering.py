from rosalind.q8a import q8a
from rosalind.q8b import q8b
from rosalind.q8c import q8c


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
