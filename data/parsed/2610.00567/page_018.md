<tbc>`P\_edges = {`<br>
`(min(u, v), max(u, v))`<br>
`for u, v, \_ in P.edges()`<br>
`}`<br>
`count = 0`<br>
`for S in permutations(H\_vertices, k):`<br>
`mapping = dict(zip(P\_vertices, S))`<br>
`if all(`<br>
`H.has\_edge(mapping[u], mapping[v])`<br>
`for u, v in P\_edges`<br>
`):`<br>
`count += 1`<br>
`return count`<br>
`def embedding\_matrix(G, aut):`<br>
`m = len(G)`<br>
`A = [[O] \* m for \_ in range(m)]`<br>
`for i in range(m):`<br>
`for j in range(m):`<br>
`A[i][j] = (`<br>
`embedding\_count(G[i], G[j])`<br>
`// aut[i]`<br>
`)`<br>
`return A`

## C.3 _K_<sub>_n_-1</sub>-minor testing

For an _n_-vertex graph _G_, the following function tests whether _G_ or its complement contains a _K_<sub>_n_-1</sub> minor.

def has\_Kn\_minus\_1\_minor(G):<br>
`n = G.order()`<br>
`K = graphs.CompleteGraph(n - 1)`<br>
`try:`<br>
`has\_G\_minor = bool(G.minor(K))`<br>
`except ValueError:`<br>
`has\_G\_minor = False`<br>
`try:`<br>
`has\_complement\_minor = bool(`<br>
`G.complement().minor(K)`<br>
`)`<br>
`except ValueError:`<br>
`has\_complement\_minor = False`<br>
`return has\_G\_minor, has\_complement\_minor`<br>
`def check\_Kn\_minus\_1\_minors(G):`<br>
`return [`<br>
`has\_Kn\_minus\_1\_minor(H)`<br>
`for H in G`<br>
`]`

Listing 1.3: Testing for a _K_<sub>_n_-1</sub> minor in a graph and its complement.

