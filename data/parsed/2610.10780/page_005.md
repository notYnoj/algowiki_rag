point \(a\in A_t\) and a point \(b\in B_t\), we call (_a,b_) a _point pair_ (or simply a _pair_) of the biclique. Two bicliques \(A_t\times B_t\) and \(A_{t^\prime}\times B_{t^\prime}\) are _edge-disjoint_ if they do not contain the same point pair.

## 2.1 Partial biclique partitions

The main tool used throughout the paper is a partial biclique partition used by Wang and Zhao \[28\] (called _partial batched range searching_ in \[28\]). Since both the approximate counting algorithm and the distance representation theorem rely heavily on this construction, we review it and derive the recurrence relations that will be used later.

Let \(I=(\alpha,\beta]\) be an interval. For every point \(a\in A\), define _D<sub>a</sub>(I_) to be the annulus centered at _a_ with inner radius \(\alpha\) and outer radius \(\beta\). When the interval _I_ is clear from the context, we simply write _D<sub>a</sub>_. We assume that the outer boundary belongs to _D<sub>a</sub>_ while the inner boundary does not. Hence, for any point \(b\in B\), \(b\in D_a\) if and only if \(\|ab\|\in(\alpha,\beta]\).

Let \(\mathcal{D}=\{D_a|a\in A\}\) be the set of all annuli centered at the points of _A_.

The purpose of a partial biclique partition is to represent all point pairs whose distances lie in a given interval by a small collection of bicliques while allowing a controlled collection of unresolved pairs.

**Definition 2** (Partial Biclique Partition)**.** _Given an interval I, a_ partial biclique partition _for A and B consists of two collections of edge-disjoint bicliques_ \(\Gamma=\{A_t\times B_t|A_t\subseteq A,B_t\subseteq B\}\) _and_ \(\Pi=\{A'_s\times B'_s|A'_s\subseteq A,B'_s\subseteq B\}\) _such that the following conditions hold._

1. _For every pair_ \((a,b)\in A_t\times B_t\in\Gamma\), \(\|ab\|\in I\).<tbc>

_2._ _For every pair of points_ \(a\in A\) _and_ \(b\in B\) _with_ \(\|ab\|\in I\)_, there exists a biclique in either_ \(\Gamma\) _or_ \(\Pi\) _that contains_ (_a,b)._

In other words, the two collections \(\Gamma\) and \(\Pi\) together record all pairs (_a,b_) with distance in _I_. Every pair recorded in a biclique of \(\Gamma\) is guaranteed to have distance in _I_, while this may not be true for the pairs recorded in \(\Pi\). For this reason, we call the pairs recorded in \(\Pi\) _uncertain pairs_, and the pairs recorded in \(\Gamma\) _certified pairs_.

The following lemma is a useful tool inherited from \[28\].

**Lemma 1** (Lemma 1 of \[28\])**.** _Let m_=|_A_| _and n_=|_B|. For any parameter_ \(1\le r\le min\{m^{1/3},n^{1/3}\}\)_, one can compute a partial biclique partition for A and B with collections_ \(\Gamma\) _and_ \(\Pi\) _in O(mr_log_r+nr_) _time such that:_

1. \(\sum_t(|A_t|+|B_t|)=O(mrlogr+nr)\).<tbc>

_2._ _For every biclique_ \(A'_s\times B'_s\in\Pi\), \(|A'_s|\le m/r^3\) _and_ \(|B'_s|\le n/r^3\).<tbc>

_3._ _The total number of uncertain pairs recorded in_ \(\Pi\) _is O(mn/r_<sup>2</sup>).

We briefly review the algorithm of Lemma 1, since it will be used repeatedly throughout the paper. Several concepts and notation introduced here will also be needed later.

### Cuttings.

Recall that D consists of _m_ annuli centered at the points of _A_, each bounded by two circles. For any compact region \(\sigma\) in the plane, let \(\mathcal{D}_\sigma\subseteq\mathcal{D}\) denote the subset of annuli whose bounding circles cross the relative interior of \(\sigma\).

For a parameter _r_ with \(1\le r\le m\), a (1_/r_)_-cutting_ for D is a collection \(\Xi\) of constant-complexity cells with pairwise disjoint interiors whose union covers the entire plane such that \(|\mathcal{D}_\sigma|\le m/r\) for every cell \(\sigma\in\Xi\). The set \(\mathcal{D}_\sigma\) is often called the _conflict list_ of \(\sigma\). The _size_ of \(\Xi\) is the number of its cells.

