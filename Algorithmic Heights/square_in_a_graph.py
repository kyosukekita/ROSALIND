file = open('Desktop/Downloads/rosalind_sq.txt', 'r').read()
N=int(file.split()[0])

tmp=[(blocks) for blocks in file.split("\n\n")]
tmp1=[block.split("\n") for block in tmp][1:]


def SQ(adj,NodeNum):
    flag=False
    for i in range(NodeNum):
        first=[j for j in range(NodeNum) if adj[i][j]==1]

        for x in range(i+1,NodeNum):
            second=[y for y in range(NodeNum) if adj[x][y]==1]
    
            if len(set(first)&set(second))>=2:
                return 1

    return -1
                

answer=[]
for i in range(N):
    NodeNum=int(tmp1[i][0].split()[0])
    adj_matrix=[[0 for _ in range(NodeNum)] for _ in range(NodeNum)]#隣接行列を思い浮かべよ
    for ele in tmp1[i][1:]:
        ele=list(map(int,ele.split(" ")))      
        adj_matrix[ele[0]-1][ele[1]-1]=1
        adj_matrix[ele[1]-1][ele[0]-1]=1
    answer.append(SQ(adj_matrix,NodeNum))

print(' '.join(map(str,answer)))
