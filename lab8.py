from sympy import symbols
from sympy.logic.boolalg import Or, And, Not, Implies
from sympy.logic.inference import satisfiable

# --- Define propositional symbols ---
# P(x,y): Pit at (x,y)
P11, P12, P21, P22 = symbols('P11 P12 P21 P22')

# W(x,y): Wumpus at (x,y)
W11, W12, W21, W22 = symbols('W11 W12 W21 W22')

# B(x,y): Breeze percept
B11, B21 = symbols('B11 B21')

# S(x,y): Stench percept
S11, S21 = symbols('S11 S21')

# --- Knowledge Base (KB) ---
KB = And(
    # Percepts (observations)
    B11,                # Breeze at (1,1)
    Not(S11),           # No stench at (1,1)
    Not(B21),           # No breeze at (2,1)
    Not(S21),           # No stench at (2,1)

    # Breeze rules
    Implies(B11, Or(P12, P21)),        # Breeze(1,1) => Pit(1,2) or Pit(2,1)
    Implies(Not(B11), Not(Or(P12, P21))),
    Implies(B21, Or(P11, P22)),        # Breeze(2,1) => Pit(1,1) or Pit(2,2)
    Implies(Not(B21), Not(Or(P11, P22))),

    # Stench rules
    Implies(S11, Or(W12, W21)),        # Stench(1,1) => Wumpus(1,2) or (2,1)
    Implies(Not(S11), Not(Or(W12, W21))),
    Implies(S21, Or(W11, W22)),        # Stench(2,1) => Wumpus(1,1) or (2,2)
    Implies(Not(S21), Not(Or(W11, W22)))
)

# --- Query 1: Is there a Pit at (1,2)? ---
query1 = P12
is_query1_entail = not satisfiable(And(KB, Not(query1)))  # KB ⊨ query if KB ∧ ¬query is unsatisfiable

# --- Query 2: Is there a Wumpus at (2,2)? ---
query2 = W22
is_query2_entail = not satisfiable(And(KB, Not(query2)))

# --- Results ---
print("Query 1: Is there a Pit at (1,2)?", "✅ Yes, entailed" if is_query1_entail else "❌ No, not entailed")
print("Query 2: Is there a Wumpus at (2,2)?", "✅ Yes, entailed" if is_query2_entail else "❌ No, not entailed")
