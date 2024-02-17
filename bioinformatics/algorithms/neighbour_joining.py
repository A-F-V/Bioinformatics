from platform import node
from re import U
from algorithms.phylogeny_tree import AdditivePhylogenyTree
from algorithms.distance_matrix import DistanceMatrix
import math


def neighbour_joining(d_mat: DistanceMatrix, inner_node_next_label=None):    # DO NOT USE heaping distance matrix
    """Performs the neighbour joining algorithm on the given distance matrix.  This is a recurisve algorithm, so base and inductive cases need to be considered. It is also a greedy algorithm in which the closest pair of nodes in the augmented distance matrix are joined.

    Args:
        d_mat (DistanceMatrix): The distance matrix to use.
        inner_node_next_label (int, optional): The next label to assign to an inner node. Defaults to None.

    Returns:
        AdditivePhylogenyTree: The resulting unrooted tree as in the additive phylogeny algorithm.
    """
    # BASE CASE, join only two nodes together.
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

    # INDUCTIVE CASE
    # 1) Compute total_distance for each element in distance matrix
    total_distance = {
        i: sum(d_mat.get(i, k) for k in d_mat.names) for i in d_mat.names
    }

    # 2) Find nodes which are closest to one another in D*, which is the same matrix except D*i,j = (n-2)*Dij - TotalDistance(i) - TotalDistance(j). The matrix is not explicitly stored, but its entries are searched.
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

    # 3) Compute the distance of the joined nodes to all other nodes. This amounts to using the formula (dik+djk-dij)/2. This gives the distance of the parent of i and j to any other node k. Can be derived by drawing out what happens when you consider these 3(4) nodes.
    scores = {k: (d_mat.get(i, k)+d_mat.get(j, k)-dij)/2 for k in d_mat.names}
    # 4) The neighbours i and j are joined / merged. They are removed from the matrix, and a new node is added.
    d_mat.add(str(nextName), scores)
    d_mat.trim(i)
    d_mat.trim(j)
    # 5) We generate the phylogeny tree for the rest of the n-2 +1 nodes.
    tree = neighbour_joining(d_mat, nextName+1)

    # 6) We now attach i and j to the parent (the merged/joined version of them). To do this, we need to find the limb length, that is the distance of i (or j) to the parent. This is calculated with the below formula. Please consult textbook for further elaboration.
    deltaij = (total_distance[i]-total_distance[j])/(n-2)
    li, lj = (dij+deltaij)/2, (dij-deltaij)/2
    tree.add_node(i, str(nextName), li)
    tree.add_node(j, str(nextName), lj)
    return tree
