In all cases, the comparison cost charged to the run at any level _i_ along the left boundary path is bounded by _n<sub>i</sub>-n_<sub>_i_+1</sub>. Summing these costs from the top of the lower-level regime (level _t_) down to the termination level _k_ yields a telescoping sum. Because \(n_{k+1}\ge 1\) for any node in the tree, and \(n_t\le\lceil n/2^t\rceil\) according to Fact 2, the total left boundary cost is bounded by:

\(\sum_{i=t}^k(n_i-n_{i+1})=n_t-n_{k+1}\le n_t-1\le\lceil n/2^t\rceil-1\le n/2^t\)

## Right Boundary Analysis:

By symmetry, the right boundary yields an identical bound. Because the run forms a prefix of any Case 2 node \(v'_i\) (with left child _L_ and right child _R_) on the right boundary, the algorithm mirrors the left boundary logic. When the boundary falls in the left child, applying the worst-case charge of 1 comparison per element gives \(s'_i\le n'_i-n'_{i+1}\) comparisons. If it falls into the right child, the left child is pure giving _a_=`true` whilst the right child is impure as it contains a boundary between runs which are maximal, giving _b_=`false`. The directional merge- sort then utilizes mergeFw to efficiently exhaust the pure left child first, ensuring the comparison cost charged at level _i_ is bounded by \(n'_i-n'_{i+1}\). At the right termination level \(k'\), the boundary perfectly aligns with the partition between the children _L_ and _R_, meaning _L_ is pure and _R_ contains no run elements. Charging 1 comparison to every element in _L_, the cost at this terminal level is \(|L|=n'_{k^\prime}-|R|=n'_{k^\prime}-n'_{k^\prime+1}\) (defining \(n'_{k^\prime+1}=|R|\) to terminate the telescoping sum). Summing this telescoping sum across the lower levels yields the exact same overall bound of _n/_2_<sup>t</sup>_ for the right boundary. Thus, the total cost charged at the lower levels are:

\(n/2^t+n/2^t=2(n/2^t)\)

If on one (or both) ends no boundary nodes exist, then the cost is trivially \(0\le n/2^t\), hence the upper bound of 2(_n/_2_<sup>t</sup>_) remains valid.

**Lemma 7.** _For a non-decreasing run of length r, the total number of merge comparisons charged to its elements across all levels of the merging tree is bounded by r_lg(_n/r_)+2_r._

_Proof._ By partitioning the tree at threshold depth \(t=\lceil lg(n/r)\rceil\), we sum the upper-level costs (Lemma 5) and lower-level costs (Lemma 6). The total comparison charge is bounded by:<tbc>

\(r\lceil lg(n/r)\rceil+2(n/2^t)\)

<tbc>To simplify this, let \(\gamma=\lceil lg(n/r)\rceil-lg(n/r)\) represent the fractional ceiling overhead, where \(0\le\gamma<1\). We can rewrite the sum in terms of \(\gamma\):<tbc>

\(r(lg(n/r)+\gamma)+2\left(n/2^{lg(n/r)+\gamma}\right)=rlg(n/r)+r(\gamma+2^{1-\gamma})\text{(1)}\)

<tbc>As \(2^{-\gamma}\) is convex, we can apply the secant line bound to \(2^{-\gamma}\) for \(\gamma\in[0,1]\):

\(2^{-\gamma}\le 1-(1/2)\gamma\)<br>
\(2(2^{-\gamma})\le 2-\gamma\)<br>
\(2^{1-\gamma}+\gamma\le 2\)

Substituting this upper limit into (1) yields the final bound:

\(rlg(n/r)+2r\)

