import os
from algorithms.distance_matrix import DistanceMatrix
from algorithms.additive_phylogeny import additive_phylogeny
from algorithms.upgma import upgma
from algorithms.four_russians_binary_encoding import LCS, Sequence, DNACode
from algorithms.sequencing_graph import paired_kmers_to_debruijn
from algorithms.reconstruct_genome_string import reconstruct_from_paired_kmers
from algorithms.neighbour_joining import neighbour_joining
from rosalind.solutions.q10d import q10d
from algorithms.suffix_array import create_suffix_array
from algorithms.needleman_wunsch import align_needleman
from algorithms.clustering import lloyd_kmeans, add_vector, assign_to_cluster
from algorithms.burrows_wheeler import bwt_matching_all, bwt
from random import random
import matplotlib.pyplot as plt
from functools import reduce
from operator import concat


top_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

##############
# Additional #
##############


def flatten(l):
    return reduce(concat, l)


def k_means_clustering_demo():
    k = 2
    C = [(0, 0), (0, 10), (-5, 0), (5, 5)]

    def gen_points(centre, n):
        output = []
        for i in range(n):
            output.append(add_vector(centre, (random()*4-2, random()*4-2)))
        return output
    n = 20
    points = flatten([gen_points(i, 50) for i in C])
    centres = lloyd_kmeans(points, k)

    assignments = [(point, assign_to_cluster(point, centres)) for point in points]
    clusters = {i: [] for i in range(len(centres))}
    for p, i in assignments:
        clusters[i].append(p)
    colors = ['r', 'g', 'b', 'y']
    for cluster in clusters:
        plt.scatter([i[0] for i in clusters[cluster]], [i[1] for i in clusters[cluster]], c=colors[cluster])
    plt.savefig("out/img/clusters.png")


def FourRussianLCS():
    n = 3000
    s1 = Sequence(DNACode, n).random()
    s2 = Sequence(DNACode, n).random()
    print(s1 == s2)
    print(LCS(s1, s2))


###########
# Example #
###########


def run_additive_phylogeny():
    path = os.path.join(top_dir, "example_data", "additive_phylogeny.txt")
    d_matrix = DistanceMatrix.from_txt_file(path)
    tree = additive_phylogeny(d_matrix)
    print(tree)


def run_upgma():
    path = os.path.join(top_dir, "example_data", "upgma.txt")
    d_matrix = DistanceMatrix.from_txt_file(path, with_ij_queue=True)  # needed for fast algorithm
    tree = upgma(d_matrix)
    print(tree)
    tree.draw()


def run_neighbour_joining():
    path = os.path.join(top_dir, "example_data", "neighbour_joining.txt")
    d_matrix = DistanceMatrix.from_txt_file(path, with_ij_queue=False)
    tree = neighbour_joining(d_matrix)
    print(tree)
    tree.draw()
############
# ROSALIND #
############


##############
# Playground #
##############

run_neighbour_joining()
