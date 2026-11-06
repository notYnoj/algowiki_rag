## 1.1.1 Multiplicative Approximation on Unweighted Graphs (Section 3)

We significantly improve upon the current best known bound of \(\tilde{O}(n^{2.25})\) \[Rod23\] for a (2,0) approximation of unweighted APSP. Specifically, we obtain the following theorems. Theorem 3.1 is also obtained in a concurrent work by Dory, Forster, Kirkpatrick, Nazari, Vassilevska Williams, and de Vos \[DFK<sup>+</sup>23\].

**Theorem 3.1.** _Let G be an undirected, unweighted graph with n vertices. Algorithm 1 computes a_ (2,0)_-approximate APSP solution in expected time_ \(\tilde{O}\left(n^{2.03184039}\right)\).

**Theorem 3.3.** _Let G be an undirected, unweighted graph with n vertices. Algorithm 3 determinis tically computes a_ (2,0)_-approximate APSP solution in time_ \(\tilde{O}(n^{2.07203166})\).

Our results use FMM with the current best known bounds \[DWZ22, GU18\] and several new combinatorial insights to bring down the running time very close to _O(n_<sup>2</sup>). We also observe that a (7/3,0)-approximation on unweighted graphs can be computed in \(\tilde{O}(n^2)\) time (see Appendix D).

## 1.1.2 Multiplicative Approximations for Long Paths (Section 4)

We improve the bounds for a (2,0)-approximation on paths of length at least _k_, for all \(k\ge 4\) on dense graphs even just using combinatorial techniques and then further using algebraic methods. Combining with Roditty’s results \[Rod23\], these imply an improvement for all cases (sparse and dense) over Dor et al.’s result \[DHZ00\] for paths of length at least 4.

Below, we state the combinatorial results and the further improvements using FMM are stated in Section 5.

**Theorem 1.1** (Stated as Corollary E.11)**.** _Let_ \(k\ge 4\) _be an even integer. Then, we can compute a_ (2,0)_-approximation for distances_ \(\delta(u,v)\ge k\) _ combinatorially in expected time_

\(\tilde{O}\left(min\left(n^{2-\frac{2}{k+4}}m\frac{2}{k+4},n^{2+\frac{1}{2(k-1)}},n^{2+\frac{2}{3k+2}}\right)\right)\)

_In particular, we output_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all u,v and_ \(\hat{\delta}(u,v)\le 2\delta(u,v)\) _whenever_ \(\delta(u,v)\ge k\).

In contrast, Roditty achieves a bound of<tbc>

\(\tilde{O}\left(min\left(n^{2-\frac{2}{k+4}}m\frac{2}{k+4},n^{2+\frac{2}{3k-2}}\right)\right)\)

\begin{tabular}{cccc}
\multicolumn{4}{c}{(2,0)-Multiplicative Approximation for \(\delta(u,v)\ge k\)} \\
_k_ & \[DHZ00\], \[Rod23\] & Algorithm 4 (Combinatorial) & Algorithm 5 (uses FMM) \\
4 & _n_<sup>11/5</sup>=_n_<sup>2.200</sup> & _n_<sup>15/7</sup>=_n_<sup>2.1429</sup> (Algorithm 15) & _n_<sup>2.01973523</sup> \\
6 & _n_<sup>17/8</sup>=_n_<sup>2.125</sup> & _n_<sup>21/10</sup>=_n_<sup>2.1000</sup> & _n_<sup>2.01084688</sup> \\
8 & _n_<sup>23/11</sup>=_n_<sup>2.091</sup> & _n_<sup>29/14</sup>=_n_<sup>2.0715</sup> & _n_<sup>2.00745825</sup> \\
10 & _n_<sup>29/14</sup>=_n_<sup>2.072</sup> & _n_<sup>37/18</sup>=_n_<sup>2.0556</sup> & _n_<sup>2.00573823</sup> \\
12 & _n_<sup>35/17</sup>=_n_<sup>2.059</sup> & _n_<sup>45/22</sup>=_n_<sup>2.0455</sup> & _n_<sup>2.00462679</sup> \\
\end{tabular}

1: Improvements in computing (2,0)-approximate APSP for \(\delta(u,v)\ge k\) on undirected, unweighted graphs with _n_ vertices and _m_ edges. For _k_=4, Algorithm 15 is more efficient than Algorithm 4. While only a few examples are shown above, we obtain improvements for all _k_. See Proposition C.4 for the derivation of some running times for Algorithm 5.

