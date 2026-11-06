That is, \(I_\ell\) is the set of rows that violate the row-regularity condition for \(\ell\), and \(J_\ell\) is the set of columns that violate the column-regularity condition for \(\ell\). Let \(A=A_\text{row}\sqcup A_\text{col}\sqcup A_\text{sm}\) denote the partition of _A_ where in _A_row we retain the entries (_i,j_) with \(i\unknown\in I_{S[i,j]}\), in _A_col we retain the entries (_i,j_) with \(i\in I_{S[i,j]}\) and \(j\unknown\in J_{S[i,j]}\), and in _A_sm we retain the entries (_i,j_) with \(i\in I_{S[i,j]}\) and \(j\in J_{S[i,j]}\); we will call these entries (_i,j_) _irregular_. In the following we argue that the three matrices _A_row_,A_col_,A_sm admit the claimed rank decompositions.

## Rank Decomposition of _A_row and _A_col.

It is simple to construct an _R_-row-regular rank-_r_ decomposition (_U_row_,V_row_,S_row) of _A_row: Take _U_row=_U_ and _V_row=_V_ , and let _S_row be the restriction of _S_ to the entries (_i,j_) satisfying that \(i\unknown\in I_{S[i,j]}\). This is clearly a valid rank-_r_ decomposition of _A_row. To see that it is also _R_-row-regular, focus on any \(\ell\in[r]\) and any row \(i\in[n]\). In _S_row we have only retained the entries \(S[i,j]=\ell\) with \(i\unknown\in I_\ell\), hence by definition \(|\{j\in[m]:S_\text{row}[i,j]=\ell\}|\le R\cdot\frac{m}{r}\). The construction for _A_col is analogous.

## Rank Decomposition of _A_sm.

Next, we construct a rank-_r/_2 decomposition (_U_sm_,V_sm_,S_sm) of _A_sm. In this step we will crucially rely on the covering lemma from before. Specifically, for each irregular pair (_i,j_) define<tbc>

\(x_{i,j}=S[i,j],\)

<tbc>and<tbc>

\(C_{i,j}=\{\ell\in[r]:i\in I_\ell\text{or}j\in J_\ell\}\backslash\{S[i,j]\}.\)

<tbc>We run Lemma 3.7 on the items \(x_{i,j}\in[r]\) and conflict sets \(C_{i,j}\subseteq[r]\). Let S denote the resulting collection of sets, and write \(T_{i,j}\in\mathcal{S}\) for the set covering (_i,j_). Let \(U_\text{sm}\in\mathbb{Z}^{[n]\times\mathcal{S}},V_\text{sm}\in\mathbb{Z}^{\mathcal{S}\times[m]},S_\text{sm}\in(\mathcal{S}\cup\{\perp\})^{n\times m}\) be the matrices defined as follows (here, for simplicity of notation we assume that the columns of _U_sm, the rows of _V_sm, and the entries of _S_sm are indexed by sets \(T\in\mathcal{S}\), but this can easily be replaced by the integers \([|\mathcal{S}|]\)):

\(U_\text{sm}[i,T]=\left\{\begin{array}{ c c }
U[i,\ell] & \text{for some}\ell\in T\text{with}i\in I_\ell, \\
0 & \text{if such}\ell\text{does not exist},
\end{array}\right.\)<br>
\(V_\text{sm}[T,j]=\left\{\begin{array}{ c c }
V[\ell,j] & \text{for some}\ell\in T\text{with}j\in J_\ell, \\
0 & \text{if such}\ell\text{does not exist},
\end{array}\right.\)<br>
\(S_\text{sm}[i,j]=\left\{\begin{array}{ c c }
T_{i,j} & \text{if (}i,j\text{) is irregular,} \\
\perp & \text{otherwise.}
\end{array}\right.\)

(The assignment 0 of _U_sm_,V_sm in the failure case is arbitrary.) We claim that (_U_sm_,V_sm_,S_sm) is a valid decomposition of _A_sm. This is trivially true for the regular pairs, so fix some irregular pair (_i,j_). Lemma 3.7 guarantees that \(x_{i,j}\in T_{i,j}\) and \(C_{i,j}\cap T_{i,j}=\emptyset\). This means that \(\ell:=x_{i,j}=S[i,j]\) is the only element in _T<sub>i,j</sub>_ that satisfies \(i\in I_\ell\) or \(j\in J_\ell\), and thus

\(U_\text{sm}[i,T_{i,j}]=U[i,\ell],\)<br>
\(V_\text{sm}[T_{i,j},j]=V[\ell,j].\)

Hence,

\(U_\text{sm}[i,S_\text{sm}[i,j]]+V_\text{sm}[S_\text{sm}[i,j],j]=U_\text{sm}[i,T_{i,j}]+V_\text{sm}[T_{i,j},j]=U[i,\ell]+V[\ell,j]=A_\text{sm}[i,j].\)

It follows that we have indeed constructed a valid rank-|S| decomposition. We finally argue that \(|\mathcal{S}|\le r/2\) for an appropriate choice of parameters. First observe that each conflict set _C<sub>i,j</sub>_ has size at most _s_:=2_r/R_, as each index _i_ is part of at most _r/R_ sets \(I_\ell\), and similarly each index _j_ is part of at most _r/R_ sets \(J_\ell\). Therefore, by Lemma 3.7 we have \(|\mathcal{S}|\le O(slog(nm))=O(rlog(nm)/R)\). Hence, picking \(R=\Theta(log(nm))\) for some sufficiently large hidden constant, we get that \(|\mathcal{S}|\le r/2\) as was intended.

