from data_processors.adj_to_small_p_tree import *


def test_binary_tree(): 
    with open('bioinformatics/tests/data/ros_p_adj_list.txt','r') as f:
        raw_data = f.readlines()
    tree = to_tree(string_to_adj_list(raw_data))
    assert len(tree.leaves())==4
    assert len(tree.nodes)==7
    assert (tree.root)=='6'

    tree_copy = tree.copy()
    assert len(tree.leaves())==4
    assert len(tree.nodes)==7
    assert (tree.root)=='6'
    for node in tree.nodes:
        assert node in tree_copy.nodes
        assert tree.nodes[node] == tree_copy.nodes[node]

    tree_app = tree_copy.apply(lambda v:"val",lambda v:2)
    assert tree_app.edges['4'][0][1] == 2
    assert tree_app.nodes['1'] == "val"
    assert tree_app.edgecost() == 2*6
