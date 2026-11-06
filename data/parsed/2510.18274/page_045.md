## C.3 Bounding the Number of Residual Witnesses of _H_

We now bound the number of residual witnesses of _H_ with respect to its flow subgraph _F_ of size _f-k_. Throughout this subsection, we write (_a,b,w_) to denote a _directed_ edge from _a_ to _b_ with weight _w_, and reserve the notation (_a,b_) exclusively for an undirected, unweighted edge between vertices _a_ and _b_. In the context of cuts and flows, we may replace an undirected edge (_a,b_) with the pair of directed edges (_a,b,_1) and (_b,a,_1) as needed. We adopt these views interchangeably.

**Claim C.8.** _The number of residual witnesses of H is at most n_<sup>_O(f_)</sup>.

_Proof._ We will attempt to (over)count the number of residual witnesses \(\mathsf{W}=(S,T,E_{H_F}(S,T)\cup X)\) of _H_. First, observe that since _E<sub>H<sub>F</sub></sub>(S,T_) contains up to \(k-k'-1\le k\le f\) edges, there are at most _n_<sup>_O(f_)</sup> choices for _E<sub>H<sub>F</sub></sub>(S,T_). Similarly, as \(|X|\le k-k'-1\le k\le f\), there are at most _n_<sup>_O(f_)</sup> choices for _X_. In what follows, we will show that for any fixed realization of \(C\subseteq S\times T\times\{1,2\}\) with \(w(C)\le k-k'-1\), the number of cuts (_S,T_) such that _E<sub>H<sub>F</sub></sub>(S,T_)=_C_ is at most _n_<sup>_O(f_)</sup>. This count is equivalent to determining the number of ways to label each \(v\in V\) with either ‘s’ or ‘t’ such that the set of directed edges from vertices labeled ‘s’ to those labeled ‘t’ corresponds exactly to _C_.

For convenience, we adopt the following terminology: a _labeling_ is a function \(\phi:V\rightarrow\{\text{‘s’,‘t’}\}\) such that \(\phi(s)=\text{‘s’}\) and \(\phi(t)=\text{‘t’}\). A directed edge \((a,b,w)\in H_F\) is called an _s-t edge_ if \(\phi(a)=\text{‘s’}\) and \(\phi(b)=\text{‘t’}\). A labeling \(\phi\) is said to be _consistent_ with _C_ if the set of _s-t_ edges is precisely _C_. Therefore, our task reduces to bounding the number of consistent labelings.

The edges of _H<sub>F</sub>_ can be partitioned into two disjoint sets, \(E_1\cup E_2\), defined as follows:

• _E_<sub>1</sub>=_H_\\_F_ is the set of undirected unit-capacitated edges. Each such edge (_a,b_) can equivalently be replaced with two directed edge (_a,b,_1) and (_b,a,_1). We adopt these views interchangeably. Let _V(E_<sub>1</sub>) denote the set of vertices incident to edges in _E_<sub>1</sub>.<tbc>

• _E_<sub>2</sub> is the set of directed edges with weight 2, corresponding to the reversal of the flow _F_. Let _V(E_<sub>2</sub>) denote the set of vertices incident to edges in _E_<sub>2</sub>.

We now proceed to count the number of labels \(\phi\) that are consistent with _C_. Our approach is to assign the labels in three steps: to _V(C_), to _V(E_<sub>2</sub>)\\_V(C_), and to the remaining vertices. By Assumption C.3, we may assume that _H_ is connected. Since _H_ and _H<sub>F</sub>_ share the same underlying graph, we have \(V(E_1)\cup V(E_2)=V\) . Consequently, assigning a label to each vertex in \(V(E_1)\cup V(E_2)\) ensures that no vertex remains unlabeled.

### Step 1: Counting the number of labels for _V(C_).

Fix _C_. There can be at most one labeling of _V(C_) that is consistent with _C_; specifically, for any \((a,b,w)\in C\), we must have \(\phi(a)=\text{‘s’}\) and \(\phi(b)=\text{‘t’}\). See Figure 2 for an illustration. Going forward, we fix the labels of the vertices in _V(C_) accordingly.

### Step 2: Counting the number of labels for _V(E_<sub>2</sub>)\\_V(C_) given a label of _V(C_).

Fix a labeling of _V(C_) from Step 1. In this step, we will label _V(E_<sub>2</sub>)\\_V(C_). Recall that _E_<sub>2</sub> is the reversal of _F_, which consists of _f-k_ edge-disjoint _s-t_ flows. Thus, the subgraph induced by _E_<sub>2</sub> consists of _f-k_ edge-disjoint _t-s_ flows. This means we can partition _E_<sub>2</sub> into _f-k_ disjoint directed paths from _t_ to _s_. Call them _P_<sub>1</sub>_,...,P_<sub>_f-k_</sub>. For each _i_, let \(\eta_i=|P_i\cap C|\) denote the number of edges in _P<sub>i</sub>_ that appear in _C_. We then have:

\(\sum_{i=1}^{f-k}\eta_i=\sum_{i=1}^{f-k}|P_i\cap C|\le|C|\le w(C)\le k-k'-1.\)

