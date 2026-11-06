<tbc>overview of these results, comparing selected prior finite-base constructions with the new variants at finite _p_ and _q_.

The largest exact construction we consider computes _p_=105 independent products of dimension _q=n_<sup>4</sup>, while graded constructions give _p_=125,133,141 with limiting fractions of retained precision at least 1/2,1/3,1/4, respectively (Section 8.2).  1 gives multiplication-count reduction factors of the new construction over LITA, Strassen, and classical multiplication at _q_=11<sup>4</sup>=14641. For example, the exact fourteen-product construction improves the padding-free recursive estimate for LITA \[22\] at _q_=7<sup>3</sup>=343 by a factor of 1.029 (Section 8.1).

## 2 Notation

We will be interested in characterizing the complexity of (multiple) matrix products and tensor contractions. We generally refer to _A_ and _B_ as the input matrices/tensors and to _C_ as the output. Any tensor contraction can be written as a product of (possibly rectangular) matrices by combining modes (dimensions) of the tensors shared between (_A,B_), (_B,C_), and (_A,C_). We associate matrix multiplication with a trilinear form by pairing its output with an independent matrix of variables _Z_:

\(\sum_{i,j=0}^{n-1}(XY)_{ij}Z_{ij}=\sum_{i,j,k=0}^{n-1}X_{ik}Y_{kj}Z_{ij}.\) (5)

This trilinear form is induced by the same tensor as the bilinear map of matrix multiplication. The trilinear form is more convenient for deriving low-rank decompositions of the tensor, which can be used to apply the bilinear map efficiently.

For positive integers _a,b,c_, we write

\(\langle a,b,c\rangle=\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}\sum_{k=0}^{c-1}X_{ij}Y_{jk}Z_{ki}\) (6)

for the trilinear form representing the matrix multiplication tensor corresponding to the product of an \(a\times b\) matrix and a \(b\times c\) matrix. Here _Z_ is indexed in transposed order relative to the entrywise pairing above. We identify a trilinear form with its coefficient tensor in the chosen bases.

A rank-one trilinear form is a product of one linear form in each variable space. For a trilinear form _T_, we write _R(T_) for the least number of rank-one forms whose sum is _T_, and <u>_R_</u>(_T_) for the border rank, the least _r_ for which _T_ is a limit of tensors of rank at most _r_. The direct sum \(T_1\oplus\cdots\oplus T_p\) uses disjoint variable spaces; in particular, \(\langle a,b,c\rangle^{\oplus p}\) denotes _p_ independent matrix products of the same dimensions.

We write multi-indices in bold, for example **i**=(_i_<sub>0</sub>_,...,i_<sub>_d_-1</sub>) for a tensor of order _d_. We use the interval notation \(\unknown 0,d-1\unknown=\mathbb{Z}\cap[0,d-1]\). Throughout the paper, \(F=\unknown 0,d-1\unknown\) denotes the set of positions in a _d_-component multi-index, with _d_ specified for each construction. Thus \(r\in F\) labels a position, while _i<sub>r</sub>_ is its index value. All set complements are relative to this coordinate set: _S<sup>c</sup>=F_\\_S_.

\begin{tabular}{cccccc}
Construction & _p_ & retained precision & over LITA & over Strassen & over classical \\
Exact & 105 & exact & 1.44\(\times\) & 2.30\(\times\) & 14.61\(\times\) \\
Border rank & 125 & \(\theta\ge 1/2\) & 1.71\(\times\) & 2.73\(\times\) & 17.31\(\times\) \\
Border rank & 133 & \(\theta\ge 1/3\) & 1.83\(\times\) & 2.91\(\times\) & 18.48\(\times\) \\
Border rank & 141 & \(\theta\ge 1/4\) & 1.93\(\times\) & 3.08\(\times\) & 19.52\(\times\) \\
\end{tabular}

1: Multiplication-count reduction factors at _q_=11<sup>4</sup>=14641, the largest dimension \(n^4\le 16000\) with integer _n_. The consecutive reference counts are _pq_<sup>log<sub>32</sub>14197</sup> (LITA \[22\]), _pq_<sup>log<sub>2</sub>7</sup> (Strassen \[36\]), and _pq_<sup>3</sup> (classical). The first two are padding-free recursive models; the third is the classical count. The precision column lists limiting fractions of classical reference accuracy from Section 7; (144) gives the comparison at fixed working precision. All entries are multiplication-count ratios rounded to two decimal places.

