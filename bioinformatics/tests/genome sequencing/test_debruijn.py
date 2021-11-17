from rosalind.q3d import q3d

def test_debruijn():
    ans = q3d("bioinformatics/tests/data/rosalind/iq3d.txt",None).strip().split("\n")
    assert len(ans) == 8