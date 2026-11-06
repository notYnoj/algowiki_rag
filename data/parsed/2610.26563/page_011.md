_whose columns form an orthonormal basis for the hyperplane_

\(1_{n+1}^\perp=\{x\in\mathbb{R}^{n+1}:1_{n+1}^Tx=0\}.\) (39)

_Equivalently, the matrix_

\(\left[\frac{1}{\sqrt{n+1}}1_{n+1}Q\right]\in\mathbb{R}^{(n+1)\times(n+1)}\)

_is orthogonal._

_Thus_

\(1_{n+1}^TQ=0,Q^TQ=I_n.\) (40)

_We use the same matrix Q as a complex-linear map_ \(\mathbb{C}^n\rightarrow\mathbb{C}^{n+1}\)_. Throughout, the tensor contractions are bilinear algebraic contractions, so no complex conjugation is used._

A simple choice for a centering embedding is to choose _Q_ based on a transposed Helmert matrix \[24\],

\(\forall k\in\unknown 0,n\unknown,l\in\unknown 0,n-1\unknown,q_{kl}=\left\{\begin{array}{ c c }
\frac{1}{\sqrt{(l+1)(l+2)}} & k\le l, \\
-\frac{l+1}{\sqrt{(l+1)(l+2)}} & k=l+1, \\
0 & k>l+1.
\end{array}\right.\) (41)

The Helmert matrix is computationally convenient because, apart from a subdiagonal part, each column is a scalar multiple of the corresponding column of the transposed prefix sum matrix, and hence it can be applied to a vector with _O(n_) operations.

We can recover tensor contractions after applying the centering embedding. For example, for any matrices \(A,B\in\mathbb{C}^{n\times n}\), embed them as

\(\bar{A}=QAQ^T,\bar{B}=QBQ^T.\) (42)

Then

\(\bar{A}\bar{B}=QABQ^T,\) (43)

so, after computing \(\bar{C}=\bar{A}\bar{B}\), we recover

\(C=Q^T\bar{C}Q.\) (44)

As an example of how the embedding may be useful, recall the symmetric matrix-vector product algorithm _c=Ab_ from Section 3. We may obtain an algorithm with \(\genfrac(){pt}{2}{n+2}{2}\) products by computing

\(\bar{A}=QAQ^T,\bar{b}=Qb,\) (45)

then

\(\bar{c}_i=\sum_j\bar{A}_{ij}(\bar{b}_i+\bar{b}_j),\) (46)

and finally recovering

\(c=Q^T\bar{c}.\) (47)

Since \(\sum_j\bar{A}_{ij}=0\), the unwanted term \(\bar{b}_i\sum_j\bar{A}_{ij}\) vanishes without an explicit correction. This example illustrates how the embedding automates cross-term elimination. As we also see later for simultaneous tensor contraction, computing the cross-term corrections explicitly can instead give a smaller multiplication count.

To apply centering to higher order tensors, we apply the linear embedding given by _Q_ along each mode of the tensor. The resulting tensor has zero sum along every fiber.

**Definition 9** (Centering map and its tensor products)**.** _For a centering matrix_ \(Q\in\mathbb{R}^{(n+1)\times n}\)_, define_

\(\mu:\mathbb{C}^n\rightarrow\mathbb{C}^{n+1},\mu(x)=Qx.\) (48)

_For a tensor whose modes are indexed by a finite set S, centering in all modes is the map_

\(\mu^{\otimes|S|}=Q^{\otimes|S|}:(\mathbb{C}^n)^{\otimes|S|}\rightarrow(\mathbb{C}^{n+1})^{\otimes|S|}.\) (49)

