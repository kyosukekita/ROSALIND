#dijkstra algorithm

import heaps

def dijkstra(graph: dict, start):
  distances = {node:float("inf") for node in graph}
  distances[start]=0

  priority_queue =[(0, start)]
  
  while priority_queue:
    #最も近い頂点を取得
    current_distance, current_node = heapq.heappop(priority_queue)
    
    #既に処理されている頂点はスキップ
    if current_distance > distances[current_node]:
      continue

    #隣接する頂点の距離を更新
    for neighbor, weight in graph[current_node].items():
      distance = current_distance + weight
    
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(priority_queue, (distance, neighbor))

  return distances


# グラフの定義（隣接リスト）
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))




#bellman-Ford 

class Edge:
  def __init__(self, src, dest, weight):
    self.src = src
    self.dest = dest
    self.weight = weight

  def bellman_ford(edges: tuple, num_vertices, start_vertex):
    distances = [float("inf")]*num_vertices
    distances[start_vertex] = 0

    for _ in range(num_vertices-1):
      for edge in edges:
        if distances[edge.stc] != float("inf") and distances[edge.stc]+ edge.weight < distances[edge.dest]:
	  distances[edge.dest] = distances[edge.stc]+ edge.weight

    
    #negative weight cycleの検出


    for edge in edges:
      if distances[edge.src]!= float("inf") and distances[edge.src]+ edge.weight < distances[edge.dest]:
        #negative cycle found
	  return None
  
    return distances

# Example usage:
edges = [
    Edge(0, 1, -1),
    Edge(0, 2, 4),
    Edge(1, 2, 3),
    Edge(1, 3, 2),
    Edge(1, 4, 2),
    Edge(3, 2, 5),
    Edge(3, 1, 1),
    Edge(4, 3, -3)
]

distances = bellman_ford(edges, 5, 0)

if distances:
    print("Vertex Distance from Source Vertex")
    for i, d in enumerate(distances):
        print(f"{i}\t\t{d}")
else:
    print("Negative cycle detected!")




#beam search
#https://inarizuuuushi.hatenablog.com/entry/2022/08/22/090000

from headq import heapify, heappush, heappop, heappushpop

def beam_search(root, k, api):
    """
    Args:
        root : root node
        k : number of remain paths during search
        api : apis for beam search
    Notes:
        api must have functions as follows.
        (1) init : this is called at the begenning of this function
        (2) step : return path-list or path-generator of extended path from inputed path
        (3) score : return score for path, higher scores indicate better
        (4) count : this function is called for every end of loop
        (5) terminate : return true if it should terminate to search else false
    """

    paths=[(None, root)]
    heapify(paths)
    api.init()
    while not.api.terminate():
        top_paths=[]
	heapify(top_paths)
	for _, path in paths:
	    for extend_path in api.step(path):
	        score=api.score(extend_path)
		if len(top_paths)<k:
		    heappush(top_paths, (score, extend_path))
		else:
		    heappushpop(top_paths, (score, extend_path))
	    paths = top_paths
	    api.count()

    result_paths=[]
    result_paths_score=[]
    for _, path in paths:
        result_paths.append(path)
	result_paths_scpre.append(score)

    return result_paths, result_paths_score

#TSP(traveling salesman problem)を例に実行
class TSPAPI:
    def __init__(self, n):
        self.iter =0
	self.n = n
    def init(self):
	self.iter = 0
    def step(self, path):
	for i in range(self.n):
	    if i not in path:
	        yield path[:] +[i]
    def score(self, path):
	"""total distance path"""
	return -sum(D[i][j] for i, j in zip(path, path[1:]))
    def count(self):
	self.iter +=!
    def terminate(self):
	return self.iter>=self.n

1, init : 初期化関数 api.init() がbeam_searchの初めに1度呼ばれます
2, step : pathを入力として探索を1階層進めた pathのiterator/generatorを返す関数です
3, score : pathを入力としてそのpathの評価値を返す関数です。値が高いほど良いことを表します。
4, count : 探索が1ラウンド（上記の説明の3）が終了すると呼び出されます。
5, terminate : beam_searchを終了するべきであればtrue, そうでないならfalseを返します。



N = 4 #都市数
D = [
    [0, 1, 2, 3],
    [4, 0, 2, 1],
    [1, 2, 0, 3],
    [2, 3, 4, 0],
]#移動コスト平均

#例えば、k=２で実行して見る
from beam_search import beam_search
root = []
k=1
api = TSPAPI(N)
paths, scores = beam_search(root, k, api)
for path, score in zip(paths[::-1], scores[::-1]):
    print("path", path, "distance", -score)
