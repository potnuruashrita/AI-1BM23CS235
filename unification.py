import re

def is_variable(x):
    return isinstance(x, str) and x[0].islower() and x.isalpha()

def is_compound(x):
    return isinstance(x, tuple)

def occurs_check(var, x, theta):
    """Check if variable `var` occurs in term `x` (to avoid infinite recursion)."""
    if var == x:
        return True
    elif is_variable(x) and x in theta:
        return occurs_check(var, theta[x], theta)
    elif is_compound(x):
        return any(occurs_check(var, arg, theta) for arg in x[1])
    return False

def unify(x, y, theta=None):
    """Unify two expressions and return substitution dictionary or None if fails."""
    if theta is None:
        theta = {}

    if theta is False:
        return False
    elif x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    elif is_compound(x) and is_compound(y) and x[0] == y[0] and len(x[1]) == len(y[1]):
        for arg_x, arg_y in zip(x[1], y[1]):
            theta = unify(arg_x, arg_y, theta)
            if theta is False:
                return False
        return theta
    else:
        return False

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif is_variable(x) and x in theta:
        return unify(var, theta[x], theta)
    elif occurs_check(var, x, theta):
        return False
    else:
        theta[var] = x
        return theta

# --- Helper to parse FOL terms into tuples (functor, [args]) ---
def parse_term(expr):
    expr = expr.replace(" ", "")
    if "(" not in expr:
        return expr  # variable or constant
    functor, args = expr.split("(", 1)
    args = args[:-1]  # remove ')'
    args_list = [parse_term(a) for a in split_args(args)]
    return (functor, args_list)

def split_args(s):
    parts, depth, current = [], 0, ""
    for ch in s:
        if ch == "," and depth == 0:
            parts.append(current)
            current = ""
        else:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            current += ch
    if current:
        parts.append(current)
    return parts

# --- Example Usage ---
if __name__ == "__main__":
    x = parse_term("P(x, f(y))")
    y = parse_term("P(f(z), f(a))")

    result = unify(x, y)
    if result:
        print("Unifier found:")
        for k, v in result.items():
            print(f"  {k} -> {v}")
    else:
        print("No unifier found.")
