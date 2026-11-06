subproblem of allocating exactly _b_ samples among the first _r_ items by forward induction, and then recover the optimal allocation by backtracking. Let _V<sub>r</sub>(b_) denote the minimum loss for this subproblem so that _V<sub>I</sub>(B<sub>t</sub>_) is the optimal value of (8).

**Algorithm 1** Dynamic Programming Batch Builder (DPBB)

1: **Precompute cost values:** for each _i_=1_,...,I_ and _d_=0_,...,B<sub>t</sub>_, compute \(\ell_{i,t}(d)\)

2: **Initialize:** set _V_<sub>0</sub>(0)=0 and \(V_0(b)=+\infty\) for \(b=1,\dots,B_t\)

3: **Solve subproblems:**

4: **for** _r_=1_,...,I_

5: **for** _b_=0_,...,B<sub>t</sub>_

6: Compute \(V_r(b)=min_{\Delta\in\{0,\dots,b\}}\{V_{r-1}(b-\Delta)+\ell_{r,t}(\Delta)\}\) and record an argmin \(\Delta_r^*(b)\)

7: **Recover the allocation:** set \(b\leftarrow B_t\)

8: **for** _r=I,...,_1

9: Set \(\Delta_r^t=\Delta_r^*(b)\) and update \(b\leftarrow b-\Delta_r^t\)

10: **Return** \(\Delta^t=(\Delta_1^t,\dots,\Delta_I^t)\)

PROPOSITION 1 **(Optimality of DPBB)**. _DPBB returns a global optimizer of_ (8). _Let_ \(C_\ell\) _denote the cost of computing each value_ \(\ell_{i,t}(d)\)_. The total computational cost is_ \(O(IB_tC_\ell+IB_t^2)\).

For the greedy procedure, define the marginal decrease from allocating one more sample to item _i_ by \(D_{i,t}(\Delta_i):=\ell_{i,t}(\Delta_i)-\ell_{i,t}(\Delta_i+1)\). The procedure in Algorithm 2 sequentially assigns the _B<sub>t</sub>_ samples to the item with the current largest marginal decrease.

**Algorithm 2** Greedy Batch Builder (GBB)

1: **Initialize:** \(\Delta^t=\mathbf{0}\)

2: **for** _n_=1_,...,B<sub>t</sub>_

3: For each _i_=1_,...,I_, compute \(D_{i,t}(\Delta_i^t)=\ell_{i,t}(\Delta_i^t)-\ell_{i,t}(\Delta_i^t+1)\)

4: Choose \(i^*\in argmax_{1\le i\le I}D_{i,t}(\Delta_i^t)\)

5: \(\Delta_{t^*}^t\leftarrow\Delta_{t^*}^t+1\)

6: **Return** \(\Delta^t=(\Delta_1^t,\dots,\Delta_I^t)\)

PROPOSITION 2 **(Conditions for greedy optimality).**

(i) _If, for every item i,_

\(D_{i,t}(0)\ge D_{i,t}(1)\ge\cdots\ge D_{i,t}(B_t-1),\) (9)

_then GBB returns a global optimizer of_ (8)_. Its computational cost is_ \(O(IB_tC_\ell)\).

k=3 k=5 k=10 0.35 TEAk EOC-m 0.30 0.30 0.25 0.25 0.25 0.20 0.20 0.20 proportion of budget 0.15 0.15 0.15 0.10 0.10 0.10 0.05 0.05 0.05 0.00 0.00 0.00 5
10 15 20 5
10 15 20 5
10 15 20 rank (1 = best) rank (1 = best) rank (1 = best)

**Figure 2** Budget allocation across items on the Gaussian instance described in §5, with _I_=20 at _k_=3,5,10. The plots show the proportion of the total budget spent on each item, with items ordered by their true mean. TEAk uses _q_<sup>∗</sup>(_t_). The dashed line marks the top-_k_ boundary.

