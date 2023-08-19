
import sys

def nearest_neighbor(graph, start):
    num_cities = len(graph)
    visited = [False] * num_cities
    tour = [start]
    total_distance = 0
    current_city = start
    visited[current_city] = True

    for _ in range(num_cities - 1):
        min_distance = sys.maxsize
        nearest_city = -1

        for city in range(num_cities):
            if not visited[city] and graph[current_city][city] < min_distance:
                min_distance = graph[current_city][city]
                nearest_city = city

        tour.append(nearest_city)
        total_distance += min_distance
        current_city = nearest_city
        visited[current_city] = True

    tour.append(start)  # Return to starting city
    total_distance += graph[current_city][start]

    return tour, total_distance

# Example graph representing distances between cities
graph = [
    [0, 2, 9999, 12, 5],
    [2, 0, 4, 8, 9999],
    [9999, 4, 0, 3, 3],
    [12, 8, 18, 0,10],
    [5, 9999, 3, 10, 0],
]

start_city = 0  # Starting city

tour, total_distance = nearest_neighbor(graph, start_city)
print("Tour:", tour)
print("Total Distance:", total_distance)