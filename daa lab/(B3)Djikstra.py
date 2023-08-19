import heapq

def dijkstra(graph,source):
  distances = {vertex : float('inf') for vertex in graph}
  distances[source] = 0
  priorityQueue = [(0,source)]
  while priorityQueue:
    currentDistance, currentVertex = heapq.heappop(priorityQueue)
    if currentDistance > distances[currentVertex]:
      continue
    for neighbour,weight in graph[currentVertex].items():
      distance = currentDistance+weight
      if distance < distances[neighbour]:
        distances[neighbour] = distance
        heapq.heappush(priorityQueue,(distance,neighbour))
  return distances


graph = {
    '1': {'2': 10, '5': 100},
    '2': {'1': 10, '3': 50},
    '3': {'2': 50, '4': 20,'5':10},
    '4': {'3': 20, '5': 60},
    '5': {'1': 100,'3': 10,'4':60}
}

print("Shortest path form source '1' is : ")
shortesPath = dijkstra(graph,'1')
for vertex,distance in shortesPath.items():
  print(f"For {vertex} : {distance}")