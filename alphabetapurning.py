import math

# Alpha-Beta Pruning Algorithm
def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta, max_depth):
    
    # Base condition: leaf node
    if depth == max_depth:
        print(f"Leaf node reached with value = {values[node_index]}")
        return values[node_index]

    if maximizing_player:
        print(f"\nMAX Node at depth {depth}, node {node_index}, α={alpha}, β={beta}")
        best = -math.inf

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                False,
                values,
                alpha,
                beta,
                max_depth,
            )
            best = max(best, val)
            alpha = max(alpha, best)

            print(f"MAX updated: best = {best}, α = {alpha}")

            # Prune
            if beta <= alpha:
                print("PRUNING at MAX node ❌")
                break

        return best

    else:
        print(f"\nMIN Node at depth {depth}, node {node_index}, α={alpha}, β={beta}")
        best = math.inf

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                True,
                values,
                alpha,
                beta,
                max_depth,
            )
            best = min(best, val)
            beta = min(beta, best)

            print(f"MIN updated: best = {best}, β = {beta}")

            # Prune
            if beta <= alpha:
                print("PRUNING at MIN node ❌")
                break

        return best


# ---------------- TEST CASE ---------------- #

# Leaf node values for the game tree
values = [3, 5, 6, 9, 1, 2, 0, -1]  # 8 leaf nodes

max_depth = 3   # Depth of tree
alpha = -math.inf
beta = math.inf

print("\n✅ Starting Alpha Beta Pruning...\n")
optimal_value = alpha_beta(0, 0, True, values, alpha, beta, max_depth)

print("\n✅ Optimal Value from Root =", optimal_value)
