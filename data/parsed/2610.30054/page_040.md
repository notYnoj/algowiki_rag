## 5.8 Operational asymptotic spectrum \(\Delta_\unknown\)

Let \(\Delta_\unknown\) be the set of functions \(F:\mathcal{F}\rightarrow\mathbb{R}_{>0}\) with \(F(\langle 1\rangle)=1\), \(F(S\oplus T)=F(S)+F(T)\) and \(F(S\otimes T)=F(S)F(T)\) for all \(S,T\in\mathcal{F}\), and with \(F(T)\le F(S)\) whenever \(T\unknown S\). This is the asymptotic spectrum of the semiring of ≈-classes of F, ordered by \(\unknown\), where _T≈S_ if \(T\unknown S\) and \(S\unknown T\).

The following theorem phrases the barrier results in the language of this asymptotic spectrum \(\Delta_\unknown\).

**Theorem 5.11** (Maximum over \(\Delta_\unknown\))**.** _For all real numbers_ \(a\ge b\ge c\ge 0\),

\(\mathrm{max}_{F\in\Delta_\unknown} F(\langle 2,1,1\rangle)^aF(\langle 1,2,1\rangle)^bF(\langle 1,1,2\rangle)^c=\left\{\begin{array}{ c c }
2^{a+b} & \text{\textit{if}}c(a+b)\le ab, \\
2^{(ab+bc+ca)^2/(4abc)} & \text{\textit{if}}c(a+b)>ab.
\end{array}\right.\)

_In particular,_ \(\mathrm{max}_{F\in\Delta_\unknown} F(\langle 2,2,2\rangle)=2^{9/4}\).

_Proof._ We sketch the proof. The central idea is that in the proof of Theorem 1.2, the properties of spectral points that are used are exactly the ones in the definition of \(\Delta_\unknown\). This establishes the upper bound (we provide a bit more detail below).

These upper bounds are subsequently attained by \(F_\theta^\star\) with the parameters of Lemma 5.6 (in the second case) and by the flattening rank R<sub>(1)</sub> (in the first case). We obtain equality because \(F_\theta^\star\in\Delta_\unknown\) (by its definition and Proposition 5.9) and \(\mathrm{R}_{(1)}\in\Delta_\unknown\) (because every relation in \(\unknown\) is a degeneration).

We now provide some more details on the upper bound. Let \(F\in\Delta_\unknown\). The proof of Proposition 4.14 uses several properties of spectral points concerning their evaluations at the tensors P_<sub>x,y,z</sub>_, and _F_ also satisfy these properties. First, _F_(P<sub>1_,m,m_</sub>)=_m<sup>p</sup>_ with _p_=log\(F(\mathsf{P}_{1,2,2})\in[0,1]\) for all \(m\ge 1\), which is the case because \(m\mapsto F(\mathsf{P}_{1,m,m})\) is multiplicative by (I3), nondecreasing by (R2) and at most _m_ by (D1). Second, \(F(\mathsf{P}_{x,y,z})\ge F(\langle 1\rangle)=1\), which follows from (R2).

Finally, the properties in Lemma 4.10, which follow from (D1)-(D4), (R) and (I) by the proofs of Lemma 4.5, Lemma 4.6 and Lemma 4.10. Zooming in on the proof of Lemma 4.5, we see that it uses that the summands are isomorphic only to compute the value of their direct sum; for _F_, additivity gives \(F(U_1\oplus\cdots\oplus U_r)=rF(U_1)\) whenever \(F(U_1)=\cdots=F(U_r)\), so that proof applies to summands with equal values of _F_. In the proof of Lemma 4.6, the summands of one type have equal values of _F_, since _F_ is multiplicative.

These are all the properties that are used in proof of Proposition 4.14 and Lemma 4.15, and hence also in the proof of Theorem 1.2. We conclude the upper bound applies.

Let \(\Delta_\unknown^\mathsf{m}:=\big\{\big(F(\langle 1,1,2\rangle),F(\langle 2,1,1\rangle),F(\langle 1,2,1\rangle)\big):F\in\Delta_\unknown\big\}\). Then \(\mathrm{log}\Delta_\mathbb{F}^\mathsf{m}\subseteq\mathrm{log}\Delta_\unknown^\mathsf{m}\subseteq Q\), for the set _Q_ of (4.4), since every relation in \(\unknown\) is a degeneration and since the proof of Theorem 5.11 shows the inequality of Proposition 4.14 for every \(F\in\Delta_\unknown\). The functions \(F_\theta^\star\) give the points (_p_<sub>1</sub>_,p_<sub>2</sub>_,p_<sub>3</sub>), since \(F_\theta^\star(\langle 1,1,2\rangle)=2^{p_1}\), \(F_\theta^\star(\langle 2,1,1\rangle)=2^{p_2}\) and \(F_\theta^\star(\langle 1,2,1\rangle)=2^{p_3}\). At these points, the inequality defining _Q_ is an equality for \(x=(1-\theta_1,1-\theta_2,1-\theta_3)\), so they lie on the curved part of the boundary of _Q_ (Figure 4, right). So Theorem 5.11 says that _aw_<sub>2</sub>+_bw_<sub>3</sub>+_cw_<sub>1</sub> has the same maximum on \(\mathrm{log}\Delta_\unknown^\mathsf{m}\) as on _Q_.

**Remark 5.12.** In fact, \(\mathrm{log}\Delta_\unknown^\mathsf{m}=Q\cap\{w\in\mathbb{R}^3:w_1+w_2\ge 1,w_1+w_3\ge 1,w_2+w_3\ge 1\}\). In particular, \(\mathrm{log}\Delta_\unknown^\mathsf{m}\) is convex and contains the part of _Q_ with \(w_1+w_2+w_3\ge 2\) shown in Figure 4. We omit the proof.

