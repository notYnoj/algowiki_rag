## A Depth one QAOA expectation values are exactly tractable

For an edge _e_={_u,v_}, let _d<sub>u</sub>,d<sub>v</sub>_ be the endpoint degrees and \(\lambda_{uv}=|N(u)\cap N(v)|\). For each single edge term _C<sub>uv</sub>_=(_I-Z<sub>u</sub>Z<sub>v</sub>)/_2 the standard depth-one QAOA calculation \[4,12\] gives

\(\langle C_{uv}\rangle_{p=1}=\frac{1}{2}+\frac{1}{4}\mathrm{sin}(4\beta)\mathrm{sin}\gamma\left(\mathrm{cos}^{d_u-1}\gamma+\mathrm{cos}^{d_v-1}\gamma\right)\)<br>
\(-\frac{1}{4}\mathrm{sin}^2(2\beta)\mathrm{cos}^{d_u+d_v-2\lambda_{uv}-2}\gamma\left(1-\mathrm{cos}^{\lambda_{uv}}(2\gamma)\right),\) (37)

with \(F_1(G;\gamma,\beta)=\sum_{\{u,v\}\in E}\langle C_{uv}\rangle_{p=1}\). This formula follows by conjugating _Z<sub>u</sub>Z<sub>v</sub>_ by the mixer and phase operators, and retaining only Pauli strings with nonzero expectation values for the initial state \(|+\rangle^{\otimes n}\). This result supplies the efficient depth one case of the main complexity dichotomy.

**Proposition A.1.** \(\mathrm{Eval}_1^{uv}\), \(\mathrm{Eval}_1^\mathrm{MC}\in\mathsf{FP}\).

_Proof._ Compute all degrees and common-neighbor counts, evaluate (37) for every edge, and sum, which requires a number of operations polynomially scaling in the problem size. Under the exact input model specified in Appendix B, repeated squaring and exact field arithmetic evaluate the formula with polynomial bit complexity.

Our results above show that, under standard complexity-theoretic assumptions, no analogous exact efficiently computable formulas are possible for arbitrary graphs with \(p\ge 2\) in general.

## B Single-query exact hardness with equal fixed mixers

The proof of Theorem 1.2 uses polynomially many values of the tied phase angle to recover the Laurent coefficients. For exact algebraic evaluation, the same coefficients can instead be read from a single cyclotomic-field output.

For exact evaluation, we use the following explicit number field representation. An exact instance supplies a common number field \(K=\mathbb{Q}(\theta)\) by an irreducible defining polynomial and isolating data identifying the chosen complex root \(\theta\). With \(d=[K:\mathbb{Q}]\), each value \(a_0+a_1\theta+\cdots+a_{d-1}\theta^{d-1}\) is represented by its list of rational basis coefficients (_a_<sub>0</sub>_,...,a_<sub>_d_-1</sub>), encoded in binary. The input supplies such lists for i, for each cost phase \(z_j=e^{\mathrm{i}\gamma_j}\), and for each mixer pair \((c_j,s_j)=(\mathrm{cos}\beta_j,\mathrm{sin}\beta_j)\). The input is promised to satisfy |_z<sub>j</sub>_|=1, \(c_j,s_j\in\mathbb{R}\), and \(c_j^2+s_j^2=1\) under that embedding. The exact oracle returns the coefficient list of the expectation value in the same field and basis. Input and output lengths are the respective total bit lengths of these presentations and coefficient lists. Other exact encodings give the same conclusions whenever conversion to and from this representation is polynomial time. This qualification matters for the one-query statement below. Write \(\zeta_t=e^{2\pi\mathrm{i}/t}\) for the primitive _t_-th root of unity. The one-query construction uses the common field \(\mathbb{Q}(\zeta_8,\zeta_q)=\mathbb{Q}(\zeta_{8q})\), where _q_ is an odd prime chosen in the proof. This field has degree 4(_q_-1); its polynomial bit-length bound is verified in the proof.<br>
With the representation above and equal fixed mixers, one exact oracle answer suffices for the counting reduction.

**Theorem B.1** (Single-query fixed-mixer hardness)**.** _Under the explicit number field representation above, for every fixed_ \(p\ge 2\)_, exact evaluation of the MaxCut QAOA expectation is_ #P_-hard under a deterministic polynomial-time reduction making one oracle call. This remains true for the designated_<tbc>

