Next, for each point \(b\in B'\), we determine the cell of \(\Xi_k\) containing _b_. Using the \(\Gamma\)-algorithm framework \[10\], as discussed in Section 3.2, this can be done in \(O(n')\) amortized time for all points \(b\in B'\).

For each cell \(\sigma\in\Xi_k\), let \(B_t=B'(\sigma)\), and let _A<sub>t</sub>_ be the union of all canonical subsets \(A'_{\sigma^\prime}\) over the ancestors \(\sigma'\) of \(\sigma\). We add the biclique \(A_t\times B_t\) to \(\Gamma\). We define A_<sub>t</sub>_ to be the collection of all nonempty canonical subsets \(A'_{\sigma^\prime}\) corresponding to ancestors \(\sigma'\) of \(\sigma\). By following the ancestor links, the elements of A_<sub>t</sub>_ can be accessed one at a time in _O_(1) time per element. Since the height of the cutting tree is \(O(logr')\), we have \(|\mathcal{A}_t|=O(logr')\). Further, since \(r'=m'\le q^{1/3}\) and _q=O_(log<sup>6</sup>log_n_), it follows that |A_<sub>t</sub>_|=_O_(loglog_n_).

The bicliques generated above for the cells \(\sigma\) of \(\Xi_k\) form a full biclique partition for all distances between points of \(A'\) and points of \(B'\). Therefore, the total running time for the subproblem \(T(m',n')\) is \(O(m'r'+n')\). Since \(r'=m'\), \(m'\le q^{1/3}\), and \(n'\le q^{2/3}\), we have

\(T(m',n')=O(m'^2+n')=O(q^{2/3}).\)

Substituting this bound into (10) yields _T(q,q_)=_O(q_<sup>4/3</sup>). Finally, substituting this bound into Recurrence (5) gives _T(n,n_)=_O(n_<sup>4/3</sup>), which proves Theorem 4.

**Corollary 2.** _Given an interval I, one can explicitly enumerate all distances in_ \(S\cap I\) _in_ \(O(n^{4/3}+|S\cap I|)\) _time._

_Proof._ Apply Theorem 4. For each biclique \(A_t\times B_t\in\Gamma\), we first enumerate the points of _A<sub>t</sub>_ in _O_(|_A<sub>t</sub>_|) time using its implicit representation. Then, for every \(a\in A_t\) and \(b\in B_t\), we output the distance \(\|ab\|\). By Theorem 4,

\(\sum_{A_t\times B_t\in\Gamma}|B_t|=O(n^{4/3})\text{and}\sum_{A_s^\prime\in\mathcal{A}}|A'_s|=O(n^{4/3}).\)

Hence the total overhead for recovering all sets _A<sub>t</sub>_ is _O(n_<sup>4/3</sup>), while the time spent outputting distances is proportional to the number of distances reported, namely \(|S\cap I|\). Therefore, the overall running time is \(O(n^{4/3}+|S\cap I|)\).

By Corollary 2, our original problem of enumerating all distances of \(S\cap I\) can be solved in _O(n_<sup>4/3</sup>) time, since \(|S\cap I|=O(n^{4/3})\).

### Wrapping things up.

We have shown that \(\delta^*\) can be computed in _O(n_<sup>4/3</sup>) deterministic time. Note that the algorithm of Corollary 2 can also report, together with each distance, the corresponding pair of points that realizes it. Therefore, a point pair whose distance is equal to \(\delta^*\) can be reported within the same time bound.

The following theorem summarizes our main result.

**Theorem 5.** _Given two sets A and B, each consisting of n points in the plane, and an integer K with_ \(1\le K\le n^2\)_, one can compute the K-th smallest distance among all interpoint distances between A and B in O(n_<sup>4/3</sup>) _deterministic time._

## 6 The asymmetric case

In this section, we consider the asymmetric version of the distance selection problem, where the sizes of the two point sets are not necessarily equal. Let _m_=|_A_| and _n_=|_B_|.

Our main result is the following.

