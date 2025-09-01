from collections import deque

# Goal state of the puzzle
goal_state = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))  # 0 represents the blank tile

# Directions in which the blank tile can move: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return state == goal_state

def swap_tiles(state, pos1, pos2):
    state_list = [list(row) for row in state]
    x1, y1 = pos1
    x2, y2 = pos2
    state_list[x1][y1], state_list[x2][y2] = state_list[x2][y2], state_list[x1][y1]
    return tuple(tuple(row) for row in state_list)

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = swap_tiles(state, (x, y), (nx, ny))
            neighbors.append(new_state)
    return neighbors

def dfs(initial_state):
    stack = [(initial_state, [])]  # (state, path)
    visited = set()
    visited.add(initial_state)

    while stack:
        state, path = stack.pop()
        
        if is_goal(state):
            return path + [state]
        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [state]))
    return None

# Example initial state
initial_state = ((1, 2, 3),
                 (4, 0, 6),
                 (7, 5, 8))

solution_path = dfs(initial_state)

if solution_path:
    print(f"Solution found in {len(solution_path) - 1} moves:")
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
