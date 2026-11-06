**Theorem 6.** _Given a set A of m points and a set B of n points in the plane, and an integer K with_ \(1\le K\le mn\)_, one can compute the K-th smallest distance among all interpoint distances between A and B in O(n_log<sup>2</sup>_m+m_log<sup>2</sup>_n+m_<sup>2/3</sup>_n_<sup>2/3</sup>) _deterministic time._

Most of the techniques developed for the symmetric case continue to apply. We therefore only highlight the new ideas and refer to the previous sections whenever the analysis is identical. However, certain care must be taken in order to achieve the claimed complexity. We use the same notation as before, including _S_, D, \(\delta^*\), _K_, \(K_\delta\), and \(\kappa(I)\).

Without loss of generality, assume \(m\le n\). We distinguish two cases.

• If \(n\ge m^2\), we give an _O(n_log<sup>2</sup>_m_)-time algorithm.<tbc>

• If _n\<m_<sup>2</sup>, we give an algorithm running in _O(n_log<sup>2</sup>_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>) time.<tbc>

<tbc>Combining the two cases yields _O(n_log<sup>2</sup>_m+m_log<sup>2</sup>_n+m_<sup>2/3</sup>_n_<sup>2/3</sup>) time for arbitrary _m_ and _n_. We begin with the easier case \(n\ge m^2\).

## 6.1 The case \(n\ge m^2\)

Throughout this subsection, we assume \(n\ge m^2\).

We begin with the following exact counting lemma.

**Lemma 11.** _Suppose that_ \(n\ge m^2\)_. Given an interval I, one can compute_ \(\kappa(I)\) _in O(n_log_m_) _time._

_Proof._ Let D denote the set of annuli defined by the points of _A_ with respect to the interval _I_.

Construct a hierarchical (1_/r_)-cutting \(\{\Xi_0,\Xi_1,\dots,\Xi_k\}\) for D with _r=m_. The construction takes _O(mr_) time. Since _r=m_, we can assume that every cell of the last cutting \(\Xi_k\) has an empty conflict list. Consequently, no annulus of D has a boundary circle intersecting the interior of any cell of \(\Xi_k\).

For every cell \(\sigma\in\Xi_k\), compute \(B(\sigma)=B\cap\sigma\). This takes _O(n_log_r_) time over all cells.

Next, compute for every cell \(\sigma\in\Xi_k\) the number \(m_\sigma\) of annuli of D that completely contain \(\sigma\). As in Section 3.2, all values \(m_\sigma\) can be computed in _O(mr_) time.

Notice that

\(\kappa(I)=\sum_{\sigma\in\Xi_k}m_\sigma|B(\sigma)|.\)

Therefore, after computing \(m_\sigma\) and \(B(\sigma)\) for all cells \(\sigma\in\Xi_k\), \(\kappa(I)\) can be readily obtained. The total running time is _O(mr+n_log_r_), which is _O(n_log_m_) since _r=m_ and \(n\ge m^2\).

By Lemma 11, given any value \(\delta\), we can determine whether \(\delta<\delta^*\) in _O(n_log_m_) time.

We now describe the distance selection algorithm.

### Overview.

The algorithm maintains an interval _I_ containing \(\delta^*\). The distances in \(S\cap I\) are called the _candidate distances_. In each iteration, we shrink _I_ so that the number of candidate distances decreases by a constant factor. Initially, \(I=(0,+\infty)\), and therefore \(|S\cap I|=O(mn)\). After _O_(log_m_) iterations, each taking _O(n_log_m_) time, we obtain an interval _I_ satisfying \(|S\cap I|=O(n)\) and containing \(\delta^*\). The total time of all iterations is thus _O(n_log<sup>2</sup>_m_). Finally, we apply a distance-reporting step that enumerates all distances in \(S\cap I\) and computes \(\delta^*\) in additional _O(n_log_m_) time.

