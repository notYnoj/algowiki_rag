and _O(kmn_<sup>1_/k_</sup>) pre-processing time \[TZ05\]. Since then a rich literature of work has followed with improvements in pre-processing and query time, space complexity and bi-criteria approximations \[MN07, BK10, WN12, AG13, Che14, Che15, EP16, ENWN16, PR10, Som16, AR20, CZ22\].

Comparisons with the concurrent work of \[DFK<sup>+</sup>23\] can be found in Theorem 3.1,  2, and  4.

## 2 Preliminaries

Let _G_=(_V,E_) be an undirected, unweighted graph with vertices _V_ and edges _E_. Let _n_ denote the number of vertices and _m_ the number of edges. Given a pair of vertices _u,v_, let \(\delta(G,u,v)\) denote the distance in _G_ between _u,v_ i.e. the length of the shortest path connecting _u_ and _v_. When the underlying graph _G_ is clear, we omit this parameter and write \(\delta(u,v)\). A path _P_ can be denoted by a sequence of vertices (_u,u_<sub>2</sub>_,...,v_) or by its endpoints _P<sub>u,v</sub>_. Given two paths _P,Q_ that share an endpoint (and no other vertices), let \(P\circ Q\) denote the concatenation of the two paths. Let \(N(u)=\{v\in V\text{s.t.}(u,v)\in E\}\) denote the neighborhood of _u_ and \(N(u,d)=\{v\in V\text{s.t.}\delta(u,v)\le d\}\) denote the depth _d_ neighborhood of _u_.

**Definition 2.1.** _Let G be an graph and_ \(\delta(G,u,v)\) _denote the length of the shortest path from u to v. A distance estimate_ \(\hat{\delta}(u,v):V\times V\rightarrow\mathbb{R}\) _is,_

1. _an_ \(\alpha\) **multiplicative approximation** _if_ \(\delta(u,v)\le\hat{\delta}(u,v)\le\alpha\delta(u,v)\) _for all_ \(u,v\in V\) _. This can also sometimes referred to as an_ \(\alpha\) **stretch approximation**.<tbc>

_2._ _a_ \(\beta\) **additive approximation** _if_ \(\delta(u,v)\le\hat{\delta}(u,v)\le\delta(u,v)+\beta\) _for all_ \(u,v\in V\) _. This can sometimes be denoted as a_ \(+\beta\) **approximation**.<tbc>

_3._ _an_ \((\alpha,\beta)\) **approximation** _if_ \(\delta(u,v)\le\hat{\delta}(u,v)\le\alpha\delta(u,v)+\beta\) _for all_ \(u,v\in V\) .

On an unweighted graph, let **BFS**(_G,w_) denote running breadth-first search on graph _G_ from root node _w_. When the graph _G_ does not need to be specified, this may also be denoted **BFS**(_w_). We also make use of a truncated **BFS**, which is an execution of **BFS** with bounded depth. A depth bounded **BFS** will be denoted **BFS**(_G,w,k_) for depth _k_ or **BFS**(_w,k_) when the graph _G_ is clear.

**Definition 2.2.** _Let G_=(_V,E_) _be an undirected, unweighted graph. A set of vertices D_ **dominates** \(U\subset V\) _if every_ \(u\in U\) _is either in D or has a neighbor in D._

_For a given vertex_ \(u\in U\)_, define the_ **representative of** _u_ **in** _D, denoted r(u,D), be an arbitrary vertex_ \(z\in D\cap N(u)\).

_For a given vertex_ \(z\in D\)_, define the_ **constituency of** _z_ **in** _U, denoted q(z,D), as the set_ \(\{u\in U\text{\textit{s.t.}}r(u,D)=z\}\).

**Definition 2.3.** _Let G_=(_V,E_) _be an undirected, unweighted graph. Let s be a degree threshold. Define_ \(V_s=\{v\in V\text{\textit{s.t.}}deg(v)\ge s\}\)_. Define_ \(E_s=\{(u,v)\in E\text{\textit{s.t.}}min(deg(u),deg(v))<s\}\).

**Lemma 2.4.** _Let U be a universe of n elements. Let_ F={_S_<sub>1</sub>_,...,S<sub>n</sub>_} _denote a collection of subsets_ \(S_i\subset U\) _such that_ \(|S_i|\ge s\) _for all i. Then, there is a deterministic algorithm **HittingSet** that computes a hitting set X of size_ \(O\left(\frac{nlogn}{s}\right)\) _of_ F _in time_ \(\tilde{O}(ns)\)_. There is also a randomized algorithm **rHittingSet** that with high probability computes a hitting set X of size_ \(O\left(\frac{nlogn}{s}\right)\) _of_ F _in time O(n)._

We note that we can easily verify that a randomly sampled set is indeed a hitting set in _O(ns_) time, by checking each set _S<sub>i</sub>_ for an element in _D_. For any vertex \(v\in V_s\), we may interpret _N(v_) as<tbc>

