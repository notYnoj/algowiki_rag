For each \((i,j)\in[p]^2\), the oracle’s answer uniquely determines the entry _M_\[_i,j_\]. The oracle must therefore distinguish between 2<sup>_p_<sup>2</sup></sup> configurations, establishing a space lower bound of \(p^2=\Omega(min(\sigma^2,n^2))\) bits. □

We finally show that any oracle which reports the maximum matching size of a bipartite graph, after _f_=2 edge updates, requires at least \(\Omega(min(\sigma^2,n^2))\) space, irrespective of the query time.

**Theorem 9.3** (Bipartite Matching)**.** _Let_ \(n,\sigma\) _be positive integers with_ \(4\le\sigma\le n(n-1)\)_. There exists an n-vertex bipartite graph_ \(G=(L\cup R,E)\) _and a susceptible set_ \(E_Q\subseteq E\) _of size_ \(\Theta(\sigma)\) _such that any subset sensitivity oracle for maximum bipartite matching requires_ \(\Omega(min(\sigma^2,n^2))\) _bits of space under f_=2 _updates._

_Proof._ Let \(p=min(\lfloor\sigma/4\rfloor,\lfloor n/4\rfloor)\) and let \(K\in\{0,1\}^{p\times p}\) be an arbitrary binary matrix. Define a bipartite graph _G_ with bipartitions<tbc>

\(L=\{l_1,\dots,l_{2p}\},R=\{r_1,\dots,r_{2p}\},\)

<tbc>and edge set<tbc>

\(E=\{(l_i,r_j):K[i,j]=1\}\cup M^*,\)

<tbc>where

\(M^*=\{(l_i,r_{p+i}),(l_{p+i},r_i):i\in[p]\}.\)

The remaining _n_-4_p_ vertices, if any, are isolated. Let _E<sub>Q</sub>=M_<sup>∗</sup>, so \(|E_Q|=2p\le\sigma\). Observe that _M_<sup>∗</sup> is the unique perfect matching of _G_. Now consider the deletion update \(F=\{(l_i,r_{p+i}),(l_{p+j},r_j)\}\subseteq E_Q\). The deleted edges isolate the vertices _r_<sub>_p+i_</sub> and _l_<sub>_p+j_</sub>, so every matching in _G-F_ has size at most 2_p_-1. See Figure 3.

We claim that the maximum matching in _G-F_ has size 2_p_-1 if and only if _K_\[_i,j_\]=1. Indeed, if _K_\[_i,j_\]=1, then \((l_i,r_j)\in E\), and replacing the two deleted matching edges by (_l<sub>i</sub>,r<sub>j</sub>_) yields a matching of size 2_p_-1. Conversely, suppose _G-F_ admits a matching of size 2_p_-1. Since _r_<sub>_p+i_</sub> and _l_<sub>_p+j_</sub> are isolated, every other vertex must be matched. In particular, all remaining degree-one vertices are forced to use their unique incident edges, leaving _l<sub>i</sub>_ and _r<sub>j</sub>_ to be matched together. Hence \((l_i,r_j)\in E\), implying _K_\[_i,j_\]=1.

Layer 1
S
1
2
3
Layer 2
X1
X2
X3
1
7
Layer 3
y1
5
y2
y3
4
5
6
Layer 4
t

Figure 2: Depiction of lower bound for colorful spanning tree for a query that deletes (_y_<sub>2</sub>_,t_) (dotted) and adds (_x_<sub>1</sub>_,t_) with color 5 (dashed).

