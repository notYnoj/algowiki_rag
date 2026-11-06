Having defined posets, we now show the connection to Multidimensional Stable Roommates by using preferences derived from a poset of agents.

**Definition 1.** Given a set _A_ of agents, a poset \((A,\succ_\mathrm{ML})\) (called the _master poset_), and an integer _d_, a preference list \(\succ_a\) on \(\genfrac(){pt}{2}{A\backslash\{a\}}{d-1}\) _is derived from_ \(\succ_\mathrm{ML}\) if whenever _a_<sub>1</sub>_,...,a_<sub>_d_-1</sub> and _b_<sub>1</sub>_,...,b_<sub>_d_-1</sub> with \(a_i\unknown_\mathrm{ML}b_i\) for all \(i\in[d-1]\), then \(\{a_1,\dots,a_{d-1}\}\unknown_v\{b_1,\dots,b_{d-1}\}\).

**Example 3.** Let \(a_1\succ a_2\succ a_3\succ a_4\succ a_5\) be a master poset. Then _a_<sub>1</sub> has one of the following two preferences: \(\{a_2,a_3\}\succ_{a_1}\{a_2,a_4\}\succ_{a_1}\{a_2,a_5\}\succ_{a_1}\{a_3,a_4\}\succ_{a_1}\{a_3,a_5\}\succ_{a_1}\{a_4,a_5\}\) or \(\{a_2,a_3\}\succ_{a_1}\{a_2,a_4\}\succ_{a_1}\{a_3,a_4\}\succ_{a_1}\{a_2,a_5\}\succ_{a_1}\{a_3,a_5\}\succ_{a_1}\{a_4,a_5\}\).

For the master poset \(\succ\) with \(a_2\succ a_3\), \(a_2\succ a_4\), \(a_3\succ a_1\), and \(a_4\succ a_1\) (and \(a_3\perp a_4\)), agent _a_<sub>1</sub> has one of the following preferences: \(\{a_2,a_3\}\succ_{a_1}\{a_2,a_4\}\succ_{a_1}\{a_3,a_4\}\) or \(\{a_2,a_4\}\succ_{a_1}\{a_2,a_3\}\succ_{a_1}\{a_3,a_4\}\).

The formal definition of MDSR-Poset reads as follows.

Again, we denote by \(\ell\)-DSR-Poset the problem MDSR-Poset restricted to instances with \(d=\ell\).

### Parameterized Complexity.

A _parameterized language L_ over a finite alphabet \(\Sigma\) is a subset \(L\subseteq\Sigma^*\times\mathbb{N}\). A parameterized language _L_ is _fixed-parameter tractable_ if there exists an algorithm which correctly decides for every instance \((I,k)\in\mathbb{N}\) whether \((I,k)\in L\) in FPT-time, that is, \(f(k)\cdot|(I,k)|^{O(1)}\), where |(_I,k_)|:=|_I_|+_k_ with |_I_| being the size of _I_ and _f_ being a computable function. The class of all fixed-parameter tractable parameterized languages is denoted by FPT.

To indicate that a parameterized language is not fixed-parameter tractable, one usually uses the notions of parameterized reductions and W\[1\]-hardness. A _parameterized reduction_ from a parameterized language _L_ to a parameterized language \(L'\) is an algorithm A which computes, given an instance (_I,k_) of _L_, an instance \((I',k')\in L'\) with \(k'\le g(k)\) for some computable function _g_ such that \((I,k)\in L\) if and only if \((I',k')\in L'\) and runs in FPT-time. W\[1\]is the class of parameterized problems which are equivalent to Clique parameterized by solution size under parameterized reductions. To show W\[1\]-hardness of a parameterized problem _L_, one usually gives a parameterized reduction to Clique or another W\[1\]-hard problem. Under the complexity-theoretic assumption \(\mathsf{FPT}\neq\mathsf{W}[1]\), W\[1\]-hardness of a parameterized problem implies that this problem is not in FPT. For more details on parameterized complexity, we refer to standard textbooks \[10, 15, 17, 37\].

## 3 Three-dimensional stable roommates with master list of 2- sets

In this section, we consider the case that the preferences are complete and derived from a master list of (_d_-1)-sets. In Section 3.1, we give a small instance with six agents not admitting a stable matching. We use this to show in Section 3.2 that already for dimension _d_=3 and preferences derived from a master list of 2-sets, deciding whether an instance admits a stable matching is NP-complete.

MDSR-Poset
Input:
An MDSR instance = (A,(>a)a A, d) and a master poset
such that the
preferences
of each agent a are derived from
Task:
Decide whether there exists a stable matching in I.

