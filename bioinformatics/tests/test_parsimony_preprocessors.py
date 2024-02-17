from data_processors.adj_to_small_p_tree import *


def test_working_translation_for_rosalind_adj(): 
    with open('bioinformatics/tests/data/ros_p_adj_list.txt','r') as f:
        raw_data = f.readlines()
    tree = to_tree(string_to_adj_list(raw_data))
    assert len(tree.leaves())==4
    assert len(tree.nodes)==7
    assert (tree.root)=='6'


    