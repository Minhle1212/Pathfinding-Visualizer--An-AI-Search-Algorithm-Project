# Pathfinding Visualizer: An AI Search Algorithm Project
 Assigment 1 for course COS30019


This project, developed for the course COS30019, Introduction to Artifical Intelignec, implements and visualizes various tree-based search algorithms for pathfinding. An AI agent navigates a 2D grid-based map with obstacles, finding a path from a start to a goal position. The process is visualized using a simple graphical user interface.

 Description
This project finds a path from an origin to a destination on an 2D map, not through walls or obstacles. It puts into practice several of the traditional search algorithms found in the field of Artificial Intelligence. The project can read map configurations from text files, apply a specified search algorithm, and output the results, such as the path found and the number of nodes visited. A graphical user interface written with Tkinter shows the map, the obstacles, and the path found.


Algorithms implemented
    Uninformed Search
Depth-First Search (DFS): Explores as far as possible along each branch before backtracking. It uses a LIFO stack to manage nodes. 

Breadth-First Search (BFS): Explores all nodes at the present depth before moving on to nodes at the next depth level. It uses a FIFO queue and is guaranteed to find the shortest path. 

Iterative Deepening Search (IDS): A hybrid approach that combines the depth-first search strategy with the completeness of breadth-first search by performing a series of depth-limited searches

    Informed Search
A* Search (A*): Expands nodes based on a combination of the cost to reach the node (g(n)) and a heuristic estimate of the cost to the goal (h(n)). It guarantees the shortest path if the heuristic is admissible. 

Greedy Best-First Search (GBFS): Expands the node that appears to be closest to the goal, based solely on the heuristic value. It is fast but does not guarantee the shortest path