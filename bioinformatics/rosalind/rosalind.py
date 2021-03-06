def rosalind_solve(input_file="rosalind/io/i.txt", output_file="rosalind/io/o.txt", func=(lambda x: x)):
    f = open(input_file, "r")
    i = f.readlines()
    i = [x.strip() for x in i] if type(i) == list else i
    f.close()
    o = func(i)
    if output_file == None:
        return o
    f = open(output_file, "w")
    o2 = "\n".join(list(map(lambda x: str(x), o))) if type(o) == list else str(o)
    f.write(o2)
    f.close()
    return o


def parse_rows_of_vectors(rows):
    return list(map(lambda x: tuple(map(float, x.split(' '))), rows))


def vector_to_row(v):
    return ' '.join(map(str, v))
