#深さ優先探索(DFS)の応用問題。DFSを使って二部グラフ判定ができる。参考：http://prd-xxx.hateblo.jp/entry/2017/10/13/004256
#重要なポイント: DFSは再帰関数と相性が良い。

file = open('Desktop/Downloads/rosalind_bip (1).txt', 'r').read()
n=int(file.split()[0])

tmp=[(blocks) for blocks in file.split("\n\n")]
tmp1=[block.split("\n") for block in tmp][1:]

graphs=[]
for i in range(n):
    graphi=[]
    for ele in tmp1[i]:
        ele=list(map(int,ele.split(" ")))
        graphi.append(ele)
    graphs.append(graphi)
#graphs:[[[3, 3], [1, 2], [3, 2], [3, 1]], [[4, 3], [1, 4], [3, 1], [1, 2]]]



"""最初は適当に1か所を黒色で塗って、後はDFSで白、黒、白と塗っていって矛盾が
無ければ2部グラフ"""

def testing_bipartiteness(graphs):
    answer=[]
    for i in range(n):
        a=graphs[i][0][0]
        graphn=[[] for _ in range(a)]#ここで各グラフ構造を作る.このグラフを次のdfs関数で処理していく。
        for edge in graphs[i][1:]:
            graphn[edge[0]-1].append(edge[1]-1)
            graphn[edge[1]-1].append(edge[0]-1) 
        
        colors=[(0) for i in range(len(graphn)+1)]#n個の頂点の色を初期化。1(黒確定)、0(未訪問)、-1(白確定)
        
        def dfs(v,color):
            #今いる点vを着色
            colors[v] = color
            #今の頂点から行けるところをチェック
            for next_node in graphn[v]:
                #同じ色が隣接してしまったらFalse
                if colors[next_node] == color:
                    return False
            #未着色の頂点があったら反転した色を指定し、再帰的に調べる
                if colors[next_node] == 0 and not dfs(next_node, -color):
                    return False
            #調べ終わったら矛盾がないのでTrue
            return True
        
        if dfs(0,1):
            answer.append("1")
        else:
            answer.append("-1")
    
    return answer


print(' '.join(testing_bipartiteness(graphs)))
