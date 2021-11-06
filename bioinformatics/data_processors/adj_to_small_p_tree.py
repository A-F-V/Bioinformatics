from algorithms.binary_tree import BinaryTree

#todo

def string_to_adj_list(s:list):
    """
    Convert a string representation of an adjacency list to a list of edges
    """
    adj_list = []
    for line in s:
        if line.strip()=="":
            continue
        edge = line.strip().split("->")
        adj_list.append(edge)
    return adj_list


def to_tree(adj_list):
    """
    Convert an adjacency list of a leaves only tree to an actual tree object
    Set values of interior nodes to ""
    """
    nodes = {}
    edges = {}
    leaflabels = 0
    for edge in adj_list:
        parent = edge[0]
        child = edge[1]
        child_name = child
        if not str(child).isdigit():
            nodes[str(leaflabels)] = child
            child_name = str(leaflabels)
            leaflabels += 1
        else:
            nodes[child] = ""
        if parent in edges:
            edges[parent].append((child_name,0))
        else:
            edges[parent] =[(child_name,0)]
    return BinaryTree(nodes, edges,None,"")