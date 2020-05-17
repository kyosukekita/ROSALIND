file = open('Desktop/Downloads/rosalind_wfmd.txt').read()
N,m,g,k=[int(i) for i in file.split()]

import math
def combination(n,k):
    return math.factorial(n)/ (math.factorial(k)*math.factorial(n-k))


"""Probability of observing i copies if a recessive allele in any generation depends completely on
numbers of alleles in previous generation. Thus we have Markov chain with transition matrix"""

""" p=(transition)*p  repeat this transition g times """

Pdom=m/(2*N)
Prec=1-Pdom
p=[combination(2*N,i)*(Prec**i)*(Pdom**(2*N-i)) for i in range(2*N+1)]#一番最初の

for gen in range(2,g+1):#g times
    temp_p=[]
    for i in range(2*N+1):
        transition=[combination(2*N,i)*((j/(2*N))**i)*(1-(j/(2*N)))**(2*N-i) for j in range(2*N+1)]
        temp_p.append(sum([transition[i]*p[i] for i in range(len(transition))]))
    p=temp_p

    
print(sum(p[k:]))
