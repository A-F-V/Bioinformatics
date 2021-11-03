from .alignment_graph import AlignmentGraph

#############################
# Needleman-Wunsch Algorithm #
#############################
def align_needleman(s1,s2,scorer,indel):
    graph = AlignmentGraph(s1,s2,scorer)
    graph = fill_graph_needleman(graph,indel)
    return trace_pointers_needleman(graph)

def fill_graph_needleman(graph,indel):
    for c in range(graph.width()):
        for r in range(graph.height()):
            if r==c==0:
                graph.set(r,c,0)
            elif r==0:
                graph.set(r,c,graph.pos(r,c-1)+indel,2)
            elif c==0:
                graph.set(r,c,graph.pos(r-1,c)+indel,1)
            else:
                graph.set(r,c,graph.pos(r-1,c)+indel,1)
                graph.update(r,c,graph.pos(r,c-1)+indel,2)
                graph.update(r,c,graph.pos(r-1,c-1)+graph.score(r,c),4)
    return graph
        
def trace_pointers_needleman(graph): #just goes for diagonal then insert then delete
    o1,o2 = "",""
    pointer = (graph.height()-1,graph.width()-1)
    while pointer != (0,0):
        r,c = pointer
        p = graph.ppos(r,c)
        if p>=4:
            o1 = graph.s1[r-1]+o1
            o2 = graph.s2[c-1]+o2
            pointer = (r-1,c-1)
        elif p>=2:
            o1 = "-"+o1
            o2 = graph.s2[c-1]+o2
            pointer = (r,c-1)
        elif p==1:
            o1 = graph.s1[r-1]+o1
            o2 = "-"+o2
            pointer = (r-1,c)
        else:
            print("ERROR")
            pointer= (r-1,c-1)
    return o1,o2
