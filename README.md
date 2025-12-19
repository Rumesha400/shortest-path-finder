# 🧭 Shortest Path Finder using Dijkstra & Bellman-Ford Algorithms

A Python-based command-line application that implements and compares **Dijkstra’s Algorithm** and **Bellman–Ford Algorithm** for finding the shortest paths in a weighted graph. The tool supports both **manual edge input** and **random graph generation**, measures execution time, and provides algorithm recommendations based on performance and graph characteristics.

---

## 🚀 Features

- Implements **Dijkstra’s Algorithm** using a priority queue (heap)
- Implements **Bellman–Ford Algorithm** with negative cycle detection
- Supports **random graph generation**
- Supports **manual edge input**
- Validates vertices and edges with proper error handling
- Compares execution time of both algorithms
- Recommends the optimal algorithm based on results
- Interactive **menu-driven CLI**

---

## 🧠 Algorithms Overview

### Dijkstra’s Algorithm
- Efficient for graphs with **non-negative weights**
- Uses a priority queue for optimal performance  
- Time Complexity: **O((V + E) log V)**

### Bellman–Ford Algorithm
- Works with **negative edge weights**
- Detects **negative weight cycles**
- Time Complexity: **O(V × E)**

---
├── shortest_path_finder.py
├── README.md

---

## 🛠️ Requirements

- Python 3.x
- Uses built-in libraries only:
  - `heapq`
  - `time`
  - `random`

---

## ▶️ How to Run

Clone the repository:
git clone https://github.com/your-username/shortest-path-finder.git

Navigate to the project directory:
cd shortest-path-finder


Run the program:
python shortest_path_finder.py

---

## 🧪 Usage Flow

1. Enter the number of vertices
2. Enter the number of edges
3. Choose edge input method:
   - Random edge generation
   - Manual edge input
4. Select an operation:
   - Run Dijkstra
   - Run Bellman-Ford
   - Compare both algorithms
   - Exit
5. Enter the starting vertex when prompted

---

## 📄 Sample Output

Dijkstra's Algorithm:
Shortest distances: {0: 0, 1: 4, 2: 7}
Time taken: 0.000012 seconds

Bellman-Ford Algorithm:
Shortest distances: {0: 0, 1: 4, 2: 7}
Time taken: 0.000031 seconds

Recommendation:
Dijkstra is faster and recommended for this graph.

---

## 📌 Use Cases

- Data Structures & Algorithms practice
- Shortest path computation
- Performance comparison of graph algorithms
- Academic assignments and mini-projects

---

## 🔮 Future Enhancements

- Support for directed/undirected graph selection
- Visualization of graph and paths
- File-based graph input
- Support for larger datasets
- GUI or web-based interface

---

## 👩‍💻 Author

Rumesh  
GitHub: https://github.com/Rumesha400

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you find this project useful, consider giving it a star!
## 📁 Project Structure

