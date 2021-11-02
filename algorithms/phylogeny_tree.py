class PTree:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node,parent):
        self.nodes.append(node)
        self.edges[node] = [parent]
        self.edges[parent].append(node)

