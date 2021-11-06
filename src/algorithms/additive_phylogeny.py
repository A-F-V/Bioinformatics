from msilib.schema import Error
from algorithms.distance_matrix import DistanceMatrix
from algorithms.phylogeny_tree import PTree
from algorithms.limb_length import limb_length_n
#
#def additive_phylogeny(d_mat):
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

#Finds the phylogeny tree of the given distance matrix
def additive_phylogeny(d_mat,nextname=None):#DO NOT USE heaping distance matrix
    if nextname is None:
        nextname = d_mat.size
        # Case 1, d_mat is just for a single element
    if d_mat.size==1:
        t = PTree()
        t.add_node(d_mat.names[0])
        return t
    if d_mat.size==2:
        t = PTree()
        i,j = d_mat.names[0],d_mat.names[1]
        t.add_node(i)
        t.add_node(j,i,d_mat.get(i,j))
        return t
    else:
        #select arbitrary element to reduce with
        j = d_mat.names[0]
        lj = int(limb_length_n(j,d_mat))
        d_bald = d_mat.balden(j,lj)
        _,i,k = limb_length_n(j,d_bald,True)
        x = d_bald.get(i,j)#distance from i to j's parent along path to k
        d_trim = d_bald.trim(j)
        tree = additive_phylogeny(d_trim,nextname+1)
        print(str(tree)+"\n"*3)
        # find the parent of j in the sub tree. This will be a distance of x from i to k
        path = tree.shortest_path(i,k) 
        #path.stop at distance x
        count = 0
        for (a,weight,b) in path:
            count +=weight
            if count==x:
                #attach to b
                tree.add_node(j,b,lj)
                return tree
            if count>x:
                m = tree.cut(a,b,weight-(count-x),nextname)
                tree.add_node(j,m,lj)
                return tree
        raise Error 



