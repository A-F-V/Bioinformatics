from rosalind.solutions.q9a import q9a
from rosalind.solutions.q9b import q9b
from rosalind.solutions.q9c import q9c
from algorithms.trie import create_suffix_trie
from algorithms.suffix_array import create_suffix_array


def test_generate_trie():
    res = q9a("bioinformatics/tests/data/rosalind/i9a.txt")
    assert len(res.split("\n")) == 9


def test_trie_matching():
    res = q9b("bioinformatics/tests/data/rosalind/i9b.txt")
    assert res == "1 4 11 15"


def test_suffix_trie():
    res = q9c("bioinformatics/tests/data/rosalind/i9c.txt").split("\n")
    edge_values = """AAATG$
G$
T
ATG$
TG$
A
A
AAATG$
G$
T
G$
$""".split("\n")

    assert len(res) == len(edge_values)
    for i in res:
        assert i in edge_values
    for j in edge_values:
        assert j in res


def test_longest_substring_trie():
    res = create_suffix_trie("ATATCGTTTTATCGTT", False)
    res = res.get_longest_repeat_string()
    assert len(res) == len("TATCGTT")


def test_suffix_array_construction():
    sarray = create_suffix_array("AACGATAGCGGTAGA$")
    assert sarray.indices == [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5]
