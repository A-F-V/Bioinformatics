from rosalind.rosalind import rosalind_solve
from data_processors.parse_hmm import *
from algorithms.hmm import *


def visible_path_prob_rosalind(text):
    hmm = parse_hmm(text)
    return hmm.visible_path_prob(text[0])


def q10d(i="bioinformatics/rosalind/io/i.txt", o="bioinformatics/rosalind/io/o.txt"):
    return rosalind_solve(i, o, visible_path_prob_rosalind)
