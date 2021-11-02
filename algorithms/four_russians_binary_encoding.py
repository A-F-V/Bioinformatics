import math
import random
from tqdm import tqdm
from .alignment_graph import Alignment_Graph
from .scoring_functions import LCS as LCSScorer,EditDistance as EditDistanceScorer
#################################
# Needleman Wunsch with offsets #
#################################


def align_needleman_with_offset(s1,s2,left=None,top=None,indel=1,scorer=(lambda x,y:1 if x==y else 0)):
    graph = Alignment_Graph(s1,s2,scorer)
    graph = fill_graph_needleman(graph,indel,0,left,top)
    return graph

def fill_graph_needleman(graph,indel,offset=0,left=None,top=None):
    width = graph.width()
    for c in (tqdm(range(width)) if width>100 else range(width)):
        for r in range(graph.height()):
            if r==c==0:
                graph.set(r,c,offset)
            elif r==0:
                if top==None:
                    graph.set(r,c,graph.pos(r,c-1)+indel,2)
                else:
                    graph.set(r,c,top[c-1])
            elif c==0:
                if left==None:
                    graph.set(r,c,graph.pos(r-1,c)+indel,1)
                else:
                    graph.set(r,c,left[r-1])
            else:
                graph.set(r,c,graph.pos(r-1,c)+indel,1)
                graph.update(r,c,graph.pos(r,c-1)+indel,2)
                graph.update(r,c,graph.pos(r-1,c-1)+graph.score(r,c),4)
    return graph
        
###################################
# A way of sequencing Permutations#
###################################
class Sequence:
    def __init__(self,chars,t,empty=False):
        self.chars = chars
        self.t = t
        self.empty= empty
    
    def random(self):
        output = ""
        for i in range(self.t):
            output += random.choice(self.chars)
        return output
    def objWithNum(self,i):
        output = ""
        v = i
        for ind in range(self.t):
            output = str(self.chars[v%len(self.chars)]) +output
            v //= len(self.chars)
        return output

    def __iter__(self):
        self.i = -1
        if self.empty:
            self.subiterT = 1
            self.subiter = iter(Sequence(self.chars,1))
        return self

    def __next__(self):
        self.i += 1
        if not self.empty:
            if self.i >= len(self.chars)**self.t:
                raise StopIteration()
            return self.objWithNum(self.i)
        else:
            try:
                return next(self.subiter)
            except StopIteration:
                if self.subiterT==self.t:
                    raise StopIteration()
                self.subiterT +=1
                self.subiter = iter(Sequence(self.chars,self.subiterT))
                return next(self.subiter)

#####################################################
# Generate Four Russian Table with Binary Encodings #
#####################################################

def accumulate_diff(diffs):
    o = []
    for i in diffs:
        if len(o) > 0:
            o.append(i+o[-1])
        else:
            o.append(i)
    return o

def to_diff(arr):
    return [arr[i]-arr[i-1] for i in range(1,len(arr))]


def compute_table_entry(s1,s2,b1,b2,indel,scorer):
    left,top = accumulate_diff(b1),accumulate_diff(b2)
    graph = align_needleman_with_offset(s1,s2,left,top,indel,scorer)
    right = [graph.pos(i,len(s2)) for i in range(0,len(s1)+1)]
    botright = right[-1]
    bottom = [graph.pos(len(s1),i) for i in range(0,len(s2)+1)]
    right,bottom = "".join(map(str,to_diff(right))),"".join(map(str,to_diff(bottom)))
    return (right,bottom,botright)

def generateTable(t,binary_encoder,indel,scorer): #binary_encoding
    table = {}
    for s1 in Sequence(DNACode,t,empty=True):
        for s2 in Sequence(DNACode,t,empty=True):
            for b1 in Sequence([0,1],len(s1)):
                for b2 in Sequence([0,1],len(s2)):
                    b1split,b2split = [int(x) for x in b1],[int(x) for x in b2]
                    table[(s1,s2,b1,b2)]=compute_table_entry(s1,s2,b1split,b2split,indel,scorer)
        # s1,s2 b1,b2 and output b1',b2' are in string form, output score is in int
    return table

def blockwidth(s,pos,t):
    return min(t,len(s)-pos)

class FourRussianWithBinaryEncoding:
    def __init__(self,s1,s2,table,t):
        self.s1 = s1
        self.s2 = s2
        self.table=table
        self.t = t
    
    def calculateScore(self):
        #### INIT
        horiz = {(0,c):str(0)*blockwidth(self.s2,c-1,self.t) for c in range(1,len(self.s2)+1,self.t)} # The horizontal diffs 
        vert = {(r,0):str(0)*blockwidth(self.s1,r-1,self.t) for r in range(1,len(self.s1)+1,self.t)} # the veritcal diffs
        basescore ={(0,0):0} #the scores at block corners  #UNIVERSAL INDEX
        for bar in horiz:
            if bar[1]==1:
                continue
            basescore[(0,bar[1]-1)]=0
        for bar in vert:
            if bar[0]==1:
                continue
            basescore[(bar[0]-1,0)]=0

        lastscore = 0
        for c in tqdm(range(0,len(self.s2),self.t)):
            for r in range(0,len(self.s1),self.t):
                #top left pos
                s1width = blockwidth(self.s1,r,self.t)
                s2width = blockwidth(self.s2,c,self.t)
                s1 = self.s1[r:r+s1width]
                s2 = self.s2[c:c+s2width]
                block = self.table[(s1,s2,vert[(r+1,c)],horiz[(r,c+1)])]
                lastscore = block[2]+basescore[(r,c)]
                basescore[(r+s1width,c+s2width)] = lastscore
                horiz[(r+s1width,c+1)]=block[1]
                vert[(r+1,c+s2width)]=block[0]
        return lastscore

def FourRussian_BE_Solve(s1,s2,indel,scorer):
    t = int(math.log(max(len(s1),len(s2)),2))//6+1
    print(f"Block width is {t}")
    table = generateTable(t,None,indel,scorer)
    print("Finished Computing Table")
    return FourRussianWithBinaryEncoding(s1,s2,table,t).calculateScore()

################################
# Interesting Problems Sped Up #
################################

DNACode = ['A','T','G','C']

def LCS(s1,s2):
    return FourRussian_BE_Solve(s1,s2,0,LCSScorer)
    

def EditDistance(s1,s2):
    return FourRussian_BE_Solve(s1,s2,-1,EditDistanceScorer)

#todo modify Four Russiasn Table to use pointers generated in Needleman and hence find global alignment (instead of just edit distance)