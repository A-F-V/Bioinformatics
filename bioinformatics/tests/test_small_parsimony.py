from algorithms.small_parsimony import small_parsimony
from data_processors.adj_to_small_p_tree import *
def test_small_parsimony():
    """
    Test small parsimony
    """
    i = "bioinformatics/tests/data/rosalind/oq7f.txt"
    f = open(i,"r")
    n = int(f.readline())
    txt = f.readlines()
    tree = to_tree(string_to_adj_list(txt))
    m = len(tree.nodes[tree.leaves()[0]])
    output = small_parsimony(tree,m)
    assert output.edgecost()==11342