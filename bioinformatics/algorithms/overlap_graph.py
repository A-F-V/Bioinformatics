
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