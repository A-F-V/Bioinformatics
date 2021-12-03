
from algorithms.sequencing_graph import DeBruijn_Graph
from algorithms.sequencing_graph import kmers_to_debruijn
from rosalind.rosalind import rosalind_solve

def kmer_debruijn_rosalind(kmers):
    return str(kmers_to_debruijn(kmers))

def q3e(i= "bioinformatics/rosalind/io/i3e.txt",o = "bioinformatics/rosalind/io/o3e.txt"):
    return rosalind_solve(i,o,kmer_debruijn_rosalind)