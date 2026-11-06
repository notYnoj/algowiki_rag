5. If \(\delta=0\) and 0_\<|I|\<n/_2, return _I_.<tbc>

6. In the remaining case, \(\delta=0\) and |_I_|=_n/_2. Let _J=V_\\_I_, construct the bipartite graph _H_, and compute any perfect matching _M_.<tbc>

7. Construct _D<sub>M</sub>_ and compute its strongly connected components.<tbc>

8. If _D<sub>M</sub>_ is strongly connected, return `NO`. Otherwise, choose any SCC _C_ whose vertex in the condensation digraph has outdegree zero, and return \(T_C=\{x_i:i\in C\}\).

## 5.3. Correctness

**Theorem 5.** _Algorithm 1 correctly decides whether a connected simple graph contains a small blocking set and constructs one whenever it exists._

_Proof._ When \(n\le 1\), no nonempty set can satisfy the required cardinality bound, so step 1 is correct. Suppose henceforth that \(n\ge 2\).

If \(\delta>0\), Corollary 1 guarantees that step 3 outputs a small blocking set.

If \(\delta=0\) and \(I=\varnothing\), Theorem 1 guarantees that no nonempty blocking set exists, so step 4 is correct.

If \(\delta=0\) and 0_\<|I|\<n/_2, Theorem 1 guarantees that _I_ itself is a small blocking set, so step 5 is correct.

The only remaining case is \(\delta=0\) and |_I_|=_n/_2. By Theorem 2, the perfect matching required in step 6 exists. By Theorems 3 and 4, the graph contains a small blocking set if and only if _D<sub>M</sub>_ is not strongly connected; in that case, the set corresponding to the chosen sink SCC is a valid small blocking set. Thus, every branch is correct.

## 5.4. Running time

We compute a maximum-cardinality critical independent set using Larson’s MCIS algorithm [11], with the matching-reuse implementation described by Strash [14]. For connected graphs, this step takes _O(m_<sup>2</sup>) time.

When \(\delta>0\), we use the iterative deletion procedure in Lemma 1, removing a vertex from the current independent set and updating its neighborhood at each iteration. With adjacency lists and counts of neighbors in the current independent set, each vertex is deleted at most once and each edge is processed only a constant number of times. This procedure therefore takes _O(n+m_) time.

In the boundary case, the Hopcroft-Karp algorithm [15] computes a perfect matching of _H_ in \(O(m\sqrt{n})\) time. Constructing _D<sub>M</sub>_, computing its SCCs<tbc>

