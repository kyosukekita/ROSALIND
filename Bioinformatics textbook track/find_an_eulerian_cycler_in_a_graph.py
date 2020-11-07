#オイラー路：グラフの全ての辺を通る路のこと。また全ての辺を一度だけ通る閉路はオイラー閉路euler circuitという
#http://compeau.cbd.cmu.edu/wp-content/uploads/2016/08/lec_36.pdf


import random

file = open('Desktop/Downloads/rosalind_ba3f.txt', 'r').read()
edges=[edge for edge in file.split("\n") if edge!='']


#グラフを描く
graph={}#graphの型は辞書
for edge in edges:
    graph[int(edge.split("-")[0])]=list(map(int,(edge.split(">")[-1].split(","))))#ここ工夫頑張ったよね


def formCycle(nodes, source):
    cycle = [source]
    while nodes[source]:
        targetInd = random.randint(0, len(nodes[source])-1)
        source = nodes[source].pop(targetInd)
        cycle.append(source)
    return cycle, nodes


def EulerianCycle(graph):
    #form a cycler by randomly walking in graph(適当にサイクルを作ってみる、使っていないノードがある)
    source = random.choice(list(graph.keys()))
    cycle, graph = formCycle(graph, source)
    
    #while there are unexplored edges in graph
    while True:
        foundNode = False
        for i,node in enumerate(cycle):#cycleに使っているノードから↓
            if graph[node]:#グラフに残っているノードがあれば、
                foundNode = True
                newCycle, graph = formCycle(graph, node)#グラフの残りのノードを使ってcyclerをつくる。↓
                cycle = cycle[:i]+newCycle+cycle[i+1:]#それを既存のサイクルの中に埋め込む。
                break
        if not foundNode:
            break
    return cycle


print("->".join(map(str,EulerianCycle(graph))))
