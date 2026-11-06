at most (6_k)<sup>t</sup>_ signed entries of the original matrix _U_, and each right input value as such a sum of entries of _V_ . There are _a+b_ input values per leaf. Computing these sums directly from the original inputs uses at most

\(T^t(a+b)(6k)^t\le D^{3k}(a+b)\le D^{3k}(N+M)\)

additions and subtractions, since \(6kT\le 2^{3k}\) for \(k\ge 81\) and _D_=2_<sup>t</sup>_.

**Requested computations.** A request specifies one entry of the output matrix of one subproblem. Starting with the _w_ specified entries of _UV_ , we pass requests down the recursion tree. Each request generates one request in a private child and six requests in shared children, all at the same local position. Requests for the same entry of the same child are merged. Let _Q<sub>j</sub>_ be the total number of distinct requests at depth _j_, counting requests in different subproblems separately. We will show that \(Q_j\le B_j\).

Group the subproblems at depth _j_ by their pattern of shared and private steps from the root. A pattern specifies the type of child at each step, but not which child is chosen. Fix a pattern with _s_ shared steps and _j-s_ private steps. We bound its requests in two ways:

• _Requests generated._ Each original request has one continuation at a private step and at most six at a shared step. It therefore generates at most 6_<sup>s</sup>_ requests with this pattern, or at most 6_<sup>s</sup>w_ over all original requests.<tbc>

• _Available positions._ The full recursion tree has _RS_ choices of private child and 6_<sup>k</sup>_ choices of shared child at each step. Thus (_RS_)<sup>_j-s_</sup>(6_<sup>k</sup>)<sup>s</sup>_ subproblems have this pattern. Each has an output matrix of size \((N/R^j)\times(M/S^j)\), so their total number of output positions is<tbc>

<tbc>\((RS)^{j-s}(6^k)^s\frac{NM}{(RS)^j}=6^s\frac{NM}{k^s},\)<tbc>

<tbc>using _RS=k_6<sup>_k_-1</sup>. Merging repeated requests caps the number of distinct requests by this number of positions.<tbc>

<tbc>Taking the smaller bound for each pattern, and noting that there are \(\genfrac(){pt}{2}{j}{s}\) patterns with _s_ shared steps, gives

\(Q_j\le\sum_{s=0}^j\genfrac(){pt}{2}{j}{s}min\left\{6^sw,6^s\frac{NM}{k^s}\right\}=B_j.\)

At depth _t_, the middle dimension is one, so each requested entry is computed by multiplying two prepared input values. This uses \(Q_t\le B_t\) scalar multiplications. We then work back up the tree: each requested parent entry is the sum of its six shared answers minus its private answer, using six additions or subtractions. Request generation and reconstruction therefore each cost \(O(\sum_{j=0}^{t-1}Q_j)\). Finally, \(B_j\le B_t\) for \(j\le t\), since each coefficient \(\genfrac(){pt}{2}{j}{s}\) in equation (6) is nondecreasing in _j_. These two costs are thus _O(tB<sub>t</sub>_).

_Proof of Theorem 2.1._ If _d_=1, then _t_=0 and the sum in equation (2) is _w_, so compute the entries directly. Otherwise, set _D_=2_<sup>t</sup>\<_2_d_. Pad the outer dimensions to the least multiples _N,M_ of _R<sup>t</sup>,S<sup>t</sup>_ that are at least _n,m_, respectively, and pad the middle dimension to _D_. Since \(R,S\le 2^{3k}\) and \(D<2d\le d^2\),

\(max\{R^t,S^t\}\le D^{3k}\le d^{6k}\le min\{n,m\}.\)

