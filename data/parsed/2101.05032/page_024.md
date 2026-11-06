_u_<sub>_i_2</sub> if either _u_<sub>_i_1</sub>_\<u_<sub>_i_2</sub> or _u_<sub>_i_1</sub>=_u_<sub>_i_2</sub> and _u_<sub>_i_1</sub> is an open right endpoint and _u_<sub>_i_2</sub> is a closed right endpoint.

Let _I_<sub>_j_1</sub> be the interval with the _i_-th smallest left endpoint (i.e., the _i_-th left endpoint in the order \(\unknown_L\)), and let _I_<sub>_j_2</sub> be the interval with the _i_-th smallest right endpoint (i.e, the _i_-th right endpoint in the order \(\unknown_U\)). Then it is clear that _v_<sup>∗</sup> must lie in the interval _I_<sub>ta</sub>, which we call the **target area** and define as follows:

If \(\ell_{j_1}\) is an open left endpoint of _I_<sub>_j_1</sub> and _u_<sub>_j_2</sub> is an open right endpoint of _I_<sub>_j_2</sub>, then \(I_\mathrm{ta}=(\ell_{j_1},u_{j_2})\).

If \(\ell_{j_1}\) is an open left endpoint of _I_<sub>_j_1</sub> and _u_<sub>_j_2</sub> is a closed right endpoint of _I_<sub>_j_2</sub>, then \(I_\mathrm{ta}=(\ell_{j_1},u_{j_2}]\).

If \(\ell_{j_1}\) is a closed left endpoint of _I_<sub>_j_1</sub> and _u_<sub>_j_2</sub> is an open right endpoint of _I_<sub>_j_2</sub>, then \(I_\mathrm{ta}=[\ell_{j_1},u_{j_2})\).

If \(\ell_{j_1}\) is a closed left endpoint of _I_<sub>_j_1</sub> and _u_<sub>_j_2</sub> is a closed right endpoint of _I_<sub>_j_2</sub>, then \(I_\mathrm{ta}=[\ell_{j_1},u_{j_2}]\).

The following lemma was essentially shown by Kahan [22]; for the sake of completeness, we give a proof for arbitrary intervals.

\(\blacktriangleright\) **Lemma B.1** (Kahan, 1991; version of Lemma 5.3 for arbitrary intervals)**.** _Assume that the current instance of_ Selection _is not yet solved. Then there is at least one non-trivial interval I<sub>j</sub> in_ I _that contains the target area I_<sub>ta</sub>.

**Proof.** First, assume that the target area is trivial, i.e., _I_<sub>ta</sub>={_v_<sup>∗</sup>}. If there is no non-trivial interval in I that contains _v_<sup>∗</sup>, then the instance is already solved, a contradiction.

Now, assume that the target area _I_<sub>ta</sub> is non-trivial. Assume that no interval in I contains the target area. Then all intervals _I<sub>j</sub>_ whose left endpoint is not after \(\ell_{j_1}\) in the order of left endpoints must have a right endpoint that strictly precedes _u_<sub>_j_<sub>2</sub></sub>. There are at least _i_ such intervals (because \(\ell_{j_1}\) is the _i_-th smallest left endpoint), and hence the _i_-th smallest right endpoint must strictly precede _u_<sub>_j_<sub>2</sub></sub> in the order of right endpoints, a contradiction to the definition of _u_<sub>_j_<sub>2</sub></sub>. \(\blacktriangleleft\)

The intervals that intersect the target area can be classified into four categories:

**(1)** _a_ non-trivial intervals that **contain** the target area;

**(2)** _b_ intervals that **are strictly contained** in the target area such that the target area contains at least one point to the left of the interval and at least one point to the right of the interval.

**(3)** _c_ intervals that contain some part of _I_<sub>ta</sub> at the left end and do not contain some part of _I_<sub>ta</sub> on the right end. Formally, an interval _I<sub>i</sub>_ with closed right endpoint _u<sub>i</sub>_ is in this category if \(u_i\in I_\mathrm{ta}\), \(I_i\cap I_\mathrm{ta}=\{v\in I_\mathrm{ta}|v\le u_i\}\) and \(\{v\in I_\mathrm{ta}|v>u_i\}\neq\emptyset\). Moreover, an interval _I<sub>i</sub>_ with open right endpoint _u<sub>i</sub>_ is in this category if \(u_i\in I_\mathrm{ta}\) and \(I_i\cap I_\mathrm{ta}=\{v\in I_\mathrm{ta}|v<u_i\}\neq\emptyset\).

**(4)** _d_ intervals that contain some part of _I_<sub>ta</sub> at the right end and do not contain some part of _I_<sub>ta</sub> on the left end. Formally, an interval _I<sub>i</sub>_ with closed left endpoint \(\ell_i\) is in this category if \(\ell_i\in I_\mathrm{ta}\), \(I_i\cap I_\mathrm{ta}=\{v\in I_\mathrm{ta}|v\ge\ell_i\}\) and \(\{v\in I_\mathrm{ta}|v<\ell_i\}\neq\emptyset\). Moreover, an interval _I<sub>i</sub>_ with open left endpoint \(\ell_i\) is in this category if \(\ell_i\in I_\mathrm{ta}\) and \(I_i\cap I_\mathrm{ta}=\{v\in I_\mathrm{ta}|v>\ell_i\}\neq\emptyset\).

We propose the following algorithm for rounds with _k_ queries. Each round is filled with as many intervals as possible, using the following order: First all intervals of category (1); then intervals of category (2); then picking intervals alternatingly from categories (3) and (4), starting with category (3). If one of the two categories is exhausted, the rest of the _k_

