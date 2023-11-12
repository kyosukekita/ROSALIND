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
