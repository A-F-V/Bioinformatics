def reconstruct_from_genome_path(genome_path:list):
    k = len(genome_path[0])
    genome_string = genome_path[0].strip()
    for i in range(1,len(genome_path)):
        node:str =  genome_path[i]
        
        genome_string += genome_path[i].strip()[-1]
    return genome_string