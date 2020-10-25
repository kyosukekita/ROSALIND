#https://tjkendev.github.io/procon-library/python/graph/scc.html
#強連結成分分解～任意の有向グラフをＤＡＧに変換するお話
#DFSを2回するだけ

file= open('Desktop/Downloads/rosalind_scc.txt').read()
tmp=[int(i) for i in file.split()[2:]]
edges=[tmp[i:i+2] for i in range(0,len(tmp),2)]

#頂点数と辺数
n,k= int(file.split()[0]), int(file.split()[1])


def Graph(edges,n):
    graph=[[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]-1].append(edge[1]-1)
    
    return graph


def rGraph(edges,n):
    rgraph=[[] for _ in range(n)]
    for edge in edges:
        rgraph[edge[1]-1].append(edge[0]-1)

    return rgraph


"""頂点サイズがＮ、順方向の有向グラフがＧ、逆方向の有向グラフ"""
def scc(N,G,RG):
    order=[]
    visited=[False for _ in range(N)]
    group=[None for _ in range(N)] #同じ強連結成分は同じラベル
    
    def dfs(s):
        """頂点ｓから始まり到達できるところまで、次々と移動していく"""
        visited[s]=True
        for t in G[s]:
            if not visited[t]:
                dfs(t)
        order.append(s)
        
    
    def rdfs(s,col):
        """頂点ｓから始まり到達できるところまで、次々と移動していく"""
        group[s]=col#groupのsをcolでラベル
        visited[s]=True
        for t in RG[s]:
            if not visited[t]:
                rdfs(t,col)
    
    
    for i in range(N):
        if not visited[i]:
            dfs(i)#行きがけのDFS
            
    visited=[False]*N
    label=0
    for s in reversed(order):
        if not visited[s]:
            rdfs(s,label)#帰りがけのDFS
            label+=1
    return label

        
print(scc(n,Graph(edges,n),rGraph(edges,n)))
