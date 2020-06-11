#幅優先探索
from collections import deque

file = open('Desktop/Downloads/rosalind_bfs.txt', 'r').read()
n=int(file.split()[0])
k=int(file.split()[1])

tmp=[int(edge) for edge in file.split()[2:]]
edges=[tmp[i:i+2] for i in range(0,len(tmp),2)]



#グラフを描く
graph=[[] for _ in range(n+1)]#graph[i]に頂点と直接つながっている頂点番号を入れる。graph0に意味はない
for edge in edges:
    graph[edge[0]].append(edge[1])


dist=[-1]*(n+1)#dist[i]には頂点1から頂点iの最短距離を入れたいので、サイズn+1のリストを作った
dist[0]=0#dist[0]に意味はない
dist[1]=0

d=deque()#新しく訪問した頂点を末尾に追加するor先頭から過去に訪問した頂点を取り出す
d.append(1)#頂点1を訪問した

while d:#dがtrueの間は処理を続ける
    v=d.popleft()#FIFO
    for i in graph[v]:#頂点ｖと直接つながっている頂点iに対し、
        if dist[i]!=-1:#訪問済みであれば
            continue#何もせず次のiについて調べる
        dist[i]=dist[v]+1#未訪問であればdist[i]を求める
        d.append(i)#今回新しく訪問した頂点iをdの末尾に追加
    
ans=dist[1:]
print(*ans) 
