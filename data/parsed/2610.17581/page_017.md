_Proof._ We begin by noting that a graph contains a triangle if and only if it has a 3-subgraph with density 1: all triangle-free graphs satisfy \(\rho_{=3}^*(G)\le 2/3\). Thus, any better-than-1.5- approximation to D_k_S yields an algorithm for TriangleFreeness as well. We combine this fact with a lower bound on the problem’s communication complexity from Woodruff and Zhang.

**Proposition 8** (\[36, Corollary 10\])**.** TriangleFreeness has randomized communication complexity \(\Omega(n^2)\).

More specifically, the result states that if two parties know (disjoint) sets of edges _E_<sub>1</sub> and _E_<sub>2</sub> on a shared set of vertices _V_ , then they must communicate \(\Omega(n^2)\) bits of information in order to answer TriangleFreeness on the graph \(G=(V,E_1\cup E_2)\). Since a cut query on unweighted graphs can be communicated in _O_(log_n_) bits, Proposition 8 immediately yields the result.

This is a tight lower bound on the query complexity of D_k_S for randomized and even deterministic algorithms on unweighted graphs, as one can deterministically learn an unweighted graph using _O(n_<sup>2</sup>/log_n_) queries \[19\]. It also gives us a lower bound for randomized algorithms on weighted graphs, although the best upper bound we have is _O(n_<sup>2</sup>) queries to learn the graph.

The construction of Proposition 8 takes the problem DISJ_<sub>N</sub>(x,y_) for \(N=\Omega(n^2)\) and embeds each index \(i\in[N]\) into a distinct (but not fully disjoint) triangle, such that the graph contains a triangle if and only if _x_ and _y_ are not disjoint. In order to prove our randomized lower bounds for D_k_SH, we take this underlying idea from \[36\] and generalize it to hypergraphs, embedding each index into a distinct _k_-subhypergraph instead. The second half of our proof is to show that two parties can compute each of our hypergraph queries using only _O(r_log_n_) bits of communication.<sup>12</sup>

**Theorem 5.5.** The randomized query complexity of D_k_SH on rank-_r_ hypergraphs is at least \(\Omega(n\genfrac(){pt}{2}{n/2}{\lfloor(2r-1)/3\rfloor}/(r^2logn))\), for any combination of cut, add, and edge queries. If _r=O_(1), this yields a lower bound of \(\Omega(n^{\lfloor(2r+2)/3\rfloor}/logn)\) queries.

_Proof._ Reduction from DISJ_<sub>N</sub>(x,y_) on _N=ln/_4_s_ bits to Densest (_r+s_)-Subhypergraph on rank-_r_ hypergraphs with _n_ vertices, where _l_ and _s_ will be defined later. Let _H_ be a rank- _r_ multihypergraph with a set _U_ of _n/_2 vertices and two sets _A_ and _B_ of _n/_4 vertices each, which are both split into blocks of \(s=\lceil(r+1)/3\rceil\) vertices, yielding blocks _A_<sub>1</sub>_,...,A_<sub>_n/_4_s_</sub> and _B_<sub>1</sub>_,...B_<sub>_n/_4_s_</sub>. First, we add \(t=\genfrac(){pt}{2}{r}{r-s}-1\) copies of the hyperedge \(A_j\cup B_j\) to our hypergraph for each \(j\in[n/4s]\). Now, let \(l=\genfrac(){pt}{2}{n/2}{r-s}=\genfrac(){pt}{2}{n/2}{\lfloor(2r-1)/3\rfloor}\), and label the _l_ subsets of _U_ with cardinality _r-s_ as _U_<sub>1</sub>_,...,U<sub>l</sub>_. For every pair \(j\in[n/4s]\) and \(k\in[l]\), we take an index \(i_{j,k}\in[N]\). If _x_<sub>_i<sub>j,k</sub>_</sub>=1, we include hyperedge \(A_j\cup U_k\) in _H_. If _y_<sub>_i<sub>j,k</sub>_</sub>=1, we include hyperedge \(B_j\cup U_k\) in _H_.

If DISJ_<sub>N</sub>(x,y_) is False, i.e., _x_<sub>_i<sub>j,k</sub>_</sub>=_y_<sub>_i<sub>j,k</sub>_</sub>=1 for some index \(i_{j,k}\in[N]\), then the subhypergraph \(A_j\cup B_j\cup U_k\) has _t_+2 hyperedges. Otherwise, every (_r+s_)-subhypergraph has at most _t_+1 hyperedges, whether it is, without loss of generality:

• a set \(A_j\cup B_j\cup U_k\) for which _x_<sub>_i<sub>j,k</sub>_</sub>=1 and _y_<sub>_i<sub>j,k</sub>_</sub>=0,<tbc>

• or a set \(A_j\cup R\) for some \(R\subseteq U\) of cardinality _r_, for which every subset \(U_k\subseteq R\) satisfies _x_<sub>_i<sub>j,k</sub>_</sub>=1.

Note that our setting of _s_ gives 3_s\>r_, and so a subset \(A_j\cup B_j\cup A_{j^\prime}\cup B_{j^\prime}\) has more than _r+s_ vertices. Thus, we can reduce DISJ_<sub>N</sub>(x,y_) to determining whether the densest (_r+s_)- subhypergraph on _H_ has _t_+2 hyperedges.

Observe that our hypergraph has at most \(m\le n/4s\cdot(t+2l)=O(n/r\cdot(n/2)^{\lfloor(2r-1)/3\rfloor})=O(n^r)\) hyperedges. The two players of DISJ_<sub>N</sub>_ can therefore simulate cut and add queries with log_m=O(r_log_n_) bits of communication, by the additivity of these functions over partitions<tbc>

<sup>12</sup>While we omit is-edge<sup>?</sup> from the statements of our results, it is easy to see that this query requires only a single bit to be sent by each party.

