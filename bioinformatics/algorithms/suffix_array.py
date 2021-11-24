from algorithms.binary_search import BinarySearch


def prefix_pattern_match(ref_text, comp_text):
    """
    Checks to see if the comp_text is the same as the start of ref_text
    """
    return len(comp_text) <= len(ref_text) and ref_text[:len(comp_text)] == comp_text


class SuffixArray:
    def __init__(self, indices, text):
        self.indices = indices
        self.text = text

    def suffix(self, i):
        return self.text[self.indices[i]:]

    def find_matching_pattern(self, pattern):
        def comparer(x):
            return 0 if prefix_pattern_match(x, pattern) else (-1 if x < pattern else 1)
        searcher = BinarySearch(0, len(self.indices)-1, comparer, emitter=self.suffix)
        frm, to = searcher.search(first=True), searcher.search(first=False)
        if frm == None or to == None:
            return []
        print((frm, to))
        output = [self.indices[i] for i in range(frm, to+1)]
        for i in output:
            print(self.suffix(i))
        return output


def create_suffix_array(text, has_dollar=True):
    """
    Create suffix array of the string text in O(n^2 logn)
    """
    # if not has_dollar:
    #    text += "$"
    n = len(text)
    # sort the suffixes, then map sorted elements to their suffix_index
    indices = list(map(lambda x: n-len(x), sorted(map(lambda i: text[i:], range(n)))))
    return SuffixArray(indices, text)
