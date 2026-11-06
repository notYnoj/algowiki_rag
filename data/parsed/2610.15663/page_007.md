## 2.2 The recursive computation

We now use Theorem 2.3 to reduce the middle dimension of a matrix product by a factor of two. A _subproblem_ consists of two input matrices and a set of entries of their product that we want to compute. The original subproblem is to multiply \(X\in\mathbb{Z}^{n\times d}\) by \(Y\in\mathbb{Z}^{d\times m}\) at the _w_ specified positions.

We first explain one reduction step, then bound three costs after iterating it: preparing input linear forms, multiplying them, and reconstructing the requested outputs. Padding the input dimensions will then give Theorem 2.1. We first count arithmetic operations on matrix values, and account for request processing and intermediate magnitudes at the end.

### One reduction step.

Fix an integer \(k\ge 2\) and let _R=k_2<sup>_k_-1</sup> and _S_=3<sup>_k_-1</sup>, as in Theorem 2.3.

**Claim 2.5** (One reduction step)**.** _Consider matrices_ \(X\in\mathbb{Z}^{N\times D}\) _and_ \(Y\in\mathbb{Z}^{D\times M}\)_, with w distinct specified entries of XY. Suppose R|N, S|M, and_ 2|_D. This subproblem reduces to RS=k_6<sup>_k_-1</sup> _private subproblems and_ 6_<sup>k</sup> shared subproblems. Each multiplies matrices of dimensions_

\(\left(\frac{N}{R}\times\frac{D}{2}\right)\text{\textit{and}}\left(\frac{D}{2}\times\frac{M}{S}\right).\)

_The private subproblems receive w requested entries in total, and the shared subproblems receive at most_ 6_w. Their answers determine the w original entries using at most_ 6_w additions and subtractions._

(a) Input preparation
X
N x D
signed block sums
N x D
R 2
6k shared
RS private
(b) Output reconstruction
XY
(r, c)
shared
private

Figure 3: One reduction step in Theorem 2.5. (a) Signed sums of at most 6_k_ parent blocks form each child input, shown for _X_; _Y_ is treated in the same way. (b) One requested parent entry is recovered from six shared answers minus one private answer. Dots mark the same local position (_r,c_) in the parent block and child outputs.

