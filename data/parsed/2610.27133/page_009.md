_Proof._ Use the balanced sequence \(\widehat{c}_1,\dots,\widehat{c}_m\) from Proposition 10. These are not necessarily the actual color-class sizes of _H_. Their sum is \(|V|-\alpha\), and _D_ is the least index for which the first _D_ terms sum to at least \(\alpha\).

Set \(g=U-L\ge 0\). We prove that \(L\ge 5g-1\). Since \(U\le\chi_P-1=L+D-1\), we obtain \(g\le D-1\). By minimality of _D_, it follows that<tbc>

\(\widehat{c}_D(D-1)\le\widehat{c}_1+\cdots+\widehat{c}_{D-1}\le\alpha-1.\)

<tbc>Consequently,

\(\alpha\ge\widehat{c}_Dg+1.\) (10)

Since \(\sum_{i=1}^m\widehat{c}_i=|V|-\alpha\), and \(\widehat{c}_i\le\widehat{c}_D\) for \(i\ge D\),

\(|V|=\alpha+\sum_{i=1}^{D-1}\widehat{c}_i+\sum_{i=D}^m\widehat{c}_i\le\alpha+(\alpha-1)+\widehat{c}_D(m-D+1).\) (11)

Since \(U=L+g=\alpha+m-D+g\) and \(U\le|V|/2\) (by definition), inequality (11) yields

\((\widehat{c}_D-2)(m-D+1)\ge 2g-1.\) (12)

We use \(L=\alpha+m-D\) and \(m-D\ge 0\) to consider the following four cases:

\(\begin{array}{ c c c c }
\widehat{c}_D & \text{From(12)} & \text{From(10)} & \text{Conclusion} \\
2 & g=0 & - & L\ge 5g-1 \\
3 & m-D\ge 2g-2 & \alpha\ge 3g+1 & L\ge 5g-1 \\
4 & m-D\ge g-1 & \alpha\ge 4g+1 & L\ge 5g \\
\ge 5 & - & \alpha\ge 5g+1 & L\ge 5g+1
\end{array}\)

Therefore, \(5g\le L+1\), which gives \(5U\le 6L+1\).

For \(L\le 3\) we obtain _U=L_. For \(L\ge 4\),

\(\frac{U}{L}\le\frac{6}{5}+\frac{1}{5L}\le\frac{5}{4}.\)

_Remark._ The conclusions of Theorem 11 also hold with _L<sub>d</sub>_ in place of _L_. Indeed, \(L\le L_d\le\chi_B\), so \(5U\le 6L+1\le 6L_d+1\) and \(\chi_B/L_d\le\chi_B/L\le 5/4\).

We prove that for fixed parameters \((|V|,\chi_P,\alpha)\), without more information, the bound _L_ is the best possible.

**Proposition 12** (Optimality)**.** _For any valid parameters_ \((|V|,\chi_P,\alpha)\)_, with_ \(0<\alpha<\frac{|V|}{2}\) _, there exists a hypergraph with these prescribed parameters that satisfies_ \(\chi_B=L\).

_Proof._ Compute _q_ and _r_ as before. Set \(m=\chi_P-\alpha\) and consider pairwise disjoint sets _S,P_<sub>1</sub>_,...,P<sub>q</sub>,Z_ with \(|S|=\alpha\), |_P<sub>i</sub>_|=_m_, and |_Z_|=_r_. Choose \(R\subseteq P_1\) with |_R_|=_r_. We define the hypergraph _H_=(_V,_E), where<tbc>

\(V=S\sqcup\sqcup_{i=1}^qP_i\sqcup Z,\mathcal{E}=\{S\sqcup P_i:i\in[q]\}\cup\{S\sqcup(P_1\backslash R)\sqcup Z\}.\)

<tbc>Thus \(|V|=\alpha+qm+r\) is attained, and every hyperedge has size \(\chi_P\). Now, we define a coloring of _H_ such that \(\alpha\) vertices in _S_ receive distinct colors, each _P<sub>i</sub>_ uses all _m_ remaining colors<tbc>

