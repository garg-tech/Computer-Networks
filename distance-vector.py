# Define max_dist to indicate no edge
max_dist = 1000

def print_path(vec):
    path = ""
    for v in vec:
        path += chr(122 - v) + " "
    return path.strip()

# def found(vec, value):
#     return value in vec

def bellman_ford(G, n, src):
    distance = [max_dist] * n
    next_hop = [-1] * n
    shortest_path = [[] for _ in range(n)]
    
    distance[src] = 0
    
    for k in range(n):  # Looping through every node
        for i in range(n):
            for j in range(n):
                if G[i][j] != 0 and distance[i] != max_dist and (distance[j] > distance[i] + G[i][j]):
                    distance[j] = distance[i] + G[i][j]
                    next_hop[j] = i
                    # if not found(shortest_path[j], i):
                    if i != src:
                        shortest_path[j] = list(shortest_path[i])
                    shortest_path[j].append(j)
        
        print(f"Iteration: {k + 1}")
        print("-" * 72)
        print(f"{'Destination':<15}{'Distance from destination':<30}{'Shortest path from source':<25}")
        print("-" * 72)
        for t in range(n):
            if t != src:
                print(f"{chr(122 - t):<15}{distance[t]:<30}{chr(122 - src)} {print_path(shortest_path[t]):<25}")
        print("-" * 72)

def main():
    graph = [
    #    Z  Y  X  W  V  U  T  S
        [0, 14, 0, 0, 0, 0, 2, 0], # Z
        [14, 0, 6, 0, 1, 0, 4, 0], # Y
        [0, 6, 0, 1, 3, 0, 0, 0], # X
        [0, 0, 1, 0, 1, 3, 0, 0], # W
        [0, 1, 3, 1, 0, 1, 9, 0], # V
        [0, 0, 0, 3, 1, 0, 2, 4], # U
        [2, 4, 0, 0, 9, 2, 0, 1], # T
        [0, 0, 0, 0, 0, 4, 1, 0] # S
    ]
    
    bellman_ford(graph, 8, 0)

if __name__ == "__main__":
    main()