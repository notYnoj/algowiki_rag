(III) **Algorithmic transfer and genericity** (§5 and §6). We transfer the canonical error bound to ADMM, sGS-ADMM, and PDHG through residual rescalings and an affine endpoint chart; with averagedness in method-specific metrics, this yields the rates of Theorem 1.1. A separate semialgebraic argument establishes its generic half.

To our knowledge, the geometry of the exact regime at orders \(d\ge 2\) has not been used to analyze first-order solvers; Appendix A organizes the related work into four threads.

### Organization.

Appendix A discusses related work, Appendices B to G carry the deferred proofs, and Appendix H details the experiments.

### Notation.

All spaces are finite-dimensional and real. S_<sup>p</sup>_ is the space of symmetric \(p\times p\) matrices with the trace inner product \(\langle H_1,H_2\rangle=\text{tr}(H_1H_2)\), Frobenius norm \(\|\cdot\|_F\), and PSD cone \(\mathbb{S}_+^p\); \(\Pi_+\) is the Frobenius projection onto \(\mathbb{S}_+^p\) and \(\Pi_-:=\text{Id}-\Pi_+\). For \(S\subseteq[n]\), \(x^S:=\prod_{i\in S}x_i\); optima carry star subscripts (_x<sub>⋆</sub>_, _X<sub>⋆</sub>_), optimal sets are calligraphic (S_<sub>⋆</sub>_, Z_<sub>⋆</sub>_), and we distinguish the number of Boolean variables _n_, a general SDP matrix size _p_, and the moment matrix size _N<sub>d</sub>_ (with _p=N<sub>d</sub>_ in the Boolean specialization). Directional derivatives \(F'(z;h)\), the cones _T<sub>C</sub>(z_), _N<sub>C</sub>(z_), the operators ri, rb, aff, cl, and the vector and operator norms are standard and collected in Appendix C.

## 2 Degeneracy of Exact Boolean Relaxations

This section makes the degeneracy phenomenon concrete; full proofs are in Appendix B.

### Boolean quotient moments.

Fix \(1\le d\le n\) and the Boolean ideal \(I_\mathrm{B}:=\langle x_1^2-1,\dots,x_n^2-1\rangle\), so that every polynomial has a unique square-free representative and \(x^Ax^B\equiv x^{A\triangle B}\), where \(\triangle\) is the symmetric difference. Index monomials by<tbc>

\(\mathcal{I}_d:=\{T\subseteq[n]:|T|\le\mathrm{min}\{d,n\}\},N_d:=|\mathcal{I}_d|,b_d(x):=(x^T)_{T\in\mathcal{I}_d}\in\mathbb{R}^{N_d};\) (2.1)

<tbc>when _d_ is fixed we write _N=N<sub>d</sub>_. For \(\Gamma\in\mathcal{I}_{2d}\), define the XOR-class matrices \((A_\Gamma)_{A,B}:=\mathbf{1}_{\{A\triangle B=\Gamma\}}\), indexed by \(A,B\in\mathcal{I}_d\). They have disjoint supports, are Frobenius orthogonal, and \(A_\emptyset=I_N\). A degree-2_d_ pseudo-moment sequence \(y=(y_\Gamma)_{\Gamma\in\mathcal{I}_{2d}}\) is encoded by the moment matrix<tbc>

\(M_d(y):=\sum_{\Gamma\in\mathcal{I}_{2d}}y_\Gamma A_\Gamma,\text{i.e.}(M_d(y))_{A,B}=y_{A\triangle B},\) (2.2)

<tbc>and the feasible _moment body_ is the spectrahedron \(\mathcal{X}_d:=\{M_d(y):y_\emptyset=1,M_d(y)\unknown 0\}\). Writ ing \(C_f:=\sum_\Gamma f_\Gamma A_\Gamma/\|A_\Gamma\|_F^2\) for the canonical matrix representative of \(f=\sum_\Gamma f_\Gamma x^\Gamma\) (so that \(\langle C_f,M_d(y)\rangle=\sum_\Gamma f_\Gamma y_\Gamma\)), at every admissible order (\(\mathrm{deg}f\le 2d\)) the relaxation of (1.1) is<tbc>

\((\mathrm{P}_d)p_d(f):=\mathrm{min}_{X\in\mathcal{X}_d}\langle C_f,X\rangle.\) (2.3)

<tbc>The identity matrix is strictly feasible and X_<sub>d</sub>_ is compact, so the minimum is attained. Moreover, (P_<sub>d</sub>_) is a standard-form SDP under an explicit independent equality encoding A_<sub>d</sub>X=e_<sub>1</sub> of full row rank _m=N(N_+1)/2-|I<sub>2_d_</sub>|+1 (Theorem B.1). Its exact dual is the SOS problem: maximize \(\gamma\) subject to \(f-\gamma\equiv b_d(x)^\top Sb_d(x)\) (mod_I_<sub>B</sub>) with the Gram matrix \(S\unknown 0\) (Appendix B). When the relaxation is exact with value _f<sub>⋆</sub>_=OPT(_f_), the optimal Gram certificates form the set

\(\mathcal{S}_\star:=\{S\unknown 0:b_d(x)^\top Sb_d(x)\equiv f-f_\star(\mathrm{mod}I_\mathrm{B})\},\) (2.4)

which is compact because every \(S\in\mathcal{S}_\star\) has the same trace \(f_\emptyset-f_\star\) (Theorem B.2).

