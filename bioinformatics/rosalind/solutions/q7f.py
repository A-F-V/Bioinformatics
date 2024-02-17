from algorithms.small_parsimony import small_parsimony
from data_processors.adj_to_small_p_tree import *

def q7f():
    i = "bioinformatics/rosalind/io/i7f.txt"
    o = "bioinformatics/rosalind/io/o7f.txt"
    with open(i,"r") as f:
        n = int(f.readline())
        txt = f.readlines()
        tree = to_tree(string_to_adj_list(txt))
        f2 = open(o,"w+")
        m = len(tree.nodes[tree.leaves()[0]])
        output = small_parsimony(tree,m)
        f2.write(f"{output.edgecost()}\n{str(output).strip()}")
    f2.close()