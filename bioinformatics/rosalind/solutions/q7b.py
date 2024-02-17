from algorithms.distance_matrix import DistanceMatrix
from algorithms.limb_length import limb_length_n

def q7b():
    i = "src/rosalind/io/i.txt"
    o = "src/rosalind/io/o.txt"
    with open(i,"r") as f:
        n = int(f.readline())
        j = f.readline().strip()
        mat = [list(map(int,f.readline().strip().split())) for _ in range(n)]
        d_mat = DistanceMatrix(mat,list(map(str,range(n))))
        f2 = open(o,"w+")
        f2.writelines(str(limb_length_n(j,d_mat)))
    f2.close()
