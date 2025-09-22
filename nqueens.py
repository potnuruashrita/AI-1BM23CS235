import random

# Count the number of conflicts (pairs of queens attacking each other)
def count_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Generate a random initial board configuration
def generate_initial_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# Hill Climbing algorithm
def hill_climbing(n):
    board = generate_initial_board(n)
    current_conflicts = count_conflicts(board)

    while True:
        neighbors = []
        n = len(board)
        # Generate all neighbors by moving each queen in its column to every other row
        for col in range(n):
            for row in range(n):
                if row != board[col]:
                    neighbor = board[:]
                    neighbor[col] = row
                    neighbors.append(neighbor)

        # Find neighbor with the least conflicts
        best_neighbor = None
        best_conflicts = current_conflicts
        for neighbor in neighbors:
            conflicts = count_conflicts(neighbor)
            if conflicts < best_conflicts:
                best_conflicts = conflicts
                best_neighbor = neighbor

        # If no better neighbor found, either solution or local minimum reached
        if best_conflicts == current_conflicts:
            if current_conflicts == 0:
                return board  # Solution found
            else:
                return None  # Stuck in local minimum

        board = best_neighbor
        current_conflicts = best_conflicts

# Random Restart Hill Climbing
def random_restart_hill_climbing(n, max_restarts=1000):
    for restart in range(max_restarts):
        solution = hill_climbing(n)
        if solution is not None:
            print(f"Solution found after {restart + 1} restart(s).")
            return solution
    print(f"No solution found after {max_restarts} restarts.")
    return None

# Print the board nicely
def print_board(board):
    n = len(board)
    for row in range(n):
        line = ['Q' if board[col] == row else '.' for col in range(n)]
        print(" ".join(line))

# Example usage
if __name__ == "__main__":
    n = 8  # Change this for different board sizes
    solution = random_restart_hill_climbing(n)
    if solution:
        print_board(solution)
    else:
        print("Failed to find a solution.")
