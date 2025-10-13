def pl_resolution(kb, query):
    """
    Perform propositional logic resolution to check if KB entails query.

    kb: list of clauses (each clause is a set of literals)
    query: clause to check entailment for (single literal)
    """

    # Negate the query and add to clauses
    clauses = kb.copy()
    clauses.append(set([negate_literal(query)]))

    new = set()

    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if set() in resolvents:  # empty clause found => contradiction
                return True
            new = new.union(resolvents)

        if new.issubset(set(map(frozenset, clauses))):
            return False  # no new clauses, entailment not found

        for clause in new:
            if clause not in clauses:
                clauses.append(set(clause))


def negate_literal(literal):
    """Negate a literal, e.g. 'A' -> '-A', '-A' -> 'A'"""
    return literal[1:] if literal.startswith('-') else '-' + literal


def resolve(ci, cj):
    """
    Resolve two clauses ci and cj and return a set of resolvent clauses.

    Each clause is a set of literals (strings).
    """
    resolvents = set()
    for li in ci:
        for lj in cj:
            if li == negate_literal(lj):
                # Resolvent is union minus li and lj
                resolvent = (ci.union(cj)) - {li, lj}
                resolvents.add(frozenset(resolvent))
    return resolvents


# Example usage:

# Knowledge Base (CNF clauses):
# R -> W  is  (~R or W)
# S -> W  is  (~S or W)
# R      is  (R)

KB = [
    {'-R', 'W'},  # ~R or W
    {'-S', 'W'},  # ~S or W
    {'R'}         # R
]

query = 'W'  # Is the ground wet?

entailed = pl_resolution(KB, query)
print(f"Query '{query}' is entailed by the knowledge base: {entailed}")
