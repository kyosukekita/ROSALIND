#幅優先探索 復習
file= open('Desktop/Downloads/rosalind_bfs.txt').read()
tmp=[int(i) for i in file.split()[2:]]
edges=[tmp[i:i+2] for i in range(0,len(tmp),2)]

#頂点数と辺数
"""BFSの場合、各頂点はキューに高々一回挿入され、高々一回取り出されるので、
その分の計算量がＯ(N), 各辺は高々一回だけ探索されることになるので、その分
の計算量がＯ(M)となる。合わせて計算量はＯ(N+M)"""
n,k= int(file.split()[0]), int(file.split()[1])


def Graph(edges):
    graph=[[] for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])   
    
    return graph


def bfs(graph):
    dist=[-1]*(n+1)
    dist[1]=0
    que=[1]
    while(len(que)!=0):
        v=que.pop(0)
        for i in graph[v]:
            if dist[i]==-1:
                dist[i]= dist[v]+1
                que.append(i)
                
    return ' '.join(map(str,dist[1:]))


print(bfs(Graph(edges)))
