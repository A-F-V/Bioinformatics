from algorithms.distance_matrix import DistanceMatrix
from algorithms.limb_length import limb_length_n
from algorithms.additive_phylogeny import additive_phylogeny
from algorithms.upgma import upgma
def q7d():
    i = "src/rosalind/io/i.txt"
    o = "src/rosalind/io/o.txt"
    with open(i,"r") as f:
        n = int(f.readline())
        mat = [list(map(int,f.readline().strip().split())) for _ in range(n)]
        d_mat = DistanceMatrix(mat,list(map(str,range(n))),True)
        f2 = open(o,"w+")
        f2.writelines(str(upgma(d_mat)))
    f2.close()