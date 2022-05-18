from platform import node
from re import U
from algorithms.phylogeny_tree import AdditivePhylogenyTree
from algorithms.distance_matrix import DistanceMatrix
import math


def neighbour_joining(d_mat: DistanceMatrix, nextName=None):  # DO NOT USE heaping distance matrix
    if d_mat.size == 2:
        tree = AdditivePhylogenyTree()
        i, j = d_mat.names[0], d_mat.names[1]
        weight = d_mat.get(i, j)
        tree.add_node(i)
        tree.add_node(j, i, weight)
        return tree

    n = d_mat.size
    if nextName is None:
        nextName = n
    #d_mat_p = d_mat.copy()

    # USED TO CALCULATE THE NEXT I AND J
    total_distance = {i: sum([d_mat.get(i, k) for k in d_mat.names]) for i in d_mat.names}

    nexti, nextj, bestscore = None, None, math.inf
    for i in d_mat.names:
        for j in d_mat.names:
            if i != j:
                score = d_mat.get(i, j)*(n-2)-total_distance[i]-total_distance[j]
                if score < bestscore:
                    nexti, nextj, bestscore = i, j, score
                # d_mat_p.set(i,j,score)
    i, j = nexti, nextj
    dij = d_mat.get(i, j)
    scores = {k: (d_mat.get(i, k)+d_mat.get(j, k)-dij)/2 for k in d_mat.names}
    d_mat.add(str(nextName), scores)
    d_mat.trim(i)
    d_mat.trim(j)
    tree = neighbour_joining(d_mat, nextName+1)
    deltaij = (total_distance[i]-total_distance[j])/(n-2)
    li, lj = (dij+deltaij)/2, (dij-deltaij)/2
    tree.add_node(i, str(nextName), li)
    tree.add_node(j, str(nextName), lj)
    return tree
