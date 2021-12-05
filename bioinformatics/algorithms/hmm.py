from math import log, inf
from functools import lru_cache, reduce


class TransitionMatrix:
    def __init__(self, states, transitions):
        self.states = states
        self.transitions = transitions

    def empty():
        return TransitionMatrix([], {})

    def __getitem__(self, key):
        return self.transitions[key]


class EmissionMatrix:
    def __init__(self, states, symbols, emissions):
        self.states = states
        self.symbols = symbols
        self.emissions = emissions

    def empty():
        return EmissionMatrix([], [], {})

    def __getitem__(self, key):
        return self.emissions[key]


class ViterbiGraph:
    def __init__(self, hmm, x, f, f_iter, default, start_val, options={"fair": True}):
        """
        The value at each node is f_iter of f applied to each edge with node, with default being initial value
        """
        self.hmm = hmm
        self.x = x
        self.options = options
        self.f = f  # function of edge, prev state, curr state, i and the graph(to get DP)
        self.f_iter = f_iter
        self.start_val = start_val
        self.default = default

    @lru_cache
    def forward(self):
        graph = {(0, "START"): self.start_val}
        for i in range(1, len(self.x) + 2):
            for state in self.hmm.states if i <= len(self.x) else ["END"]:
                if i == 1:
                    edge = (1/len(self.hmm.states) if self.options["fair"]
                            else 1) * self.hmm.emissions[(state, self.x[0])]
                    graph[(i, state)] = self.f_iter(self.default, self.f(edge, "START", state, i, graph))
                else:
                    edges = [self.f((self.hmm.transitions[(prev_state, state)] *
                                    self.hmm.emissions[state, self.x[i-1]]) if state != "END" else 1,
                                    prev_state, state, i, graph) for prev_state in self.hmm.states]  # gets weight and applies f
                    graph[i, state] = reduce(self.f_iter, edges, self.default)
        self.graph = graph

    def backward(self):
        output = ""
        current = "END"
        for i in range(len(self.x)+1, 1, -1):
            prev_state = self.graph[i, current][1]
            output = prev_state+output
            current = prev_state
        return output

    def __getitem__(self, key):
        if key == "START":
            return self.graph[0, "START"]
        if key == "END":
            return self.graph[len(self.x)+1, "END"]
        return self.graph[key]


class HMM:
    def __init__(self, symbols, states, transitions: TransitionMatrix, emissions: EmissionMatrix, options={"fair": True}):
        self.symbols = symbols
        self.states = states
        self.transitions = transitions
        self.emissions = emissions
        self.options = options

    def hidden_path_prob(self, pi):
        prob = 1/len(self.states) if self.options["fair"] else 1
        for edge in zip(pi[:-1], pi[1:]):
            prob *= self.transitions[edge]
        return prob

    def cond_visible_path_prob(self, x, pi):
        prob = 1
        for edge in zip(pi, x):
            prob *= self.emissions[edge]
        return prob

    def viterbi(self, x):
        def f(edge, prev_state, curr_state, i, graph):
            return (log(edge)+graph[i-1, prev_state][0], prev_state)

        def f_iter(prev_best, fedge):  # argmax
            return fedge if prev_best[0] < fedge[0] else prev_best

        graph = ViterbiGraph(self, x, f, f_iter, (-inf, "START"),
                             (1/len(self.states) if self.options["fair"] else 1, "START"))
        graph.forward()
        return graph.backward()

    def visible_path_prob(self, x):
        return self.forward(x)["END"]

    def forward(self, x):
        def f(edge, prev_state, curr_state, i, graph):
            return edge*graph[i-1, prev_state]

        def f_iter(prev, fedge):  # sum
            return prev+fedge

        graph = ViterbiGraph(self, x, f, f_iter, 0, 1)
        graph.forward()
        return graph
