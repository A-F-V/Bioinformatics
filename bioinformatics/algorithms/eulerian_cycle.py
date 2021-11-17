from algorithms.sequencing_graph import Graph

def random_cycle(start,graph:Graph):
    """
    Find a random cycle in a graph starting and ending at first.
    A non recursive implementation.
    """
    edges = graph.edges
    cycle = [start]
    current = start
    while(current!=start or len(cycle)==1):
        nxt = edges[current].pop()
        if len(edges[current])==0:
            del edges[current]
        cycle.append(nxt)
        current = nxt
    return cycle

def eulerian_cycle(graph:Graph):
    """
    Find an Eulerian cycle in a graph.
    Does not check feasability.
    """
    cgraph = graph.copy()
    start = list(cgraph.nodes)[0]
    cycle = random_cycle(start,cgraph)
    while len(cgraph.edges)>0:
        for i in range(len(cycle)):
            node = cycle[i]
            if node in cgraph.edges: # if node has outgoing edges 
                smaller_cycle = random_cycle(node,cgraph)
                cycle = cycle[:i]+smaller_cycle+cycle[i+1:]
                break
    return cycle

def unbalanced_nodes(graph:Graph):
    """
    Find unbalanced nodes in a graph. Place Natural sinks at start and sources at end.
    """
    in_degree = {i:0 for i in graph.nodes}
    out_degree = {i:0 for i in graph.nodes}
    for source in graph.edges:
        out_degree[source] = len(graph.edges[source])
        for sink in graph.edges[source]:
            in_degree[sink] += 1
    unbalanced = []
    for node in graph.nodes:
        if in_degree[node]<out_degree[node]: # node is a source
            unbalanced.append(node)
        if in_degree[node]>out_degree[node]: # node is a sink
            unbalanced.insert(0,node)
    return unbalanced
        

def eulerian_path(graph:Graph):
    """
    Find an Eulerian path in a graph.
    """
    cgraph = graph.copy()
    pivots = unbalanced_nodes(cgraph)
    cgraph.add_edge(pivots[0],pivots[1])
    path = eulerian_cycle(cgraph)
    crossover = None
    for i in range(len(path)-1):
        if path[i] == pivots[0] and path[i+1] == pivots[1]:
            crossover = i+1
    return path[crossover:]+path[1:crossover]
