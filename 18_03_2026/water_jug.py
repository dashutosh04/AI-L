import time
import math

def get_valid_moves(state, A, B):
    x, y = state
    moves = []
    
    if x < A: moves.append(((A, y), "Fill Jug A"))
    if y < B: moves.append(((x, B), "Fill Jug B"))
    if x > 0: moves.append(((0, y), "Empty Jug A"))
    if y > 0: moves.append(((x, 0), "Empty Jug B"))
    if x > 0 and y < B:
        pour = min(x, B - y)
        moves.append(((x - pour, y + pour), "Pour Jug A into Jug B"))
    if y > 0 and x < A:
        pour = min(y, A - x)
        moves.append(((x + pour, y - pour), "Pour Jug B into Jug A"))
        
    return moves

def evaluate_state(state, is_ai_turn, A, B, T):
    x, y = state
    
    if x == T or y == T:
        return -1000 if is_ai_turn else 1000
        
    dist = min(abs(x - T), abs(y - T))
    base_score = max(A, B) - dist
    
    if is_ai_turn:
        return base_score 
    else:
        return -base_score

def minimax(state, depth, alpha, beta, is_ai_turn, visited, use_pruning, A, B, T):
    x, y = state
    
    if x == T or y == T or depth == 0:
        return evaluate_state(state, is_ai_turn, A, B, T), None
        
    moves = get_valid_moves(state, A, B)
    valid_moves = [m for m in moves if m[0] not in visited]
    
    if not valid_moves:
        return 0, None
        
    best_move = None

    if is_ai_turn:
        max_eval = -math.inf
        for next_state, move_desc in valid_moves:
            new_visited = visited.copy()
            new_visited.add(next_state)
            
            eval_score, _ = minimax(next_state, depth - 1, alpha, beta, False, new_visited, use_pruning, A, B, T)
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (next_state, move_desc)
                
            if use_pruning:
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval, best_move
        
    else:
        min_eval = math.inf
        for next_state, move_desc in valid_moves:
            new_visited = visited.copy()
            new_visited.add(next_state)
            
            eval_score, _ = minimax(next_state, depth - 1, alpha, beta, True, new_visited, use_pruning, A, B, T)
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (next_state, move_desc)
                
            if use_pruning:
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval, best_move

def play(A, B, T, max_depth, use_pruning=True):
    print(f"--- Adversarial Water Jugs ---")
    print(f"Jug A: {A}L | Jug B: {B}L | Target: {T}L")
    
    current_state = (0, 0)
    global_visited = {current_state}
    is_ai_turn = False
    
    while True:
        print(f"\nCurrent State: Jug A = {current_state[0]}L, Jug B = {current_state[1]}L")
        
        if current_state[0] == T or current_state[1] == T:
            winner = "AI" if not is_ai_turn else "Human"
            print(f"\nGame Over! {winner} reached the target of {T}L and wins!")
            break
            
        valid_moves = get_valid_moves(current_state, A, B)
        available_moves = [m for m in valid_moves if m[0] not in global_visited]
        
        if not available_moves:
            print("\nNo valid moves left. It's a draw!")
            break

        if is_ai_turn:
            print("AI is thinking...")
            start_time = time.time()
            
            score, best_move = minimax(
                current_state, max_depth, -math.inf, math.inf, True, global_visited.copy(), use_pruning, A, B, T
            )
            
            exec_time = time.time() - start_time
            print(f"AI took {exec_time:.4f} seconds.")
            
            if best_move:
                current_state, move_desc = best_move
                print(f"AI plays: {move_desc} -> New State: {current_state}")
                global_visited.add(current_state)
            else:
                print("AI concedes.")
                break
        else:
            print("Your turn. Available moves:")
            for i, (state, desc) in enumerate(available_moves):
                print(f"  {i+1}: {desc} (Results in {state})")
                
            while True:
                try:
                    choice = int(input(f"Choose a move (1-{len(available_moves)}): ")) - 1
                    if 0 <= choice < len(available_moves):
                        current_state, move_desc = available_moves[choice]
                        print(f"You played: {move_desc}")
                        global_visited.add(current_state)
                        break
                    else:
                        print("Invalid choice. Try again.")
                except ValueError:
                    print("Please enter a number.")
        
        is_ai_turn = not is_ai_turn

if __name__ == "__main__":
    play(4, 3, 2, 7, use_pruning=True)