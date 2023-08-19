graph = {
 '0': ['1', '2','3'],
 '1': ['0', '2', '4'],
 '2': ['0','1','4'],
 '3': ['4','0'],
 '4': ['1','2', '3']
}
visited = set() # Set to keep track of visited nodes.
def dfs(visited, graph, node):
  if  node not in visited: # If the node has not been visited
    print(node) # Print the node
    visited.add(node) # Mark the node as visited
    for child in graph[node]: # Explore each child of the node
        dfs(visited, graph, child) # Recursive call to explore child nodes
# Driver Code
dfs(visited, graph, '0') 