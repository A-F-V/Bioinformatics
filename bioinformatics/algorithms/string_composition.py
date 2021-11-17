def composition(text,k,ordered=False):
    """
    Computes the composition of a string.
    """
    comp = [text[i:i+k] for i in range(len(text)-k+1)]
    if ordered:
        comp.sort()
    return comp
