#幅（深さ）優先探索を使って、連結成分の個数を調べる
#https://qiita.com/drken/items/996d80bcae64649a6580
#https://algo-logic.info/connected-components-num/

file= open('Desktop/Downloads/rosalind_cc.txt').read()
tmp=[int(i) for i in file.split()[2:]]
edges=[tmp[i:i+2] for i in range(0,len(tmp),2)]

#頂点数と辺数
n,k= int(file.split()[0]), int(file.split()[1])

seen=[False]*(n+1)
def bfs(graph,start):
    seen[start]=True
    for i in graph[start]:
        if (seen[i]==False):
            bfs(graph,i)
            
def Graph(edges):
    graph=[[] for _ in range(k)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])#ここ注意。グラフは無向だからな！両方加える！
    
    return graph
    
def cc(graph):
    count=0
    for i in range(1,n):
        if (seen[i]==False):
            bfs(graph,i)
            count+=1
            
    return count


print(cc(Graph(edges)))


#別解
def connected_components(graph):   
    dist=[-1]*(n+1)#-1ならば未訪問
    d=deque()
    
    count=0
    for x in range(1,n+1):
        if (dist[x]!=-1):
            continue
        
        dist[x]=0
        d.append(x)
        
        while(len(d)!=0):
            v=d.popleft()
            for i in graph[v]:
                if dist[i]==-1:
                    dist[i]= dist[v]+1
                    d.append(i)   
        count+=1
        
    return count
