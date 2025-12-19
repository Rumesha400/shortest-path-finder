import heapq
import time
import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        if 0 <= u < self.V and 0 <= v < self.V:
            self.edges.append((u, v, weight))
        else:
            raise ValueError(f"Edge ({u}, {v}) includes invalid vertex. Ensure vertices are in range [0, {self.V - 1}].")

    def dijkstra(self, start):
        if start < 0 or start >= self.V:
            raise ValueError(f"Starting vertex {start} is invalid.")
        distances = {i: float('inf') for i in range(self.V)}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for edge in self.edges:
                if edge[0] == current_vertex:
                    neighbor, weight = edge[1], edge[2]
                    distance = current_distance + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def bellman_ford(self, start):
        if start < 0 or start >= self.V:
            raise ValueError(f"Starting vertex {start} is invalid.")
        distances = {i: float('inf') for i in range(self.V)}
        distances[start] = 0

        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Check for negative weight cycles
        for u, v, weight in self.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

        return distances

    def compare_algorithms(self, start):
        print("\nComparing Dijkstra and Bellman-Ford Algorithms:\n")

        # Measure Dijkstra
        start_time = time.time()
        dijkstra_result = self.dijkstra(start)
        dijkstra_time = time.time() - start_time

        # Measure Bellman-Ford
        start_time = time.time()
        try:
            bellman_ford_result = self.bellman_ford(start)
            bellman_ford_time = time.time() - start_time
        except ValueError as e:
            bellman_ford_result = str(e)
            bellman_ford_time = time.time() - start_time

        # Display results
        print(f"Dijkstra's Algorithm:\nShortest distances: {dijkstra_result}\nTime taken: {dijkstra_time:.6f} seconds\n")
        if isinstance(bellman_ford_result, str):
            print(f"Bellman-Ford Algorithm:\n{bellman_ford_result}\nTime taken: {bellman_ford_time:.6f} seconds\n")
        else:
            print(f"Bellman-Ford Algorithm:\nShortest distances: {bellman_ford_result}\nTime taken: {bellman_ford_time:.6f} seconds\n")

        # Recommendation
        print("Recommendation:")
        if isinstance(bellman_ford_result, str):
            print("Bellman-Ford failed due to negative weight cycles. Use Dijkstra for non-negative weights.")
        elif dijkstra_time < bellman_ford_time:
            print("Dijkstra is faster and recommended for this graph.")
        else:
            print("Bellman-Ford is more robust and recommended for graphs with negative weights.")


def main():
    print("Shortest Path Finder using Dijkstra and Bellman-Ford algorithms")
    
    # Step 1: Input number of vertices
    try:
        vertices = int(input("Enter the number of vertices: "))
        if vertices <= 0:
            print("Number of vertices must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer for the number of vertices.")
        return

    g = Graph(vertices)

    # Step 2: Input number of edges
    try:
        edges = int(input("Enter the number of edges: "))
        if edges <= 0 or edges > vertices * (vertices - 1):
            print(f"Invalid number of edges. It should be between 1 and {vertices * (vertices - 1)}.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer for the number of edges.")
        return

    # Step 3: Choose edge generation method
    print("\nChoose edge generation method:")
    print("1. Generate random edges")
    print("2. Enter edges manually")
    try:
        method = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("Invalid input. Please enter either 1 or 2.")
        return

    if method == 1:
        # Random edge generation
        generated_edges = set()
        while len(generated_edges) < edges:
            u, v = random.randint(0, vertices - 1), random.randint(0, vertices - 1)
            while u == v or (u, v) in generated_edges or (v, u) in generated_edges:
                u, v = random.randint(0, vertices - 1), random.randint(0, vertices - 1)
            w = random.randint(1, 20)  # Random weight between 1 and 20
            g.add_edge(u, v, w)
            generated_edges.add((u, v))
        print("\nRandom edges generated successfully:")
        for edge in g.edges:
            print(f"Edge from {edge[0]} to {edge[1]} with weight {edge[2]}")
    elif method == 2:
        # Manual edge input
        entered_edges = set()
        print("Enter edges in the format (source destination weight):")
        while len(entered_edges) < edges:
            try:
                u, v, w = map(int, input(f"Enter edge {len(entered_edges) + 1}/{edges}: ").split())
                if (u, v) in entered_edges or (v, u) in entered_edges:
                    print("Duplicate edge detected. Please enter a unique edge.")
                    continue
                if u < 0 or v < 0 or u >= vertices or v >= vertices:
                    print(f"Invalid vertices. Enter vertices between 0 and {vertices - 1}.")
                    continue
                g.add_edge(u, v, w)
                entered_edges.add((u, v))
            except ValueError:
                print("Invalid input format. Please enter the edge as three space-separated integers.")
    else:
        print("Invalid choice! Please restart the program and choose either 1 or 2.")
        return

    print("\nEdges added to the graph:")
    for edge in g.edges:
        print(f"Edge from {edge[0]} to {edge[1]} with weight {edge[2]}")

    # Step 4: Ask for algorithm choice after edges are successfully added
    while True:
        print("\nChoose an option:")
        print("1. Run Dijkstra")
        print("2. Run Bellman-Ford")
        print("3. Compare Dijkstra and Bellman-Ford")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
            continue

        if choice == 4:
            print("Exiting the program.")
            break

        if choice in [1, 2, 3]:
            start = int(input("Enter the starting vertex: "))
            
            if choice == 1:
                try:
                    result = g.dijkstra(start)
                    print("Shortest distances from vertex", start, "using Dijkstra:")
                    for vertex, distance in result.items():
                        print(f"Vertex {vertex} -> Distance {distance}")
                except ValueError as e:
                    print(e)

            elif choice == 2:
                try:
                    result = g.bellman_ford(start)
                    print("Shortest distances from vertex", start, "using Bellman-Ford:")
                    for vertex, distance in result.items():
                        print(f"Vertex {vertex} -> Distance {distance}")
                except ValueError as e:
                    print(e)

            elif choice == 3:
                g.compare_algorithms(start)

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()