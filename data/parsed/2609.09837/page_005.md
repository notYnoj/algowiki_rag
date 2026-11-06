# The Parameterized Complexity of Coloring Discovery

5

union of paths. For a connected graph _G_, its diameter is the largest distance between two vertices and its radius is the minimum, over all vertices, of the largest distance to another vertex. The domination number is the minimum size of a set of vertices whose closed neighborhoods cover _V(G_).

We use standard notions from parameterized complexity. A parameterized reduction maps an instance (I_,k_) in time _f(k_)|I|<sup>O(1)</sup> to an equivalent instance \((\mathcal{I}',k')\) such that \(k'\le g(k)\) for some computable functions _f_ and _g_. For integer programming, we use Lenstra’s theorem: an integer linear program (ILP) with _p_ integer variables and binary encoding length _L_ can be solved in _f(p)L_<sup>O(1)</sup> time \[26\].

We will use the following reachability statement between colorings. The componentwise reachability criterion for slides is standard in Colored Token Swapping \[34, discussion preceding Lemma 1\]. The arbitrary-swap criterion is its complete-graph special case. The diameter-dependent bound follows from a classical bound for transposition graphs \[29, Theorem 1.4.12\].

**Lemma 1.** _Let_ \(\varphi,\psi:V(G)\rightarrow[q]\) _be colorings of an n-vertex graph._

1. _The coloring_ \(\psi\) _is reachable from_ \(\varphi\) _by swaps if and only if_ \(|\varphi^{-1}(c)|=|\psi^{-1}(c)|\) _for every_ \(c\in[q]\)_. If it is reachable, n_-1 _swaps suffice._<tbc>

_2._ _The coloring_ \(\psi\) _is reachable from_ \(\varphi\) _by slides if and only if these equalities hold separately in every connected component. If they hold, at most_ \(\sum_K(|V(K)|-1)(2diam(K)-1)\) _slides suffice, where isolated components contribute zero._

An equitable _q_-coloring is a proper coloring whose color-class sizes differ by at most one \[28\]. If _n=aq+r_ with \(0\le r<q\), exactly _r_ classes have size _a_+1 and _q-r_ classes have size _a_. We use the known W\[1\]-hardness of Equitable Coloring parameterized by _q_+ddp(_G_) \[19\]. Gomes et al. also prove hardness on interval graphs when _q_, treewidth, and maximum degree are taken together as the parameter \[20\]. Ordering an interval representation by nondecreasing left endpoint gives bandwidth at most the maximum degree: if _uv_ is an edge with the left endpoint of _u_ first, every interval ordered between _u_ and _v_ intersects _u_. Hence Equitable Coloring is W\[1\]-hard for _q_+bw(_G_) as well.

### 3 Algorithms

#### 3.1 Color flipping

For flips, color names that do not occur initially are interchangeable and we may assume \(q\le n\). Further details are provided in Appendix A.1.

**Theorem 1.** _Let k_=vc(_G). In_ 2<sup>O(_k_log_k_)</sup>(_n+m_) _time, one can compute the minimum number of flips needed to reach a proper coloring, or determine that no proper q-coloring exists. In particular,_ Flip-CD _is fixed-parameter tractable parameterized by_ vc(_G)._

