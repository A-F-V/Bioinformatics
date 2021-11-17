def rosalind_solve(input_file="rosalind/io/i.txt",output_file="rosalind/io/o.txt",func=(lambda x:x)):
    f = open(input_file,"r")
    i = f.readlines()
    i = [x.strip() for x in i] if type(i)== list else i
    f.close()
    o  = func(i)
    if output_file == None:
        return o
    f = open(output_file,"w")
    o2 = list(map(lambda x:x+"\n",o)) if type(o) == list else o
    f.write(o2)
    f.close()
    return o
    f.writelines(o2)
    f.close()
    return o