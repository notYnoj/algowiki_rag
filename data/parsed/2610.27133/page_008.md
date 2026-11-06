Recolor all vertices in the first _d_ color classes with the \(\alpha\) unique colors so that each of these colors is used at least twice. This yields a bipanchromatic coloring of _H_ with \(L_d=\chi_P-d\) colors.

Since \(c_i\ge 2\) for every _i_, we have \(d\le\lceil\alpha/2\rceil\). Consequently, \(\chi_B\ge L_d=\chi_P-d\ge\beta\).

To obtain a bound for _d_, write Euclidean division of \(|V|-\alpha\) by \(m=\chi_P-\alpha\) as:<tbc>

\(|V|-\alpha=qm+r,\)<br>
\(q=\left\lfloor\frac{|V|-\alpha}{\chi_P-\alpha}\right\rfloor\ge 2,0\le r<m.\)

<tbc>Define

\(D=max\left\{\left\lceil\frac{\alpha}{q+1}\right\rceil,\left\lceil\frac{\alpha-r}{q}\right\rceil\right\},L=\chi_P-D.\) (7)

Unlike _L<sub>d</sub>_, which uses the chosen coloring, _L_ depends only on \(|V|,\chi_P\), and \(\alpha\).

**Proposition 10** (Least class recoloring)**.** _Assume that the parameters of a hypergraph are defined as above. If_ \(0<\alpha<|V|/2\)_, then_<tbc>

\(d\le D\le\left\lceil\frac{\alpha}{2}\right\rceil,\beta\le L\le L_d\le\chi_B.\)

<tbc>_Proof._ For every \(j\in[m]\), if \(c_j\ge q+1\), the first _j_ classes contain at least _j(q_+1) vertices. Otherwise, the last _m-j_ classes contain at most (_m-j)q_ vertices, so the first _j_ contain at least _jq+r_. Thus<tbc>

\(\sum_{i=1}^jc_i\ge jq+min\{j,r\}.\)

<tbc>The balanced sequence

\(\widehat{c}_1=\cdots=\widehat{c}_r=q+1,\widehat{c}_{r+1}=\cdots=\widehat{c}_m=q\)

attains equality for every _j_. Its first _j_ terms sum to at least \(\alpha\) exactly when both \(j(q+1)\ge\alpha\) and \(jq+r\ge\alpha\), so _D_ is its least such index. Therefore \(d\le D\). Since \(q\ge 2\) and \(r\ge 0\), the formula for _D_ gives \(D\le\lceil\alpha/2\rceil\), proving the stated bounds.

_Remark._ If the three-hyperedge family described in \[5, Proposition 1\] satisfies \(0<\alpha<|V|/2\), then its parameters considered in Proposition 10 are _q_=3, _r_=0, and \(D=\alpha/3\). Thus \(L=\chi_P-\alpha/3=\chi_B\). The boundary case \(2\alpha=|V|\) is covered by the observation at the start of this section. So, our order-aware bound gives the exact bipanchromatic number throughout that family.

Let \(U=min\{\chi_P-1,\lfloor|V|/2\rfloor\}\). If \(0<\alpha<|V|/2\), then \(\beta\le L\le L_d\le\chi_B\le U\), and _U_ is an upper bound for \(\chi_B\).

Now, we examine the relations between _U_, \(\chi_B\), and _L_.

**Theorem 11** (Improved bound ratio)**.** _The bounds L and U always satisfy_<tbc>

\(5U\le 6L+1,1\le\frac{\chi_B}{L}\le\frac{U}{L}\le\frac{5}{4}.\) (8)

<tbc>_In particular,_ \(L\le 3\) _implies U=L. For all feasible inputs,_<tbc>

\(\frac{\chi_B}{L}\le\frac{6}{5}+\frac{1}{5L}.\) (9)

