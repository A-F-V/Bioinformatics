from rosalind.solutions.q3c import q3c


def test_overlap():
    ans = q3c("bioinformatics/tests/data/rosalind/iq3c.txt", None).strip().split("\n")
    assert len(ans) == 4
