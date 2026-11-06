<tbc>Lemma 5.1 (Compact formula for the infGMRES residual). _Let_ \(b_m^*=e_1^*R_m^{-1}\)_. For_ \(s\neq 0\),

\(\frac{\mathcal{R}_m(s)}{\|z\|_2}=\frac{1}{\sqrt{1+\|z\|_2^2\|(sI_m-K_m)^{-*}b_m\|_2^2}}.\)

_Proof._ R_<sub>m</sub>(s_) is the distance from \(\|z\|_2e_1\) to the column space of \(\left[\begin{array}{ c }
I_m \\
0_{1\times m}
\end{array}\right]-s\underline{H_m}\). We determine the direction orthogonal to this column space.

By (3.3), the nested QR factors, and \(K_m=R_mJ_mR_m^{-1}\), we have

\(\left(\left[\begin{array}{ c }
I_m \\
0_{1\times m}
\end{array}\right]-s\underline{H_m}\right)\left[\begin{array}{ c c }
\|z\|_2 & 0 \\
0 & R_{m-1}
\end{array}\right]R_m^{-1}=\left[\begin{array}{ c }
\|z\|_2b_m^* \\
K_m
\end{array}\right]-s\left[\begin{array}{ c }
0 \\
I_m
\end{array}\right]\)<br>
\(=\left[\begin{array}{ c }
\|z\|_2b_m^* \\
K_m-sI_m
\end{array}\right].\)

Because \(\left[\begin{array}{ c c }
\|z\|_2 & 0 \\
0 & R_{m-1}
\end{array}\right]R_m^{-1}\) is nonsingular, so \(\left[\begin{array}{ c }
I_m \\
0_{1\times m}
\end{array}\right]-s\underline{H_m}\) and \(\left[\begin{array}{ c }
\|z\|_2b_m^* \\
K_m-sI_m
\end{array}\right]\) have the same column space.

For \(s\neq 0\), nilpotency of _K<sub>m</sub>_ makes _sI<sub>m</sub>-K<sub>m</sub>_ nonsingular. Thus this column space has a one-dimensional orthogonal complement, which is spanned by<tbc>

\(\left[\begin{array}{ c }
1 \\
\|z\|_2(sI_m-K_m)^{-*}b_m
\end{array}\right].\)

<tbc>Then R_<sub>m</sub>(s_) is the length of the projection of \(\|z\|_2e_1\) onto this direction. So

\(\frac{\mathcal{R}_m(s)}{\|z\|_2}=\frac{1}{\sqrt{1+\|z\|_2^2\|(sI_m-K_m)^{-*}b_m\|_2^2}}.\) □

Theorem 5.2 (An infGMRES residual lower bound). _Let_ \(C_m=\|[A_0,\dots,A_{m-1}]\|_2\)_. For every_ |_s|\>_1,

(5.1) \(\frac{\mathcal{R}_m(s)}{\|z\|_2}\ge\frac{|s|-1}{\sqrt{(|s|-1)^2+C_m^2}}.\)

_Let_ \(C_\infty^2:=\sum_{j\ge 0}\|A_j\|_2^2\)_, then_ \(C_m\le C_\infty\)_, so we can replace C<sub>m</sub> by_ \(C_\infty\)_. Moreover, if A(s_) _is analytic in a disk centered at zero with radius greater than one, then_ \(C_\infty<\infty\).

_Proof._ The generator recurrence (3.1) gives \([A_0,\dots,A_{m-1}]V_m=ze_1^*\), so

\([A_0,\dots,A_{m-1}]Q_m=zb_m^*.\)

Taking 2-norm yields \(\|z\|_2\|b_m\|_2\le C_m\).

For |_s|\>_1, \(\|K_m\|\le 1\) and \(K_m^m=0\) give

\(\|(sI_m-K_m)^{-1}\|_2=\left\|s^{-1}\sum_{j=0}^{m-1}\left(\frac{K_m}{s}\right)^j\right\|_2\le\sum_{j=0}^{m-1}|s|^{-j-1}\le(|s|-1)^{-1}.\)

Now with Lemma 5.1, we can prove (5.1). The inequality \(C_m\le C_\infty\) follows from

\(C_m^2=\left\|\sum_{j=0}^{m-1}A_jA_j^*\right\|_2\le\sum_{j=0}^{m-1}\|A_j\|_2^2\le C_\infty^2.\)

