woman-optimal stable matching. At each step, the algorithm employs breakmarriage operations to generate neighboring stable matchings. Tziavelis et al (2020) innovated the first unbiased and voluntary methods for deriving an equitable stable matching within cubic time, which encompass the Late Discontent Suspension (EDS), Early Discontent Suspension (LDS), and Permanent Discontent Ban (PDB) algorithms. Few studies have considered optimizing the sex equality cost in the SMTI problem.

## 3 Preliminaries

This section provides formal definitions related to the bipartite stable _b_-matching problem, a general framework for the SMTI and HRT problems, as well as the sex equality cost.

### 3.1 Bipartite stable _b_-matching

An undirected bipartite graph _G_=(_V,E_), preference lists _L_, and a quota function \(b:V\rightarrow\mathbb{N}\) are the inputs of a bipartite stable _b_-matching problem. In the graph _G_, \(V=U\cup W\), where _U_ and _W_ are disjoint sets. Each vertex in _U_ is connected to a subset of vertices in _W_, and similarly, vertices in _W_ are connected to subsets in _U_. Each agent \(v\in V\) has a preference list _L<sub>v</sub>_ consisting of agents who are adjacent to _v_. We refer to all the agents in _L<sub>v</sub>_ as _v_’s _candidates_. Additionally, the preference list of each agent may include ties. We denote _r<sub>v</sub>(x_) as the rank of _x_ in _v_’s preference list. If _v_ prefers _x_ and _y_ equally, this is denoted by _r<sub>v</sub>(x_)=_r<sub>v</sub>(y_). If _v_ strictly prefer _x_ to _y_, we write _r<sub>v</sub>(x)\<r<sub>v</sub>(y_). Furthermore, we define \(\phi_v(x)=\{y\in L_x|y\neq v,r_x(v)=r_x(y)\}\) as a set of agents who have the same rank as _v_ in agent _x_’s preference list.

A _b_-matching _M_ is a subset of _E_ such that each agent _v_ is connected to at most _b(v_) edges in _M_, that is, \(deg_M(v)\le b(v)\), where _deg<sub>M</sub>_ denotes the degree of vertex _v_ in the graph _G<sub>M</sub>_=(_V,M_). The size of _M_, defined as |_M_|, refers to the number of matched pairs. We denote _M(v_) as the set of agents who are connected to agent _v_ in _M_, referred to as _v_’s _partners_. An agent _v_ is _full_ if _deg<sub>M</sub>(v_)=_b(v_) and is _free_ if _deg<sub>M</sub>(v)\<b(v_). The set of all free agents in _M_ is denoted by _F<sub>M</sub>_. For each free agent \(f\in F_M\), let \(\xi_f^M=\{x\in L_f|x\notin M(f)\}\) denote the set of agents who are candidates for _f_ but are not currently matched with it in matching _M_. A matching _M_ is said to be _perfect_ if and only if there are no free agents.

The agent _x_ is termed as _v_’s _worst partner_ if \(x\in M(v)\) and \(r_v(x)=max\{r_v(y)|y\in M(v)\}\). In a _b_-matching _M_, (_u,w_) is a _blocking pair_ (BP) if and only if:

(i). \(u\in L_w\), \(w\in L_u\), and \((u,w)\notin M\);<tbc>

(ii). _u_ either is free, or strictly prefers _w_ over its worst partner in _M_;<tbc>

(iii). _w_ either is free, or strictly prefers _u_ over its worst partner in _M_.

BP (_u,w<sub>i</sub>_) dominates BP (_u,w<sub>j</sub>_) from _u_’s point of view if _u_ strictly prefers _w<sub>i</sub>_ to _w<sub>j</sub>_. Similarly, BP (_u<sub>i</sub>,w_) dominates BP (_u<sub>j</sub>,w_) from _w_’s point of view if _w_ strictly prefers _u<sub>i</sub>_ to _u<sub>j</sub>_. A BP is an _undominated blocking pair_ (UBP) of _v_ if there are no other BPs dominating it from _v_’s perspective. Removing UBPs may decrease the number of BPs more effectively than merely eliminating BPs (Cao et al 2023; Gelain et al 2013). A<tbc>

