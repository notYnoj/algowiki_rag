<tbc>Once we solve this for each (_r,b_), an optimal allocation vector \(\Delta^t\) is recovered by backtracking. \(\Delta_I^t=\Delta_I^*(B_t)\), leaving a residual budget \(B_t-\Delta_I^t\) for items 1_,...,I_-1. Then \(\Delta_{I-1}^t=\Delta_{I-1}^*(B_t-\Delta_I^t)\) and so on down to item 1:

\(\Delta_r^t=\Delta_r^*\big(B_t-\sum_{j=r+1}^I\Delta_j^t\big),r=I,I-1,\dots,1.\)

By construction, backtracking recovers an allocation whose components sum to _B<sub>t</sub>_ and whose objective value is _V<sub>I</sub>(B<sub>t</sub>_). It is therefore a global optimizer of (8). The total runtime is the cost of precomputing the _I(B<sub>t</sub>_+1) values \(\ell_{i,t}(d)\) which is \(O(IB_tC_\ell)\) and the cost of filling in the _O(IB<sub>t</sub>_) DP states (each requiring a minimization over at most _B<sub>t</sub>_+1 values of \(\delta\)) which is \(O(IB_t^2)\). \(\square\)

_Proof of Proposition 2(i)_ For any allocation \(\Delta\), the improvement relative to assigning no samples in the current round is<tbc>

\(\sum_{j=1}^I\ell_{j,t}(0)-\sum_{j=1}^I\ell_{j,t}(\Delta_j)=\sum_{j=1}^I\sum_{h=0}^{\Delta_j-1}\big[\ell_{j,t}(h)-\ell_{j,t}(h+1)\big]=\sum_{j=1}^I\sum_{h=0}^{\Delta_j-1}D_{j,t}(h),\)

<tbc>where the inner sum is zero when \(\Delta_j=0\). Minimizing \(\sum_j\ell_{j,t}(\Delta_j)\) is therefore equivalent to maximizing

\(G(\Delta):=\sum_{j=1}^I\sum_{h=0}^{\Delta_j-1}D_{j,t}(h)\)

subject to \(\sum_j\Delta_j=B_t\). Let \(\Delta^G\) denote the greedy allocation and \(\Delta\) any other feasible allocation. We will show \(G(\Delta^G)\ge G(\Delta)\). If \(\Delta=\Delta^G\), there is nothing to prove. Otherwise, since both allocations sum to _B<sub>t</sub>_, there exist indices _i_, _j_ with \(\Delta_i>\Delta_i^G\) and \(\Delta_j<\Delta_j^G\). We show that one can transfer a sample from _i_ to _j_ without decreasing _G_.

Because \(\Delta_i>\Delta_i^G\), the term \(D_{i,t}(\Delta_i-1)\) appears in \(G(\Delta)\). Since \(\Delta_i-1\ge\Delta_i^G\), (9) gives<tbc>

\(D_{i,t}(\Delta_i-1)\le D_{i,t}(\Delta_i^G).\)

<tbc>Because \(\Delta_j<\Delta_j^G\), the term \(D_{j,t}(\Delta_j)\) does not appear in \(G(\Delta)\). Since \(\Delta_j\le\Delta_j^G-1\), (9) gives<tbc>

\(D_{j,t}(\Delta_j)\ge D_{j,t}(\Delta_j^G-1).\)

<tbc>Consider the greedy step at which the \((\Delta_j^G)\)th sample was assigned to item _j_. Before that step, _j_ had received \(\Delta_j^G-1\) samples and _i_ had received at most \(\Delta_i^G\) samples. The marginal gain of allocating to _j_ at that step was \(D_{j,t}(\Delta_j^G-1)\) and the marginal gain of _i_ was at least \(D_{i,t}(\Delta_i^G)\) by (9). Since greedy chose _j_,<tbc>

\(D_{j,t}(\Delta_j^G-1)\ge D_{i,t}(\Delta_i^G).\)

<tbc>Combining the three inequalities,

\(D_{j,t}(\Delta_j)\ge D_{j,t}(\Delta_j^G-1)\ge D_{i,t}(\Delta_i^G)\ge D_{i,t}(\Delta_i-1).\)

