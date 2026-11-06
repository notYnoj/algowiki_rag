This partitioning process can be naturally described by a binary tree \(T=T(\sigma)\), that we call a _partitioning tree_ associated with the ordering \(\sigma\) (see Figure 1). Each node \(v\in V(T)\) is associated with a vertical strip _S(v_) of the bounding box _B_. The strip _S(r_) of the root vertex _r_ of _T_ is the bounding box _B_. For every inner vertex \(v\in V(T)\), if _S=S(v_) is the vertical strip associated with _v_, and if \(L\in\mathcal{L}\) is the first line in \(\sigma\) that lies strictly in _S_, then line _L_ partitions _S_ into two sub-strips, that we denote by _S<sub>L</sub>_ and _S<sub>R</sub>_. Vertex _v_ then has two children, whose corresponding strips are _S<sub>L</sub>_ and _S<sub>R</sub>_ respectively. We say that _v owns_ the line _L_, and we denote _L=L(v_). For each leaf node _v_, the corresponding strip _S(v_) contains exactly one active column of _X_, and _v_ does not own any line of L. For each vertex \(v\in V(T)\), let \(N(v)=|X\cap S(v)|\) be the number of points from _X_ that lie in _S(v_), and let width(_v_) be the width of the strip _S(v_).

Given a partition tree _T_ for point set _X_, we refer to the vertical strips in \(\{S(v)\}_{v\in T}\) as _T_-strips.

We can use the partitioning trees in order to show the following well known bound on OPT(_X_)<sup>2</sup>:

**Claim 2.6** _For any semi-permutation X,_ \(\mathsf{OPT}(X)\le O(r(X)logc(X))\)_, where r(X_) _and c(X_) _are the number of active rows and columns of X respectively._

## 2.4 The WB-1 Bound

The WB-1 bound<sup>3</sup> is defined with respect to an ordering (or a permutation) \(\sigma\) of the auxiliary columns, or, equivalently, with respect to the partitioning tree \(T(\sigma)\). It will be helpful to keep both these views in mind. In this paper, we will make a clear distinction between a weak variant of the WB-1 bound, as defined by Wilber himself in \[Wil89\] and a strong variant, as mentioned in \[Iac13\].

Let _X_ be a semi-permutation, and let L be the corresponding set of auxiliary columns. Consider an arbitrary fixed ordering \(\sigma\) of columns in L and its corresponding partition tree \(T=T(\sigma)\). For each inner node \(v\in V(T)\), consider the set \(X'=X\cap S(v)\) of input points that lie in the strip _S(v_), and let \(L(v)\in\mathcal{L}\) be the line that _v_ owns. We denote \(X'=\{p_1,p_2,\dots,p_k\}\), where the points are ordered in the increasing order of their _y_-coordinates; since _X_ is a semi-permutation, no two points of _X_ may have the same _y_-coordinate. For \(1\le j<k\), we say that the ordered pair (_p<sub>j</sub>,p_<sub>_j_+1</sub>) of points form a _crossing_ of _L(v_) iff _p<sub>j</sub>,p_<sub>_j_+1</sub> lie on the opposite sides of the line _L(v_). We let cost(_v_) be the total number of crossings of _L(v_) by the points of \(X\cap S(v)\). When _L=L(v_), we also write cost(_L_) to denote cost(_v_). If _v_ is a leaf vertex, then its cost is set to 0.

We note a simple observation, that the cost can be bounded by the number of points on the smaller side.

**Observation 2.7** _Let X be a semi-permutation,_ \(\sigma\) _an ordering of the auxiliary columns in_ L_, and let_ \(T=T_\sigma\) _be the corresponding partitioning tree. Let_ \(v\in V(T)\) _be any inner vertex of the tree, whose two child vertices are denoted by v_<sub>1</sub> _and v_<sub>2</sub>_. Then_ \(\mathsf{cost}(v)\le 2min\{|X\cap S(v_1)|,|X\cap S(v_2)|\}\).

**Definition 2.8 (WB-1 bound)** _For any semi-permutation X, an ordering_ \(\sigma\) _of the auxiliary columns in_ L_, and the corresponding partitioning tree_ \(T=T_\sigma\)_, the (weak) WB-1 bound of X with respect to_ \(\sigma\) _is:_

\(\mathsf{WB}_\sigma(X)=\mathsf{WB}_T(X)=\sum_{v\in V(T)}\mathsf{cost}(v).\)

<sup>2</sup>The algorithm in the claim in fact corresponds to searching in a balanced static BST. <sup>3</sup>Also called Interleaving bound \[DHIP07\], the first Wilber bound, "interleave lower bound" \[Wil89\], or alternation bound \[Iac13\]

