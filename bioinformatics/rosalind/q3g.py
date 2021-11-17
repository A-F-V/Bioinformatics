
from algorithms.sequencing_graph import DeBruijn_Graph,Graph
from algorithms.eulerian_cycle import eulerian_path
from rosalind.rosalind import rosalind_solve
from data_processors.adj_to_graph import agg_adj_to_graph

def eulerian_path_rosalind(rows):
    graph = agg_adj_to_graph(rows)
    return "->".join(map(str,eulerian_path(graph)))

def q3g(i= "bioinformatics/rosalind/io/i3g.txt",o = "bioinformatics/rosalind/io/o3g.txt"):
    return rosalind_solve(i,o,eulerian_path_rosalind)