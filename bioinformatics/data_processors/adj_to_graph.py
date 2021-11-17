from algorithms.sequencing_graph import Graph

def agg_adj_to_graph(data:list):
    """
    Generate a graph from an adjency list where destinations are aggregated
    """
    nodes = set()
    edges = {}
    for row in data:
        row = row.split()
        source = int(row[0])
        nodes.add(source)
        sinks = set(map(int,row[2].split(','))) 
        for sink in sinks:
            nodes.add(sink)
        edges[source] = sinks
    return Graph(nodes,edges)