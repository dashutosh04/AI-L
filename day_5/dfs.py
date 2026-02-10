MAZE = [
    [1,1,1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1]
]
START = (0, 0)
END = (4, 6)

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
