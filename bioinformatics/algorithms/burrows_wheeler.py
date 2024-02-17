from re import L


def bwt(text, s_array=None):
    """
    Burrows-Wheeler transform
    :param text: string
    :param s_array: suffix array
    :return: BWT of text
    """
    if s_array is not None:
        return "".join(text[-1] if s_i == 0 else text[s_i-1] for s_i in s_array)
    c_rot = [text[i:] + text[:i] for i in range(len(text))]
    c_rot = sorted(c_rot)
    return "".join(map(lambda x: x[-1], c_rot))


def number_letters(text):
    numberings = {}
    output = []
    for i in text:
        if i not in numberings:
            numberings[i] = 1
        output.append(f'{i}_{numberings[i]}')
        numberings[i] += 1
    return output


def index_list(li):
    return {li[i]: i for i in range(len(li))}


def first_col_from_bwt(bwt):
    return "".join(sorted(list(bwt)))


def last_to_first_mapping(bwt):
    f_col = number_letters(first_col_from_bwt(bwt))
    l_col = number_letters(bwt)
    indexed_f_col = index_list(f_col)
    return {i: indexed_f_col[l_col[i]] for i in range(len(l_col))}


def inverse_bwt(bwt):
    """
    Given the BWT, construct original text
    """
    first_col = first_col_from_bwt(bwt)
    fcol = number_letters(first_col)
    lcol = number_letters(bwt)
    lcol_indexed = index_list(lcol)
    output = ["$_1"]
    terminator = lcol[0]
    while True:
        forward_i = lcol_indexed[output[-1]]
        output.append(fcol[forward_i])
        if output[-1] == terminator:
            break
    return ("".join(map(lambda x: x[0], output)))[1:]+"$"


def find_col_letter_range(col, letter, start, end):  # can be precomputed to speed up
    """
    Find the range of indices of a letter in a column between start and end
    range is inclusive at first, exclusive at last.
    This means that the first letter is at first and last occurence is at last
    """
    first, last = -1, -1
    for i in range(start, end):
        if col[i][0] == letter:
            first = i if first == -1 else first
            last = i+1
    return first, last


def bwt_matching(first_col, last_col, pattern, ltf_mapping):  # O(n^2) but can be made into O(n)
    """
    Gives the ranges of matches for each pattern.
    first and last column are NUMBERED
    """
    first_index, last_index = find_col_letter_range(first_col, pattern[-1], 0, len(first_col))
    if first_index == -1:
        return (-1, -1)
    for pos in range(len(pattern)-2, -1, -1):
        prev_letter = pattern[pos]
        start, end = find_col_letter_range(last_col, prev_letter, first_index, last_index)
        if start == -1 or end == start:
            return (-1, -1)
        first_index, last_index = ltf_mapping[start], ltf_mapping[end-1]+1
    return first_index, last_index


def bwt_matching_all(bwt, patterns):
    f_col, l_col = number_letters(first_col_from_bwt(bwt)), number_letters(bwt)
    ltf_mapping = last_to_first_mapping(bwt)
    return [
        bwt_matching(f_col, l_col, pattern, ltf_mapping)
        for pattern in patterns
    ]
