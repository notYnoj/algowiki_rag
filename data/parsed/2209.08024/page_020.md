## 5.2 Spread and zero-weight vertices

Let _w_ be a weight function on a tree T such that at least one vertex weight is positive. The _spread_ of _w_ is defined as \(\sigma_w=w(\mathcal{T})/min_{v\in V(\mathcal{T}),w(v)>0}w(v)\).

Let _T_ be a centroid tree of (T_,w_). By definition, if _u_ is a parent of _v_, then \(w(T_v)\le\frac{1}{2}w(T_u)\). More generally, if _v_ is at depth _d_, then \(w(T_v)\le 2^{-d}w(\mathcal{T})\). Thus, the depth of a positive-weight vertex _v_ cannot be more than \(1+log\frac{w(\mathcal{T})}{w(v)}\le 1+log\sigma_w\).

In particular, if all vertex weights are positive, then the height of every centroid tree is at most \(1+log\sigma_w\), so the algorithm of the previous section runs in time \(\mathcal{O}(nloglog\sigma)\).

If we allow zero-weight vertices, however, then this is not necessarily true, since there could be a large unbalanced zero-weight subtree. Also, the top-tree component of our algorithm does not allow zero weights for technical reasons. We believe that the top tree implementation of \[AHLT05\] can be adapted to this changed requirement, but for a simpler presentation, we prefer to use the standard interface, as defined in \[AHLT05\].

The solution to both problems is to change the zero weights by a very small amount, as follows. Let T be a tree on _n_ vertices, let \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\), and let \(\varepsilon>0\). We define the positive weight function \(w_\varepsilon:V(\mathcal{T})\rightarrow\mathbb{R}_+\) on _G_ as follows:

\(w_\varepsilon(v)=\left\{\begin{array}{ c c }
w(v), & \text{if}w(v)\neq 0 \\
\varepsilon, & \text{otherwise.}
\end{array}\right.\)

We now prove that a centroid tree of \((\mathcal{T},w_\varepsilon)\) is also a centroid tree of (T_,w_) if \(\varepsilon\) is small enough. For this, it is enough to show that for every subgraph, no new centroids are introduced.

**Lemma 5.1.** _Let_ T _be a tree on n vertices, and let_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_. For each small enough_ \(\varepsilon>0\)_, each centroid of_ \((\mathcal{T},w_\varepsilon)\) _is a centroid of_ (T_,w)._

_Proof._ Let _k\<n_ be the number of zero-weight vertices w.r.t. _w_. Let _c_ be a centroid of (T_,g_) and let \(C\in\mathbb{C}(\mathcal{T}-c)\). We have

\(w(C)\le w_\varepsilon(C)\le\frac{1}{2}w_\varepsilon(\mathcal{T})=\frac{1}{2}\left(w(\mathcal{T})+\varepsilon k\right)<\frac{1}{2}w(\mathcal{T})+\frac{1}{2}\varepsilon n.\)

If \(\varepsilon\) is small enough, this implies that \(w(C)\le\frac{1}{2}w(\mathcal{T})\). Repeating the argument for each \(C\in\mathbb{C}(\mathcal{T}-c)\) shows that _c_ is a centroid of (T_,w_).

Note that if all weights are integers, we can simply set \(\varepsilon=1/n\) (or set \(\varepsilon=1\) and multiply each other weight by _n_). In general, we can treat \(\varepsilon\) symbolically, without explicitly computing a value for it.

We now show that the height of the centroid tree w.r.t. \(w_\varepsilon\) is essentially bounded by the spread of _w_; in other words, replacing _w_ with \(w_\varepsilon\) ensures that the computed centroid tree is "reasonable". Note that we can ignore the spread of \(w_\varepsilon\) here (which may be very large, if \(\varepsilon\) is very small).

**Lemma 5.2.** _Let_ T _be a tree on n vertices, let_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, and let_ \(\varepsilon>0\) _be defined as in Lemma 5.1. Each centroid tree of_ \((\mathcal{T},w_\varepsilon)\) _has height_ \(\mathcal{O}(log\sigma_w+logn)\).

_Proof._ Let _T_ be a centroid tree of \((\mathcal{T},w_\varepsilon)\). By Lemma 5.1, _T_ is also a centroid tree of (T_,w_). Thus, the depth of each node _v_ with _w(v)\>_0 is at most \(1+log\sigma_w\). Now consider a subtree _T<sub>u</sub>_ with _w(T<sub>u</sub>_)=0. Then the weight w.r.t. \(w_\varepsilon\) of each node in _T<sub>u</sub>_ is the same, so the spread of \(w_\varepsilon\) restricted to _V(T<sub>u</sub>_) is \(|V(T_u)|\le n\). This implies that the height of each zero-weight vertex in _T_ is at most \(2+log\sigma_w+logn\), concluding the proof.

Lemmas 5.1 and 5.2 imply that we can replace _w_ with \(w_\varepsilon\) before running the algorithm. This yields

**Theorem 5.4** (Restatement of Thm. 1.5)**.** _Let_ T _be a tree on n vertices and w be a weight function. We can compute a centroid tree of_ (T_,w_) _in time_ \(\mathcal{O}(nlogh)\subseteq\mathcal{O}(nloglog\left(\sigma+n\right))\)_, where h is the height of the computed centroid tree and_ \(\sigma\) _is the spread of w._

