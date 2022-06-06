from algorithms.distance_matrix import DistanceMatrix
from algorithms.phylogeny_tree import AdditivePhylogenyTree
from algorithms.limb_length import limb_length_n
#
# def additive_phylogeny(d_mat):
#    tree = PTree()
#    while d_mat.size>1:
#        (dij,i,j) = d_mat.smallest_ij()
#        mscores = {}
#        for k in d_mat.names:
#            if k!=i and k!=j:
#                dmk = (d_mat.get(i,k)+d_mat.get(j,k)-d_mat(i,j))/2
#                mscores[k]=dmk
#
#        d_mat.remove(i)
#        d_mat.remove(j)

# Finds the phylogeny tree of the given distance matrix

# DELETE The nextlabel specifies the name to assign to the next leaf (the first leaf in distance matrix) defaulting to 1 (so that the tree is labelled 1 to n).


def additive_phylogeny(d_mat: DistanceMatrix, inner_node_next_label=None):
    """Performs the additive phylogeny algorithm on the given distance matrix.  This is a recurisve algorithm, so base and inductive cases need to be considered.

    Args:
        d_mat (DistanceMatrix): The distance matrix to use.
        inner_node_next_label (int): The next label to assign to an inner node.

    Raises:
        Error: upon failure to construct tree if, for example, it is non additive.

    Returns:
        AdditivePhylogenyTree: The resulting tree.
    """
    if inner_node_next_label is None:
        inner_node_next_label = d_mat.size+1
    # BASE CASE
    if d_mat.size == 1:
        t = AdditivePhylogenyTree()
        t.add_node(d_mat.names[0])
        return t
    if d_mat.size == 2:
        t = AdditivePhylogenyTree()
        a, x = d_mat.names[0], d_mat.names[1]
        t.add_node(a)
        t.add_node(x, a, d_mat.get(a, x))
        return t
    # INDUCTIVE CASE
    else:
        # 1) Select node, find its limb length, balden and trim.
        x = d_mat.names[0]
        l_x = int(limb_length_n(x, d_mat))
        d_bald = d_mat.balden(x, l_x)
        # Needed for the combination step. Correspond to two leaves that are in different subtrees relative to x.
        _, a, b = limb_length_n(x, d_bald, True)
        d_ax = d_bald.get(a, x)  # distance from a to x's parent along path to b
        d_trim = d_bald.trim(x)

        # 2) Recurse on the smaller problem (d_trim)
        tree = additive_phylogeny(d_trim, inner_node_next_label+1)

        # 3) Attach the leaf to the tree at the corresponding point.
        # i and k are in different subtrees and the path between them goes through the parent of j.
        path = tree.shortest_path(a, b)
        # Go along path until you find edge/node where attaching j to will make distance from j to i equal to the distance in matrix.
        count = 0
        for (v_i, weight, v_j) in path:
            count += weight
            if count == d_ax:
                # attach to v_j directly
                tree.add_node(x, v_j, l_x)
                return tree
            if count > d_ax:
                mid = tree.cut(v_i, v_j, weight-(count-d_ax), inner_node_next_label)
                tree.add_node(x, mid, l_x)
                return tree
        raise "Unable to create tree"
