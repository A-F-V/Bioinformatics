from algorithms.hmm import *


def parse_table(row_header, col_header, table: list):
    output = {}
    for i in range(1, len(table)):
        row = table[i]
        entry = row.split()[1:]
        output.update({(row_header[i-1], col_header[j]): float(entry[j]) for j in range(len(col_header))})
    return output


def parse_row(text):
    return text.strip().split()


def parse_hmm(text):
    symbols = parse_row(text[2])
    states = parse_row(text[4])
    transitions = TransitionMatrix(states, parse_table(states, states, text[6:6+len(states)+1]))
    emissions = EmissionMatrix(states, symbols, parse_table(states, symbols, text[6+len(states)+2:]))
    return HMM(symbols, states, transitions, emissions)
