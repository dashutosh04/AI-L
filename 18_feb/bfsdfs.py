from collections import deque
import matplotlib.pyplot as plt
import pandas as pd


MAZE = [
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1],
]

START = (0, 0)
END = (4, 4)


def maze_print(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                print(".", end=" ")
            else:
                print("#", end=" ")
        print()


rows = len(MAZE)
cols = len(MAZE[0])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(maze, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored = 0

    while queue:
        (x, y), path_taken = queue.popleft()
        nodes_explored += 1

        if (x, y) == end:
            return path_taken, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path_taken + [(nx, ny)]))

    return None, nodes_explored


print("\nMaze:")
maze_print(MAZE)


def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0

    while stack:
        (x, y), path_taken = stack.pop()
        nodes_explored += 1

        if (x, y) == end:
            return path_taken, nodes_explored

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    if maze[nx][ny] == 1 and (nx, ny) not in visited:
                        stack.append(((nx, ny), path_taken + [(nx, ny)]))

    return None, nodes_explored


def compare_algorithms(maze, start, end):
    bfs_path, bfs_nodes = bfs(maze, start, end)
    dfs_path, dfs_nodes = dfs(maze, start, end)

    print("\n--- Comparison ---")
    print("BFS Path:", bfs_path)
    print("BFS Nodes Explored:", bfs_nodes)
    print("DFS Path:", dfs_path)
    print("DFS Nodes Explored:", dfs_nodes)
    if bfs_path and dfs_path:
        print("BFS Path Length:", len(bfs_path))
        print("DFS Path Length:", len(dfs_path))
        if len(bfs_path) < len(dfs_path):
            print("BFS found a shorter path.")
        elif len(bfs_path) > len(dfs_path):
            print("DFS found a shorter path.")
    


def plot_paths(maze, bfs_path, dfs_path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    ax1.set_title("BFS Path in the Maze")
    if bfs_path:
        bfs_x, bfs_y = zip(*bfs_path)
        ax1.plot(bfs_y, bfs_x, marker="o", color="blue", label="BFS Path")
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 0:
                ax1.scatter(j, i, color="black")
    
    ax1.invert_yaxis()
    ax1.legend()
    
    ax2.set_title("DFS Path in the Maze")
    if dfs_path:
        dfs_x, dfs_y = zip(*dfs_path)
        ax2.plot(dfs_y, dfs_x, marker="o", color="green", label="DFS Path")
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 0:
                ax2.scatter(j, i, color="black")
    
    ax2.invert_yaxis()
    ax2.legend()
    
    plt.tight_layout()
    plt.show()


plot_paths(MAZE, bfs(MAZE, START, END)[0], dfs(MAZE, START, END)[0])
compare_algorithms(MAZE, START, END)
