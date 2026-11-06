**Theorem 6.1.** _For any constant_ \(\varepsilon>0\)_, there exists a randomized algorithm that runs in time_

\(\frac{n^2}{2^{log^{\Omega(1)}(n)}}\)

_and, with high probability_<sup>21</sup>_, computes a_ \((1+\varepsilon)\)_-approximation to the edit distance for two strings with total length n._

We now focus on the query-based algorithm on the sparsified grid introduced in Section 5.2.

**Definition 5.6** (Restated)**.** The Sparsified Edit Distance Grid Graph is defined given the following parameters:

• Rounding threshold for columns: \(\mathcal{B}_x:=n/M^S=\widetilde{\Theta}(n^{0.99})\);<tbc>

• Length-relative rounding factor for rows: \(\phi_y:=2^{\left\lfloor log^{0.009}(n)\right\rfloor}\).

**Vertices** We only consider vertices \(\langle x,y\rangle\) such that

• B_<sub>x</sub>|x_;<tbc>

• Let \(s\in[S]\cup\{0\}\) be the largest scale such that _I<sub>s</sub>|x_. Then \((I_s/\phi_y)|y\).<tbc>

<sup>21</sup>A probability of at least 1-1_/n_.

\begin{tabular}{ccc}
Symbol & What it stands for & Note \\
_M_ & branching factor & \(M:=2^{\left\lfloor log(log^{0.109}(n))\right\rfloor}\) \\
_S_ & number of scales & \(S:=3\cdot\left\lfloor log_M(n^{0.01})\right\rfloor\) \\
_I<sub>s</sub>_ & width of scale _s_ & _I<sub>s</sub>_:=_n/M_<sup>_S-s_</sup> \\
B_<sub>x</sub>_ & rounding threshold for columns & B_<sub>x</sub>_:=_n/M<sup>S</sup>_ \\
\(\phi_y\) & length-relative rounding factor for rows & \(\phi_y:=2^{\left\lfloor log^{0.009}(n)\right\rfloor}\) \\
\multirow{2}{*}{\(\widetilde{S}\)} & \multirow{2}{*}{set of active scales} & **ED:** each scale chosen w.p. _S_<sup>-0.98</sup> u.a.r. \\
 & & **LCS:** each scale in \([S]\cap 3\mathbb{Z}\) chosen w.p. _S_<sup>-0.98</sup> u.a.r. \\
\(\eta_{l,r,i}\) & whether to sample _i_-th sub-interval of (_l,r_\] & \(\eta_{l,r,1\dots M}\sim\text{Uni}(\eta':\eta'\in\{0,1\}^M,\sum\eta'_i=M/2)\) \\
ew & edge weight of sparsified grid & equal to the length of best path in rotated grid \\
apprew & constant approximation of ew & for ED only \\
\(\widehat{\text{ans}}\) & length of the best \(\widetilde{S}\)-regular path & computed via (20) \\
appr & constant approximation of \(\widehat{\text{ans}}\) & for ED only, computed via (23) \\
est & our estimate for \(\widehat{\text{ans}}\) & computed via (22) \\
_m<sub>i</sub>_ & the _i_-th anchor, given (_l,r_\] in context & \(m_i:=l+i\cdot\frac{r-l}{M}\) \\
\(\unknown\) & the set of possible anchor paths \(\widehat{Y}\) & \(\widehat{Y}=(\widehat{y}_i)\) defines a path that visits each \(\langle m_i,\widehat{y}_i\rangle\) \\
<o>_y_</o><sub>i</sub> & y-coordinate for _i_-th anchor on active scale & \(\overline{y_i}:=(I_{s-1}/\phi_y)\cdot\left|\frac{y_l+i\cdot\frac{y_r-y_l}{M}}{I_{s-1}/\phi_y}\right|\) \\
\end{tabular}

2:  of notation

