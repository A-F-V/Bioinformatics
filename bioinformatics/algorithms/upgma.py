from platform import node
from re import U
from algorithms.phylogeny_tree import UPGMATree
from algorithms.distance_matrix import DistanceMatrix


def upgma(d_mat:DistanceMatrix): # O(n^2log(n)) with use of heapq
    tree = UPGMATree(d_mat.names)
    n = d_mat.size
    while d_mat.size>=2:
        weight,i,j = d_mat.smallest_ij()
        nodeNew = str(n)
        n+=1
        tree.add_parent(i,j,nodeNew,d_mat.get(i,j))
        di,dj = tree.degree[i],tree.degree[j]
        scores = {m:(d_mat.get(m,i)*di+d_mat.get(m,j)*dj)/(di+dj) for m in d_mat.names} 
        d_mat.add(nodeNew,scores)
        d_mat.trim(i)
        d_mat.trim(j)
    return tree

    