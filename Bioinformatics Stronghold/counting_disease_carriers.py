import math
file = open('Desktop/Downloads/rosalind_afrq.txt').read()
A=[float(i) for i in file.split()]

B=[]
for k in range(len(A)):
    q=math.sqrt(A[k])
    p=1-q
    Bk=1-(p**2) #Hardy-Weinberg Principle states that (p^2) + (2pq) + (q^2) = 1
    B.append(Bk)
    
print(*B)
