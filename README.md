# Pathfinding Visualizer
This is a Python program that allows users to visulaize pathfinding algorithms using Pygame. Users can add obstables, choose different algorithms, and visualize the pathfinding process step-by-step.

## Features
* Supportds several pathfinding algorithms, including A* and Dijkstra's
* Users can add or remove obstacles and visualize the pathfinding process step-by-step
* The program provides real-time feedback on the progress of the pathfinding algorithm


## Getting Started
To use this program, you will beed to have Python3 and Pygame installed on your computer. You can install Python3 by heading to this website: https://www.python.org/downloads/

To install Pygame, use the following command:
```
pip install pygame
```

Once installed, download the git repo and navigate to the directory:
```
git clone https://github.com/gnoixs/pathfinder.git
```

You can run the program using the following command:
```
python main.py
```

## Algorithms
This program supports the following pathfinding algorithms:

* A*: A* (pronounced "A star") is a popular pathfinding algorithm that combines the best features of Dijkstra's algorithm and greedy search. It finds the shortest path between two points by calculating the cost of each possible path and using a heuristic function to estimate the remaining distance to the goal. A* is widely used in video games and robotics due to its efficiency and accuracy.

* BFS (Breadth-First Search): BFS is a simple pathfinding algorithm that explores all possible paths in a maze or graph, starting from the root node and moving outwards in a breadth-first manner. It is guaranteed to find the shortest path in an unweighted graph or maze, but may not be efficient for larger and more complex problems.

* Bidirectional A*: Bidirectional A* is an optimization of the A* algorithm that simultaneously searches from both the start and end nodes, meeting in the middle when the paths intersect. This approach can significantly reduce the time and memory required to find the shortest path in a large graph or maze.

* DFS (Depth-First Search): DFS is another simple pathfinding algorithm that explores all possible paths in a maze or graph, but moves deeper into each path before backtracking to explore other paths. It is not guaranteed to find the shortest path in a maze or graph, but may be more efficient than BFS for some problems.

* Dijkstra's Algorithm: Dijkstra's algorithm is a popular pathfinding algorithm that finds the shortest path between two nodes in a weighted graph. It works by exploring the graph in a breadth-first manner, starting from the source node and updating the cost of each possible path as it goes. Dijkstra's algorithm is guaranteed to find the shortest path in a graph with non-negative weights.

* Greedy Search: Greedy search is a pathfinding algorithm that chooses the path that looks the best at each step, without considering the long-term consequences of that choice. It is often used as a heuristic for more complex algorithms like A* or bidirectional A*. Greedy search may not always find the shortest path, but is often faster and requires less memory than more complex algorithms.

## Usage
To use this program, fow these steps:

1. Select the start and end node
2. Add or remove obstables using the mouse
3. Choose the algorithm that you want to use
4. Visualize the pathfinding process by selecting the start button

## Example

## License
MIT License

Copyright (c) [2020] [Samantha Xiong]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
