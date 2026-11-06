After an FPT-algorithm for the parameter maximum number of agents incomparable to a single agent in Section 4.2.1, we have seen W\[1\]-hardness for the stronger parameter width of the master poset. It remains open whether 3DSR-Poset parameterized by the width of the master poset lies in XP.

We now investigate a third parameter measuring similarity to a strictly ordered master poset, namely the (agent) deletion distance to a strictly ordered master poset.

## 4.3 Deletion distance to a strictly ordered master poset

We saw that MDSR-Poset is fixed-parameter tractable when parameterized by the maximum number of agents incomparable to a single agent, but it is W\[1\]-hard when parameterized by the width of the poset. We now consider another natural parameter measuring the similarity to a strict order, namely the deletion distance to a strict order, i.e., the minimum number of agents which need to be deleted such that the resulting preferences are derived from a strict order (note that this does not pose any condition on the preferences of the deleted agents). Notably, this parameter is orthogonal to the two parameters investigated before (width of the poset and maximum number of agents incomparable to an agent), as can be seen from the following two examples: If the master poset is the weak order \(a_1\perp_\text{ML}a_2\succ_\text{ML}a_3\perp_\text{ML}a_4\succ_\text{ML}a_5\perp_\text{ML}a_6\succ_\text{ML}\cdots\succ_\text{ML}a_{n-1}\perp_\text{ML}a_n\), thus \(\kappa(\text{ML})=2\), while one has to delete _n/_2 agents in order to obtain a strict order. If the preferences of all but one agent are derived from a strict order, and the last agent’s preferences are derived from the inverse of this strict order, then the deletion distance is one while any master poset from which this preferences are derived contains a tie of size at least _n_-1 and thus has width at least _n_-1. In this section, reducing from Multicolored clique we show that MDSR is W\[1\]-hard parameterized by the deletion distance to a strictly ordered master poset. First, we formally introduce the parameter.

**Definition 2.** For an MDSR-instance I, let \(\lambda(\mathcal{I})\) denote the minimum number of agents such that the preferences of the instance arising through the deletion of these agents are derived from a strict order.

Note that the agents which were deleted to arrive at a strictly ordered master poset may have arbitrary preferences. We now present an example for this parameter.

**Example 6.** Consider an MDSR instance I with _d_=3 and the following preferences.

\(a_1:\{a_2,a_3\}\succ\{a_3,a_4\}\succ\{a_2,a_5\}\succ\{a_2,a_4\}\succ\{a_3,a_5\}\succ\{a_4,a_5\},\)<br>
\(a_2:\{a_1,a_3\}\succ\{a_3,a_4\}\succ\{a_1,a_5\}\succ\{a_1,a_4\}\succ\{a_3,a_5\}\succ\{a_4,a_5\},\)<br>
\(a_3:\{a_1,a_2\}\succ\{a_1,a_4\}\succ\{a_2,a_5\}\succ\{a_2,a_4\}\succ\{a_1,a_5\}\succ\{a_4,a_5\},\)<br>
\(a_4:\{a_1,a_5\}\succ\{a_1,a_2\}\succ\{a_2,a_5\}\succ\{a_1,a_3\}\succ\{a_3,a_5\}\succ\{a_2,a_3\},\)<br>
\(a_5:\{a_2,a_3\}\succ\{a_3,a_4\}\succ\{a_1,a_2\}\succ\{a_2,a_4\}\succ\{a_1,a_3\}\succ\{a_1,a_4\}.\)

After the deletion of _a_<sub>5</sub>, the preferences are

\(a_1:\{a_2,a_3\}\succ\{a_3,a_4\}\succ\{a_2,a_4\},\)<br>
\(a_2:\{a_1,a_3\}\succ\{a_3,a_4\}\succ\{a_1,a_4\},\)<br>
\(a_3:\{a_1,a_2\}\succ\{a_1,a_4\}\succ\{a_2,a_4\},\)<br>
\(a_4:\{a_1,a_2\}\succ\{a_1,a_3\}\succ\{a_2,a_3\}.\)

which are derived from the strict order \(a_1\succ a_2\succ a_3\succ a_4\). Hence, \(\lambda(\mathcal{I})=1\).

