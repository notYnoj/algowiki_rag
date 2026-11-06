a random construction `rDecompose` which samples all vertices with identical probability. Finally, we check that the dominating sets are computed correctly and are not too large. If there is an error in the sample dominating sets, we return an exact `APSP` solution.

In Phase 1, we compute the sets _X(u,i_), _C(u,i_). For a given _i_, if \(|N(u,r_i)|\ge s_i\) is large, we let _X(u,i_) be an arbitrary subset of size _s<sub>i</sub>_ within this neighborhood. On the other hand, if |_N(u,r<sub>i</sub>_)|_\<s<sub>i</sub>_ is small, we let \(C(u,i)=N(u,r_i)\cap D_{i+1}\) given \(|N(u,r_i)\cap D_{i+1}|\) is small. If we are unable to compute either _X(u,i_) or _C(u,i_), we return an exact `APSP` computation.

Then, for vertices _u_ with degree at most _s_<sub>_k_<sub>0</sub>+2</sub>, we compute a depth 2 `BFS` in the graph _G_<sub>_k_<sub>0</sub>+1</sub>. Finally, we augment _D<sub>i</sub>_ with a hitting set for _X(u,i_) for all _u_ with large _N(u,r<sub>i</sub>_). Note that when we augment _D<sub>i</sub>_, this does not affect the sets _r(u,D<sub>i</sub>_) for \(\mathrm{deg}(u)\ge s_i\) or _q(w,D<sub>i</sub>_) for \(w\in D_i\). These relationships are fixed at the computation of `rDecompose`.

In Phase 2, we begin by iteratively executing `Dijkstra` from each vertex \(w\in D_j\) on the graph _G<sub>j,w</sub>_ consisting of edges _E<sub>j</sub>,E_<sup>∗</sup> as well as \(w\times V\) and \(D_{j_1}\times D_{j_2}\) for all indices \(j+j_1+j_2\le 2k+1\). Before the execution of `Dijkstra`, each vertex \(w\in D_j\) examines its constituency (Definition 2.2) and updates its distance estimates where an improvement can be found.

Finally, each vertex _u_ examines _p(u,D<sub>i</sub>_) and _C(u,i_) where appropriate to update its distance estimates for all other vertices \(v\in V\) .

## Preliminaries for Proving Theorem E.1

A key ingredient of our algorithm is computing small neighborhoods of each vertex. In the following lemma, we describe how to compute _X(u,i),C(u,i_) efficiently.

**Lemma E.3.** _Suppose_ \(\beta\ge 4\)_. Let_ \(u\in V\) _and_ \(k_0+1\le i\le k_0+\frac{\beta}{2}-1\)_. Algorithm 15 computes X(u,i),C(u,i_) _in time_ \(O\left(n^{2+\frac{1}{k}}\right)\) _such that,_

1. \(X(u,i)\subset N(u,r_i)\) _and_ \(|X(u,i)|\ge s_i\) _if_ \(|N(u,r_i)|\ge s_i\).<tbc>

_2._ \(C(u,i)=N(u,r_i)\cap D_{i+1}\) _if_ \(|N(u,r_i)\cap D_{i+1}|<12s_{k-1}\mathrm{log}n\).

_Proof._ Fix some iteration _i_ and vertex _u_. We conduct a `BFS` on the graph _G_ from _u_ until we either encounter a vertex at depth _r<sub>i</sub>_+1 or _s<sub>i</sub>_ distinct vertices. If we encounter _s<sub>i</sub>_ distinct vertices first, then \(|N(u,r_i)|\ge s_i\), so define _X(u,i_) to be the distinct vertices encountered thus far. Otherwise, if we encounter a vertex at depth _r<sub>i</sub>_+1 first, then |_N(u,r<sub>i</sub>_)|_\<s<sub>i</sub>_ and we can efficiently compute \(C(u,i)=N(u,r_i)\cap D_{i+1}\) by iterating over the distinct vertices found and querying their membership in _D_<sub>_i_+1</sub>.

To bound the time required to compute these sets, note that finding _s<sub>i</sub>_ distinct vertices requires time at most \(s_i^2\). In particular, we can bound the time consumed by computing the `BFS` as,<tbc>

\(s_i^2\le s_{k_0+1}^2=n^{2-\frac{2(k_0+1)}{k}}\)

<tbc>Note \(k_0=\beta-2=\frac{2}{3}(k-1)-2=\frac{2}{3}k-\frac{8}{3}\). Summing over all vertices _u_ and iterations _i_, the total time consumed is,

\(O\left(n^{3-\frac{2(k_0+1)}{k}}\right)=O\left(n^{3-\frac{4k/3-10/3}{k}}\right)=O\left(n^\frac{5}{3}+\frac{10}{3k}\right)=O\left(n^{2+\frac{1}{k}}\right)\)

The last inequality holds whenever \(k\ge 7\) or alternatively \(\beta=\frac{2}{3}(k-1)\ge 4\). Computing _C(u,i_) requires only _s<sub>i</sub>_ time as we only need to iterate over the vertices found in _N(u,r<sub>i</sub>_).

