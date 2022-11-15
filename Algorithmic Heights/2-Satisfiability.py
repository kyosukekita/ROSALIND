#2-SAT
#https://tjkendev.github.io/procon-library/python/graph/2-sat.html
#https://ja.wikipedia.org/wiki/%E5%85%85%E8%B6%B3%E5%8F%AF%E8%83%BD%E6%80%A7%E5%95%8F%E9%A1%8C
#https://qiita.com/sysdev/items/c6b707666541bacd22bf
#https://qiita.com/recuraki/items/72cdaab3eca9de1b1a4e


file = open('/Users/kita/Downloads/rosalind_2sat (2).txt').read()
k= int(file.split("\n")[0])

formulas=[]
for i in range(k):
    formula=[[int(r.split(" ")[0]),int(r.split(" ")[1])] for r in file.split("\n\n")[i+1].split("\n")]
    formulas.append(formula)

    
    
"""頂点サイズはＮ、順方向の有向グラフはＧ、逆方向の有向グラフはRG"""
def scc(N,G,RG):
    order=[]
    visited=[0 for _ in range(N+1)]
    group=[-1 for _ in range(N+1)] #同じ強連結成分は同じラベル
    
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
            
    visited=[0 for _ in range(N+1)]
    label=0
    for s in reversed(order):
        if not visited[s]:
            rdfs(s,label)#帰りがけのDFS
            label+=1
    return group



def graph_rgraph(edges,n):
    graph=[[] for _ in range(2*n+1)]
    rgraph=[[] for _ in range(2*n+1)]
    
    for edge in edges:
        if edge[0]<0:
            i0=-edge[0]+n; i1=-edge[0]
        else:
            i0=edge[0]; i1=edge[0]+n

        if edge[1]<0:
            j0=-edge[1]+n; j1=-edge[1]
        else:
             j0=edge[1]; j1=edge[1]+n
        
        #print(i1,j0,j1,i0)
        #(~a→b)
        graph[i1].append(j0)
        graph[j1].append(i0)
        #(~b→a)
        rgraph[j0].append(i1)
        rgraph[i0].append(j1)
        
    return graph, rgraph


def answer(group,n):
    #復元のコード
    l=[]
    for i in range(1,n+1):
        if group[i]==group[i+n]: #aと~aが同じグループにいたらダメ
            return None
        if group[i]>group[i+n]:
            l.append(i)
        else:
            l.append(-i)
 
    return l


for i in range(k):
    N=formulas[i][0][0]
    edges=formulas[i][1:]
    graph, rgraph=graph_rgraph(edges,N)
    
    group=scc(2*N, graph, rgraph)
    #print(group)

    if answer(group,N)== None:
        print(0)
    else:
        print(1, end=" ")
        l=answer(group,N)
        print(*l)
