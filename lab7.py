def negate_literal(literal):
    return literal[1:] if literal.startswith('-') else '-' + literal

def resolve(ci, cj):
    resolvents = set()
    for li in ci:
        for lj in cj:
            if li == negate_literal(lj):
                resolvent = (ci.union(cj)) - {li, lj}
                resolvents.add(frozenset(resolvent))
    return resolvents

def pl_resolution(kb, query):
    clauses = kb.copy()
    clauses.append(set([negate_literal(query)]))  # add negated query
    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if frozenset() in resolvents:
                return True  # empty clause found
            new = new.union(resolvents)
        if new.issubset(set(map(frozenset, clauses))):
            return False  # no new clauses
        for clause in new:
            if clause not in clauses:
                clauses.append(set(clause))

# Define KB clauses
KB = [
    {'-R', 'W'},  # ~R or W
    {'-S', 'W'},  # ~S or W
    {'R'}         # R
]

query = 'W'

entailed = pl_resolution(KB, query)
print(f"Query '{query}' is entailed by the knowledge base: {entailed}")
