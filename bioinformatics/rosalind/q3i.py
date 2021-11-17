
from algorithms.sequencing_graph import DeBruijn_Graph,Graph
from algorithms.eulerian_cycle import eulerian_path
from algorithms.reconstruct_genome_string import reconstruct_from_kmers
from algorithms.reconstruct_genome_string import construct_k_universal_circular_string
from rosalind.rosalind import rosalind_solve
from data_processors.adj_to_graph import agg_adj_to_graph

def universal_string_rosalind(k):
    k = int(k[0])
    return construct_k_universal_circular_string(k)

def q3i(i= "bioinformatics/rosalind/io/i3i.txt",o = "bioinformatics/rosalind/io/o3i.txt"):
    return rosalind_solve(i,o,universal_string_rosalind)