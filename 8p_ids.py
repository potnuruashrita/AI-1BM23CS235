goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def get_neighbors(state):
    zero = state.index(0)
    x, y = divmod(zero, 3)
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_zero = nx * 3 + ny
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors

def depth_limited_dfs(start, limit):
    stack = [(start, 0, [start])]  # (state, depth, path)
    visited = set()
    while stack:
        state, depth, path = stack.pop()
        if state == goal_state:
            return path
        if depth < limit:
            visited.add(state)
            for neighbor in get_neighbors(state):
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1, path + [neighbor]))
            # Note: We do not remove from visited here to avoid revisiting nodes at same or shallower depths
    return None

def iterative_deepening(start, max_depth=50):
    for depth in range(max_depth):
        result = depth_limited_dfs(start, depth)
        if result:
            return result
    return None

# Example start state
start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

solution = iterative_deepening(start_state, max_depth=20)

if solution:
    print(f"Solution found in {len(solution) - 1} moves:")
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found within depth limit.")
