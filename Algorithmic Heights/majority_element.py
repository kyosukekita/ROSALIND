import collections


file = open('Desktop/Downloads/rosalind_maj (1).txt').read()
k,n=[int(i) for i in file.split("\n")[0].split()]
A=[int(i) for i in file.split()[2:]]

P=[]
for i in range(0,len(A),n):
    P.append(A[i:i+n])


answer=[]
for p in P:
    p.sort()
    mode=collections.Counter(p).most_common()[0][0]
    if p.count(mode)>n//2:
        answer.append(mode)
    else:
        answer.append(-1)

print(' '.join(map(str,answer)))
