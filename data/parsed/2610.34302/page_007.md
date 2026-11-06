Input: metric (P,d), radius r\>0<br>
Output: a collection N of pairs (C,p), where the sets C partition P and \(C\subseteq B(p,r)\)<br>
\(\mathcal{N}\leftarrow\emptyset\), \(U\leftarrow P\)<br>
while \(U\neq\emptyset\) do<br>
   Choose an arbitrary point \(p\in U\)<br>
   \(C\leftarrow U\cap B(p,r)\), \(U\leftarrow U\backslash C\)<br>
   Add (C,p) to N<br>
return N

### Greedy ball cover.

For the logarithmic approximation, we instead run the standard greedy Set Cover algorithm where the universe is P and the available sets are all radius-r balls centered at points of P. Importantly, the center chosen at a step is allowed to be a point that has already been covered.

Input: metric (P,d), radius r\>0<br>
Output: a collection G of pairs (C,p), where the sets C partition P and \(C\subseteq B(p,r)\)<br>
\(\mathcal{G}\leftarrow\emptyset\), \(U\leftarrow P\)<br>
while \(U\neq\emptyset\) do<br>
   Choose \(p\in P\) maximizing \(|U\cap B(p,r)|\)<br>
   \(C\leftarrow U\cap B(p,r)\), \(U\leftarrow U\backslash C\)<br>
   Add (C,p) to G<br>
return G

The sets C returned by Algorithm 2.2 form a partition of P, and each such set is contained in the radius-r ball around its chosen center. Unlike Algorithm 2.1, the center p need not belong to the currently uncovered set U and need not belong to the cluster C.

### The constant-approximation construction.

At every level i, we compute a separated ball cover with radius \(r_i/(\alpha+2)\). For each source s, we add edges to the centers that lie in the annulus A<sub>i</sub>(s).

### The logarithmic-approximation construction.

The logarithmic construction is identical except that the level covers are produced by the greedy Set Cover routine.

## 2.2 Running Time.

Both ball-cover routines can be implemented in \(\tilde{O}(n^2)\) time for a fixed radius. First compute all radius-r balls. During the covering process, maintain the number of uncovered points in each ball. Whenever a cluster C is removed from the uncovered set, update the counters of all balls containing each point of C; this costs \(\tilde{O}(n|C|)\) time for the iteration and \(\tilde{O}(n^2)\) time over all iterations. A priority queue with lazy updates gives the required maximum-coverage choice in Algorithm 2.2.

There are \(L+1=O(\alpha log\Delta)\) levels. For either graph construction, computing all covers therefore takes \(\tilde{O}(\alpha n^2log\Delta)\) time. Once the covers are computed, all edge sets can be constructed by checking, for every level i, every source s, and every selected center p, whether \(p\in A_i(s)\). This<tbc>

**Algorithm 2.1:** SeparatedBallCover(P,d,r)

**Algorithm 2.2:** GreedyBallCover(P,d,r)

