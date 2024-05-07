def find_shortest_path(G, Vertices, Edges, edge, Source):
    distance = [float('inf')] * Vertices
    parent = [-1] * Vertices
    flag = 1

    distance[Source] = 0

    for _ in range(Vertices - 1):
        for k in range(Edges):
            u, v = edge[k][0], edge[k][1]
            if distance[u] + G[u][v] < distance[v]:
                distance[v] = distance[u] + G[u][v]
                parent[v] = u

    for k in range(Edges):
        u, v = edge[k][0], edge[k][1]
        if distance[u] + G[u][v] < distance[v]:
            flag = 0

    print("Destination\tCost\tPath")
    if flag:
        for i in range(Vertices):
            nodes = []
            next_node = i
            while next_node != -1:
                nodes.insert(0, next_node)
                next_node = parent[next_node]

            path_str = ""
            for node in nodes:
                path_str += str(node) + " --> "
            path_str = path_str[:-5]  # Remove the trailing " --> "
            print(f"{i}\t\t{distance[i]}\t{path_str}")
            
if __name__ == "__main__":
    Vertices = 6
    edge = [[0, 1],[0,2],[1,0], [1, 2],[1,3],[2,0],[2,1] ,[2, 3],[2,4], [3,2],[3, 4], [3,5],[4, 5]]  # Replace with your edge list
    graph = [
        [0, 1, 5, 0, 0, 0],
        [1, 0, 3, 4, 0, 0],
        [5, 3, 0, 5, 9, 0],
        [0, 4, 5, 0, 2, 6],
        [0, 0, 9, 2, 0, 3],
        [0, 0, 0, 6, 3, 0]
    ]

    print("The Adjacency Matrix representation of the graph")
    for i in range(Vertices):
        for j in range(Vertices):
            print(f"{graph[i][j]}\t", end="")
            if graph[i][j] != 0:
                edge.append([i, j])

        print()

    for i in range(Vertices):
        print(f"\nSource vertex {i}\n")
        find_shortest_path(graph, Vertices, len(edge), edge, i)
        
        
    