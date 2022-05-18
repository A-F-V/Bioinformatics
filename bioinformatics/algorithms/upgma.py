from platform import node
from re import U
from algorithms.phylogeny_tree import UPGMATree
from algorithms.distance_matrix import DistanceMatrix


def upgma(d_mat: DistanceMatrix):  # O(n^2log(n)) with use of heapq
    """The UPGMA algorithm for constructing an ultrametric tree (a tree where the distance to any leaf from the root is the same). Runs in O(n^2log(n)) time if priority queue is used along with closed formula for merging clusters. This is a greedy algorithm.

    Args:
        d_mat (DistanceMatrix)

    Returns:
        UPPGMATree
    """
    tree = UPGMATree(d_mat.names)
    n = d_mat.size
    while d_mat.size >= 2:
        # 1) Find the two closest clusters
        weight, i, j = d_mat.smallest_ij()
        nodeNew = str(n)
        n += 1
        # 2) Merge
        tree.add_parent(i, j, nodeNew, d_mat.get(i, j))
        di, dj = tree.degree[i], tree.degree[j]
        # 3) Calculate distance of cluster from other clusters using closed formula on pg 25 of Bioinformatics II text book
        scores = {m: (d_mat.get(m, i)*di+d_mat.get(m, j)*dj)/(di+dj) for m in d_mat.names}
        # 4) Update distance matrix
        d_mat.add(nodeNew, scores)
        d_mat.trim(i)
        d_mat.trim(j)
    return tree
