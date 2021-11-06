from data_processors.adj_to_small_p_tree import *


def test_working_translation_for_rosalind_adj(): 
    f = open('bioinformatics/tests/data/ros_p_adj_list.txt','r')
    raw_data = f.readlines()
    f.close()
    tree = to_tree(string_to_adj_list(raw_data))
    assert len(tree.leaves())==4
    assert len(tree.nodes)==7
    assert (tree.root)=='6'


    