




#warshall_floyd法で解いてみる。

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
