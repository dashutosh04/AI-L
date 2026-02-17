import pandas as pd
import matplotlib.pyplot as plt

MAZE = [
    [1,1,1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1]
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

directions = [(0,1), (1,0), (0,-1), (-1,0)]

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


print("\nMaze:")
maze_print(MAZE)

print("\n--- DFS ---")
dfs_path, dfs_nodes = dfs(MAZE, START, END)
print("DFS Path:", dfs_path)
print("DFS Nodes Explored:", dfs_nodes)

graph = plt.figure(figsize=(6, 6))
plt.title("DFS Path and BFS Path in the Maze")
plt.xlim(-1, cols)
plt.ylim(-1, rows)
for i in range(rows):
    for j in range(cols):
        if MAZE[i][j] == 0:
            plt.scatter(j, rows - 1 - i, color="black", s=100)
        else:
            plt.scatter(j, rows - 1 - i, color="white", edgecolor="black", s=100)
if dfs_path:
    path_x = [y for x, y in dfs_path]
    path_y = [rows - 1 - x for x, y in dfs_path]
    plt.plot(path_x, path_y, color="blue", linewidth=2)
    
if bfs_path:
    bfs_path_x = [y for x, y in bfs_path]
    bfs_path_y = [rows - 1 - x for x, y in bfs_path]
    plt.plot(bfs_path_x, bfs_path_y, color="orange", linewidth=2)

plt.scatter(START[1], rows - 1 - START[0], color="green", s=100, label="Start")
plt.scatter(END[1], rows - 1 - END[0], color="red", s=100, label="End")
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")
plt.show()

