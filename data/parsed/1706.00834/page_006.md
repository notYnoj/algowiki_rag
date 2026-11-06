<tbc>and sink nodes, respectively. Note that the number of edges in any path in G from _s_ to _t_ is at most _D=n_-1. Also the total number of paths in G is N=2<sup>_n_-2</sup>. The corollary below shows the superiority of the performance of CH over EH in terms of regret bound which is a direct result of Theorems 1 and 2. EH offers worse regret guarantee as its bound has an additional loss range factor.

**Corollary 3** _Given a complete DAG_ G _with n nodes, let L_<sup>∗</sup> _be the total loss of the best path. Then with proper tuning of the learning rate_ \(\eta\) _over the trials for both EH and CH, we obtain the following regret guarantees:_

\(\mathcal{R}_{EH}=\mathcal{O}(n\sqrt{L^*}),\mathcal{R}_{CH}=\mathcal{O}(n^\frac{1}{2}(logn)^\frac{1}{2}\sqrt{L^*}).\)

**Remark.** For EH, projections are simply a renormalization of the path weights which is done efficiently via weight pushing (Mohri, 2009; Takimoto and Warmuth, 2003). On the other hand, for CH, iterative Bregman projections (Bregman, 1967) are needed for projecting back into the unit-flow (Koolen et al., 2010). These methods are known to converge to the exact projection (Bregman, 1967; Bauschke and Borwein, 1997); however, there will always be a gap to the full convergence. These remaining gaps to the exact projections have to be accounted for as additional loss in the regret bounds (e.g. see Rahmanian et al. (2018)). Additionally, the relatively expensive projection operation in CH makes it less computationally efficient compared to EH.

**3. Learning Multipaths**

We begin with defining directed multigraphs, multiedges<sup>2</sup> and multi-DAGs.

**Definition 4 (Directed Multigraph)** _A **directed multigraph** is an ordered pair_ H=(_V,M_) _comprising of a set V of vertices or nodes together with a set M of **multiedges**. Each multiedge_ \(m\in M\) _is an ordered pair m_=(_v,U_) _where_ \(v\in V\) _and_ \(U\subseteq V\)_. Furthermore, we denote the set of "outgoing" and "incoming" multiedges for vertex v by_ \(M_v^{(out)}\) _and_ \(M_v^{(in)}\)_, respectively, which are defined as_

\(M_v^{(out)}:=\{m\in M|m=(v,U)\text{\textit{for some}}U\subseteq V\},\)<br>
\(M_v^{(in)}:=\{m\in M|m=(u,U)\text{\textit{for some}}u\in V\text{\textit{and}}U\subseteq V\text{\textit{s.t.}}v\in U\}.\)

**Definition 5 (Base Directed Graph)** _The **base directed graph** of a given directed multigraph_ H=(_V,M_) _is a directed graph_ B(H)=(_V,E_) _where_

\(E=\{(v,u)|\exists(v,U)\in M\text{\textit{s.t.}}u\in U\}.\)

**Definition 6 (Multi-DAG)** _A directed multigraph_ H=(_V,M_) _is a **multi-DAG** if it has a single "source" node_ \(s\in V\) _with no incoming multiedges and its base directed graph_ B(H) _is acyclic. Additionally, we refer to the set of nodes in V with no outgoing multiedges as the set of "sink" nodes which is denoted by_ \(\mathcal{T}\subset V\) .

2. Our definitions of multigraphs and multiedges are closely related to _hyper-graphs_ and _hyper-arcs_ in the literature (see e.g. Martin et al. (1990)).

