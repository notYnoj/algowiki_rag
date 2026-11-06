<tbc>Every iteration removes \(\Omega_{c,\rho}(n_i)\) vertices. Thus, the sequence (_n<sub>i</sub>)<sub>i</sub>_ decreases geometrically, and<tbc>

\(\sum_in_i=\mathcal{O}_{c,\rho}(n).\)

<tbc>For the second term of (1), we have<tbc>

\(\sum_i\sum_{u\in U_i}\mathrm{deg}_{G_i}(u)=\sum_{r\ge 1}|S_r|,\text{with}S_r:=\{(i,u)|u\in U_i\text{and}\mathrm{deg}_{G_i}(u)\ge r\}.\)

<tbc>For every _r_ with \(S_r\neq\emptyset\), let _i<sub>r</sub>_ be the smallest index such that _U<sub>i<sub>r</sub></sub>_ contains a vertex of degree at least _r_. The geometric decrease and \(|U_i|=\Theta(n_i)\) imply<tbc>

\(|S_r|\le\sum_{i\ge i_r}|U_i|=\mathcal{O}_{c,\rho}(|U_{i_r}|).\)

<tbc>For every \(r\ge 1\), let<tbc>

\(A_r:=\{v\in V(G)|\mathrm{deg}_G(v)\ge r\}.\)

<tbc>Because _U<sub>i<sub>r</sub></sub>_ consists of the lower half of the degree order and contains a vertex of degree at least _r_, every vertex of _V(G<sub>i<sub>r</sub></sub>_)\\_U<sub>i<sub>r</sub></sub>_ has degree at least _r_ in _G<sub>i<sub>r</sub></sub>_, and hence also in _G_. Therefore,<tbc>

\(\left\lfloor\frac{n_{i_r}}{2}\right\rfloor\le|A_r|\text{and consequently}|U_{i_r}|\le|A_r|+1.\)

<tbc>Since \(S_r=\emptyset\) for \(r\ge n\) and \(\sum_{r\ge 1}|A_r|=2m\), we obtain

\(\sum_i\sum_{u\in U_i}\mathrm{deg}_{G_i}(u)=\sum_{r=1}^{n-1}|S_r|\le\mathcal{O}_{c,\rho}\left(\sum_{r=1}^{n-1}(|A_r|+1)\right)=\mathcal{O}_{c,\rho}(n+m).\)

Substituting both estimates into (1) proves the claim. \(\lrcorner\)

We conclude by Claims 29 and 30.

## 7 Finding Small Patterns

We next design a randomized linear-time algorithm that returns a triangle (if one exists) in graphs from a class of linear neighborhood complexity. The main idea is to use an sd-degeneracy sequence of the input graph to guide the search. In the next three (almost-)linear algorithms we assume that the edges of the input graph are preprocessed into a static dictionary in O(_n+m_) expected time and O(_n+m_) space, supporting adjacency queries in O(1) expected time.

**Theorem 8.** _For every graph class_ C _of linear neighborhood complexity, Triangle Detection can be solved in expected time_ O<sub>C</sub>(_n+m_) _on n-vertex m-edge graphs of_ C.

_Proof._ Let _G_ be any input graph. By Theorem 2, we get an sd-degeneracy sequence (_u_<sub>1</sub>_,v_<sub>1</sub>)_,...,(u_<sub>_n_-1</sub>_,v_<sub>_n_-1</sub>) of _G_ of width _d_=O<sub>C</sub>(1) in randomized time O<sub>C</sub>(_n+m_).

For every \(i\in[n-1]\), we define _G<sub>i</sub>_:=_G_-{_u_<sub>1</sub>_,...,u_<sub>_i_-1</sub>}. Note that to find a triangle in _G=G_<sub>1</sub> (if any), it is enough to return a triangle of _G_<sub>1</sub> that contains _u_<sub>1</sub> or obtain the guarantee that _not_ all the triangles of _G_<sub>1</sub> contain _u_<sub>1</sub>, and recursively apply this strategy to _G_<sub>2</sub>. Indeed, at each step we either find a triangle in _G<sub>i</sub>_ or move to _G_<sub>_i_+1</sub> with the promise that _G_<sub>_i_+1</sub> contains a triangle if and only if _G<sub>i</sub>_ contains one.

