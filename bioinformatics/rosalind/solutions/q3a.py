from algorithms.string_composition import composition
from rosalind.rosalind import rosalind_solve

def compose_rosalind(in_text):
    k = int(in_text[0])
    text = in_text[1]
    return composition(text,k,True)

def q3a(i= "bioinformatics/rosalind/io/i3a.txt",o = "bioinformatics/rosalind/io/o3a.txt"):
    return rosalind_solve(i,o,compose_rosalind)