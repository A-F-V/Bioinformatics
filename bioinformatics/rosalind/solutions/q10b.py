from rosalind.rosalind import rosalind_solve
from data_processors.parse_hmm import *
from algorithms.hmm import *


def cond_path_prob_rosalind(text):
    x = text[0]
    symbols = parse_row(text[2])
    path = text[4]
    states = parse_row(text[6])
    transitions = TransitionMatrix.empty()
    emissions = EmissionMatrix(states, symbols, parse_table(states, symbols, text[8:]))
    hmm = HMM(symbols, states, transitions, emissions)
    return hmm.cond_visible_path_prob(x, path)


def q10b(i="bioinformatics/rosalind/io/i.txt", o="bioinformatics/rosalind/io/o.txt"):
    return rosalind_solve(i, o, cond_path_prob_rosalind)
