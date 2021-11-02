from algorithms.phylogeny_tree import PTree

def additive_phylogeny(d_mat):
    tree = PTree()
    while d_mat.size>1:
        (dij,i,j) = d_mat.smallest_ij()
        mscores = {}
        for k in d_mat.names:
            if k!=i and k!=j:
                dmk = (d_mat.get(i,k)+d_mat.get(j,k)-d_mat(i,j))/2
                mscores[k]=dmk
        
        d_mat.remove(i)
        d_mat.remove(j)
