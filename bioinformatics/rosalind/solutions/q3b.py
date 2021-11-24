from algorithms.string_composition import composition
from algorithms.reconstruct_genome_string import reconstruct_from_genome_path
from rosalind.rosalind import rosalind_solve

def reconstruct_rosalind(in_text):
    return reconstruct_from_genome_path(in_text)

def q3b(i= "bioinformatics/rosalind/io/i3b.txt",o = "bioinformatics/rosalind/io/o3b.txt"):
    return rosalind_solve(i,o,reconstruct_rosalind)