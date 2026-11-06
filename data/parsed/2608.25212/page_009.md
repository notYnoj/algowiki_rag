**Lemma 11** (Lemma 18 of \[12\], Lemma 3.1 of \[11\])**.** _There is an_ O(_dn+m)-time algorithm that, given an sd-degeneracy sequence of an n-vertex m-edge graph G of width d, outputs a signed tree model of G with_ O(_dn_) _transversal pairs._

Assume that the graph _G_ comes with a total ordering of its vertices; for convenience, assume that the vertex set of _G_ is \[_n_\], ordered naturally. We then define the _interval biclique partition_ of _G_ as the partitioning of the edge set of _G_ into bicliques, where each side of each biclique is an integer subinterval of \[_n_\]. The following lemma implies that a small-size signed tree model can be efficiently turned into a small-size interval biclique partition.

**Lemma 12** (Item 1 of Theorem 1 of \[12\])**.** _There is an_ O(_p_log_n)-time algorithm that, given a signed tree model of an n-vertex graph G with p transversal pairs, outputs an interval biclique partition of G with_ O(_p_) _bicliques._

We will rely on the following consequence of Lemmas 11 and 12.

**Lemma 13.** _There is an_ O(_dn_log_n+m)-time algorithm that, given an sd-degeneracy sequence of an n-vertex m-edge graph G of width d, outputs an interval biclique partition of G with_ O(_dn_) _bicliques._

### 2.4 Matrix multiplication

An interval biclique partition with O(_n_) bicliques of an _n_-vertex graph _G_ allows one to multiply any adjacency matrix of _G_ with any _n_-vector in O(_n_) time. More precisely:

**Lemma 14** (Theorem 33 in \[12\])**.** _For every abelian group_ A_, there exists an algorithm that takes on input an interval biclique partition with b bicliques of an n-vertex graph G with adjacency matrix M and an n-vector_ \(X\in\mathcal{A}^n\) _and computes the product MX, in time_ O(_n+b_) _and_ O(_n+b_) _group operations._

Note that, as the adjacency matrix _M_ is a {0,1}-matrix, the multiplication of _M_ with a vector of group elements is well-defined. This lemma has a short proof that encodes _M_ into an \(n\times n\left\{-1,0,1\right\}\)- matrix with O(_b_) nonzero entries. As a direct consequence of Lemma 14, one can multiply _M_ with any \(n\times n\) matrix in time O(_n(n+b_)) (assuming the group operations take constant time).

## 3 Finding an sd-degeneracy sequence deterministically

In this section, we provide an algorithm that computes an sd-degeneracy sequence of constant width in graphs of bounded versatile symmetric difference. The algorithm is time-optimal for dense graphs (i.e., _n_-vertex graphs with \(\Theta(n^2)\) edges). More generally, the algorithm computes an sd-degeneracy sequence of width \(\mathcal{O}(n^\alpha)\) in graphs of versatile symmetric difference of exponent \(\alpha\).

It uses classic data structures for strings. Given a word _w_ of finite length _s_, a longest common extension (LCE) query \(i,j\in[s]\) asks for the largest integer _k_ such that \(w[i]w[i+1]\cdots w[i+k-1]=w[j]w[j+1]\cdots w[j+k-1]\).

**Theorem 15** (Section 4 of \[39\])**.** _Fix a finite alphabet_ \(\Sigma\)_. There is an_ O(_s)-time algorithm, that given a word w of length s over_ \(\Sigma\)_, builds a data structure that answers each LCE query on w in constant time._

