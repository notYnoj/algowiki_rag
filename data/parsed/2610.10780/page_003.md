but not all, distances in \(S\cap I\), while keeping the representation error sufficiently small for the prune- and-search framework to remain correct. As a result, each iteration runs in _O(n_<sup>4/3</sup>) time and the overall running time becomes _O(n_<sup>4/3</sup>log_n_).

## Our solution to the bottlenecks.

To obtain an _O(n_<sup>4/3</sup>)-time algorithm, we address the two bottlenecks in different ways.

For the decision bottleneck, the lower bound for exact counting essentially blocks any further improvement. Since a prune-and-search algorithm requires _O_(log_n_) iterations and each iteration appears to require at least one decision query, it is difficult to avoid the _O(n_<sup>4/3</sup>log_n_) barrier using exact counting. In contrast, the randomized algorithm of Chan and Zheng \[10\] uses random sampling and therefore needs only _O_(1) counting queries, leading to an _O(n_<sup>4/3</sup>) expected-time algorithm.

The key observation behind our deterministic algorithm is that the prune-and-search framework does not require the exact number of distances in \([0,\delta]\). An approximation is sufficient, provided that the approximation error is carefully controlled. We prove a new _approximate counting theorem_ (Theorem 1) that computes an approximate count for \(K_\delta\) in _o(n_<sup>4/3</sup>) time. Moreover, the running time decreases as the allowed error increases. The theorem immediately yields a _quasi-decision_ procedure (Theorem 2), which replaces the exact decision algorithm of Wang \[24\], and the procedure runs in _o(n_<sup>4/3</sup>) time. This does not contradict the \(\Omega(n^2)\) lower bound for exact counting, because the quasi- decision procedure is allowed to return "unsure" when the threshold is too close to the true count.

For the representation bottleneck, we further enhance the partial biclique partition technique of Wang and Zhao \[28\] and make it significantly more efficient. Two new ingredients are introduced. First, we use the \(\Gamma\)-framework of Chan and Zheng \[10\] to accelerate point location operations once the subproblem sizes become sufficiently small. Second, we introduce a new notion called _capture cells_ in hierarchical cuttings. Capture cells allow us to represent only a carefully selected subset of the distances while still guaranteeing that a constant fraction of all relevant distances are recorded. The idea of using capture cells is crucial to the success of our approach and is one of the most interesting components of this paper. This leads to a new _distance representation theorem_ (Theorem 3) that runs in _o(n_<sup>4/3</sup>) time.

## Putting the pieces together.

For a positive integer _i_, let log<sup>(_i_)</sup>_n_ denote the _i_-fold iterated logarithm of _n_, i.e., log<sup>(1)</sup>_n_=log_n_, and log<sup>(_i_)</sup>_n_=log(log<sup>(_i_-1)</sup>_n_) for \(i\ge 2\).

Our algorithm proceeds in _O_(log<sup>∗</sup>_n_) phases and maintains an interval _I_ containing \(\delta^*\). For _i_=1,2_,...,O_(log<sup>∗</sup>_n_), the goal of the _i_-th phase is to transform an interval _I_ satisfying<tbc>

\(|S\cap I|=O\big(n^{4/3}(log^{(i-1)}n)^4\big)\)

<tbc>(and _O(n_<sup>2</sup>) when _i_=1) into a smaller interval \(I'\subseteq I\) satisfying

\(|S\cap I'|=O\big(n^{4/3}(log^{(i)}n)^4\big),\)

while maintaining \(\delta^*\in I'\). Initially _i_=1 and \(I=(0,+\infty)\), and hence \(|S\cap I|=O(n^2)\).

The _i_-th phase consists of _O_(log<sup>(_i_)</sup>_n_) iterations. Each iteration, which reduces the remaining candidate distances by a constant fraction, takes _O(n_<sup>4/3</sup>/log<sup>(_i_)</sup>_n_) time for _i_=1,2, and _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>) time for \(i\ge 3\). Consequently, the first two phases each require _O(n_<sup>4/3</sup>) time, while the total time of all remaining phases is

\(O\left(n^{4/3}\sum_{i=3}^{O(log^*n)}\frac{1}{log^{(i)}n}\right)=O(n^{4/3}).\)

After _O_(log<sup>∗</sup>_n_) phases, we obtain an interval _I_ satisfying \(|S\cap I|=O(n^{4/3})\) and containing \(\delta^*\). A final enumeration step then computes \(\delta^*\) from \(S\cap I\) in additional _O(n_<sup>4/3</sup>) time. To achieve this,<tbc>

