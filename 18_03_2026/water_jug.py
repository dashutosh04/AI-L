import time

A = 4
B = 3
T = 2

def get_moves(state):
    x, y = state
    moves = []
    moves.append((A, y))
    moves.append((x, B))
    moves.append((0, y))
    moves.append((x, 0))
    pour = min(x, B - y)
    moves.append((x - pour, y + pour))
    pour = min(y, A - x)
    moves.append((x + pour, y - pour))
    return list(set(moves))

def is_goal(state):
    return state[0] == T or state[1] == T

def evaluate(state, depth, maximizing):
    if is_goal(state):
        return 10 - depth if maximizing else depth - 10
    return 0

def minimax(state, depth, maximizing, visited):
    if state in visited:
        return 0
    if is_goal(state) or depth == 0:
        return evaluate(state, depth, maximizing)
    visited.add(state)
    if maximizing:
        max_eval = float('-inf')
        for move in get_moves(state):
            eval = minimax(move, depth - 1, False, visited.copy())
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_moves(state):
            eval = minimax(move, depth - 1, True, visited.copy())
            min_eval = min(min_eval, eval)
        return min_eval

def alpha_beta(state, depth, alpha, beta, maximizing, visited):
    if state in visited:
        return 0
    if is_goal(state) or depth == 0:
        return evaluate(state, depth, maximizing)
    visited.add(state)
    if maximizing:
        max_eval = float('-inf')
        for move in get_moves(state):
            eval = alpha_beta(move, depth - 1, alpha, beta, False, visited.copy())
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_moves(state):
            eval = alpha_beta(move, depth - 1, alpha, beta, True, visited.copy())
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(state, use_alpha_beta=True):
    best_val = float('-inf')
    best_state = None
    for move in get_moves(state):
        if use_alpha_beta:
            value = alpha_beta(move, 10, float('-inf'), float('inf'), False, set())
        else:
            value = minimax(move, 10, False, set())
        if value > best_val:
            best_val = value
            best_state = move
    return best_state

def play_game():
    state = (0, 0)
    while True:
        print("\nCurrent state:", state)
        moves = get_moves(state)
        for i, m in enumerate(moves):
            print(f"{i}: {m}")
        choice = int(input("Choose move: "))
        state = moves[choice]
        if is_goal(state):
            print("You win!")
            break
        print("AI is thinking...")
        state = best_move(state, use_alpha_beta=True)
        print("AI moves to:", state)
        if is_goal(state):
            print("AI wins!")
            break

def compare_performance():
    state = (0, 0)
    start = time.time()
    minimax(state, 10, True, set())
    print("Minimax Time:", time.time() - start)
    start = time.time()
    alpha_beta(state, 10, float('-inf'), float('inf'), True, set())
    print("Alpha-Beta Time:", time.time() - start)

if __name__ == "__main__":
    compare_performance()
    play_game()