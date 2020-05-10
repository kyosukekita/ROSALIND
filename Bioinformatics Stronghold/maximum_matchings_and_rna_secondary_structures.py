import math

def permutation(n,k):
    temp=1
    for i in range(n-k+1,n+1):
        temp*=i
    return temp
        
def max_match(seq):
    A=seq.count("A")
    U=seq.count("U")
    G=seq.count("G")
    C=seq.count("C")
    
    GC=permutation(max(C,G),min(C,G))
    AU=permutation(max(A,U),min(A,U))
    max_matching=AU*GC
    
    print(max_matching)

    
RNA="""UGCGAGACUGUCUAGGGCAGGAUAACGACCGCUUCACAUGGGAUUGCCGUUUUGACAAAG
UCCCUCGCUACCAUCCCCCAC"""
max_match(RNA)    
