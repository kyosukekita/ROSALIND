#ダイクストラ法；各辺の重みが非負でないと使えない。
#Youtubeを参考にした。https://pastebin.com/3Q9rqGHA

file = open('Desktop/Downloads/rosalind_dij.txt', 'r').read()
n=int(file.split()[0])
k=int(file.split()[1])

tmp=[int(edge) for edge in file.split()[2:]]
edges=[tmp[i:i+3] for i in range(0,len(tmp),3)]

#グラフを描く
graph={}
for edge in edges:
    if edge[0] not in graph:
        graph[edge[0]]={edge[1]:edge[2]}
    else:
        graph[edge[0]].update({edge[1]:edge[2]})   


def dijkstra(graph,start):
    shortest_distance=[float("inf")]*(n+1)#startからの距離。初期値は∞
    shortest_distance[start]=0 
    unseenNodes=graph
    path=[]#ここに答えを入れる
    

    while unseenNodes:#未探索ノードがある限り
        minNode=None
        for node in unseenNodes:
            if minNode is None:
                minNode=node
            elif shortest_distance[node]<shortest_distance[minNode]:
                minNode=node#未探索ノードの中で、shortest_distanceが最も小さいものを選ぶ
        
        for childNode, weight in graph[minNode].items():
            if weight+shortest_distance[minNode] <shortest_distance[childNode]:
                shortest_distance[childNode]= weight+shortest_distance[minNode]#次は、childNodeについてやり直し。
        unseenNodes.pop(minNode)
       
    
    for i in range(len(shortest_distance)):
        if shortest_distance[i]==float("inf"):
            shortest_distance[i]=-1
    
    return shortest_distance[1:]
    
    
answer=dijkstra(graph,1)
print(*answer)
