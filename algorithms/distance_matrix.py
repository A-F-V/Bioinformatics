from heapq import *
class DistanceMatrix: #lazy implementation, indexed via names
    def __init__(self,mat,names):#takes 2d list and names and creates named matrix
        self.names = names  
        self.data = {}
        self.smallest = []
        self.size = len(names)
        for i in range(len(names)-1):
            name = names[i]
            self.data[name] = {names[j]:mat[i][j] for j in range(i+1,len(names))} #BECAUSE OF SYMMETRY
            for jname in self.data[name]:
                heappush(self.smallest,(self.data[name][jname],name,jname))
    
    def remove(self,name):
        if name in self.data:
            self.data.remove(name)
        if name in self.names:
            self.names.remove(name)
            self.size -=1

    def get(self,i,j):
        if i ==j:
            return 0
        if i in self.names and j in self.names:
            if i in self.data and j in self.data[i]:
                return self.data[i][j]
            else:
                return self.data[j][i]
    
    def add(self,name,score): #as a dict from names to scores (not as a 2d list)
        self.names.append(name)
        self.data[name] = score
        for iname in self.names:
            if iname !=name:
                heappush(self.smallest,(score,name,iname))


    def smallest_ij(self): #maintains iname < jname
        # priority q accounting for lazy removal
        if self.size>1:
            while True:
                (d,iname,jname) = heappop(self.smallest)
                if iname in self.names and jname in self.names:
                    return (d,min(iname,jname),max(iname,jname))
