import copy


class BinaryTree: # Simple so no node as degree 2 other than root
    '''
    Dictionary Based Implementation
    '''
    def __init__(self,nodes,edges,root=None,val=0): 
        self.nodes = nodes #a dict of node name to val pairs
        self.edges = edges # a dict of node name to a list of neighbours (child name, edgeval)
        self.root = root #the name of the root
        if self.root is None:
            self.root = list(set(self.edges.keys()) - set(self.nodes.keys()))[0]
            self.nodes[self.root] = val

    def is_leaf(self,node):
        return node not in self.edges

    def leaves(self,node="ROOT"):

        if node == "ROOT":
            return self.leaves(self.root)
        if node is None:
            return []
        if self.is_leaf(node):
            return [node]
        else:
            return self.leaves(self.left(node)[0]) + self.leaves(self.right(node)[0]) #ignore weight

    def rec_make_tree(root,val,leftedge,rightedge,left,right):
        nodes = {root:val,**left.nodes,**right.nodes}
        edges = {root:[(left.root,leftedge),(right.root,rightedge)],**left.edges,**right.edges}
        return BinaryTree(nodes,edges,root)

    def left(self,node):
        if node in self.edges:
            children = self.edges[node]
            if len(children) >=1:
                return children[0]
        return None

    def right(self,node):
        if node in self.edges:
            children = self.edges[node]
            if len(children) >=2:
                return children[1]
        return None

    def edgecost(self,node="ROOT"):
        if node == "ROOT":
            return self.edgecost(self.root)
        if self.is_leaf(node):
            return 0
        ln,lw = self.left(node)
        rn,rw = self.right(node)
        return lw+rw+self.edgecost(ln)+self.edgecost(rn)

    def copy(self):
        return BinaryTree(copy.deepcopy(self.nodes),copy.deepcopy(self.edges),self.root,self.nodes[self.root])

    def apply(self,fv,fe):
        self.nodes = {n:fv(self.nodes[n]) for n in self.nodes}
        self.edges = {k:list(map(lambda p:(p[0],fe(p[1])),self.edges[k])) for k in self.edges}
        return self
    
    def merge(self,other,fv,fe): # Can be improved a lot
        self.nodes = {n:fv(self.nodes[n],other.nodes[n]) for n in self.nodes}
        final_edges = {}
        for f in self.edges:
            final_edges[f] = []
            for edge1 in self.edges[f]:
                t1 = edge1[0]
                weight1 = edge1[1]
                for edge2 in other.edges[f]:
                    t2 = edge2[0]
                    if t1==t2:
                        weight2= edge2[1]
                        final_edges[f].append((t1,fe(weight1,weight2)))

        self.edges = final_edges
        return self

    def __str__(self,both=True):
        output = ""
        for f in self.edges:
            for edge in self.edges[f]:
                tval = self.nodes[edge[0]]
                weight = edge[1]
                fval = self.nodes[f]
                output += f"{fval}->{tval}:{weight}\n"
                if both:
                    output += f"{tval}->{fval}:{weight}\n"
        return output