Note that we require each agent to list each size-(_d_-1) set of other agents. We denote by \(\ell\)-DSR the restriction of MDSR to instances with \(d=\ell\). It is known that a 3-dimensional stable matching does not always exist, and 3-DSR is NP-complete \[36\].

A _master list_ ML is a preference list over \(\genfrac(){pt}{2}{V}{d-1}\). A preference list \(\succ_v\) for an agent _a_ is _derived from a master list_ ML by deleting all (_d_-1)-sets containing _a_.

**Example 2.** Let _A_={_a_<sub>1</sub>_,a_<sub>2</sub>_,a_<sub>3</sub>_,a_<sub>4</sub>} be a set of agents, _d_=3, and let \(\{a_1,a_2\}\succ\{a_2,a_4\}\succ\{a_1,a_3\}\succ\{a_3,a_4\}\succ\{a_2,a_3\}\succ\{a_1,a_4\}\) be the master list.

Then the preferences of _a_<sub>1</sub> are \(\{a_2,a_4\}\succ_{a_1}\{a_3,a_4\}\succ_{a_1}\{a_2,a_3\}\), the preferences of _a_<sub>2</sub> are \(\{a_1,a_3\}\succ_{a_2}\{a_3,a_4\}\succ_{a_2}\{a_1,a_4\}\), the preferences of _a_<sub>3</sub> are \(\{a_1,a_2\}\succ_{a_3}\{a_2,a_4\}\succ_{a_3}\{a_1,a_4\}\), and the preferences of _a_<sub>4</sub> are \(\{a_1,a_2\}\succ_{a_4}\{a_1,a_3\}\succ_{a_4}\{a_2,a_3\}\).

Next, we define the Multidimensional Stable Roommates with Master List of (_d_-1)-Sets problem (MDSR-ML-Sets).

Again, we denote by \(\ell\)-DSR-ML-Sets the problem MDSR-ML-Sets restricted to instances with \(d=\ell\).

We now turn to the case that the master list orders single agents instead of (_d_-1)-sets of agents. We first need the definition of a partially ordered set.

A _partially ordered set (poset)_ is a pair \((V,\unknown)\), where \(\unknown\) is a binary relation over the set _V_ such that (i) \(v\unknown v\) for all \(v\in V\), (ii) \(v\unknown w\) and \(w\unknown v\) if and only if _v=w_, and (iii) if \(u\unknown v\) and \(v\unknown w\), then \(u\unknown w\).

If \(v\unknown w\) and \(v\neq w\), then we write \(v\succ w\). If neither \(v\unknown w\) nor \(w\unknown v\), then we say that _v_ and _w_ are _incomparable_, and write \(v\perp w\). Instead of \(v\unknown w\) or \(v\succ w\), we may also write \(w\unknown v\) or \(w\prec v\). A _weak order_ is a poset such that for every _a,b_, and _c_ with \(a\perp b\) and \(b\perp c\) also \(a\perp c\) hold.

A _chain_ of \((V,\unknown)\) is a subset \(X=\{x_1,x_2,\dots,x_k\}\subseteq V\) such that \(x_i\succ x_{i+1}\) for all \(i\in[k-1]\). An _anticchain_ is a subset \(X\subseteq V\) such that for all \(v,w\in X\) with \(v\neq w\), we have \(v\perp w\). The _width_ of a poset is the size of a maximum antichain.

For a poset \(\succ\) over a set _V_, \(\kappa_\succ(v):=|\{w\in V:v\perp w\}|\) be the number of elements incomparable with _v_. We define \(\kappa(\succ):=max_{v\in V}\kappa_\succ(v)\). As an example, consider the poset \((\{v_1,v_2,v_3,v_4\},\succ)\) with \(v_1\succ v_2\), \(v_2\succ v_3\), and \(v_1\succ v_4\). Here, _v_<sub>1</sub> is comparable to all other agents, _v_<sub>2</sub> and _v_<sub>3</sub> are only incomparable to _v_<sub>4</sub>, and _v_<sub>4</sub> is incomparable to _v_<sub>2</sub> and _v_<sub>3</sub>, and we have \(\kappa(\succ)=2\). Note that if \(\bar{G}_\succ\) is the incomparability graph of the poset \((V,\succ)\) (i.e., the graph whose vertex set is _V_ and there is an edge between \(v,w\in V\) if and only if \(v\perp w\)), then \(\Delta(\bar{G}_\succ)=\kappa(\succ)\), where \(\Delta(\bar{G}_\succ)\) is the maximum vertex degree in \(\bar{G}_\succ\). If \(\succ\) is a weak order, then the parameter \(\kappa(\succ)\) equals the maximum size of a tie.

Dilworth’s Theorem \[14\] states that the width of a poset is the minimum number of chains such that each element of the poset is contained in one of these chains.

Multidimensional Stable Roommates (MDSR)
Input: An integer d, a set A of agents together with a preference list {a over
for each agent a A.
Task: Decide whether a stable matching exists.

MDSR-ML-Sets
Input: An integer d, a set A of agents, and a master list {a over
from which the preference list of each agent is derived.
Task: Decide whether a stable matching exists.

