where _R<sub>i</sub>_ has polynomial coefficients in \(\xi,\varepsilon\).

_Decode._ For every block _j_ in group _i_, evaluate this same polynomial at \(\xi=i+\varepsilon j\). By the definition of \(B'_i\),

\(\widetilde{P}_i(i+\varepsilon j)=F_i(A(i+\varepsilon j),B_{i,j})+\varepsilon R_i(i+\varepsilon j,\varepsilon)\equiv F_i(A_i,B_{i,j})(\mathrm{mod}\varepsilon).\)

The last congruence follows from \(A(i+\varepsilon j)\equiv A(i)=A_i(\mathrm{mod}\varepsilon)\). Concatenating the recovered blocks gives _F<sub>i</sub>(A<sub>i</sub>,B<sub>i</sub>_) modulo \(\varepsilon\). Interpolation, evaluation, and concatenation are linear decoding maps. There are 2_M_-1 applications of the given packing, each using _N_ sources of the original sizes.

We apply this lemma after concatenating the same-left source products into one wider product. With independent left inputs, each target can then be put into the canonical Full set _I_<sub>0</sub>.

**Theorem 2.9** (Multivariate polynomial packing)**.** _Let c,d be positive integers, take u,w from_ (4)_, and put_ \(\alpha=2w-1\)_. If_ \(w\ge 2\)_, then for all positive integers a,b,t with_ \(ct\ge a+2b-1\)_, there is a packing modulo_ \(\varepsilon\) _of w independent copies of_ \(F_{a,b}^{(d)}\) _on coefficient sizes_ \(p\times q,q\times wr\)_, using_ \(\alpha\) _copies of_ \(F_{a,b+t}^{(d)}\) _on sizes_ \(p\times q,q\times ur\)_, for all positive integers p,q,r._

_Proof._ Take the Full sets _I<sub>i</sub>_ and same-left packing from Lemma 2.7. Its _u_ source right inputs can be concatenated horizontally: the resulting single source has column width _ur_, and its output splits into the original _u_ outputs. Apply Lemma 2.8 with _M=w_, _N_=1, and \(S=F_{a,b+t}^{(d)}\). This gives independent targets _F_<sub>_a,b,I<sub>i</sub>_</sub> with the claimed sizes and source count.

For each _i_, choose the variable permutation \(\pi_i\) sending the first _d_ positions to the elements of _I<sub>i</sub>_ in increasing order, and the remaining positions to its complement in increasing order. Given canonical inputs (_A<sub>i</sub>,B<sub>i</sub>_), encode \((\pi_iA_i,\pi_iB_i)\) in target _i_ and undo \(\pi_i\) on its output. Renaming variables commutes with multiplication and sends exactly the input lengths and output ranges of \(F_{a,b}^{(d)}\) to those of _F_<sub>_a,b,I<sub>i</sub>_</sub>. Consequently the decoded result is \(F_{a,b}^{(d)}(A_i,B_i)\). The variable permutations depend only on _c,d_; their induced coefficient reindexings are linear.

For the exponent bound, take \(c\ge 2\) and _d=c_<sup>3</sup>. Rounding in (4) loses at most a factor of two, so

\(\frac{(1+2/c)^{2d}}{2(d+1)}\le\frac{w}{u}\le\frac{(1+2/c)^{2d}}{d+1},\mathrm{log}(w/u)=4c^2+O(c).\) (5)

In particular _w\>_2_u_: using \(\mathrm{log}(1+x)\ge x/(1+x)\), the logarithm of the lower bound is at least 2_c_<sup>2</sup>-3log_c_-2log2_\>_log2 for \(c\ge 2\).

## 3 Reducing all matrix dimensions

We now turn the column reduction into a reduction in rows, inner dimension, and columns simultaneously. We also establish the \(a\leftrightarrow b\) symmetry and the terminal multiplication bound needed to compose these reductions.

