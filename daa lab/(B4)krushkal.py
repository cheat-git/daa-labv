graph = [
    [999, 10, 999, 999, 5],
    [10, 999, 1, 6, 999],
    [999, 1, 999, 2, 7],
    [999, 6, 2, 999, 3],
    [5, 999, 7, 3, 999]
]

parent = [0, 1, 2, 3, 4]  # Parent array to track disjoint sets

def find_parent(a):
    while parent[a] != a:
        a = parent[a]
    return a

def merge_sets(a, b):
    i = find_parent(a)
    j = find_parent(b)
    parent[i] = j

def kruskal():
    edge_count = 0
    total_cost = 0

    while edge_count < len(graph) - 1:
        min_weight = 999
        selected_a = 0
        selected_b = 0

        for i in range(len(graph)):
            for j in range(len(graph)):
                if find_parent(i) != find_parent(j) and graph[i][j] < min_weight:
                    min_weight = graph[i][j]
                    selected_a = i
                    selected_b = j

        merge_sets(selected_a, selected_b)
        print(f"{selected_a+1} --> {selected_b+1} with weight: {min_weight}")
        total_cost += min_weight
        edge_count += 1

    print(f"Minimum Cost: {total_cost}")

kruskal()
