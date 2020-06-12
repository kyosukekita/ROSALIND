#深さ優先探索で連結グラフの数を求める(はずだったがscipyのツールを使ってしまった...)
#https://note.nkmk.me/python-scipy-connected-components/


import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

file = open('Desktop/Downloads/rosalind_cc (1).txt', 'r').read()
n=int(file.split()[0])
k=int(file.split()[1])

tmp=[int(edge) for edge in file.split()[2:]]
edges=[tmp[i:i+2] for i in range(0,len(tmp),2)]


#グラフを描く
graph=[[] for _ in range(n+1)]
for edge in edges:
    graph[edge[0]-1].append(edge[1]-1)  

    
#隣接行列を描く
adj_list=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    while len(graph[i])>0:
        adj_list[i][graph[i].pop(0)]+=1


#scipyの関数を使って連結グラフの数を出力
a=np.array(adj_list)
n,_=connected_components(a)
print(n)
