from collections import deque

MAZE = [
    [1, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 1]
]

START = (0, 0)
TREASURE = (2, 3)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def print_pattern(maze, start, treasure, path=None):
    rows, cols = len(maze), len(maze[0])

    clean_path = []
    if path:
        clean_path = [p[0] for p in path]

    for i in range(rows):
        for j in range(cols):

            if (i, j) in clean_path:
                print("*", end=" ")

            elif (i, j) == start:
                print("S", end=" ")

            elif (i, j) == treasure:
                print("T", end=" ")

            elif maze[i][j] == 1:
                print("o", end=" ")

            else:
                print("x", end=" ")

        print()


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def search_treasure(maze, start, treasure):
    rows, cols = len(maze), len(maze[0])

    q = deque([start])
    visited = [start]
    parent = {start: None}

    while q:
        current = q.popleft()

        if current == treasure:
            path = []

            while current:
                path.append((current, f"H - {manhattan(current, treasure)}"))
                current = parent[current]

            return path[::-1]

        neigh = []

        for d in directions:
            ni = current[0] + d[0]
            nj = current[1] + d[1]

            nxt = (ni, nj)

            if (
                0 <= ni < rows
                and 0 <= nj < cols
                and maze[ni][nj] == 1
                and nxt not in visited
            ):
                visited.append(nxt)
                neigh.append(nxt)

        neigh.sort(key=lambda x: manhattan(x, treasure))

        for nxt in neigh:
            parent[nxt] = current
            q.append(nxt)

    return None


def main():
    print("====== ORIGINAL MAZE ======")
    print_pattern(MAZE, START, TREASURE)

    print("====== VISITED SET ======")
    print(search_treasure(MAZE, START, TREASURE))

    print("====== SOLVED MAZE ======")
    print_pattern(MAZE, START, TREASURE,
                  search_treasure(MAZE, START, TREASURE))


if __name__ == "__main__":
    main()