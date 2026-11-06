<tbc>(resp. \(+\infty\)) element such that \(-\infty<x\) and \(-\infty<x\) in every observed comparison (resp. \(+\infty>x\) and \(+\infty>x\)).

## 4.3 Random Walks on Noisy Binary Search Trees

To compute an approximate rank \(\tau_x\) for the query element _x_, our algorithm will perform a discrete- time random walk on each of _T_<sub>0</sub> and _T_<sub>1</sub>. These random walks rely on a _test_ operation defined as follows:

_Definition 4.1 (test operation)._ A _test_ of element _x_ with a vertex _u_ is performed by (i) comparing _x_ with the elements _s<sub>L(u)</sub>,s<sub>L(u)-1</sub>,...,s<sub>L(u)-k+1</sub>, (ii) comparing _x_ with the elements _s<sub>R(u)</sub>,s<sub>R(u)+1</sub>,s<sub>R(u)+k-1</sub>, (iii) decrementing _L(u_) by _k_, and finally (iv) incrementing _R(u_) by _k_. Vertex _u passes_ the test if the majority result among the comparisons performed in step (i) reports _x_ as the larger element, and the majority result among the comparisons performed in step (ii) reports _x_ as the smaller element. Otherwise, _u fails_ the test.

For a fixed \(j\in\{0,1\}\), the random walk on _T<sub>j</sub>_ proceeds as follows. At time 0, i.e., before the first step, the _current_ vertex _v_ coincides with the root _r_ of _T<sub>j</sub>_. Then, at each time step, _x_ is tested with all the children of the current vertex _v_, and we _walk_ from _v_ to the next vertex (possibly _v_ itself) according to the following rules:

\(\bullet\) If _exactly one_ child _u_ of _v passes_ the test, we walk from _v_ to _u_.<tbc>

\(\bullet\) If _all_ the children of _v fail_ the test, we walk from _v_ to its parent, if _v_’s parent exists (if the parent of _v_ does not exist, then _v=r_, and we walk to _r_ itself);<tbc>

\(\bullet\) If _more than one_ child of _v passes_ the test, we walk from _v_ to itself.

Fix an upper bound \(\rho=120\lceil lnm\rceil\) on the total number of steps. The walk stops as soon as one of the following two conditions is met:

**Success:** The current vertex _v_ is a leaf of _T<sub>j</sub>_, in which case we say that the random walk returns _v_;

**Timeout:** The \(\rho\)-th time step is completed and the success condition is not met.

## 4.4 Analysis

We now analyze the behavior of our random walks and establish the main result of this section. The key ingredient of the analysis is to show that one of the two random walks, i.e., the one whose noisy binary search tree contains the leaf that corresponds to the true rank of _x_ in _S_, is likely to succeed, and that any walk that succeeds returns either such a leaf, or a nearby one.

Let \(i^*=rank(x,S\cup\{x\})=rank(_x,S_), let _T_<sup>∗</sup> be the unique tree in {_T_<sub>0</sub>_,T_<sub>1</sub>} such that _i_<sup>∗</sup> belongs to the interval of a leaf in _T_<sup>∗</sup>, and let \(T'\) be the other tree.

_Definition 4.2 (good/bad vertex)._ A vertex _v_ of _T_<sup>∗</sup> is _good_ if \(i^*\in I(v)\), it is _bad_ if either _i_<sup>∗</sup>_\<_min_I(v_)-_cd_ or _i_<sup>∗</sup>_\>_max_I(v_)+_cd_, and it is _neutral_ if it is neither good nor bad.

Notice that all the vertices in _T_<sup>∗</sup> are either good or bad, that the intervals corresponding to the vertices in _T_<sup>∗</sup> at the same depth are pairwise disjoint, and that the set of good vertices in _T_<sup>∗</sup> is exactly a root-to-leaf path in _T_<sup>∗</sup>. Furthermore, all path-vertices of \(T'\) are either bad or neutral. Moreover, in both \(T'\) and _T_<sup>∗</sup>, all the children of a bad vertex are also bad. The following two lemmas provide bounds on the probability that a good/bad vertex passes a test.

Lemma 4.3. _Consider a test performed on a good vertex u. The probability that u fails the test is at most_ \(\frac{2}{50}\) .

Proof. For _i_=0_,...,k_-1, let _X<sub>i</sub>_ (resp. _Y<sub>i</sub>_) be an indicator random variable that is 1 iff the comparison between _x_ and _s<sub>L(u)-i</sub>_ reports _x_ as the larger element (resp. the comparison between _x_<tbc>

