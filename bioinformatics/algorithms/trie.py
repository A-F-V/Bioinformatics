

class Trie:
    def __init__(self, nodes, labelled_edges, root, terminals):
        self.root = root
        self.nodes = nodes
        self.edges = {}  # give from and gives some to+value pairs
        for so, val in labelled_edges:
            si = labelled_edges[(so, val)]
            if so in self.edges:
                self.edges[so].append((si, val))
            else:
                self.edges[so] = [(si, val)]
        self.labelled_edges = labelled_edges  # give from and val and I give to
        self.parent = {labelled_edges[(so, val)]: so for so, val in labelled_edges}  # get reverse edges
        self.edge_values = {(so, labelled_edges[(so, val)]): val for so, val in labelled_edges}
        self.terminals = terminals  # these represent the positions that are the end of patterns

    def __str__(self):
        edges_strings = []
        for sr, val in self.labelled_edges:
            si = self.labelled_edges[(sr, val)]
            edges_strings.append(f"{sr}->{si}:{val}")
        return '\n'.join(edges_strings)

    def __repr__(self):
        return self.__str__()

    def reconstruct_word(self, end_node):
        """
        Given the end node, reconstruct the word
        """
        path = [end_node]
        while path[0] != self.root:
            path.insert(0, self.parent[path[0]])
        word = ""
        for i in range(len(path) - 1):
            word += self.edge_values[(path[i], path[i + 1])]
        return word

    def prefix_match(self, word):
        """
        Returns all the node positions of patterns matched by part or all of "word"
        """
        terminals_passed = []
        current_node = self.root
        for char in word:
            if (current_node, char) not in self.labelled_edges:
                return terminals_passed
            next_node = self.labelled_edges[(current_node, char)]
            if next_node in self.terminals:
                terminals_passed.append(next_node)
            current_node = next_node
        return terminals_passed

    def compress_non_branching_path(self):
        """
        Will take the trie and for all paths that don't branch, it will compress the path into 1 edge. All terminals (i.e. the end pos of a pattern) must be a leaf otherwise breaks trie. This is why adding the special dollar character is important as it fixes this problem.
        Needs to clean edges, labelled_edges, parent and edge_values
        """
        def compress(edges_used):
            if(len(edges_used) <= 1):
                return
            word = "".join(map(lambda x: x[1], edges_used))
            nodes = list(map(lambda x: x[0], edges_used))
            start = nodes[0]
            end = self.labelled_edges[(nodes[-1], word[-1])]

            for i in range(0, len(edges_used)):  # cleans edges,labelled_edges,parent,edge_values for all interior nodes
                node = edges_used[i][0]
                char = edges_used[i][1]
                next_node = end if i == len(edges_used)-1 else edges_used[i + 1][0]
                if i == 0:
                    self.edges[start].remove((next_node, char))
                    del self.labelled_edges[(start, char)]
                    del self.edge_values[(start, next_node)]
                else:
                    del self.edges[node]
                    del self.labelled_edges[(node, char)]
                    del self.parent[node]
                    del self.edge_values[(node, next_node)]
                    self.nodes.remove(node)
            # performs compression which is on start and end

            self.edges[start].append((end, word))
            self.labelled_edges[(start, word)] = end
            self.parent[end] = start
            self.edge_values[(start, end)] = word

        def dfs(start):
            stack = []
            for edge in list(self.edges[start]):
                char = edge[1]
                stack.append([(start, char)])
            while len(stack) > 0:
                path = stack.pop()
                char = path[-1][1]
                last_node = path[-1][0]
                current_node = self.labelled_edges[(last_node, char)]

                done = self.node_is_leaf(current_node)
                if done:
                    compress(path)
                else:
                    branches = len(self.edges[current_node]) > 1
                    if branches:
                        compress(path)
                        for edge in list(self.edges[current_node]):
                            next_char = edge[1]
                            stack.append([(current_node, next_char)])
                    else:
                        next_char = self.edges[current_node][0][1]
                        stack.append(path + [(current_node, next_char)])

        def rec(edges_used):  # make non recursive
            char = edges_used[-1][1]
            last_node = edges_used[-1][0]
            current_node = self.labelled_edges[(last_node, char)]

            done = current_node not in self.edges or len(self.edges[current_node]) == 0
            if done:
                compress(edges_used)
            else:
                branches = len(self.edges[current_node]) > 1
                if branches:
                    compress(edges_used)
                    for edge in list(self.edges[current_node]):
                        next_char = edge[1]
                        rec([(current_node, next_char)])
                else:
                    next_char = self.edges[current_node][0][1]
                    rec(edges_used + [(current_node, next_char)])

        # because compress alters this list, we need to make a copy before we do loop
       # for edge in list(self.edges[self.root]):
       #     char = edge[1]
       #     rec([(self.root, char)])
        dfs(self.root)
        for node in self.edges:
            assert len(self.edges[node]) >= 2

    def node_is_leaf(self, node):
        return node not in self.edges or len(self.edges[node]) == 0


class SuffixTrie(Trie):
    def __init__(self, nodes, edges, root, terminals):
        Trie.__init__(self, nodes, edges, root, terminals)

    def get_suffix_terminal_node(self, i):
        return self.terminals[i]

    def get_longest_repeat_string(self):
        """
        Finds the longest path to a penultimate node.
        """
        def long_path(node, pre_text):
            if self.node_is_leaf(node):
                return ""
            else:
                best = pre_text
                for next_node, text in self.edges[node]:
                    attempt = long_path(next_node, pre_text + text)
                    if len(attempt) > len(best):
                        best = attempt
                return best
        return long_path(self.root, "")


def create_trie(words):
    nodes = set([0])
    root = 0
    edges = {}
    nextNode = 1
    terminals = set()
    for word in words:
        currentNode = root
        for char in word:
            if (currentNode, char) in edges:
                currentNode = edges[(currentNode, char)]
            else:
                edges[(currentNode, char)] = nextNode
                currentNode = nextNode
                nodes.add(nextNode)
                nextNode += 1
        terminals.add(currentNode)
    terminals = sorted(list(terminals))
    return Trie(nodes, edges, root, terminals)


def match_text_to_patterns(text, patterns):
    """
    Returns all indices where the text matches a pattern
    """
    trie = create_trie(patterns)
    matches = []
    for i in range(len(text)):
        if len(trie.prefix_match(text[i:])) != 0:
            matches.append(i)
    return matches


def create_suffix_trie(text, has_dollar=True):
    if not has_dollar:
        text += "$"
    patterns = map(lambda i: text[i:], range(len(text)))
    trie = create_trie(patterns)
    trie.compress_non_branching_path()
    return SuffixTrie(trie.nodes, trie.labelled_edges, trie.root, trie.terminals)
