#https://yttm-work.jp/algorithm/algorithm_0012.html

file = open('Desktop/Downloads/rosalind_ba5d.txt').read()
source=int(file.split("\n")[0])
sink=int(file.split("\n")[1])

edges=[edge for edge in file.split("\n")[2:] if edge!='']
#グラフを描く
graph={}
for edge in edges:
    start=int(edge.split("-")[0])
    end,weight=[int(i) for i in (edge.split(">")[-1].split(":"))]#ここ工夫頑張ったよね
    if start not in graph:
        graph[start]={end:weight}
    else:
        graph[start].update({end:weight})

        

dist=[-float("inf") for _ in range(sink+1)]
dist[source]=0#初期化
last_update_node=[-1 for _ in range(sink+1)]#コストを更新するときにその頂点の直前の頂点を保持する

#ベルマンフォードの最長経路verで最長経路の長さを求める
while True:
    is_updated=False#更新の有無を確認
    for node in graph:
        for childnode, weight in graph[node].items():
            if dist[childnode]<dist[node]+weight:
                dist[childnode]=dist[node]+weight
                last_update_node[childnode]=node#コストを更新するときにその頂点の直前の頂点を保持する
                is_updated=True
    if(is_updated==False):
        break
        
"""更新した頂点IDの配列が完成したら、終点の頂点IDから順番に
始点までの頂点IDを保存していく"""

route_id=[]#経路保存
current_route_id=sink #今チェック中の経路ID
route_id.append(sink)
while (True):
    next_id=last_update_node[current_route_id]
    
    #始点じゃなかったら追加
    if current_route_id!=source:
        route_id.insert(0,next_id)
        current_route_id=next_id
    else:
        break
    
print(dist[sink])
print("->".join(map(str,route_id)))
