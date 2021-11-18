
from algorithms.sequencing_graph import DeBruijn_Graph
from algorithms.sequencing_graph import text_to_debruijn
from rosalind.rosalind import rosalind_solve

def debruijn_rosalind(in_text):
    k = int(in_text[0])
    text = in_text[1]
    return str(text_to_debruijn(k,text))

def q3d(i= "bioinformatics/rosalind/io/i3d.txt",o = "bioinformatics/rosalind/io/o3d.txt"):
    return rosalind_solve(i,o,debruijn_rosalind)