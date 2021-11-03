import math
def limb_length(j,d_mat): #find the length of j to its parent in the final, simple tree -> either leaf or def >=3 
    # complexity is O(n^2) , simply try all other pairs and find min cost
    bestscore,besti,bestk = math.inf,"",""
    for i in d_mat.names:
        for k in d_mat.names:
            if i !=j and k!=j:
                testval = (d_mat.get(i,j)+d_mat.get(j,k)-d_mat.get(i,k))/2
                if testval<bestscore:
                    bestscore,besti,bestk = testval,i,k
    return bestscore

# returns both limb length and optionally i and k which ae in different trees
def limb_length_n(j,d_mat,withik=False): #find the length of j to its parent in the final, simple tree -> either leaf or def >=3 
    # complexity is O(n) , fix 1 and try all others (cannot all be in same tree)
    bestscore,besti,bestk = math.inf,"",""
    i =d_mat.names[0] if d_mat.names[0]!=j else d_mat.names[1]
    for k in d_mat.names:
        if i !=j and k!=j:
            testval = (d_mat.get(i,j)+d_mat.get(j,k)-d_mat.get(i,k))/2
            if testval<bestscore:
                bestscore,besti,bestk = testval,i,k
    return (bestscore,besti,bestk) if withik else bestscore