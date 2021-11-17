from algorithms.four_russians_binary_encoding import LCS, Sequence,DNACode
from rosalind.q7f import q7f
from algorithms.needleman_wunsch import align_needleman
###########
# Example #
###########
def FourRussianLCS():
    n= 3000
    s1 = Sequence(DNACode,n).random()
    s2 = Sequence(DNACode,n).random()
    print(s1==s2)
    print(LCS(s1,s2))


############
# ROSALIND #
############

q7f()

##############
# Playground #
##############

#Q2 Supo 1
Q2Scorer = lambda x,y: 5 if x==y else -3
a,b = align_needleman("CGTGAA","GACTTAC",scorer= Q2Scorer,indel=-4)
print(a)
print(b)


#FourRussianLCS()

