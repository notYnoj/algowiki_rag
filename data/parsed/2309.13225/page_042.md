_Proof._ This holds simply by observing that every distance estimate is produced by some path in the original graph _G_.

Every estimate in Phase 1 found by concatenating two paths in _G<sub>i</sub>_, a subgraph of _G_.

In Phase 2, the only edges added are of the form \(u\times V\) . However, the weights of these edges, if finite, are computed by a previous step as the length of some path from _u_ to the relevant vertex \(w\in V\) .

We present the key lemma for correctness below. In particular, we prove that we have a good additive approximation after the (_k_<sub>0</sub>+3)-th iteration.

**Lemma 5.11.** _Let P be a shortest path between u,v. In Phase 2 of Algorithm 6, let w be a vertex of P with_ \(\mathrm{deg}(w)\ge s_{k_0+3}\)_. Then, for every vertex_ \(x\in P\)_, the_ (_k_<sub>0</sub>+3)_-th iteration of Phase 2 finds a path of length_ \(\delta(w,x)+5\) _from w_<sup>∗</sup> _to x where w_<sup>∗</sup>=_r(w,D_<sub>_k_<sub>0</sub>+3</sub>).

_Proof._ Let _P<sub>w,x</sub>_ denote the sub-path of _P_ between _w_ and _x_.

**Case 1:** \(\mathrm{deg}(P_{w,x})\le s_{k_0}\) Consider the path _P<sub>w,x</sub>_. By Lemma A.3, since \(\mathrm{deg}(w)\ge s_{k_0+3}\), we have that, \(L(P_{w,x})\subset\{k_0+1,k_0+2\}\) so that,

\(\hat{\delta}_{k_0+3}(w^*,x)\le\delta(w,x)+5\)

**Case 2:** deg(_P<sub>w,x</sub>)\>s_<sub>_k_<sub>0</sub></sub> We now arrive at the key case depending on Phase 1. Let _y_ denote the vertex in _P<sub>w,x</sub>_ closest to _x_ with degree \(\mathrm{deg}(y)\ge s_{k_0+2}\) and _z_ be a vertex of maximum degree on _P<sub>w,x</sub>_. Then, let _i_<sup>∗</sup> be the integer \(1\le i\le l\) such that \(\frac{n}{2^{i^*}}\le\mathrm{deg}(z)<\frac{n}{2^{i^*-1}}\). Let _y_<sup>∗</sup>=_r(y,D_<sub>_k_<sub>0</sub>+2</sub>) and _z_<sup>∗</sup>=_r(z,C_<sub>_i_<sup>∗</sup></sub>).

In particular, since \(P\subset F_{i^*}\) we have in the _i_<sup>∗</sup> iteration of Phase 1 that \(X_{i^*}(z^*,w^*)\le\delta(z,w)+2\) and \(X_{i^*}(z^*,y^*)\le\delta(z,y)+2\). Now, since \(B'_i\) is an Euler tour distance matrix, it is therefore a 1- bounded difference matrix by the triangle inequality. Then, the procedure `BDtoMonotone` creates a row-monotone matrix keeping values bounded in _O(n_). Finally, _B<sub>i</sub>_ is a row-monotone matrix as the sub-matrix of a row-monotone matrix. Thus, we can use `MonotoneMinPlus`(_A_<sub>_i_<sup>∗</sup></sub>_,B_<sub>_i_<sup>∗</sup></sub>) to compute,<tbc>

\(\hat{\delta}_{i^*}(w^*,y^*)\le X_{i^*}(w^*,z^*)+X_{i^*}(z^*,y^*)\le\delta(w,z)+\delta(z,y)+4=\delta(w,y)+4\)

<tbc>Now, in the (_k_<sub>0</sub>+3)-th iteration in Phase 2, when we execute `dijkstra` from _w_<sup>∗</sup>, we have an edge to _y_<sup>∗</sup> with weight at most \(\delta(w,y)+4\). If deg(_x)\>s_<sub>_k_<sub>0</sub>+2</sub>, and therefore _y=x_, we take an extra edge \((x^*,x)\in E^*\) to find a path of length at most \(\delta(w,y)+4+1=\delta(w,x)+5\). Otherwise, after using the edge \((y^*,y)\in E^*\), the remaining edges of _P<sub>w,x</sub>_ are in _E_<sub>_k_<sub>0</sub>+3</sub> and we can conclude,

\(\hat{\delta}_{k_0+3}(w^*,x)\le\hat{\delta}_{i^*}(w^*,y^*)+1+\delta(y,x)\le\delta(w,y)+\delta(y,x)+5=\delta(w,x)+5\)

## 5.3 Additive Approximations for Constant Length Paths

In this section, we give a simpler algorithm that uses fast matrix multiplication to obtain fast algorithms for general additive approximations on small distances. We employ this result in the proof of Theorem 3.3.

