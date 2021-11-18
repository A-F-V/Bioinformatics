
from algorithms.sequencing_graph import DeBruijn_Graph,Graph
from algorithms.eulerian_cycle import eulerian_path
from algorithms.reconstruct_genome_string import reconstruct_from_kmers
from algorithms.reconstruct_genome_string import reconstruct_from_paired_kmers
from rosalind.rosalind import rosalind_solve
from data_processors.adj_to_graph import agg_adj_to_graph

def paired_composition_rosalind(data):
    k,d = data[0].split(" ")
    k,d = int(k),int(d)
    pairs = list(map(lambda x:tuple(x.split("|")),data[1:]))
    return reconstruct_from_paired_kmers(pairs,k,d)

def q3j(i= "bioinformatics/rosalind/io/i3j.txt",o = "bioinformatics/rosalind/io/o3j.txt"):
    return rosalind_solve(i,o,paired_composition_rosalind)