from collections import deque
file=open('Desktop/Downloads/rosalind_ba5n.txt').read()
tmps=[i for i in file.split("\n") if i!='']


#前処理はfind_a_eulerian_path_in_a_graph.pyと同じ
edges={}
for edge in tmps:
    edges[int(edge.split("-")[0])]=list(map(int,(edge.split(">")[-1].split(","))))

nodeNum=0#グラフに出現する全ノードの数    
for node in edges:
    for ele in edges[node]:
        if ele>nodeNum:
            nodeNum=ele
nodeNum+=1

def topological_sorting(edges,n): 
    graph=[[] for _ in range(n+1)]
    deg=[0]*(n+1) #各頂点の出自数(引数0には意味はない)
      
    for node in edges.keys():
        for childnode in edges[node]:
            graph[childnode].append(node)
            
            deg[node]+=1
     
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
    
    return ', '.join(map(str,order[::-1]))

topological_sorting(edges,nodeNum)
