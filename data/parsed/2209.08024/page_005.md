a constant factor). Our lower bound on the running time applies, informally, to any deterministic algorithm in which the input weights affect program flow only in the form of binary decisions, involving arbitrary computable functions. The model thus excludes using the weights for addressing memory, e.g., via hashing.

More precisely, consider a tree T on _n_ vertices. We say that a _binary decision tree D_<sub>T</sub> _solves_ T for a class of weight functions W mapping _V_(T) to \(\mathbb{R}_{\ge 0}\), if the leaves of _D_<sub>T</sub> are search trees on T , every branching of _D_<sub>T</sub> is of the form "\(f(w)\ge 0\)?" for some computable function \(f:\mathcal{W}\rightarrow\{-1,+1\}\), and for every weight function \(w\in\mathcal{W}\), starting from the root of _D_<sub>T</sub> and following branchings down the tree, we reach a leaf _T_ of _D_<sub>T</sub> that is a valid centroid tree for (T_,w_). The height of _D_<sub>T</sub> is then a lower bound on the worst-case running time.

**Theorem 1.6.** _Let_ \(h\ge 3\) _and_ \(n\ge h+1\) _be integers. Then there is a tree_ T _on at most n vertices and a class_ W _of weight functions on V_(T) _such that for every_ \(w\in\mathcal{W}\)_, every centroid tree of_ (T_,w_) _has height h, and every binary decision tree that solves_ T _for_ W _has height_ \(\Omega(nlogh)\).

We can nonetheless improve the running time, when the weights are restricted in certain (natural) ways. We define the _spread_ \(\sigma\) of a weight function _w_ as the ratio between the total weight _w_(T), and the smallest _non-zero_ weight of a vertex. As we show, \(\mathcal{O}(nlogh)\subseteq\mathcal{O}(nloglog\left(\sigma+n\right))\) and therefore, when \(\sigma\in n^{\mathcal{O}(1)}\) (for instance, if the weights are integers stored in RAM words), we obtain a running time of O(_n_loglog_n_).

When many vertices have zero weight, we obtain further improvements, e.g., if only O(_n/_log_n_) of the weights are non-zero, we can compute a centroid tree in O(_n_) time, even if the height _h_ is large. We defer the precise statement of these refined bounds and the discussion of their optimality to Section 5.

## Approximate centroid trees.

Finally, we consider the approximation guarantees of a generalized form of centroid trees. Let us call a vertex _v_ of a tree T an \(\alpha\)-centroid, for \(0\le\alpha\le 1\), if \(w(\mathcal{H})\le\alpha\cdot w(\mathcal{T})\), for all components H of T-_v_. An \(\alpha\)-centroid tree is an STT in which every vertex _x_ is an \(\alpha\)-centroid of its subtree T\[_V(T<sub>x</sub>_)\].

Observe that the standard centroid tree is a \(\frac{1}{2}\)-centroid tree, and all STTs are 1-centroid trees. Also note that an \(\alpha\)-centroid is a \(\beta\)-centroid for all \(\beta\ge\alpha\) and that the existence of an \(\alpha\)-centroid is not guaranteed for \(\alpha<\frac{1}{2}\) (consider a single edge with the two endpoints having the same weight). On the other hand, an \(\alpha\)-centroid for \(\alpha<\frac{1}{2}\), if it exists, is unique, and therefore the \(\alpha\)-centroid tree is also unique. To see this, consider an \(\alpha\)-centroid _c_ that splits T into components T<sub>1</sub>_,...,_T_<sub>k</sub>_. If an alternative \(\alpha\)-centroid \(c'\) were in component T_<sub>i</sub>_, then its removal would yield a component containing all vertices in T-_V_(T_<sub>i</sub>_), of weight at least \((1-\alpha)\cdot w(\mathcal{T})>\alpha\cdot w(\mathcal{T})\).

Denote by \(\mathtt{cent}^\alpha(\mathcal{T},w)\) the maximum cost of an \(\alpha\)-centroid tree of (T_,w_), or 0 if no \(\alpha\)-centroid tree exists. We refine our guarantee from Theorem 1.1 to approximate centroid trees:

**Theorem 1.7.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, m=w_(T)_. We have_

\((i)\mathtt{cent}^\alpha(\mathcal{T},w)\le\frac{1}{1-\alpha}\cdot\mathtt{OPT}(\mathcal{T},w)-\frac{\alpha}{1-\alpha}m,\text{\textit{for}}\alpha\in(0,1),\)<br>
\((ii)\mathtt{cent}^\alpha(\mathcal{T},w)\le\frac{1}{2-3\alpha}\cdot\mathtt{OPT}(\mathcal{T},w)-\frac{3\alpha-1}{2-3\alpha}m,\text{\textit{for}}\alpha\in\left[\frac{1}{3},\frac{1}{2}\right].\)

Note that the second bound is a strengthening of the first when \(\alpha<\frac{1}{2}\). In particular, for \(\alpha\le\frac{1}{3}\), it implies that an \(\alpha\)-centroid tree is _optimal_, if it exists.

We show that the result is tight when \(\alpha\ge\frac{1}{2}\) by proving a matching lower bound.

**Theorem 1.8.** _For every_ \(\alpha\in[\frac{1}{2},1)\) _there is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>_) _with_ \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\)_, w<sub>n</sub>_(T_<sub>n</sub>_)=1 _and_

\(\mathtt{cent}^\alpha(\mathcal{T}_n,w_n)\ge\frac{1}{1-\alpha}\cdot\mathtt{OPT}(\mathcal{T}_n,w_n)-\frac{\alpha}{1-\alpha}.\)

Note that if \(\alpha>\frac{1}{2}\), we cannot prove such a lower bound for _all_ \(\alpha\)-centroid trees of (T_<sub>n</sub>,w<sub>n</sub>_) (as in Theorem 1.2), since a \(\frac{1}{2}\)-centroid tree exists and has stronger approximation guarantees according to Theorem 1.1.

