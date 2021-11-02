from algorithms.alignment_graph import AlignmentGraph

#############################
# Smith-Waterman Algorithm #
#############################
def align_smith(s1,s2,scorer,indel):
    graph = AlignmentGraph(s1,s2,scorer)
    graph = fill_graph_smith(graph,indel)
    print(graph.pos(len(s1),len(s2)))
    return trace_pointers_smith(graph)

def fill_graph_smith(graph,indel):
    for c in range(graph.width()):
        for r in range(graph.height()):
            if r==c==0:
                graph.set(r,c,0)
            elif r==0:
                graph.set(r,c,0,0)
            elif c==0:
                graph.set(r,c,0,0)
            else:
                graph.update(r,c,graph.pos(r-1,c)+indel,1)
                graph.update(r,c,graph.pos(r,c-1)+indel,2)
                graph.update(r,c,graph.pos(r-1,c-1)+graph.score(r,c),4)
    return graph
        
def trace_pointers_smith(graph): #just goes for diagonal then insert then delete
    bestpos = (0,0)
    bestscore = 0
    for r in range(graph.height()):
        for c in range(graph.width()):
            if bestscore<graph.pos(r,c):
                bestscore = graph.pos(r,c)
                bestpos = (r,c)
    o1,o2 = "",""
    pointer = bestpos
    print(bestscore)
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
            print("Done")
            break
    return bestscore,o1,o2