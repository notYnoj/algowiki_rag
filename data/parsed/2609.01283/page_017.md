The following lemma shows how to compute a randomized union representation of \(M^{\vee k}\) from a linear representation of _M_. For the sake of completeness, we provide a proof in the appendix.

**Lemma 3.2** (\[NSV94\])**.** _Let M be a linear matroid of rank r on m elements, represented by an_ \(r\times m\) _matrix A over a finite field_ F _with_ \(|\mathbb{F}|\ge poly(kr)\)_. For each_ \(i\in[k]\)_, let C<sub>i</sub> be an_ \(m\times m\) _diagonal matrix whose diagonal entries are independent, uniformly random elements from_ F_. Then the_ \(rk\times m\) _matrix_

\(U:=\left(\begin{array}{ c }
AC_1 \\
AC_2 \\
\vdots \\
AC_k
\end{array}\right)\)

_is a randomized union representation of_ \(M^{\vee k}\).

**Remark 3.3** (Parallel Elements in _k_-Fold Union)**.** _Observe that it is possible that an independent set in_ \(M^{\vee k}\) _contains k identical copies of an element, i.e., the columns of A corresponding to this independent set may contain k identical columns. This is consistent with the definition of_ \(M^{\vee k}\)_, since an independent set_ \(S\subseteq E\) _in_ \(M^{\vee k}\) _is partitioned into k blocks_ \(S_1\unknown\cdots\unknown S_k\)_, each being an independent set in M; thus each such block may contain at most one copy of such an element. The representation U remains valid, as the diagonal scalings C_<sub>1</sub>_,...,C<sub>k</sub> assign independent random multipliers to each (element, copy) pair._

## Intersection of two _k_-Fold Matroid Unions

Given two linear matroids _M_<sub>1</sub> and _M_<sub>2</sub> of rank _r_ on a common ground set _E_, we consider the problem of identifying existence of a common basis in \(M_1^{\vee k}\) and \(M_2^{\vee k}\) of size _kr_. Let _U_<sub>1</sub> and _U_<sub>2</sub> be the \(kr\times m\) union representation matrices for \(M_1^{\vee k}\) and \(M_2^{\vee k}\), respectively, constructed using independent random diagonal matrices as given in Theorem 3.2. With each element \(e\in E\), we associate a value _x<sub>e</sub>_ drawn uniformly from a large enough finite field F. Define a diagonal matrix \(D\in\mathbb{F}[Y]^{m\times m}\) with an indeterminate _Y_ as follows:

\(D_{e,e}:=x_eY^{W+wt(e)}\text{for all}e\in E,\)

and \(D_{e,e^\prime}=0\) for \(e\neq e'\).

We next define the _Mixed Laplacian_ \(\mathcal{L}_\cap\) of size \(kr\times kr\) as:

\(\mathcal{L}_\cap:=U_1DU_2^T.\)

The following theorem extends the classical Cauchy-Binet approach for matroid intersection \[Har09, CLL14\] to the _k_-fold union setting.

**Theorem 3.4** (Enumerating Common Bases)**.** _Suppose both_ \(M_1^{\vee k}\) _and_ \(M_2^{\vee k}\) _have rank kr, and_ \(|\mathbb{F}|\ge poly(kr)\)_. Then_

\(det(\mathcal{L}_\cap)=Y^{krW}\sum_{S\in\mathcal{B}(M_1^{\vee k})\cap\mathcal{B}(M_2^{\vee k})}\alpha_S\big(\prod_{e\in S}x_e\big)Y^{\sum_{e\in S}wt(e)},\)

_where_ \(\alpha_S:=det\big((U_1)_S\big)det\big((U_2)_S\big)\) _for any common basis S is non-zero with probability_ \(1-\frac{1}{(kr)^{\Omega(1)}}\)_. Furthermore, with the same probability bound, the minimum degree of Y in_ \(det(\mathcal{L}_\cap)\) _minus krW equals the weight of a minimum-weight common basis._

