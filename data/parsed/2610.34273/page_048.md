## A Flattening Rank, Cut Bounds, and Triangle Covers

We give the rank bounds used in the introduction. The flattening argument and its graph-cut specialization are standard; see Christandl, Vrana, and Zuiddam \[CVZ19, Definition 1.1.19, Proposition 1.1.20, and Example 1.1.21\]. We state them in our coordinate conventions, include the bipartite equality case, and then give the triangle-cover argument with OpenAI’s improved matrix multiplication bound. Appendix B treats asymptotic subrank separately.

**Definition A.1** (flattening rank)**.** Let \(k\ge 2\) be an integer, let _T_ be a complex _k_-th order tensor, and choose coordinates of positive dimensions (_d_<sub>1</sub>_,...,d<sub>k</sub>_) for _T_. If _T_=0, use the zero coefficient table of these dimensions. Let \(\varnothing\neq S\unknown\{1,\dots,k\}\) and write <o>_S_</o>={1_,...,k_}\\_S_. In these coordinates, the _flattening across S_ is the matrix Flat_<sub>S</sub>(T_) with rows indexed by \(\mathbf{a}\in\prod_{v\in S}[d_v]_0\) and columns indexed by \(\mathbf{b}\in\prod_{v\in\overline{S}}[d_v]_0\), defined by

\(\mathrm{Flat}_S(T)_{\mathbf{a},\mathbf{b}}=T_{c_1,\dots,c_k},c_v=\left\{\begin{array}{ c c }
a_v, & v\in S, \\
b_v, & v\in\overline{S},
\end{array}\right.(1\le v\le k).\)

The indices on each side are ordered by increasing vertex label and then lexicographically. The _flattening rank_ is FR_<sub>S</sub>(T_)=rank(Flat_<sub>S</sub>(T_)). A different representative of a nonzero tensor permutes the rows and columns, so this rank is independent of the representative. For _T_=0, every choice gives a zero matrix, and hence FR_<sub>S</sub>_(0)=0.

**Lemma A.2** (properties of flattening rank)**.** _Let_ \(k\ge 2\) _be an integer, let A,B be complex k-th order tensors, and let_ \(\varnothing\neq S\unknown\{1,\dots,k\}\)_, with complement <o>S</o>. Then_

\(\mathrm{Q}(A)\le\mathrm{FR}_S(A)\le\mathrm{R}(A),\mathrm{FR}_S(A\otimes_KB)=\mathrm{FR}_S(A)\mathrm{FR}_S(B).\)

_Moreover,_ \(A\unknown B\) _implies_ \(\mathrm{FR}_S(A)\le\mathrm{FR}_S(B)\)_, and_ FR_<sub>S</sub>_(l_<sub>k</sub>(q_))=_q for every nonnegative integer q._

_Proof._ The claims involving a zero tensor follow from R(0)=Q(0)=FR_<sub>S</sub>_(0)=0 and the fact that \(A\unknown 0\) implies _A_=0. We may therefore assume that _A_ and _B_ are nonzero and work in fixed coordinates.

A simple tensor \(x_1\otimes_C\cdots\otimes_Cx_k\) flattens to the outer product of the vector \(\otimes_{K_{v\in S}}x_v\) and the vector \(\otimes_{K_{v\in\overline{S}}}x_v\). It therefore has matrix rank at most 1. A rank decomposition of _A_ into _r_ simple tensors gives a sum of _r_ matrices of rank at most 1, proving \(\mathrm{FR}_S(A)\le\mathrm{R}(A)\).

Suppose that local matrices _L_<sub>1</sub>_,...,L<sub>k</sub>_ map _B_ to _A_. Expanding the entries in Definition 2.4 gives

\(\mathrm{Flat}_S(A)=\left(\otimes_{K_{v\in\overline{S}}}L_v\right)\mathrm{Flat}_S(B)\left(\otimes_{K_{v\in\overline{S}}}L_v\right)^\mathsf{T}.\)

Here the products are the usual Kronecker products of matrices, with their factors in increasing vertex order. Multiplication on the left or right cannot increase matrix rank, so \(\mathrm{FR}_S(A)\le\mathrm{FR}_S(B)\). For \(q\ge 1\), the flattening of l_<sub>k</sub>(q_) has exactly one entry 1 in each position whose row and column are constant tuples with the same value in \[_q_\]<sub>0</sub>. These positions use _q_ distinct rows and _q_ distinct columns; all other entries are zero. Its rank is therefore _q_. The assertion for _q_=0 follows from the definition of l_<sub>k</sub>_(0). Applying monotonicity to \(\mathrm{l}_k(\mathrm{Q}(A))\unknown A\) proves \(\mathrm{Q}(A)\le\mathrm{FR}_S(A)\).

After separate permutations of its rows and columns, \(\mathrm{Flat}_S(A\otimes_KB)\) is the matrix Kronecker product of Flat_<sub>S</sub>(A_) and Flat_<sub>S</sub>(B_). To recall why matrix rank is multiplicative under this<tbc>

