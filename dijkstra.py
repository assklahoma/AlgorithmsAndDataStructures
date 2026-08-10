import sys

print("Graph Algorithms: Dijkstra's Algorithm")

def dijkstra(graph, start_vertex):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    distances[start_vertex] = 0
    visited = [False] * num_vertices
    previous_vertices = [-1] * num_vertices
    
    for _ in range(num_vertices):
        min_dist = sys.maxsize
        u = -1
        
        for i in range(num_vertices):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i
                
        if u == -1:
            break
            
        visited[u] = True
        
        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v]:
                new_dist = distances[u] + graph[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    previous_vertices[v] = u
                    
    return distances, previous_vertices

def print_paths(distances, previous_vertices, start_vertex):
    print(f"\nShortest paths from Vertex {start_vertex}:\n")
    for i in range(len(distances)):
        if i == start_vertex:
            continue
            
        if distances[i] == sys.maxsize:
            print(f"To vertex {i}: Unreachable")
            continue
            
        path = []
        curr = i
        while curr != -1:
            path.insert(0, curr)
            curr = previous_vertices[curr]
            
        print(f"To vertex {i}: Path {path}, Total Distance = {distances[i]}")

#Example Graph Matrix
graph_matrix = [
    [0, 6, 2, 0, 8, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 7, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

start_node = 0
distances, previous = dijkstra(graph_matrix, start_node)
print_paths(distances, previous, start_node)
