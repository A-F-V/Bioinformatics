from algorithms.distance_matrix import DistanceMatrix
from algorithms.limb_length import limb_length_n
from algorithms.additive_phylogeny import additive_phylogeny
from algorithms.upgma import upgma
def q7d():
    i = "rosalind/io/i.txt"
    o = "rosalind/io/o.txt"
    f = open(i,"r")
    n = int(f.readline())
    mat = []
    for _ in range(n):
        mat.append(list(map(int,f.readline().strip().split())))
    d_mat = DistanceMatrix(mat,list(map(str,range(n))),True)
    f2 = open(o,"w+")
    f2.writelines(str(upgma(d_mat)))
    f.close()
    f2.close()