from rosalind.q3b import q3b
def test_reconstruction():
    ans = q3b("bioinformatics/tests/data/rosalind/iq3b.txt",None)
    assert ans == "ACCGAAGCT"