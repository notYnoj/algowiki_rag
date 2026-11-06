<tbc>Ashvinkumar _et al._ showing how the framework can be applied to the parallel and distributed models of computation \[ABC<sup>+</sup>23\].

## 1.2 Techniques

Our main contribution is a new recursive scaling algorithm called ScaleDown: see Section 4, including an overview in Section 4.1. In this subsection, we highlight other techniques that may be of independent interest.

**Low-Diameter Decomposition.** One of our key subroutines is an algorithm that decomposes any directed graph with _non-negative_ edge weights into strongly-connected components (SCCs) of small diameter. In particular, the algorithm computes a small set of edges _E<sup>rem</sup>_ such that all SCCs in the graph _G_\\_E<sup>rem</sup>_ have small weak diameter. Although the lemma below only applies to non-negative weights, we will show that it is in fact extremely useful for our problem.

**Lemma 1.2.** _There is an algorithm_ LowDiamDecomposition(_G,D_) _with the following guarantees:_

• _INPUT: an m-edge, n-vertex graph G_=(_V,E,w_) _with non-negative integer edge weight function w and a positive integer D._<tbc>

• _OUTPUT: A set of edges E<sup>rem</sup> with the following guarantees:_<tbc>

– _each SCC of G_\\_E<sup>rem</sup> has weak diameter at most D; that is, if u,v are in the same SCC, then_ \(\mathrm{dist}_G(u,v)\le D\) _and_ \(\mathrm{dist}_G(v,u)\le D\).<tbc>

**–** _For every_ \(e\in E\), \(\mathrm{Pr}[e\in E^{rem}]=O\left(\frac{w(e)\cdot\mathrm{log}^2n}{D}+n^{-10}\right)\)_. These probabilities are not guaranteed to be independent._<sup>6</sup><tbc>

• _RUNNING TIME: The algorithm has running time O(m_log<sup>2</sup>_n+n_log<sup>3</sup>_n)._

The decomposition above is similar to other low-diameter decompositions used in both undirected and directed graphs, though the precise guarantees vary a lot between papers \[Awe85, AGLP89, AP92, ABCP92, LS93, Bar96, BGK<sup>+</sup>14, MPX13, PRS<sup>+</sup>18, FG19, CZ20, BPW20, FGdV21\]. The closest similarity is to the algorithm Partition of Bernstein, Probst-Gutenberg, and Wulff- Nilsen \[BPW20\]. The main difference is that the algorithm of \[BPW20\] needed to work in a dynamic setting, and as a result their algorithm is too slow for our purposes. Our decomposition algorithm follows the general framework of \[BPW20\], but with several key differences to ensure faster running time; our algorithm is also simpler, since it only applies to the static setting. For the reader’s convenience, we present the entire algorithm from scratch in Section 6.

**No Negative-Weight Cycle Assumption via a Black-Box Reduction.** Although it is possible to prove Theorem 1.1 directly, the need to return the negative-weight cycle somewhat complicates the details. For this reason, we focus most of our paper on designing an algorithm that returns correct distances when the input graph contains no negative-weight cycle and guarantees nothing otherwise. See the description of subroutine SPmain in Theorem 3.4 as an example. We can focus on the above case because we have a black-box reduction from Theorem 1.1 to the above case that incurs an extra _O_(log<sup>2</sup>(_n_)) factor in the runtime. This reduction is essentially the same as the reduction from the minimum cost-to-profit ratio cycle problem to the negative cycle detection problem \[Law66, Law76\]. We include our reduction in Section C for completeness. Note that the more general cost-to-profit ratio cycle problem can be solved in near-linear time via a similar reduction \[Law66, Law76\].

<sup>6</sup>The 10 in the exponent suffices for our application but can be replaced by an arbitrarily large constant.

