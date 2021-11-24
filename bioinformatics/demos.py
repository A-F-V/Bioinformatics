from algorithms.four_russians_binary_encoding import LCS, Sequence, DNACode
from algorithms.sequencing_graph import paired_kmers_to_debruijn
from algorithms.reconstruct_genome_string import reconstruct_from_paired_kmers
from rosalind.solutions.q9h import q9h
from algorithms.needleman_wunsch import align_needleman
from algorithms.clustering import lloyd_kmeans, add_vector, assign_to_cluster
from random import random
import matplotlib.pyplot as plt
from functools import reduce
from operator import concat
###########
# Example #
###########


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


def paired_kmer_reconstruction():
    pairs = """GAGA|TTGA
    TCGT|GATG
    CGTG|ATGT
    TGGT|TGAG
    GTGA|TGTT
    GTGG|GTGA
    TGAG|GTTG
    GGTC|GAGA
    GTCG|AGAT"""
    pairs = pairs.split('\n')
    pairs = [tuple(i.split("|")) for i in pairs]
    print(pairs)
    print(reconstruct_from_paired_kmers(pairs))

############
# ROSALIND #
############


q9h()

##############
# Playground #
##############


# FourRussianLCS()
