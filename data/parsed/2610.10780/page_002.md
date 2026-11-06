problem \[10\], segment intersection counting \[10\], computing closest points for segments \[6, 25\], computing many faces in line arrangement \[1, 4, 13, 14, 23, 26\], etc. If a similar lower bound could be established for distance selection, then the randomized algorithm of Chan and Zheng \[10\] would be optimal. On the deterministic side, however, the best known complexity remained _O(n_<sup>4/3</sup>log_n_) \[28\], leaving a logarithmic gap between deterministic and randomized algorithms.

### Our result.

In this paper, we close the gap between the best known deterministic and randomized complexities by presenting a deterministic _O(n_<sup>4/3</sup>)-time algorithm for distance selection.

We consider a more general bichromatic version of the problem. Let _A_ and _B_ be two sets of points in the plane with _m_=|_A_| and _n_=|_B_|, respectively. Let _S_ denote the set of all pairwise distances between points of _A_ and points of _B_. Given an integer _K_ with \(1\le K\le mn\), the goal is to compute the _K_-th smallest distance in _S_. The original monochromatic problem can be easily reduced to this bichromatic problem.

We first consider the symmetric case _m=n_. Previous work typically solved the bichromatic problem first (with the same time complexities as discussed above), with the monochromatic problem obtained as a consequence. We follow the same approach. Our main result is a deterministic _O(n_<sup>4/3</sup>)- time algorithm for the symmetric bichromatic distance selection problem.

We also study the asymmetric case \(m\neq n\). For this problem, the best previously known algorithm runs in _O_((_m_log_n+n_log_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>)log(_m+n_)) time \[28\]. By extending the framework developed for the symmetric case, we obtain a deterministic algorithm with running time _O(m_log<sup>2</sup>_n+n_log<sup>2</sup>_m+m_<sup>2/3</sup>_n_<sup>2/3</sup>). Note that if _m=O_(1), then the running time becomes _O(n_), matching the complexity of the classical linear-time selection algorithm. On the other hand, if _m=n_, then the bound becomes _O(n_<sup>4/3</sup>), matching the complexity of our symmetric case algorithm. Thus, the asymmetric bound naturally interpolates between linear time and the symmetric _O(n_<sup>4/3</sup>) time.

## 1.1 Our techniques

We give an overview of our algorithm on solving the symmetric case bichromatic problem.

Like the previous deterministic algorithms \[20, 28\], our algorithm follows a prune-and-search framework. Let \(\delta^*\) denote the sought _K_-th smallest distance in _S_. The algorithm maintains an interval _I_ containing \(\delta^*\). In each iteration, the goal is to shrink _I_ to a smaller interval \(I'\subseteq I\) such that \(\delta^*\in I'\) and \(|S\cap I'|\le\rho\cdot|S\cap I|\) for some constant \(\rho<1\). Repeating this process for _O_(log_n_) iterations reduces the number of candidate distances to a manageable size. To implement the framework efficiently, two bottlenecks must be overcome.

### Two bottlenecks.

The first is a _decision bottleneck_. Given a value \(\delta\), we need to determine whether \(\delta<\delta^*\). Observe that \(\delta<\delta^*\) if and only if \(K_\delta<K\), where \(K_\delta\) is the number of distances of _S_ at most \(\delta\). Hence, we need a _decision algorithm_ to compute \(K_\delta\).

The second is a _representation bottleneck_. Given an interval _I_, we need a compact representation of the distances in \(S\cap I\) so that we can select a small set of representative distances. These representative distances are then used to shrink _I_ to a smaller interval \(I'\). Conceptually, this step plays the role of a deterministic sampling procedure.

In the algorithm of Katz and Sharir \[20\], both bottlenecks were handled in _O(n_<sup>4/3</sup>log_n_) time, leading to an overall running time of _O(n_<sup>4/3</sup>log<sup>2</sup>_n_).

Wang and Zhao \[28\] improved the framework by using a recent counting algorithm of Wang \[24\], which computes \(K_\delta\) in _O(n_<sup>4/3</sup>) time for any given \(\delta\). This matches an \(\Omega(n^{4/3})\) lower bound in a restricted model \[10, 15\], and therefore essentially settles the decision bottleneck. To address the representation bottleneck, Wang and Zhao introduced a new partial biclique partition technique (called _partial batched range searching_ in \[28\]). Their technique produces a compact representation of most,<tbc>

