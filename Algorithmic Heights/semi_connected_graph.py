#general_sink.pyと同じコードで解けた

file = open('Desktop/Downloads/rosalind_sc.txt', 'r').read()
N=int(file.split()[0])

tmp=[(blocks) for blocks in file.split("\n\n")]
tmp1=[block.split("\n") for block in tmp][1:]


def semiConnected(graph,NodeNum):
    answer=-1
    for i in range(NodeNum):
        visited=[False for _ in range(NodeNum)]
        def dfs(s):
            visited[s]=True
            for t in graph[s]:
                if visited[t]==False:
                    dfs(t)
        
        
        visited=[False for _ in range(NodeNum)]
        dfs(i)
        if visited.count(True)==NodeNum:
            answer=1
            break

    return answer
                

answer=[]
for i in range(N):
    graphi=[[] for _ in range(len(tmp1[i]))]
    NodeNum=int(tmp1[i][0].split()[0])
    for ele in tmp1[i][1:]:
        ele=list(map(int,ele.split(" ")))      
        graphi[ele[0]-1].append(ele[1]-1)
    answer.append(GeneralSink(graphi,NodeNum))

print(' '.join(map(str,answer)))
