from heapq import *

#can do i,j with priority queue to find smallest i,j
class DistanceMatrix: #lazy implementation, indexed via names
    def __init__(self,mat,names,with_ij_queue=False):#takes 2d list and names and creates named matrix
        self.names = names  
        self.data = {}
        self.smallest = []
        self.with_ij_queue = with_ij_queue
        self.size = len(names)
        for i in range(len(names)-1):
            name = names[i]
            self.data[name] = {names[j]:mat[i][j] for j in range(i+1,len(names))} #BECAUSE OF SYMMETRY
            if with_ij_queue:
                for jname in self.data[name]:
                    heappush(self.smallest,(self.data[name][jname],name,jname))
    
    def remove(self,name):
        if name in self.data:
            self.data.pop(name)
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
    
    def set(self,i,j,val):
        if i in self.names and j in self.names:
            if i in self.data and j in self.data[i]:
                self.data[i][j]=val
            else:
                self.data[j][i]=val


    def add(self,name,score): #as a dict from names to scores (not as a 2d list)
        self.names.append(name)
        self.size +=1
        self.data[name] = score
        if self.with_ij_queue:
            for iname in self.names:
                if iname !=name:
                    heappush(self.smallest,(score[iname],name,iname))


    def smallest_ij(self): #maintains iname < jname
        # priority q accounting for lazy removal
        if self.size>1:
            while True:
                (d,iname,jname) = heappop(self.smallest)
                if iname in self.names and jname in self.names:
                    return (d,min(iname,jname),max(iname,jname))
    def to_2d_list(self):
        return [[self.get(i,j) for j in self.names] for i in self.names]

    def copy(self):
        return DistanceMatrix(self.to_2d_list(),list(self.names),self.with_ij_queue)

    def balden(self,j,amt,copy=False):
        output = self.copy() if copy else self
        for i in self.names:
            if i !=j:
                output.set(i,j,output.get(i,j)-amt)
        return output

    def trim(self,j,copy=False):
        output = self.copy() if copy else self
        output.remove(j)
        return output

