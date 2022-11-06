#testing_acyclicity.py
"""「トポロジカルソートをしていく過程で、サイクルに含まれる頂点は一度も
シンク（有向グラフにおいて出次数が0であるような頂点）になることはありえない」という性質を使う。"""

from collections import deque

def testing_acyclicity(edges,n): 
    graph=[[] for _ in range(n+1)]
    deg=[0]*(n+1) #各頂点の出自数(引数0には意味はない)
    
    for edge in edges:
        graph[edge[1]].append(edge[0]) #edge[1]← edge[0]
        deg[edge[0]]+=1
        
    #シンクをキューに挿入する
    d=deque()
    for i in range(1,n+1):
        if deg[i]==0:
            d.append(i)
    
    #探索開始
    order=[]
    while (len(d)!=0):
        #キューから頂点を取り出す
        v=d.popleft()
        order.append(v)
        
        #vへと伸びている頂点たちを探索する
        for i in graph[v]:
            #辺(i,v)を削除する
            deg[i]-=1
            
            #それによってiが新たにシンクになったらキューに挿入
            if (deg[i]==0):
                d.append(i)
    
    if len(order)==n:
        return 1
    
    return -1
    
    
file = open('Desktop/Downloads/rosalind_dag (1).txt', 'r').read()#ファイルの最後の空行を削除してください。
N=int(file.split()[0])

tmp=[(blocks) for blocks in file.split("\n\n")]
tmp1=[block.split("\n") for block in tmp][1:]

graphs=[]
for i in range(N):
    graphi=[]
    for ele in tmp1[i]:
        ele=list(map(int,ele.split(" ")))
        graphi.append(ele)
    graphs.append(graphi)



answer=[]
for i in range(N):
    n=graphs[i][0][0]
    edges=graphs[i][1:]
    answer.append(testing_acyclicity(edges,n))

print(' '.join(map(str,answer)))
