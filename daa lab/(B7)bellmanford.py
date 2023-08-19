class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest 
        # path from src to any other vertex can have at most |V| - 1 
        # edges
        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices
            # of the picked vertex.Consider only those vertices which are
            # still in queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles. The above step 
        # guarantees shortest distances if graph doesn't contain 
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        for i in range(self.V):
            print("Vertex distance from source", i, "is:", dist[i])

# Example usage:
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)
g.bellman_ford(0)

# def bellman_ford(vertices, edges, start):
#  distances = {v: float('inf') for v in vertices}
#  distances[start] = 0
#  for _ in vertices:
#   for u, v, weight in edges:
#    if distances[u] + weight < distances[v]:
#      distances[v] = distances[u] + weight
#  return distances
# # Example usage
# vertices = ['A', 'B', 'C', 'D', 'E','F']
# edges = [('A', 'B', -4),
#         ('B', 'E', -2), 
#         ('B', 'D', -1), 
#         ('D', 'A', 6),
#         ('A', 'F', -3),   
#         ('D', 'F', 4), 
#         ('E', 'F', 2), 
#         ('C','B', 8),
#         ('C','F', 3) ]
# start_vertex = 'A'
# shortest_distances = bellman_ford(vertices, edges, start_vertex)
# print("Shortest distances from vertex", start_vertex + ":", 
# shortest_distances)
