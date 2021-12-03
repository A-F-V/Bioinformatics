from algorithms.distance_matrix import DistanceMatrix
from algorithms.limb_length import limb_length_n

def q7b():
    i = "src/rosalind/io/i.txt"
    o = "src/rosalind/io/o.txt"
    f = open(i,"r")
    n = int(f.readline())
    j = f.readline().strip()
    mat = []
    for _ in range(n):
        mat.append(list(map(int,f.readline().strip().split())))
    d_mat = DistanceMatrix(mat,list(map(str,range(n))))
    f2 = open(o,"w+")
    f2.writelines(str(limb_length_n(j,d_mat)))
    f.close()
    f2.close()
