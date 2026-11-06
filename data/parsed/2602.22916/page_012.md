**Lemma 6** (Shortcuts in planar graphs \[8, 11\])**.** _Planar graphs admit construction of low-congestion shortcuts with parameters c,_ \(d=\tilde{O}(D)\) _within_ \(\tilde{O}(D)\) _deterministic rounds._

After constructing shortcuts for a given partition \(\{G_i\}_{i=1}^k\), the following task is solved deterministically in \(\tilde{O}(c+d)\) rounds \[8, 11\]:

**Lemma 7** (PA in planar graphs \[8, 11\])**.** _The PA problem can be solved in the given partition deterministically in_ \(\tilde{O}(D)\) _rounds on a planar graph G._

The PA problem is a very powerful building block that is used in many state-of-the-art algorithms. In our case, we will use the following procedure repeatedly.

**Lemma 8** (Lemma 16 of \[10\])**.** _Let T be a tree, and r be a vertex of T . There is a deterministic algorithm that roots T at r, and for each node_ \(u\in T\) _computes the subtree sum using_ \(\tilde{O}(1)\) _part-wise aggregations._

**Dual computations.** We will also perform computations related to faces of _G_ and to the dual tree _T_<sup>∗</sup>. To do that, we use procedures of \[9\] that rely on low-congestion shortcuts and PA on a related graph \(\hat{G}\), which can be fully simulated in CONGEST via _G_ with a constant overhead in the round complexity. See also Sections 3, 4 and appendix A of \[1\].

**Lemma 9** (Learn faces, Lemma 4 of \[9\])**.** _In_ \(\tilde{O}(D)\) _deterministic rounds, a vertex_ \(v\in G\) _learns the IDs of faces that contain it, and for each incident edge e, learns the IDs of its endpoints in G_<sup>∗</sup>.

**Lemma 10** (Aggregations on faces, Corollary 5 of \[9\])**.** _Assuming each vertex v has an input x<sub>v,f</sub> for each face f of G that it participates in. Then, in_ \(\tilde{O}(D)\) _deterministic rounds any aggregate operator_ \(\oplus\) _is computed over the input of vertices of each face f in G s.t. each vertex_ \(v\in f\) _learns_ \(\oplus_{u\in f}x_{u,f}\).

**Lemma 11** (Subtree sums on dual tree, Section 4.2.2 of \[9\])**.** _Let g be a face whose ID is known to all_ \(v\in G\)_, and let T_<sup>∗</sup> _be a spanning tree of the dual graph G_<sup>∗</sup>_, such that, each vertex_ \(v\in G\) _knows for each incident edge e whether it is in T_<sup>∗</sup>_, and v knows the two IDs of faces that e participates in. In addition, for each face f , there is an input value x<sub>f</sub> that is known to all of its vertices. Then, within_ \(\tilde{O}(D)\) _deterministic rounds, T_<sup>∗</sup> _is rooted in g and subtree sums are computed on T_<sup>∗</sup> _w.r.t. g as the root. I.e., each vertex v of a face f knows the ID of the parent of f in the rooted T_<sup>∗</sup>_, and v knows the subtree sum_ \(\sum_{f^\prime\in T_f^*}x_{f^\prime}\).

**Derandomized components.** Procedures that use \[9\] (like Lemma 9, Lemma 10, and Lemma 11) were originally randomized. However, they can be easily derandomized. In particular, those procedures use a classic randomized connectivity algorithm \[7\]. But, by \[1\] (footnote 20 in Appendix A), these procedures can be derandomized using a derandomization of \[10\] for the same connectivity algorithm. In more detail, the connectivity algorithm is Boruvka-like \[3\]. Initially, each vertex is its own component. Then, distinct components merge over incident edges in phases. In order to have only a small (polylogarithmic) number of phases, it is beneficial if the merges have a simple structure, like star-shape. One common way to achieve it is to use a fair coin flip. It is however well-known, as shown for example in \[10\], that this can be achieved deterministically using the classical Cole-Vishkin \[4\] coloring algorithm. In addition, traditional methods of aggregating information on the low-congestion shortcuts were originally randomized \[7\], but since then were derandomized \[8, 11\]. Those components are standard, and used in \[12\]’s deterministic separator algorithm as well.

## 5.2 The Algorithm

We now give a distributed deterministic implementation of Algorithm 1. Recall that Algorithm 1 mostly follows Ghaffari-Parter \[9\], the lines highlighted in blue in Algorithm 1 specify which components differ from Ghaffari-Parter. For each such component, we describe the intuition behind its implementation and provide a proof. Proof ideas are provided also for steps that we borrow from previous work (e.g. \[9\] or works on low-congestion shortcuts \[7, 8, 11\]) in Appendix A. The computational tasks we use are mainly the standard part-wise aggregation primitive.

