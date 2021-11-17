
def prefix(i):
    return i[:-1]
def suffix(i):
    return i[1:]

class Overlap_Graph:
    def __init__(self, patterns):
        self.nodes = patterns
        self.edges = {i:set([j for j in patterns if prefix(j)==suffix(i)])for i in patterns}
        
    def __str__(self):
        output = ""
        for so in self.edges:
            for si in self.edges[so]:
                output += so + " -> " + si + "\n"
        return output
    
    def __repr__(self):
        return self.__str__()
    
class DeBruijn_Graph:
    def __init__(self, nodes,edges):
        self.nodes = nodes
        self.edges = edges
        
        
    def __str__(self):
        output = ""
        for so in self.edges:
            output += so + " -> " + ",".join(self.edges[so]) + "\n"
        return output.strip()
    
    def __repr__(self):
        return self.__str__()
    

def text_to_debruijn(k,text):
    raw_edges = [(text[i:i+k-1],text[i+1:i+k]) for i in range(len(text)-k+1)]
    nodes = set([i for i,j in raw_edges])
    edges = {i:[] for i in nodes}
    for i,j in raw_edges:
        edges[i].append(j)
    return DeBruijn_Graph(nodes,edges)

def kmers_to_debruijn(kmers):
    raw_edges = [(prefix(mer),suffix(mer)) for mer in kmers]
    nodes = set([i for i,j in raw_edges])
    edges = {i:[] for i in nodes}
    for i,j in raw_edges:
        edges[i].append(j)
    return DeBruijn_Graph(nodes,edges)