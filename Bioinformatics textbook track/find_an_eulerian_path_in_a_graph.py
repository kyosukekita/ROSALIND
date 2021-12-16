import random

file = open('Desktop/Downloads/rosalind_ba3g.txt', 'r').read()
edges=[edge for edge in file.split("\n") if edge!='']


#グラフを描く
graph={}#graphの型は辞書
for edge in edges:
    graph[int(edge.split("-")[0])]=list(map(int,(edge.split(">")[-1].split(","))))#ここ工夫頑張ったよね

nodeNum=0#グラフに出現する全ノードの数    
for node in graph:
    for ele in graph[node]:
        if ele>nodeNum:
            nodeNum=ele
nodeNum+=1

#隣接行列を描く
adj=[[0 for _ in range(nodeNum)] for _ in range(nodeNum)]
for node in graph:
    for next_node in graph[node]:
        adj[node][next_node]+=1
        adj[next_node][node]+=1 #有向グラフだけど、ノードの次数計算のために反対向きも入れる


#ノードの次数を調べる
"""あるグラフが準オイラーグラフであるための必要十分条件は、次数が奇数であるものがちょうど２つ"""
deg=[0 for _ in range(nodeNum)]
for i in range(nodeNum):
    for j in range(nodeNum):
        deg[i]+=adj[i][j]

v1,v2=[i for i in range(len(deg)) if deg[i]%2!=0]
if v1 in graph:
    start=v1
    end=v2
else:
    start=v2
    end=v1

    
def formCycle(nodes, source):
    """サイクルを作る"""
    cycle = [source]
    if source in nodes:
        while nodes[source]:
            targetInd = random.randint(0, len(nodes[source])-1)
            source = nodes[source].pop(targetInd)
            if source not in nodes:
                break
            cycle.append(source)
    return cycle, nodes

def EulerianPath(graph,start,end):
    #最初のノードと最後のノードは、ノードの次数から明らか
    path=[start,end]
    #while there are unexplored edges in graph
    while True:
        foundNode = False
        for i,node in enumerate(path):#pathに使っているノードから↓
            if (node in graph) :
                if graph[node]:#グラフに残っているノードがあれば、
                    foundNode = True
                    newCycle, graph = formCycle(graph, node)#グラフの残りのノードを使ってcyclerをつくる。↓
                    path = path[:i]+newCycle+path[i+1:]#それを既存のサイクルの中に埋め込む。
                    break
        if not foundNode:
            break
    return path
   

print("->".join(map(str,EulerianPath(graph,start,end))))
