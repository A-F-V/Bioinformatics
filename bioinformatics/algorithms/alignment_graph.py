class Alignment_Graph:
    def __init__(self,s1,s2,scorer):
        self.s1 = s1
        self.s2 = s2
        self.grid = [0]*((len(self.s1)+1)*(len(self.s2)+1))
        self.pointers = [0]*((len(self.s1)+1)*(len(self.s2)+1))
        self.scoringFunction = scorer
    
    def pos(self,r,c):
        return self.grid[c+r*(len(self.s2)+1)]
    
    def ppos(self,r,c):
        r,c = max(r,0),max(c,0)
        return self.pointers[c+r*(len(self.s2)+1)]

    def set(self,r,c,v,p=0):
        self.grid[c+r*(len(self.s2)+1)] = v
        self.pointers[c+r*(len(self.s2)+1)] = p

    def update(self,r,c,v,p):
        before = self.pos(r,c)
        if(before<v):
            self.set(r,c,v,p)
        elif before==v:
            self.pointers[c+r*(len(self.s2)+1)] |= p

    def width(self):
        return len(self.s2)+1

    def height(self):
        return len(self.s1)+1

    def score(self,r,c):
        return self.scoringFunction(self.s1[r-1],self.s2[c-1])

    def prnt(self):
        for r in range(len(self.s1)+1):
            o = [self.pos(r,c) for c in range(len(self.s2)+1)]
            print(o)