import numpy as np

file= open('Desktop/Downloads/rosalind_ddeg.txt').read()
n=int(file.split()[0])
k=int(file.split()[1])

tmp=[int(edge) for edge in file.split()[2:]]
edges=[tmp[i:i+2] for i in range(0,len(tmp),2)]

#隣接行列を作る
adj=[[0 for j in range(n)] for j in range(n)]
for i in range(k):
    adj[edges[i][0]-1][edges[i][1]-1]+=1
    adj[edges[i][1]-1][edges[i][0]-1]+=1


answer=[]
for ele in adj:
    count=0
    for i in range(len(ele)):
        if ele[i]==1:
            count+=np.count_nonzero(adj[:][i])
    answer.append(count)
print(' '.join(map(str,answer)))
