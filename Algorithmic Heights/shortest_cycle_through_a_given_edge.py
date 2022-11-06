"""重みに負が含まれていない限り、dijkstraでもbellman-fordでもどちらでも良い"""

def dijkstra(graph,NodeNum,start,end):
    shortest_distance=[float("inf")]*(NodeNum+1)#startからの距離。初期値は∞
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
       
    
    return shortest_distance[end]


file = open('Desktop/Downloads/rosalind_cte (1).txt', 'r').read()#ファイルの最後の空行を削除してください。
N=int(file.split()[0])

tmp=[(blocks) for blocks in file.split("\n\n")]
tmp1=[block.split("\n") for block in tmp][1:]


answer=[]
for i in range(N):
    """アイディア：指定されたエッジの後ろのノードから、前のノードへ行けるかダイクストラ法で確認する。"""

    NodeNum=int(tmp1[i][0].split()[0])
    end=int(tmp1[i][1].split()[0]) 
    start=int(tmp1[i][1].split()[1])
    weight=int(tmp1[i][1].split()[2])
    
    graphi={}            
    for ele in tmp1[i][1:]:
        ele=list(map(int,ele.split(" ")))      
        if ele[0] not in graphi:
            graphi[ele[0]]={ele[1]:ele[2]}
        else:
            graphi[ele[0]].update({ele[1]:ele[2]})
        
        
    tmp=dijkstra(graphi,NodeNum,start,end)
    if tmp!=float("inf"):
        answer.append(tmp+weight)
    else:
        answer.append(-1)
    
print(' '.join(map(str,answer)))




#以下warshall_floyd法で解いてみる。時間は間に合わない。

graphs=[]
NodeNum=[]
start=[]
middle=[] 

#グラフを描く
def make_graph(file):
    N=int(file.split()[0])
    tmp=[(blocks) for blocks in file.split("\n\n")]
    tmp1=[block.split("\n") for block in tmp][1:]
    
    
    for i in range(N):
        graph={}
    
        for ele in tmp1[i][1:]:
            ele=list(map(int,ele.split(" ")))
            if ele[0] not in graph:
                graph[ele[0]]={ele[1]:ele[2]}
            else:
                graph[ele[0]].update({ele[1]:ele[2]})
        
        graphs.append(graph)
        
        
        NodeNum.append(int(tmp1[i][0].split()[0]))
        start.append(int(tmp1[i][1].split()[0]))
        middle.append(int(tmp1[i][1].split()[1]))

file = open('Desktop/Downloads/rosalind_cte.txt', 'r').read()
make_graph(file)


def warshall_floyd(graph,NodeNum,start,middle):
    dp=[[float("inf") for _ in range(NodeNum+1)] for _ in range(NodeNum+1)]
    
    for Node in graph:
        for childNode, weight in graph[Node].items():
            dp[Node][childNode]=weight
    
    for k in range(NodeNum+1):#経由する点
        for i in range(NodeNum+1):#始点
            for j in range(NodeNum+1):#終点
                dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j]);
    
    
    ans=dp[start][middle]+dp[middle][start]
    
    if ans==float("inf"):
        return -1
    else:
        return ans
     
     
    for i in range(len(graphs)):
    print(warshall_floyd(graphs[i],NodeNum[i],start[i],middle[i]))
