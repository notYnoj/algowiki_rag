`A = embedding\_matrix(G, aut)`

`export\_matrix(`

`A,`

`filename=f"matrix\_{n}.csv"`

`)`

`save\_matrix\_pdf(`

`A,`

`labels,`

`filename=f"matrix\_{n}.pdf"`

`)`

`minor\_results = check\_Kn\_minus\_1\_minors(G)`

### C.6 Computational output

When n=5, the first computation reports that there are 21 connected graphs on five vertices and writes the matrix to the file `matrix\_5.pdf`. The second computation outputs the bitstrings listed in  3.

We can verify the tree decomposition and the conditions for each of the 5-vertex graphs using the code below

## D  to verify tree decompositions and automorphism-avoidance conditions

`from itertools import combinations`

`def vertices\_covered\_by\_q\_edges(H, q):`

`"""`

`Return True if there exist q edges in H`

`whose endpoints cover all vertices of H.`

`"""`

`V = set(H.vertices())`

`E = list(H.edges(labels=False))`

`if not V:`

`return True # empty graph`

`if len(V) \> 2\*q:`

`return False # impossible even in best case`

`for edgeset in combinations(E, q):`

`covered = set()`

`for u, v in edgeset:`

`covered.add(u)`

`covered.add(v)`

`if covered == V:`

`return True`

