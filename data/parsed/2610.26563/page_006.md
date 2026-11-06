For each set of _w_ distinct index values, symmetry leaves \(\genfrac(){pt}{2}{w}{s,t,v}\) distinct monomials, one per tripartition of those values. Including repeated-index tuples gives \(\genfrac(){pt}{2}{n}{w}\genfrac(){pt}{2}{w}{s,t,v}+O(n^{w-1})=n^w/(s!t!v!)+O(n^{w-1})\) distinct monomials. We obtain a decomposition of rank at most _n<sup>w</sup>/w_!+_O(n_<sup>_w_-1</sup>) by first computing the aggregate

\(\sum_{\mathbf{i}\in\unknown 0,n-1\unknown^w}\big(\sum_{U\subseteq\unknown 0,w-1\unknown,|U|=t}X_{\mathbf{i}|_{U^c}}\big)\big(\sum_{V\subseteq\unknown 0,w-1\unknown,|V|=s}Y_{\mathbf{i}|_{V^c}}\big)\big(\sum_{W\subseteq\unknown 0,w-1\unknown,|W|=v}Z_{\mathbf{i}|_{W^c}}\big).\) (14)

Its summand is invariant under permutations of **i**, so the distinct-index contribution requires only \(\genfrac(){pt}{2}{n}{w}\) rank-one terms, one for each increasing tuple \(i_0<\cdots<i_{w-1}\), with coefficient _w_!. Repeated-index tuples contribute _O(n_<sup>_w_-1</sup>) additional terms. When expanding this trilinear product, terms for which (_U,V,W_) is not a tripartition of \(\unknown 0,w-1\unknown\) must satisfy at least one of the following two conditions.

**Definition 3** (Replicated Term)**.** \(|U\cap V\cap W|\ge 1\)<br>
_In this case, some index in_ **i** _is omitted in X, Y, and Z, and hence there are at most n_<sup>_w_-1</sup> _distinct monomial terms, each appearing at least n times._

**Definition 4** (Linearly Reducible Term)**.** \(|(U\cap V)\backslash W|\ge 1\) _(or similar with U,V,W permuted)<br>
In this case, some index in_ **i** _appears only in one type of variable (X, Y, or Z). We may sum that tensor of variables over the corresponding index to obtain a trilinear form with n_<sup>_w_-1</sup> _terms (again a tensor contraction with one less index)._

Subtracting these lower-order cross terms gives the stated rank bound. Further examples and complete equations for computing the cross terms are given in \[35\]. In the following sections, we review well-known constructions of fast matrix multiplication algorithms, and show that, when written as high-order tensor contractions, they may be similarly understood in terms of replicated and linearly reducible terms.

## 4 Background on Fast Matrix Multiplication

### 4.1 Direct sums of independent matrix-matrix products

For bilinear maps with disjoint input and output spaces, the direct sum is the map that evaluates all of them at once. Hence the problem of independent matrix multiplications is a direct sum of matrix multiplication tensors. The elementary upper bounds

\(R(T_1\oplus\cdots\oplus T_p)\le\sum_{i=1}^PR(T_i),\underline{R}(T_1\oplus\cdots\oplus T_p)\le\sum_{i=1}^p\underline{R}(T_i)\) (15)

come from applying separate algorithms (rank decompositions). Rank additivity was conjectured by Strassen, but has been proven false for general tensors \[33\]. Rank additivity of matrix-multiplication remains an open problem. For instance, \(R(\langle 2,2,2\rangle^{\oplus 2})=14\) already follows from the Alder-Strassen bound \[2\]: the algebra \(\mathbb{C}^{2\times 2}\times\mathbb{C}^{2\times 2}\) has dimension eight and two maximal two-sided ideals, giving the lower bound \(2\cdot 8-2=14\), while two applications of Strassen’s algorithm attain it. See also Rupniewski \[28\] for more general direct-sum results.

### 4.2 Schönhage’s Asymptotic Sum Theorem

Schönhage’s asymptotic sum inequality \[30\] is the standard route from a border-rank bound for simultaneous matrix multiplication to a bound on the exponent \(\omega\). Thus trilinear aggregation algorithms for simultaneous matrix multiplication yield bounds on the matrix multiplication exponent. The asymptotic sum inequality gives much stronger bounds on \(\omega\) than using _m_ independent products merely as blocks of one product of dimension _nm_<sup>1/3</sup>. For exact-rank constructions, the inequality also has a direct algorithmic interpretation described next.

Suppose the construction input to the theorem is an exact bilinear construction of rank _r_ that reduces _m_ independent matrix multiplications of dimension _n_ to _r_ scalar products. At the next recursive level, each scalar product becomes a matrix-matrix product of dimension _n_. We may compute these _r_ products by<tbc>

