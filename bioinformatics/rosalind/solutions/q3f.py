
from algorithms.sequencing_graph import DeBruijn_Graph,Graph
from algorithms.eulerian_cycle import eulerian_cycle
from rosalind.rosalind import rosalind_solve
from data_processors.adj_to_graph import agg_adj_to_graph

def eulerian_cycle_rosalind(rows):
    graph = agg_adj_to_graph(rows)
    return "->".join(map(str,eulerian_cycle(graph)))

def q3f(i= "bioinformatics/rosalind/io/i3f.txt",o = "bioinformatics/rosalind/io/o3f.txt"):
    return rosalind_solve(i,o,eulerian_cycle_rosalind)