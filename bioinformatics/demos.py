from algorithms.four_russians_binary_encoding import LCS, Sequence,DNACode
from algorithms.sequencing_graph import paired_kmers_to_debruijn
from algorithms.reconstruct_genome_string import reconstruct_from_paired_kmers
from rosalind.q3j import q3j
from rosalind.q7f import q7f
from algorithms.needleman_wunsch import align_needleman
###########
# Example #
###########
def FourRussianLCS():
    n= 3000
    s1 = Sequence(DNACode,n).random()
    s2 = Sequence(DNACode,n).random()
    print(s1==s2)
    print(LCS(s1,s2))

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

q3j()

##############
# Playground #
##############




#FourRussianLCS()

