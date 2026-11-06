# Faster Algorithms for Induced Patterns

21

`return False`

`def bag\_is\_spannable(G, bag, p, q):`

`"""`

`Check if bag can be spanned by p vertices and q edges.`

`"""`

`H = G.subgraph(bag)`

`B = list(bag)`

`if len(B) \< p:`

`return False`

`for P in combinations(B, p):`

`R = [v for v in B if v not in P]`

`HR = H.subgraph(R)`

`if vertices\_covered\_by\_q\_edges(HR, q):`

`return True`

`return False`

`def verify\_decomposition(G, T, conditions, p, q):`

`p = int(p)`

`q = int(q)`

`# Parse bags`

`bags = T.split("-")`

`bag\_lists = [[int(v) for v in bag] for bag in bags]`

`# Parse conditions`

`conds = []`

`for c in conditions.split(","):`

`c = c.strip()`

`if not c:`

`continue`

`i, j = map(int, c.split("\<"))`

`if i \>= j:`

`return False, f"Invalid condition {i}\<{j}"`

`conds.append((i, j))`

`# Spanning condition`

`for idx, bag in enumerate(bag\_lists):`

`if not bag\_is\_spannable(G, bag, p, q):`

`return (`

`False,`

`f"Bag {idx+1} not spannable by p={p}, q={q}"`

`)`

