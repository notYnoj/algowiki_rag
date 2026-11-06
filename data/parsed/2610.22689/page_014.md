<tbc>Fix \(\varepsilon>0\). For each \(j\ge 1\), define the subset<tbc>

\(\mathcal{C}_j(\varepsilon):=\left\{\mathrm{Ad}_{e^{t_1a_i_1\dots e^{t_qa_i_q}}}(a_{i_0})\right|\left|\begin{array}{ c }
0\le q\le j-1, \\
i_0,\dots,i_q\in\{1,\dots,k\}, \\
|t_r|<\varepsilon,1\le r\le q
\end{array}\right\}\subseteq\mathfrak{g},\)

<tbc>where the product is understood as the identity when _q_=0, and consider the subspace

\(S_j(\varepsilon):=\mathrm{span}_\mathbb{R}\mathcal{C}_j(\varepsilon)\subseteq\mathfrak{g}.\)

Thus, \(\mathcal{C}_j(\varepsilon)\) contains conjugates evaluated at all parameter values in the indicated intervals, rather than at a single fixed choice of parameters. In particular, \(S_1(\varepsilon)=\mathcal{F}_1^\mathbf{a}\).

We first show that

\(\mathcal{F}_j^\mathbf{a}\subseteq S_j(\varepsilon)(j\ge 1).\) (35)

Indeed, let \(c\in S_{j-1}(\varepsilon)\). Writing _c_ as a finite linear combination of elements of \(\mathcal{C}_{j-1}(\varepsilon)\) and using the linearity of the adjoint action shows that<tbc>

\(\mathrm{Ad}_{e^{ta_i}}(c)\in S_j(\varepsilon)\text{for every}|t|<\varepsilon.\)

<tbc>Since \(c\in S_{j-1}(\varepsilon)\subseteq S_j(\varepsilon)\), we have, for every nonzero \(|t|<\varepsilon\),

\(\frac{\mathrm{Ad}_{e^{ta_i}}(c)-c}{t}\in S_j(\varepsilon).\) (36)

The space \(S_j(\varepsilon)\) is a linear subspace of the finite-dimensional normed space g, and is therefore closed. Taking the limit of (36) as \(t\rightarrow 0\) gives

\([a_i,c]=\left.\frac{d}{dt}\right|_{t=0}\mathrm{Ad}_{e^{ta_i}}(c)\in S_j(\varepsilon).\) (37)

The recursive definition of the filtration (see (33)) now proves (35) by induction on _j_.

We next select the basis elements. Suppose that, through stage _j_-1, we have selected exactly \(\mathrm{dim}(\mathcal{F}_{j-1}^\mathbf{a})\) linearly independent elements within \(\mathcal{C}_{j-1}(\varepsilon)\), and let _W_<sub>_j_-1</sub> denote their span. Since<tbc>

\(W_{j-1}\subseteq S_{j-1}(\varepsilon)\subseteq S_j(\varepsilon)\)

<tbc>and \(\mathcal{F}_j^\mathbf{a}\subseteq S_j(\varepsilon)\), we obtain

\(\mathrm{dim}\big(S_j(\varepsilon)/W_{j-1}\big)=\mathrm{dim}(S_j(\varepsilon))-\mathrm{dim}(W_{j-1})\ge\mathrm{dim}(\mathcal{F}_j^\mathbf{a})-\mathrm{dim}(\mathcal{F}_{j-1}^\mathbf{a}).\) (38)

As \(\mathcal{C}_j(\varepsilon)\) spans \(S_j(\varepsilon)\), its image spans the quotient \(S_j(\varepsilon)/W_{j-1}\). We may therefore select

\(c_j:=\mathrm{dim}(\mathcal{F}_j^\mathbf{a})-\mathrm{dim}(\mathcal{F}_{j-1}^\mathbf{a})\)

elements of \(\mathcal{C}_j(\varepsilon)\) whose cosets are linearly independent in \(S_j(\varepsilon)/W_{j-1}\). Appending these elements to the previously selected collection produces a linearly independent set of cardinality \(\mathrm{dim}(\mathcal{F}_j^\mathbf{a})\).

Repeating the preceding selection through stage D<sub>**a**</sub> (see Definition VI.2) produces _n_=dim(g) linearly independent elements and hence a basis {_b_<sub>1</sub>_,...,b<sub>n</sub>_} of g.

**Remark VI.3.** The argument of Ref. \[9, Section 2\] also gives a useful criterion for making individual selections. Suppose that _W_ is the span of the elements already selected and that an available conjugate<tbc>

\(c\in W\cap\mathcal{C}_{j-1}(\varepsilon)\)

<tbc>satisfies \([a_i,c]\notin W\). Let \(\pi_W:\mathfrak{g}\rightarrow\mathfrak{g}/W\) denote the quotient map. Since \(c\in W\), the expansion

\(\mathrm{Ad}_{e^{ta_i}}(c)=c+t[a_i,c]+O(t^2)\)

