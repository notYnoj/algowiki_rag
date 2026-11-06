<tbc>Assume that we have just finished step _m_ of Toeplitz infGMRES. Now we wish to determine whether using equation (3.12) to update _u_<sub>_m_+1</sub> at step _m_+1 will cause severe cancellation. This means that we need an indicator to estimate \(\kappa_{m+1}^\text{canc}\), with the known quantities at step _m_.

To estimate this cancellation, we use the computable indicator

(3.13) \(\eta_m=\left\{\begin{array}{ c c }
\frac{2\|G_mS_mt_m(1:m-1)\|_2}{|t_m(m)|\|u_m\|_2}, & |t_m(m)|\|u_m\|_2>0, \\
+\infty, & |t_m(m)|\|u_m\|_2=0,
\end{array}\right.\)

where _G<sub>m</sub>_:=\[_q_<sub>1,1</sub>_,...,q_<sub>1_,m_</sub>\] is the first block row of _Q<sub>m</sub>_.

By the definitions of _G<sub>m</sub>_ and _S<sub>m</sub>_, we have

\(G_mS_m=[q_{1,1},\dots,q_{1,m}]R_m(:,2:m)R_{m-1}^{-1}=[a_2,\dots,a_m]R_{m-1}^{-1}=[u_2,\dots,u_m].\)

Thus, with _c_<sub>_m_+1</sub>=\[_u_<sub>2</sub>_,...,u<sub>m</sub>_\]_t<sub>m</sub>_(1:_m_-1), the numerator of \(\eta_m\) is 2\(\|c_{m+1}\|_2\). So

\(\frac{\eta_m}{\kappa_{m+1}^\text{canc}}=\frac{2\|c_{m+1}\|_2}{\|a_{m+1}\|_2+\|c_{m+1}\|_2}\frac{\|u_{m+1}\|_2}{\|u_m\|_2}.\)

By the reverse triangle inequality, the first ratio on the right differs from one by at most \(1/\kappa_{m+1}^\text{canc}\). Hence when \(\kappa_{m+1}^\text{canc}\) is large, \(\eta_m\) tracks prospective cancellation up to \(\|u_{m+1}\|_2/\|u_m\|_2\) and is of the same order when the norms of consecutive recovery vectors are comparable.

**3.4. Dynamic stabilization.** To weaken the cancellation, we recover selected Arnoldi vectors when the cancellation is detected. Here we consider how to construct selected Arnoldi vectors.

Because of the Toeplitz structure of _V<sub>m</sub>_, there exist vectors \(e^{i,m}\in\mathbb{C}^m\) satisfying

(3.14) \(q_{i,m}=G_me^{i,m},1\le i\le m.\)

Here we can always assume _e<sup>i,m</sup>_ is padded with zeros to arbitrarily large length.

Lemma 3.2 (Block recovery). _The recurrence of_ {_e<sup>i,m</sup>_} _is_

(3.15) \(e^{1,m}=e_m,\)

(3.16) \(e^{i,m}=\frac{e^{i-1,m-1}-\sum_{k=i}^{m-1}S_m(k,m-1)e^{i,k}}{S_m(m,m-1)},2\le i\le m.\)

_Proof._ The relation _e_<sup>1_,m_</sup>=_e<sub>m</sub>_ follows directly from the identity _q_<sub>1_,m_</sub>=_G<sub>m</sub>e<sub>m</sub>_. Moreover,

(3.17) \(Q_mS_m=Q_mR_m(:,2:m)R_{m-1}^{-1}=\left[\begin{array}{ c }
[u_2,\dots,u_m] \\
Q_{m-1}
\end{array}\right].\)

For \(2\le i\le m\), taking block row _i_ and column _m_-1 of (3.17) and using _q<sub>i,k</sub>_=0 for _k\<i_ gives

\(q_{i-1,m-1}=\sum_{k=i}^mS_m(k,m-1)q_{i,k}.\)

Solving for _q<sub>i,m</sub>_, using _G<sub>k</sub>=G<sub>m</sub>_(:,1:_k_), and zero-padding yields the recurrence. \(\square\)

