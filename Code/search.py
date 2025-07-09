
import sys
from collections import deque
import heapq
import subprocess

class Node:
    def __init__(self, parent =None, position=None):
        self.parent = parent;
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    def __lt__(self, other):
        return self.g < other.g

def get_h_value(x, y, goal):
    return abs(x - goal.position[0]) + abs(y - goal.position[1]) 

def validSpace(newNodePos, cityMap):
    return newNodePos[0] < 0 or newNodePos[0] > (len(cityMap) - 1) or newNodePos[1] < 0 or newNodePos[1] > len(cityMap[len(cityMap)-1]) - 1

def isWall(newNodePos, cityMap):
    return cityMap[newNodePos[0]][newNodePos[1]] != 0

def reconstruct_path(current_node): 
    path = []
    while current_node:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]

def aStarSearch(cityMap, start, goal):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    goal_node = Node(Node, goal)
    goal_node.g = goal_node.h = goal_node.f = 0
    openList = [] 
    closedList = set() 
    openList.append(start_node)
    while openList:
        current_node = min(openList, key=lambda node: node.f)
        openList.remove(current_node)
        closedList.add(current_node.position)

        if current_node == goal_node:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1], len(closedList)
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        neighbors = []

        for direction in directions:
            new_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            if validSpace(new_position, cityMap) or isWall(new_position, cityMap):
                continue

            new_node = Node(current_node, new_position)
            neighbors.append(new_node)
        for neighbor in neighbors:
            if neighbor.position in closedList:
                continue
            neighbor.g = current_node.g + 1
            neighbor.h = get_h_value(neighbor.position[0], neighbor.position[1], goal_node)
            neighbor.f = neighbor.g + neighbor.h
            if any(open_node for open_node in openList if neighbor == open_node and neighbor.f >= open_node.f):
                continue

            openList.append(neighbor)
    return None, len(closedList)

def DFS(city_map, start, goal):
    start_node = Node(None, start)
    goal_node = Node(Node, goal)

    stack = []
    visited = set()

    stack.append(start_node)

    while stack:
        current_node = stack.pop()
        visited.add(current_node.position)

        if current_node == goal_node:
                path = []
                current = current_node
                while current:
                    path.append(current.position)
                    current = current.parent
                return path[::-1], len(visited) 
        
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        neighbors = []

        for direction in directions:
            new_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            if validSpace(new_position, city_map) or isWall(new_position, city_map):
                continue

            new_node = Node(current_node, new_position)

            
            if new_node.position not in visited:
                neighbors.append(new_node)

        stack.extend(neighbors) 
    return None, len(visited)

def BFS(city_map, start, goal):
    start_node = Node(None, start)
    goal_node = Node(None, goal)
    queue = deque([start_node])
    visited = set()
    visited.add(start_node.position)

    while queue:
        current_node = queue.popleft()

        if current_node == goal_node:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1], len(visited) 
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        neighbors = []

        for direction in directions:
            new_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            if validSpace(new_position, city_map) or isWall(new_position, city_map):
                continue

            new_node = Node(current_node, new_position)
            if new_node.position not in visited:
                neighbors.append(new_node)
                visited.add(new_node.position)
        queue.extend(neighbors)
    return None, len(visited)

def IDS(city_map, start, goal):
    start_node = Node(None, start)
    goal_node = Node(None, goal)

    def DLS(current_node, goal_node, depth_limit):
        if current_node == goal_node:
            return reconstruct_path(current_node), True

        if depth_limit <= 0:
            return None, False

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] 
        for direction in directions:
            new_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            if validSpace(new_position, city_map) or isWall(new_position, city_map):
                continue

            new_node = Node(current_node, new_position)

            
            path, found = DLS(new_node, goal_node, depth_limit - 1)
            if found:
                return path, found  

        return None, False
    depth = 0
    while True:
        
        path, found = DLS(start_node, goal_node, depth)
        if found:
            return path, depth  
        depth += 1  

def GBFS(city_map, start, goal):
    start_node = Node(None, start)
    goal_node = Node(None, goal)

    open_list = []
    heapq.heappush(open_list, (start_node.h, start_node))
    visited = set()

    while open_list:
        _, current_node = heapq.heappop(open_list)
        visited.add(current_node.position)
        if current_node == goal_node:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1], len(visited)

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for direction in directions:
            new_position = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            if validSpace(new_position, city_map) or isWall(new_position, city_map):
                continue

            new_node = Node(current_node, new_position)
            new_node.h = get_h_value(new_node.position[0], new_node.position[1], goal_node)

            if new_node.position not in visited:
                heapq.heappush(open_list, (new_node.h, new_node))

    return None, len(visited)


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    grid_size = eval(lines[0].strip())  
    start = eval(lines[1].strip())  
    goal = eval(lines[2].split('|')[0].strip())  
    
    city_map = [[0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]

    for line in lines[3:]:
        x, y, w, h = eval(line.strip())
        for i in range(h):
            for j in range(w):
                city_map[y + i][x + j] = 1  

    return city_map, start, goal
def save_results(city_map, start, goal, path, output_file='path_data.txt'):
    with open(output_file, 'w') as f:
       
        f.write(f"{len(city_map)}, {len(city_map[0])}\n")

        for row in city_map:
            f.write(' '.join(map(str, row)) + '\n')

        f.write(f"{start}\n")
        f.write(f"{goal}\n")
        for step in path:
            f.write(f"{step}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return

    filename = sys.argv[1]
    method = sys.argv[2]

    city_map, start, goal = read_file(filename)

    if method == 'A*':
        path, num_nodes = aStarSearch(city_map, start, goal)
    elif method == 'DFS':
        path, num_nodes = DFS(city_map, start, goal)
    elif method == 'BFS':
        path, num_nodes = BFS(city_map, start, goal)
    elif method == 'GBFS':
        path, num_nodes = GBFS(city_map, start, goal)
    elif method == 'IDS':
        path, num_nodes = IDS(city_map, start, goal)
    else:
        print("Unknown search method. Use 'A*', 'DFS', or 'BFS', 'GBFS.")
        return

    if path:
        print(f"{filename} {method}")
        print(f"Goal reached: {goal}, Nodes expanded: {num_nodes}")
        print(f"Path: {path}")
        save_results(city_map, start, goal, path)


        subprocess.run(['python', 'gui.py', 'path_data.txt'])
    else:
        print(f"{filename} {method}")
        print(f"No goal is reachable; Nodes expanded: {num_nodes}")


if __name__ == '__main__':
    main()
    


