def rosalind_solve(input_file="rosalind/io/i.txt",output_file="rosalind/io/o.txt",func=(lambda x:x)):
    f = open(input_file,"r")
    i = f.readlines()
    f.close()
    o  = func(i)
    if output_file == None:
        return o
    f = open(output_file,"w")
    o2 = list(map(lambda x:x+"\n",o))
    f.writelines(o2)
    f.close()
    return o