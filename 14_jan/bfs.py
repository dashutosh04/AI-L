from collections import deque

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

print("\n--- BFS ---")
bfs_path, bfs_nodes = bfs(MAZE, START, END)
print("BFS Path:", bfs_path)
print("BFS Nodes Explored:", bfs_nodes)


