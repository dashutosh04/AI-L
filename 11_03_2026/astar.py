import heapq

goal_state = ((1,2,3),(4,5,6),(7,8,0))

goal_positions = {}
for i in range(3):
    for j in range(3):
        goal_positions[goal_state[i][j]] = (i,j)

def h1(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

def h2(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                gi, gj = goal_positions[val]
                dist += abs(i - gi) + abs(j - gj)
    return dist

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def a_star(start, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start))
    visited = set()
    g_cost = {start: 0}
    parent = {start: None}
    nodes_explored = 0

    while pq:
        f, g, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal_state:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, nodes_explored, len(path) - 1

        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_val = new_g + heuristic(neighbor)
                heapq.heappush(pq, (f_val, new_g, neighbor))
                parent[neighbor] = current

    return None, nodes_explored, 0

start_state = ((1,2,3),(4,0,6),(7,5,8))

path1, nodes1, depth1 = a_star(start_state, h1)
path2, nodes2, depth2 = a_star(start_state, h2)

print("H1 Misplaced Tiles")
print("Nodes Explored:", nodes1)
print("Solution Depth:", depth1)

print("H2 Manhattan Distance")
print("Nodes Explored:", nodes2)
print("Solution Depth:", depth2)