def rosalind_solve(filei,filej,func):
    f = open(filei,"r")
    w1 = f.readline().rstrip('\n')
    w2 = f.readline().rstrip('\n')
    f.close()
    o  = func(w1,w2)
    f = open(filej,"w")
    f.writelines(o)
    f.close()