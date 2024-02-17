
def prefix(i):
    return i[:-1]
def suffix(i):
    return i[1:]


class Graph:
    def __init__(self, nodes:set,edges:dict):
        self.nodes = nodes
        self.edges = {i:edges[i] for i in edges if len(edges[i])!=0}
        
    def __str__(self):
        output = "".join(
            f"{str(so)} -> " + ",".join(map(str, self.edges[so])) + "\n"
            for so in self.edges
            if len(self.edges[so]) != 0
        )
        return output.strip()
    
    def __repr__(self):
        return self.__str__()
    
    def copy(self):
        nodes = self.nodes.copy()
        edges = {i:self.edges[i].copy() for i in self.edges}
        return Graph(nodes,edges)
    
    def add_edge(self,a,b):
        if a in self.edges:
            self.edges[a].add(b)
        else:
            self.edges[a] = {b}
class Overlap_Graph(Graph):
    def __init__(self, patterns):
        nodes = set(patterns)
        edges = {i: {j for j in patterns if prefix(j)==suffix(i)} for i in patterns}
        Graph.__init__(self,nodes,edges)
    
class DeBruijn_Graph(Graph):
    def __init__(self, nodes,edges):
        Graph.__init__(self,nodes,edges)
        
        

def text_to_debruijn(k,text):
    raw_edges = [(text[i:i+k-1],text[i+1:i+k]) for i in range(len(text)-k+1)]
    nodes = {i for i,j in raw_edges}
    edges = {i:set() for i in nodes}
    for i,j in raw_edges:
        edges[i].add(j)
    return DeBruijn_Graph(nodes,edges)

def kmers_to_debruijn(kmers):
    raw_edges = [(prefix(mer),suffix(mer)) for mer in kmers]
    nodes = set([i for i,j in raw_edges]+[j for i,j in raw_edges])
    edges = {i:set() for i in nodes}
    for i,j in raw_edges:
        edges[i].add(j)
    return DeBruijn_Graph(nodes,edges)

def paired_kmers_to_debruijn(paired_kmers): # paired_kmers = [(a_1,b_1),(a_2,b_2),...]
    raw_edges = [((prefix(mer[0]),prefix(mer[1])),(suffix(mer[0]),suffix(mer[1]))) for mer in paired_kmers]
    nodes = set([i for i,j in raw_edges]+[j for i,j in raw_edges])
    edges = {i:set() for i in nodes}
    for i,j in raw_edges:
        edges[i].add(j)
    return DeBruijn_Graph(nodes,edges)