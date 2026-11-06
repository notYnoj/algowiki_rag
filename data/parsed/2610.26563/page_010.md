**Definition 7** (Compatible combination and conflict-free family)**.** _Let_ S _be a family of tripartitions of the same coordinate set F. A mixed choice_ (_U<sub>i</sub>,V<sub>j</sub>,W<sub>k</sub>_) _is_ compatible _if_

\(U_i\sqcup V_j\sqcup W_k=F.\) (38)

_The family_ S _is_ conflict-free _if every compatible choice is diagonal, i.e., compatibility implies i=j=k._

Figure 1 visualizes tripartitions and their conflicts using Sierpiński’s triangle. In panel (b), mixing parts from the selected tripartitions produces the additional starred tripartition; panel (c) illustrates a conflict-free selection.

**Problem 1** (Cross-term elimination)**.** _For_ \(N\ge 1\)_, determine_

\(M_N=max\{|\mathcal{S}|:\mathcal{S}\subseteq B_{N,N,N}\text{\textit{is conflict-free}}\}.\)

**Lemma 3.** _If_ S _is conflict-free, then each of the three projections_ \(t\mapsto U_t\), \(t\mapsto V_t\)_, and_ \(t\mapsto W_t\) _is injective._

_Proof._ If _U<sub>i</sub>=U<sub>j</sub>_ for \(i\neq j\), then (_U<sub>i</sub>,V<sub>j</sub>,W<sub>j</sub>_) is a non-diagonal compatible choice. The arguments for _V_ and _W_ are identical.

Consequently, a balanced conflict-free family has only replicated or linearly reducible cross terms. The following subsections develop embeddings that annihilate these terms by expanding the local dimension from _n_ to _n_+2. Section 5.6 later shows how replicated terms can instead be cancelled by lower-order aggregates while using only dimension _n_+1.

For a conflict-free family \(\mathcal{S}\subseteq B_{N,N,N}\), the parts _U<sub>t</sub>_ are distinct, so \(|\mathcal{S}|\le\genfrac(){pt}{2}{3N}{N}\). Together with the Salem- Spencer construction used by Coppersmith and Winograd \[29, 15\], this upper bound gives \(M_N=\genfrac(){pt}{2}{3N}{N}^{1-o(1)}\) as \(N\rightarrow\infty\).

## 5.3 Centering

We introduce a modewise zero-sum lifting and call it _centering_. It automatically ensures that linearly reducible terms vanish.

In particular, we embed tensors \(X^{(U)},Y^{(V)},Z^{(W)}\in(\mathbb{C}^n)^{\otimes 2N}\) into tensors \(\bar{X}^{(U)},\bar{Y}^{(V)},\bar{Z}^{(W)}\in(\mathbb{C}^{n+1})^{\otimes 2N}\) such that the sum, equivalently the average, along every fiber is zero. We achieve this embedding by a tensor product of simple embeddings from C_<sup>n</sup>_ to C<sup>_n_+1</sup>. Let \(1_m=(1,\dots,1)^T\in\mathbb{R}^m\) denote the all-ones vector.

**Definition 8** (Centering embedding)**.** _A centering embedding is a real matrix_<tbc>

\(Q\in\mathbb{R}^{(n+1)\times n}\)

(1,0,0)
W
U
W
U
S1
S1
S2
S3
S2
V
V

(a) One subdivision

(b) Conflict

(c) Conflict-free

Figure 1: Sierpiński’s triangle, obtained by repeatedly removing central subtriangles, visualizes conflicts between tripartitions. (a) One subdivision, labelled by membership in _U,V,W_. Blue points mark selected tripartitions; mixed projections create an additional contraction in (b) (star), but not in (c).

