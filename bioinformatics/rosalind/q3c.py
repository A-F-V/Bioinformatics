
from algorithms.sequencing_graph import Overlap_Graph
from rosalind.rosalind import rosalind_solve
def overlap_rosalind(in_text):
    return str(Overlap_Graph(in_text))

def q3c(i= "bioinformatics/rosalind/io/i3c.txt",o = "bioinformatics/rosalind/io/o3c.txt"):
    return rosalind_solve(i,o,overlap_rosalind)