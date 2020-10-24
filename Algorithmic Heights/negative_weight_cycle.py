#https://yttm-work.jp/algorithm/algorithm_0012.html

#負閉路検出
def HasNegativeLoopRoute(graph,NodeNum):
    dist=[0]*(NodeNum)

    #頂点の数*辺の数だけ繰り返す
    for i in range(NodeNum):
        for Node in graph :            
            for childNode, weight in graph[Node].items():
                if (dist[childNode]>dist[Node]+weight): #エッジの始点の距離が更新済み
                    dist[childNode] = dist[Node]+weight #頂点までの距離を更新
                    #ベルマンフォードは頂点数*辺の数が最大とされているので、
                    #最大値を回した状況でも更新があるのは負閉路があると判断できる。
                    if (i==NodeNum-1):
                        return 1
                    
    return -1


file = open('Desktop/Downloads/rosalind_nwc.txt', 'r').read()#ファイルの書式を自分で変えてください。
N=int(file.split()[0])

tmp=[(blocks) for blocks in file.split("\n\n")]
tmp1=[block.split("\n") for block in tmp][1:]

answer=[]
for i in range(N):
    graphi={}
    NodeNum=int(tmp1[i][0].split()[0])
    for ele in tmp1[i][1:]:
        ele=list(map(int,ele.split(" ")))      
        if (ele[0]-1) not in graphi:
            graphi[ele[0]-1]={ele[1]-1:ele[2]}
        else:
            graphi[ele[0]-1].update({ele[1]-1:ele[2]}) 
    answer.append(HasNegativeLoopRoute(graphi,NodeNum))
        
print(' '.join(map(str, answer)))
