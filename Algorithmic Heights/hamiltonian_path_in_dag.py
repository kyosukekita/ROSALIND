"""もしトポロジカルソートされたノードのすべてのノードが隣接する次のノードへの辺を持つなら、元のDAGは
ハミルトン路を含む。もし、ハミルトン路が含まれるなら、トポロジカルソートの結果は一意。"""


def topological_sorting(edges,n): 
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
    
    if len(d)>1:
        return -1#シンクが2つ以上あったらDAGではない

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
    
    return ' '.join(map(str, [1]+order[::-1]))#最後向きを反対にするのを忘れずに


file = open('Desktop/Downloads/rosalind_hdag.txt', 'r').read()#ファイルの最後の空行を削除してください。
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



for i in range(N):
    n=graphs[i][0][0]
    edges=graphs[i][1:]
    print(topological_sorting(edges,n))
