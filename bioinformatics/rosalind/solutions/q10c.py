from rosalind.rosalind import rosalind_solve
from data_processors.parse_hmm import *
from algorithms.hmm import *


def viterbi_rosalind(text):
    hmm = parse_hmm(text)
    return hmm.viterbi(text[0])


def q10c(i="bioinformatics/rosalind/io/i.txt", o="bioinformatics/rosalind/io/o.txt"):
    return rosalind_solve(i, o, viterbi_rosalind)
