
from algorithms.sequencing_graph import DeBruijn_Graph
from rosalind.rosalind import rosalind_solve

def overlap_rosalind(in_text):
    k = int(in_text[0])
    text = in_text[1]
    return str(DeBruijn_Graph(k,text))

def q3d(i= "bioinformatics/rosalind/io/i3d.txt",o = "bioinformatics/rosalind/io/o3d.txt"):
    return rosalind_solve(i,o,overlap_rosalind)