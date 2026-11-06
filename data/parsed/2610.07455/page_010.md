The same argument works over every finite domain. If the indicator of the core relation has degree _d_, each arriving constraint contributes a fixed polynomial whose terms involve at most _d_ variables. Across all scopes, there are only _O<sub>R</sub>(n<sup>d</sup>_) possible terms. The algorithm stores the coefficient of each term, and after the stream it tries all assignments and returns the largest value. This gives the _O<sub>R</sub>(n<sup>d</sup>_log_n_) upper bound and extends the Boolean argument of Kol, Paramonov, Saxena, and Yu to arbitrary finite domains.

## The lower bound.

We again reduce from one-way INDEX. We call the values of Alice’s instance at assignments chosen by Bob _point evaluations_. The following CUT example shows how degree lets Bob combine these point evaluations to recover his bit.

**Example 2.7** (Four point evaluations for CUT)**.** Alice receives bits _b<sub>ij</sub>_ indexed by \((i,j)\in[N]^2\). She creates vertices _x_<sub>1</sub>_,...,x<sub>N</sub>_ and _y_<sub>1</sub>_,...,y<sub>N</sub>_, and inserts the edge {_x<sub>i</sub>,y<sub>j</sub>_} whenever _b<sub>ij</sub>_=1. Let _P_ denote the resulting graph.

Bob receives a pair (_p,q_). He uses four assignments. The assignment _s_<sub>00</sub> sets every variable to 0. The assignment _s_<sub>10</sub> sets only _x<sub>p</sub>_ to 1, the assignment _s_<sub>01</sub> sets only _y<sub>q</sub>_ to 1, and the assignment _s_<sub>11</sub> sets only _x<sub>p</sub>_ and _y<sub>q</sub>_ to 1. In the ideal reduction, Bob makes four copies of Alice’s streaming state and appends a different input to each copy, one for each of these assignments. The four point evaluations satisfy

\(\text{val}_P(s_{11})-\text{val}_P(s_{10})-\text{val}_P(s_{01})+\text{val}_P(s_{00})=-2b_{pq}.\)

To see the cancellation, consider one edge of _P_. An edge not incident to _x<sub>p</sub>_ or _y<sub>q</sub>_ contributes zero to the signed sum. An edge incident to exactly one of them contributes equally to two terms with opposite signs. The only edge that can remain is {_x<sub>p</sub>,y<sub>q</sub>_}. If it is present, it is cut under _s_<sub>10</sub> and _s_<sub>01</sub> but not under _s_<sub>00</sub> or _s_<sub>11</sub>, giving a total contribution of -2.

Thus Bob can recover _b<sub>pq</sub>_ if the run from each copy reveals the value of _P_ at its chosen assignment. If Bob could directly hard-pin the chosen assignment, he could append the required constraints in each run. For CUT, it is enough to force either that assignment or its complement, since complementation preserves the value of every CUT-instance. The optimum of the resulting instance, after subtracting the known number of pinning constraints, would reveal the required point evaluation.

Roughly, the same ideal reduction extends to every core relation of degree _d_. Alice’s bits are indexed by [_N]<sup>d</sup>_, and Bob considers 2_<sup>d</sup>_ assignments obtained by changing the selected variable in each of _d_ groups. A signed sum of their values cancels every constraint except the one indexed by Bob’s query. If Bob could hard-pin each assignment in one run of the streaming algorithm, these 2_<sup>d</sup>_ optimum values would reveal his bit.

It would be tempting to use the same satisfiability hard-pinning lemma, Lemma 4.4. However, it only controls assignments that satisfy the whole pinning instance. An optimum for the exact- optimization problem might instead violate one pinning constraint and gain many constraints from Alice’s instance. We therefore replace the constant-size pinning gadget by large blocks whose constraints outweigh every possible gain from _P_.

**Example 2.8** (Strong pinning for CUT)**.** The graph _P_ has 2_N_ vertices, at most _N_<sup>2</sup> edges, and maximum degree at most _N_. Fix an assignment _s_ to its vertices. We want to add a gadget that forces every optimum to agree with _s_ on the original vertices, up to complementing every value. To do this, we introduce extra vertices. Let _L_=1000_N_, and create two blocks _Z_<sub>0</sub>_,Z_<sub>1</sub>, each containing<tbc>

