#topological_sorting.py

from collections import deque


file= open('Desktop/Downloads/rosalind_ts.txt').read()
tmp=[int(i) for i in file.split()[2:]]
edges=[tmp[i:i+2] for i in range(0,len(tmp),2)]

#頂点数と辺数
n,k= int(file.split()[0]), int(file.split()[1])


def topological_sorting(edges): 
    graph=[[] for _ in range(n+1)]
    deg=[0]*(n+1) #各頂点の出自数(引数0には意味はない)
    
    for edge in edges:
        graph[edge[1]].append(edge[0])
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
    
    return ' '.join(map(str, order[::-1]))#最後向きを反対にするのを忘れずに
    
print(topological_sorting(edges))
