<tbc>triangles through each edge; we define the lopsided version.

**Definition 14** (Lopsided All-Edges Sparse Triangle Counting, #Lop-AE-SparseTri(_n,D_))**.** This is the same problem as Lop-AE-SparseTri(_n,D_), except that for every edge \((a,b)\in W\) we ask for the number of triangles it lies in, that is, the number of common neighbors of _a_ and _b_ in _M_.

In matrix language, let \(X\in\{0,1\}^{n\times D}\) and \(Y\in\{0,1\}^{D\times n}\) be the biadjacency matrices of the edges between _A_ and _M_ and between _M_ and _B_, that is, _X\[a,v_\]=1 if and only if \(a\in A\) and \(v\in M\) are adjacent, and _Y\[v,b_\]=1 if and only if \(v\in M\) and \(b\in B\) are adjacent (padded with zeros if _M_ has fewer than _D_ vertices). Then Lop-AE-SparseTri(_n,D_) asks for the entries of the Boolean product of _X_ and _Y_ at the positions in _W_, and #Lop-AE-SparseTri(_n,D_) asks for the corresponding entries of the product of _X_ and _Y_ over the integers. In the language of Section 2, _W_ is the set of wanted positions, and we call its elements the **_query pairs_**.

The counting version #Lop-AE-SparseTri(_n,D_) is also equivalent, up to polylogarithmic factors, to the problem of Theorem 5 and Corollary 26, that is, to computing the wanted entries \((XY)[I,J]\), \((I,J)\in W\), of a thin matrix product, for matrices \(X\in\mathbb{Z}^{n\times D}\) and \(Y\in\mathbb{Z}^{D\times n}\) whose entries have absolute value _n_<sup>_O_(1)</sup>.<sup>8</sup>

Besides asking for the wanted entries of a Boolean thin matrix product, the detection version Lop-AE-SparseTri(_n,D_) can also be viewed as offline Set Disjointness (see, e.g., \[KPP16, VX20\]): the sets are the neighborhoods in _M_ of the vertices of _A_ and _B_, over a universe of at most _D_ elements, and a query pair \((a,b)\in W\) asks whether the sets of _a_ and _b_ are disjoint. The reductions below (mostly from prior work) produce at most \(n^2/\sqrt{D}\) query pairs and sets of at most \(\sqrt{D}\) elements, which is the regime of \[KPP16\] and of \[VX20, Corollary 3.12\].

With the above discussion in mind, Theorem 5 gives the following.

**Corollary 15.** _Let_ \(D\ge 4\) _be a power of four with_ \(n\ge D^{18}\)_, and consider an instance of_ #Lop-AE-SparseTri(_n,D_) _or of_ Lop-AE-SparseTri(_n,D_) _with_ |_W_| _query pairs. If_ \(|W|\le n^2/\sqrt{D}\)_, then the instance can be solved deterministically in O(n_<sup>2</sup>log<sup>2</sup>_D/D_<sup>1/18</sup>) _time. In general, splitting W into sets of at most_ \(n^2/\sqrt{D}\) _query pairs solves it deterministically in time_

\(O\big((n^2+|W|\sqrt{D})log^2D/D^{1/18}\big).\)

_Proof._ Apply Theorem 5 with _N=n_ to the two biadjacency matrices: the entries (_XY_)\[_a,b_\], \((a,b)\in W\), are the numbers of common neighbors, and they are nonzero exactly for the query pairs that lie in a triangle. For larger _W_, apply the theorem to each of at most \(\lceil|W|\sqrt{D}/n^2\rceil+1\) pieces.

The data structure of Section 4 improves the saving _D_<sup>1/18</sup> to _D_<sup>0.063</sup> (Corollary 26), and gives the following.

**Corollary 16.** _Let_ \(n\ge D^{18}\)_, and consider an instance of_ #Lop-AE-SparseTri(_n,D_) _or of_ Lop-AE-SparseTri(_n,D_) _with_ |_W_| _query pairs. It can be solved deterministically in O_(|_W|D_<sup>0.437</sup>+_n_<sup>2</sup>_/D_<sup>0.063</sup>) _time._

_Proof._ This is Corollary 26 with _N=n_, applied to the two biadjacency matrices as above.

<sup>8</sup>An instance of #Lop-AE-SparseTri(_n,D_) asks for the wanted entries of a thin matrix product of two 0/1 matrices. To reduce to #Lop-AE-SparseTri, we use a standard idea: split each matrix into its positive and negative parts and write their entries in binary, \(X=\sum_i2^iX_i\) and \(Y=\sum_j2^jY_j\) with 0/1 matrices _X<sub>i</sub>_ and _Y<sub>j</sub>_. Then \(XY=\sum_{i,j}2^{i+j}X_iY_j\), so a product with _b_-bit entries costs _O(b_<sup>2</sup>) instances of #Lop-AE-SparseTri(_n,D_) with the same query pairs _W_.

