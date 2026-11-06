<tbc>number of errors that can be corrected in the decoding problem. However, in \[Jor+25\], for max-2- LINSAT over F<sub>2</sub> with random target sets, it was shown that this advantage is outweighed by the lower optimal-decoding threshold of cycle codes, relative to the LDPC ensembles in which bits are contained in three or more parity checks.

Here, we investigate a natural next question: what happens when we no longer restrict our attention to a binary alphabet? DQI reduces Max-2-LINSAT to decoding a non-binary generalization of cycle codes. Prior to the present work, these were poorly understood compared to binary cycle codes. One of the main contributions of this paper is to initiate the study of _q_-ary cycle codes (hereafter simply "cycle codes"). We resolve several foundational questions about the decoding complexity and reliability of _homological_ cycle codes, in which the two nonzero coefficients in a column of the parity check matrix sum to zero. These results are summarized in  1. A polynomial-time linear programming (LP) decoder also has a provably positive error-rate guarantee on this ensemble (Corollary 2), although we do not prove that it attains the ML threshold.

\begin{tabular}{ccc}
 & **Binary cycle codes** & **Nonbinary cycle codes (this paper)** \\
 & F<sub>2</sub> & F_<sub>q</sub>_, any prime power _q\>_2 \\
Parity-check & 2 checks per bit; & 2 checks per symbol; \\
structure & _D_ bits per check \[NZ16\] & _D_ symbols per check (§3) \\
 rate & \(1-\frac{2}{D}+\frac{1}{m}\) \[NZ16\] & \(1-\frac{2}{D}+\frac{1}{m}\) (§3) \\
Minimum distance & _d_<sub>min</sub>=_g<sub>G</sub>_, & _d_<sub>min</sub>=_g<sub>G</sub>_ (same as _q_=2) \\
Guaranteed & \(t_\mathrm{wc}=\left\lfloor\frac{g_G-1}{2}\right\rfloor\) \[NZ16\] & \(t_\mathrm{wc}=\left\lfloor\frac{g_G-1}{2}\right\rfloor\) (§3) \\
unique-decoding radius & & \\
ML word error: & \(\delta_\mathrm{rel}(D,2)=\delta_\mathrm{cyc}(D,2)\), & If \(q/D^{2/3}\le 1/32\) then \\
 & where \(\delta_\mathrm{cyc}\) is as defined in (78). & \(\left(1-\frac{16q}{D^{2/3}}\right)\delta_\mathrm{cyc}\le\delta_\mathrm{rel}(D,q)\le\delta_\mathrm{cyc}(D,q)\), \\
 & Proven in \[DZ97; NZ16\]. & where \(\delta_\mathrm{cyc}(D,q)\) is as defined in (78). \\
 & & Proven in §3.2 and Appendix A. \\
Exact ML / & Minimum-weight _T_-join; & NP-hard for every fixed _q\>_2 \\
nearest-codeword computation & polynomial time \[EJ73\] & (§3.1, Theorem 2) \\
Efficient average-case & & \\
decoding & The same \(\delta_\mathrm{rel}(D,2)\) is attained by & Polynomial-time LP decoding corrects \(\Theta(m)\) \\
 & & randomly located symbol errors: \(P_\mathrm{W}^\mathrm{LP}\rightarrow 0\) \\
 & & for every \(0<p<p_\mathrm{LP}^\mathrm{cert}(D,c)\) (Corollary 2). \\
 & & This certified rate need not equal the ML \\
 & & threshold. Observed recovery extends \\
 & & beyond this rate (§3.3.3). \\
\end{tabular}

** 1: Binary versus nonbinary homological cycle codes.** Here the block length is _m_ and the number of parity checks is _n_. The graph degree is _D_, and therefore _m=Dn/_2. For independent uniformly distributed nonzero errors, maximum-likelihood (ML) decoding limits concern whole-word error averaged over the Linial-Simkin ensemble of Definition 4, as \(n\rightarrow\infty\) at fixed degree _D_, fixed finite field size _q_, fixed Linial-Simkin girth parameter _c_, and fixed error probability \(p\in(0,1-1/q)\).

