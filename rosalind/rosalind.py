def rosalind_solve(filei="rosalind/io/i.txt",filej="rosalind/io/o.txt",func=(lambda x:x)):
    f = open(filei,"r")
    w1 = f.readline().rstrip('\n')
    w2 = f.readline().rstrip('\n')
    f.close()
    o  = func(w1,w2)
    f = open(filej,"w")
    f.writelines(o)
    f.close()