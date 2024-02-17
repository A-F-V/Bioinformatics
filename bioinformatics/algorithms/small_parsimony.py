from math import inf
from numpy import argmin
from algorithms.binary_tree import BinaryTree
class SmallParsimonyChar:
    def __init__(self,tree:BinaryTree,charSet,distance): 
     #leaves are the names to characters
        #distance is a function taking two chars and returning a number
        #each leaf is given an index and a character
        self.leaves = {leaf:tree.nodes[leaf] for leaf in tree.leaves()}
        self.charSet = charSet
        self.tree = tree
        self.s = {} #score for subtree v of value k
        self.optimal_tv = {} # the k which gives the lowest parsimony score for v
        self.d = distance

    def is_leaf(self,node):
        return node in self.leaves
    
    def daughter(self,node):
        return self.tree.left(node)[0]

    def son(self,node):
        return self.tree.right(node)[0]

    def dp_tree_char_scores(self,k,v): #the DP to build up tree
        if v in self.s and k in self.s[v]:
            return self.s[v][k]
        if self.is_leaf(v):
            self.s[v] = {c:(inf if c!=self.leaves[v] else 0) for c in self.charSet}
        else:
            best_dscore,best_sscore,best_dkv,best_skv = inf,inf,None,None
            for i in self.charSet:
                score = self.dp_tree_char_scores(i,self.daughter(v)) +self.d(i,k)
                if(score<best_dscore):
                    best_dscore = score
                    best_dkv = i
            for i in self.charSet:
                score = self.dp_tree_char_scores(i,self.son(v)) +self.d(i,k)
                if(score<best_sscore):
                    best_sscore = score
                    best_skv = i
            if v not in self.s:
                self.s[v] = {}
            self.s[v][k] = best_dscore+best_sscore
            self.optimal_tv[(v,k)] = (best_dkv,best_skv)

        return self.s[v][k]

    def best_k(self,node):
        if self.is_leaf(node):
            return self.leaves[node]
        bestscore = inf
        bestk = None
        for k in self.charSet:
            score = self.dp_tree_char_scores(k,node)
            if score<bestscore:
                bestscore = score
                bestk = k
        return bestk

    def small_parsimony_tree(self,root=None,k=None):
        if root is None:
            root = self.tree.root
            k = self.best_k(root)
            return self.small_parsimony_tree(root,k)
        if self.is_leaf(root):
            return BinaryTree({root:self.tree.nodes[root]},{},root)
        descendent_ks = self.optimal_tv[(root,k)]
        daughter,son = self.daughter(root),self.son(root)
        dk,sk = descendent_ks[0],descendent_ks[1]
        dist_d,dist_s= self.d(dk,k),self.d(sk,k)
        return BinaryTree.rec_make_tree(root,k,dist_d,dist_s,self.small_parsimony_tree(daughter,dk),self.small_parsimony_tree(son,sk))

def small_parsimony(tree:BinaryTree,m,charSet=['A','C','G','T'],distance= lambda x,y:0 if x==y else 1): 
    # Performs small parisomny on each character and merges
    output_tree = tree.copy().apply(lambda x:"",lambda x:0) # create empty tree with same structure
    for pos in range(m):
        char_tree = tree.copy().apply(lambda x:x[pos] if len(x)!=0 else "",lambda x:0)
        spc = SmallParsimonyChar(char_tree,charSet,distance).small_parsimony_tree()
        output_tree = output_tree.merge(spc,lambda x,y:x+y,lambda x,y:x+y)
    return output_tree