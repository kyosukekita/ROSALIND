#https://wakabame.hatenablog.com/entry/2017/09/03/141133

file = open('Desktop/Downloads/rosalind_ba7a.txt').read()
n=int(file.split("\n")[0])

edges=[edge for edge in file.split("\n")[1:] if edge!='']
#グラフを描く
graph={}
for edge in edges:
    start=int(edge.split("-")[0])
    end,weight=[int(i) for i in (edge.split(">")[-1].split(":"))]#ここ工夫頑張ったよね
    if start not in graph:
        graph[start]={end:weight}
    else:
        graph[start].update({end:weight})

max_node=max(graph)


#BFSとかでやるのが定石だろうけど、これでもいいか..?
def warshall_floyd(graph,max_node,n):
    dp=[[float("inf") for _ in range(max_node+1)] for _ in range(max_node+1)] #各ノード間の距離
    
    for Node in graph:
        for childNode,weight in graph[Node].items():
            dp[Node][childNode]=weight
    
    for k in range(max_node+1):
        for i in range(max_node+1):
            for j in range(max_node+1):
                dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j])
    
    for i in range(len(dp)):
        for j in range(len(dp)):
            if i==j:
                dp[i][j]=0
    
    for i in range(n):
        print(" ".join(map(str,dp[i][:n])), end="")
        print("")
        

warshall_floyd(graph,max_node,n)
            
