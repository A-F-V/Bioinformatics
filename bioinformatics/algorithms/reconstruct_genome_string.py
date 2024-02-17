from algorithms.eulerian_cycle import eulerian_path
from algorithms.sequencing_graph import kmers_to_debruijn
from algorithms.four_russians_binary_encoding import Sequence
from algorithms.eulerian_cycle import eulerian_cycle
from algorithms.sequencing_graph import paired_kmers_to_debruijn


def reconstruct_from_genome_path(genome_path:list):
    k = len(genome_path[0])
    genome_string = str(genome_path[0]).strip()
    for i in range(1,len(genome_path)):
        node:str =  genome_path[i]
        
        genome_string += str(genome_path[i]).strip()[-1]
    return genome_string

def reconstruct_from_kmers(kmers:list):
    graph = kmers_to_debruijn(kmers)
    genome_path = eulerian_path(graph)
    return reconstruct_from_genome_path(genome_path)

def construct_k_universal_circular_string(k:int):
    kmers = list(Sequence(["0","1"],k))
    graph = kmers_to_debruijn(kmers)
    genome_path = eulerian_cycle(graph)
    return reconstruct_from_genome_path(genome_path)[:-(k-1)]
    
def reconstruct_from_paired_kmers(paired_kmers:list,k:int,d:int):
    graph = paired_kmers_to_debruijn(paired_kmers)
    genome_path = eulerian_path(graph)
    upper_path = reconstruct_from_genome_path(list(map(lambda x:x[0],genome_path)))
    lower_path = reconstruct_from_genome_path(list(map(lambda x:x[1],genome_path)))
    return upper_path + lower_path[-(k+d):]