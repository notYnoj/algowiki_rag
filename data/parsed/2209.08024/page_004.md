(_ii)_ _There is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>), where w<sub>n</sub> is the uniform distribution on V_(T_<sub>n</sub>), and for every centroid tree C<sub>n</sub> of_ (T_<sub>n</sub>,w<sub>n</sub>_)<tbc>

<tbc>\(lim_{n\rightarrow\infty}\frac{\mathtt{cost}_{w_n}(C_n)}{\mathtt{OPT}(\mathcal{T}_n,w_n)}=2.\)<tbc>

<tbc>_In both cases_ \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\).

Note that the fact that \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\) in Theorem 1.2 establishes that the _asymptotic_ approximation ratio is 2. By this we mean that every bound of the form \(\mathtt{cent}\le c\cdot\mathtt{OPT}+o(\mathtt{OPT})\) must have \(c\ge 2\).

We next show a stronger guarantee when the underlying tree has bounded degree.

**Theorem 1.3.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, and let_ \(\Delta\) _be the_ maximum degree _of_ T_. Then_

\(\mathtt{cent}(\mathcal{T},w)\le\left(2-\frac{1}{2^\Delta}\right)\cdot\mathtt{OPT}(\mathcal{T},w).\)

We complement this result by two lower bounds. The first establishes the tightness of the approximation ratio. The second shows a (slightly smaller) lower bound on the approximation ratio for instances where `OPT` is unbounded.

**Theorem 1.4.** _Let_ \(\Delta\ge 3\) _be integer._

(_i)_ _There is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>_) _such that_ T_<sub>n</sub> has maximum degree at most_ \(\Delta\)_, and for every centroid tree C<sub>n</sub> of_ (T_<sub>n</sub>,w<sub>n</sub>_)<tbc>

<tbc>\(lim_{n\rightarrow\infty}\frac{\mathtt{cost}_{w_n}(C_n)}{\mathtt{OPT}(\mathcal{T}_n,w_n)}=2-\frac{1}{2^\Delta}.\)<tbc>

_(ii)_ _There is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>_) _such that_ T_<sub>n</sub> has maximum degree at most_ \(\Delta\), \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\)_, w<sub>n</sub>_(T_<sub>n</sub>_)=1_, and for every centroid tree C<sub>n</sub> of_ (T_<sub>n</sub>,w<sub>n</sub>_)

<tbc>\(\mathtt{cost}_{w_n}(C_n)\ge\left(2-\frac{4}{2^\Delta}\right)\cdot\mathtt{OPT}(\mathcal{T}_n,w_n)-1.\)

We remark that Theorem 1.4(i) does not exclude the possibility of a bound of the form \(\mathtt{cent}\le c\cdot\mathtt{OPT}+o(\mathtt{OPT})\), where \(c<2-\frac{1}{2^\Delta}\), as here `OPT`(T_<sub>n</sub>,w<sub>n</sub>_) is bounded. Part (ii), however, establishes that a bound of the form \(\mathtt{cent}\le c\cdot\mathtt{OPT}+o(\mathtt{OPT})\) must have \(c\ge 2-\frac{4}{2^\Delta}\). We leave open the problem of closing the gap in the asymptotic approximation ratio in terms of \(\Delta\).

## Computing centroid trees.

On the algorithmic side, we show that the weighted centroid tree can be computed in O(_n_log_n_) time. Previously, the fastest known constant-approximation algorithm \[BK22\] took O(_n_<sup>3</sup>) time (similarly achieving an approximation ratio of 2). The main step of our algorithm, finding the weighted centroid of a tree, is achievable in O(log_n_) time, assuming that the underlying tree is stored in a _top tree_ data structure \[AHLT05\]. Iterating this procedure in combination with known algorithms for _constructing_ and _splitting_ top trees yields the algorithm that runs in O(_n_log_n_) time. We also develop an improved, _output-sensitive_ algorithm, with running time O(_n_log_h_), where _h_ is the height of the resulting centroid tree, yielding a running time O(_n_loglog_n_) in the typical case when the height is O(log_n_).

**Theorem 1.5.** _Let_ T _be a tree on n vertices and w be a weight function. We can compute a centroid tree of_ (T_,w_) _in time_ O(_n_log_h), where h is the height of the computed centroid tree._

One may ask whether the weighted centroid tree can be computed in linear time, similarly to the unweighted centroid tree, or to the weighted centroid BST. We show that, assuming a general decision tree model of computation, this is not possible, and the algorithm of Theorem 1.5 is optimal for all _n_ and _h_ (up to<tbc>

