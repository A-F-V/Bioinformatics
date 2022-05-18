from rosalind.rosalind import rosalind_solve
from data_processors.parse_hmm import *
from algorithms.hmm import *


def path_prob_rosalind(text):
    path = text[0]
    states = parse_row(text[2])
    transitions = TransitionMatrix(states, parse_table(states, states, text[4:]))
    emissions = EmissionMatrix.empty()
    hmm = HMM([], states, transitions, emissions)
    return hmm.hidden_path_prob(path)


def q10a(i="bioinformatics/rosalind/io/i.txt", o="bioinformatics/rosalind/io/o.txt"):
    return rosalind_solve(i, o, path_prob_rosalind)
