where

\(G_t=(V,E_t),E_t=\big\{\{\pi_t(u),\pi_t(v)\}:\{u,v\}\in E\big\}.\)

An agent starts at a specified vertex and must traverse an available edge at each time step, without waiting at a vertex. The objective of restless exploration is to find a restless temporal walk that visits every vertex. Combining Theorems 10 and 14 of Ayoubi and Narayanan, for lifetime \(L\ge n(n-1)\), every VPG based on _G_ admits restless exploration from every starting vertex if and only if _G_ contains no small blocking set [10]. Equivalently, if _G_ contains a small blocking set, one can construct a permutation sequence and a starting vertex for which the corresponding VPG admits no restless exploration.

**Definition 1** (Small blocking set)**.** For an independent set \(S\subseteq V\) , let _N(S_) denote the set of vertices adjacent to at least one vertex of _S_. A nonempty independent set \(S\subseteq V\) is a _small blocking set_ of _G_ if<tbc>

\(|S|=|N(S)|<\frac{n}{2}.\)

<tbc>We study whether a small blocking set exists and how to construct one when it does. To describe the cardinality relationship between an independent set and its neighborhood, define the _difference_ of an independent set \(X\subseteq V\) by<tbc>

\(d(X)=|X|-|N(X)|.\)

<tbc>The small blocking set detection and construction problem can therefore be stated equivalently as finding an independent set \(S\subseteq V\) such that

\(S\neq\varnothing,d(S)=0,|S|<\frac{n}{2},\)

or determining that no such set exists.

To solve this problem, we use critical independent sets.

**Definition 2** (Critical independent set [11])**.** An independent set \(I\subseteq V\) is a _critical independent set_ (CIS) if

\(d(I)\ge d(X)\)

for every independent set \(X\subseteq V\) . A critical independent set of largest cardinality among all critical independent sets is called a _maximum-cardinality critical independent set_.

