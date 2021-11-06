#import flatten

def flatten_list(l):
    """
    Flatten a list of lists
    """
    return [item for sublist in l for item in sublist]

class PTree:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node,parent=None,weight=0):
        self.nodes.append(node)
        if parent != None:
            self.edges[node] = {parent:weight}
            self.edges[parent][node] = weight
        else:
            self.edges[node] = {}

    def connect(self,a,b,weight):
        if a in self.nodes and b in self.nodes:
            self.edges[a][b] = weight
            self.edges[b][a] = weight

    def is_neighbour(self,i,k):
        return k in self.edges[i]

    def shortest_path(self,i,k):
        queue = [i]
        visited = set()
        visited.add(i)
        parents = {i:None}
        while queue:
            node = queue.pop(0)
            for neighbour in self.edges[node]:
                if neighbour == k:
                    path = [(node,self.edges[node][k],k)]
                    last_move = path[0]
                    while last_move[0]!=i:
                        child = last_move[0]
                        parent  = parents[child]
                        weight = self.edges[parent][child]
                        path.insert(0,(parent,weight,child))
                        last_move = path[0]
                    return path
                if neighbour not in visited:
                    parents[neighbour] = node
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False

    def cut(self,i,j,amt,name=None):
        m = name if name != None else f"({str(i)},{str(j)})"
        if(self.is_neighbour(i,j)):
            length = self.edges[i][j]
            self.edges[i].pop(j)
            self.edges[j].pop(i)
            self.add_node(m)
            self.edges[m]= {i:amt,j:length-amt}
            self.edges[i][m] = amt
            self.edges[j][m] = length-amt
            return m

    def __str__(self):
        return "\n".join(flatten_list([[f"{i}->{j}:{weight}" for j,weight in self.edges[i].items()] for i in self.nodes]))

    def __repr__(self):
        return self.__str__()

class UPGMATree:
    def __init__(self,leafs):
        self.nodes = {leaf:0 for leaf in leafs}
        self.edges = {leaf:{} for leaf in leafs}
        self.degree = {leaf:1 for leaf in leafs}

    def add_parent(self,a,b,parent,diameter_weight):
        height = diameter_weight/2
        self.degree[parent] = self.degree[a] + self.degree[b]
        self.nodes[parent] = height
        aheight,bheight = self.nodes[a],self.nodes[b]
        self.edges[parent] = {a:height-aheight,b:height-bheight}
        self.edges[a][parent] = height-aheight
        self.edges[b][parent] = height-bheight

    def __str__(self):
        return "\n".join(flatten_list([[f"{i}->{j}:{weight}" for j,weight in self.edges[i].items()] for i in self.nodes]))

    def __repr__(self):
        return self.__str__()

    