_Proof of Theorem 6.2. Openness._ Fix \(g\in\mathcal{E}_\mathrm{sc}(a,d)\), and let _S_ be a certificate for _g_ that is positive definite on \(u^\perp\). Write \(\kappa>0\) for the smallest eigenvalue of _S_ restricted to \(u^\perp\). For \(h\in\mathcal{Q}(a,d)\), the matrix _S_+B_<sub>a,d</sub>(h_) still annihilates _u_ and represents _g+h_. By (G.3) it stays positive definite on \(u^\perp\) whenever \(\|h\|_\mathrm{coef}<\kappa/(2\sqrt{|\mathcal{I}_{2d}|-1})\). Hence \(g+h\in\mathcal{E}_\mathrm{sc}(a,d)\).

_Density._ If \(g\in\mathcal{E}(a,d)\), primal Slater gives an optimal Gram matrix \(S\unknown 0\) representing _g_, and \(u^\top Su=g(a)=0\) forces _Su_=0. For every \(\varepsilon>0\), \(S+\varepsilon S_\mathrm{int}\) represents \(g+\varepsilon r_{a,d}\) and is positive definite on \(u^\perp\), so \(g+\varepsilon r_{a,d}\in\mathcal{E}_\mathrm{sc}(a,d)\), and \(g+\varepsilon r_{a,d}\rightarrow g\) as \(\varepsilon\rightarrow 0\).

_Semialgebraicity._ With \(P_{u^\perp}=I_N-uu^\top/N\), membership in E<sub>sc</sub>(_a,d_) is the existential first-order formula \(\exists S,t:\mathcal{G}_d(S)=g,Su=0,S-tP_{u^\perp}\unknown 0\), _t\>_0; PSD-ness is finitely many minor inequalities. Membership in E(_a,d_) is \(g\in\mathcal{Q}(a,d)\) together with \(\nexists X\in\mathcal{X}_d:\|X-uu^\top\|_F^2>0,\langle C_g,X\rangle\le 0\). The Tarski-Seidenberg theorem and closure under complements make both cells semialgebraic \[BCR98\].

_Dimension._ Abbreviate E<sub>sc</sub>:=E<sub>sc</sub>(_a,d_) and E:=E(_a,d_); density gives \(\mathcal{E}_\mathrm{sc}\subseteq\mathcal{E}\subseteq\mathrm{cl}\mathcal{E}_\mathrm{sc}\). The semialgebraic frontier theorem gives dim(clE<sub>sc</sub>\\E<sub>sc</sub>)_\<_dimE<sub>sc</sub> and dimclE<sub>sc</sub>=dimE<sub>sc</sub> \[BCR98, Propositions 2.8.2 and 2.8.13\]. Hence dim(E\\E<sub>sc</sub>)_\<_dimE. The open neighborhood of _r<sub>a,d</sub>_ shows dimE=dimQ(_a,d_)=|I<sub>2_d_</sub>|-1. The exceptional set therefore has zero Lebesgue measure in Q(_a,d_).

### G.3 Ambient genericity

**Proposition G.1** (Simultaneous SC at every uniquely rank-one exact order)**.** _There is an open dense full-measure semialgebraic set_ \(\mathcal{G}_\mathrm{gen}\subseteq\mathcal{P}_n\) _such that every_ \(f\in\mathcal{G}_\mathrm{gen}\) _has a unique Boolean minimizer and, at every order_ \(d_\star(f)\le d\le n\)_, the relaxation admits a rank-(N<sub>d</sub>_-1) _optimal certificate._

_Proof._ First exclude the finite union of proper tie hyperplanes \(E_\mathrm{tie}:=\bigcup_{a\neq b}\{f:f(a)=f(b)\}\); each is proper because some linear monomial distinguishes _a_ from _b_. For each pair (_a,d_), let _B<sub>a,d</sub>_:=E(_a,d_)\\E<sub>sc</sub>(_a,d_) and lift it to the full coefficient space by the additive constant, \(\widetilde{B}_{a,d}:=\{g+c:g\in B_{a,d},c\in\mathbb{R}\}\). The map \((g,c)\mapsto g+c\) is injective on this domain (because _g(a_)=0 recovers _c=f(a_)), so for nonempty _B<sub>a,d</sub>_,

\(\mathrm{dim}\widetilde{B}_{a,d}=\mathrm{dim}B_{a,d}+1<|\mathcal{I}_{2d}|\le 2^n\)

by Theorem 6.2. Let _E_<sub>bad</sub> be the union of _E_<sub>tie</sub> with the finitely many \(\widetilde{B}_{a,d}\), and set G<sub>gen</sub>:=P_<sub>n</sub>_\\cl_E_<sub>bad</sub>. Finite unions and closures preserve semialgebraicity and dimension, so dimcl_E_<sub>bad</sub>_\<_2_<sup>n</sup>_ and G<sub>gen</sub> is open, dense, and full measure. For \(f\in\mathcal{G}_\mathrm{gen}\) with minimizer _x<sub>⋆</sub>_, Theorem 6.1 gives \(d_\star(f)\le n\) and unique rank-one exactness at every order \(d\in[d_\star(f),n]\). At each such order, \(f-f(x_\star)\in\mathcal{E}(x_\star,d)\). Since _f_ avoids the corresponding lifted bad set, this normalized objective lies in E<sub>sc</sub>(_x<sub>⋆</sub>,d_).

The proof of Theorem 6.3 in §6 assembles Theorem G.1 with Theorems B.1, B.2, 3.2 and 4.2 and the transfer results of §5.

## H Details of the Illustrative Experiments

This appendix records the setup behind Figure 1 and one further illustration for a higher-degree objective. The experiments are illustrations of the theory rather than a benchmark; no timing comparison is intended.

### General setup.

All runs except the saved run of panel (a) use the exact ADMM of §5 with multiplier step \(\tau=1\) and a fixed penalty \(\sigma\) (reported per experiment), implemented in MATLAB, stopped when the maximal KKT residual falls below 10<sup>-10</sup>. The maximal KKT residual is max{_r_<sub>p</sub>_,r_<sub>d</sub>_,r_<sub>g</sub>} with _r_<sub>p</sub>=<tbc>

