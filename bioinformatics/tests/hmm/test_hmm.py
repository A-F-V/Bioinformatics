from rosalind.solutions.q10a import q10a
from rosalind.solutions.q10b import q10b
from rosalind.solutions.q10c import q10c
from rosalind.solutions.q10d import q10d


def test_path_prob():
    assert abs(float(q10a('bioinformatics/tests/data/rosalind/q10a.txt'))-5.01732865318e-19) < 1e-25


def test_cond_path_prob():
    assert abs(float(q10b('bioinformatics/tests/data/rosalind/q10b.txt')-1.93157070893e-28)) < 1e-25


def test_viterbi():
    assert q10c('bioinformatics/tests/data/rosalind/q10c.txt') == 'AAABBAAAAA'


def test_cond_path_prob():
    assert abs(float(q10d('bioinformatics/tests/data/rosalind/q10d.txt')-1.1005510319694847e-06)) < 1e-8
