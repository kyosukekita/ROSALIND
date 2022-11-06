#bellmanford_algorithm2.pyと同じコード

file = open('Desktop/Downloads/rosalind_sdag.txt', 'r').read()
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


def bellmanford(start,NodeNum):
    distances=[float("inf")]*(NodeNum+1) #各頂点の最短距離保存配列
    distances[start]=0 #初期化

    #更新がある限り繰り返す
    while True:
        
        #ルート更新判定用
        is_updated= False 

        for Node in graph :
            for childNode, weight in graph[Node].items():
                if (distances[Node] != float("inf")) & (distances[childNode]>distances[Node]+weight): #エッジの始点の距離が更新済み
                    distances[childNode] = distances[Node]+weight #頂点までの距離を更新
                    is_updated=True
        
        if(is_updated==False):
            break
    
    for i in range(len(distances)):
        if distances[i]==float("inf"):
            distances[i]=　-1
    
    return distances[1:]

print(' '.join(map(str,bellmanford(1,n))))
