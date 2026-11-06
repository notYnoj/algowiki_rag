Here, we instead study the problem to reduce _from_, namely APSP or Min-Plus Product, and give subcubic algorithms for a large class of input graphs (or matrices) satisfying a certain _structural property_. Then, to design APSP-based hardness reductions, we can first apply this subcubic-time algorithm to handle the structured part of the graph (or matrix) and reduce to its unstructured core, which is often easier to reduce from. This perspective can be seen as a recent trend with comparably few successful applications \[2, 1, 35, 70, 37\], including the aforementioned work introducing the "Fredman’s trick meets dominance product" technique \[35\].

A significant challenge is to identify the _right_ structural property. We propose a new, expressive one: a rank measure for matrices that we call the _select-plus rank_.

## 1.4.1 Select-Plus Rank

**Definition 1.17** (Select-Plus Rank)**.** _The_ select-plus rank _of a matrix_ \(A\in(\mathbb{Z}\cup\{\perp\})^{n\times m}\)_, denoted by r(A), is the smallest integer_ \(r\ge 0\) _such that there are integer matrices_ \(U\in\mathbb{Z}^{n\times r}\) _and_ \(V\in\mathbb{Z}^{r\times m}\) _satisfying for all_ \((i,j)\in[n]\times[m]\):

\(A[i,j]\in\{U[i,1]+V[1,j],\dots,U[i,r]+V[r,j]\}\cup\{\perp\}.\)

This definition is reminiscent of standard matrix rank, which can be characterized as the smallest _r_ such that _A=UV_ for some \(U\in\mathbb{Z}^{n\times r}\) and \(V\in\mathbb{Z}^{r\times m}\), i.e., such that each entry can be written as:

\(A[i,j]=U[i,1]\cdot V[1,j]+\cdots+U[i,r]\cdot V[r,j].\)

Hence, the select-plus rank can be seen as the modification where we replace multiplication by addition, and addition by "selection".<sup>8</sup> In many aspects it also behaves like the standard matrix rank, e.g., the select-plus rank of an \(n\times n\) matrix ranges from 0 to _n_.

Our key technical result is the following algorithm.

**Theorem 1.18** (Low-Rank Min-Plus Product)**.** _The min-plus product of two given matrices A,B can be computed in deterministic time_ \(n^{3+o(1)}\cdot(r/n^{3-\omega})^{\Omega(1)}\)_, provided that we have access to a select-plus rank-r decomposition of A or B (or of a matrix C that approximates A∗B with entry-wise additive error_ \(\pm O(1)\)_)._

The point is that when the select-plus rank is at most \(r\le n^{3-\omega-\epsilon}\) the running time is truly subcubic, \(n^{3-\Omega(\epsilon)}\). In particular, if \(\omega=2\) the running time is subcubic for ranks up to \(r\le n^{1-\epsilon}\)--i.e., unless all matrices have almost full rank, we obtain a subcubic-time algorithm for Min-Plus Product!

Theorem 1.18 implies that low-rank APSP, i.e., APSP on graphs whose adjacency lists have select-plus rank at most \(n^{3-\omega-\epsilon}\), can be solved in subcubic time. This result unifies and generalizes several previously studied classes of graphs known to admit subcubic-time algorithms, including sparse graphs, graphs with small weights in \([n^{3-\omega-\epsilon}]\) \[88, 57, 9, 90, 104\], node-weighted graphs \[31, 102, 4\], and even graphs with at most \(n^{3-\omega-\epsilon}\) distinct edge weights per node \[102, 4\].

In the following, we will first explore how the claimed universe reductions and fine-grained lower bounds can be derived from Theorem 1.18 (Section 1.4.2), and then describe on a high level how Theorem 1.18 can be proved (Section 1.4.3).

## 1.4.2 Low-Rank Min-Plus Product in Action

The main power of our new low-rank technique is that it allows us to significantly restrict the set of "hard" Min-Plus Product instances. Such restrictions are already known, though mostly simple ones. For example, call any index _k_ attaining the minimum min_<sub>k</sub>(A_\[_i,k_\]+_B_\[_k,j_\]) a _witness_ of (_A∗B_)\[_i,j_\]. In a hard instance _A∗B_ we expect that most entries have only very few, say at most \(n^\epsilon\), witnesses. Otherwise we could narrow our<tbc>

<sup>8</sup>Another reasonable notion could be the _min-plus rank_ of a matrix, defined analogously with the condition that _A_\[_i,j_\]=min{_U_\[_i,_1\]+_V_\[1_,j_\]_,...,U_\[_i,r_\]+_V_\[_r,j_\]}. This is a strictly more restrictive notion, i.e., the select-plus rank is always upper- bounded by the min-plus rank. Therefore, all of our algorithmic results immediately also apply to the min-plus rank. However, for some applications (specifically, Lemma 5.3) we crucially exploit the extra freedom that the select-plus rank offers.

