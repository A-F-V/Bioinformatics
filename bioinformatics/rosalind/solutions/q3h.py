
from algorithms.sequencing_graph import DeBruijn_Graph,Graph
from algorithms.eulerian_cycle import eulerian_path
from algorithms.reconstruct_genome_string import reconstruct_from_kmers
from rosalind.rosalind import rosalind_solve
from data_processors.adj_to_graph import agg_adj_to_graph

def reconstruct_from_kmers_rosalind(rows):
    kmers = rows[1:]
    return reconstruct_from_kmers(kmers)

def q3h(i= "bioinformatics/rosalind/io/i3h.txt",o = "bioinformatics/rosalind/io/o3h.txt"):
    return rosalind_solve(i,o,reconstruct_from_kmers_rosalind)