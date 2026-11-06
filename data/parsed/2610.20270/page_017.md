_Proof._ The _F<sub>A,B</sub>_ with \(A\le B\) form a basis of S_<sup>N</sup>_. Within one XOR class, G_<sub>d</sub>_ maps each basis element to the same monomial. Hence its kernel on that class consists of the coefficient vectors summing to zero, and the differences from the reference unit \(F_\Gamma^\circ\) form a basis of it. Distinct classes have disjoint supports. This proves the kernel assertion and independence of the _D<sub>i</sub>_. Since \(\mathcal{G}_d(E_{\emptyset,\emptyset})=1\), the normalization row is not in their span, so A_<sub>d</sub>_ has full row rank. The equalities A_<sub>d</sub>X=e_<sub>1</sub> state that the entries of _X_ are constant on each XOR class and that the common diagonal value is one. This is the first identity in (B.4). Its direction space is T_<sub>d</sub>_, and orthogonal complementation gives the row space. Finally \(I_N\in\mathcal{R}_d\) (matrices in T_<sub>d</sub>_ have zero diagonal) and A_<sub>d</sub>I<sub>N</sub>=e_<sub>1</sub>, so _I<sub>N</sub>_ is the unique feasible point in \(\mathrm{ran}(\mathcal{A}_d^*)\), namely \(\mathcal{A}_d^\dagger e_1\).

One may instead impose all pairwise consistency equalities, but then the rows are redundant and \(\mathcal{A}_d\mathcal{A}_d^*\) is singular; the independent choice (B.3) is a linear-algebra preprocessing decision, unrelated to strict complementarity.

## The SOS problem is the exact dual.

With the encoding (B.3), the primal is \(\mathrm{min}\{\langle C_f,X\rangle:\mathcal{A}_dX=e_1,X\unknown 0\}\). It has the strictly feasible point _I<sub>N</sub>_, and its feasible set is compact, since the diagonal entries are one and PSD forces \(|X_{A,B}|\le 1\). Hence the minimum is attained and strong duality holds. Writing the equality multiplier as \(\lambda=(\gamma,\nu_1,\dots,\nu_{m-1})\), the Lagrangian dual is<tbc>

\(\mathrm{max}_{\gamma,\nu,S}\gamma\mathrm{s}.\mathrm{t}.\gamma E_{\emptyset,\emptyset}+\sum_{j=1}^{m-1}\nu_jD_j+S=C_f,S\unknown 0.\) (B.5)

<tbc>Applying G_<sub>d</sub>_ eliminates the consistency multipliers and gives the SOS problem

\((\mathrm{D}_d)\mathrm{max}_{\gamma\in\mathbb{R},S\unknown 0}\gamma\mathrm{s}.\mathrm{t}.f-\gamma\equiv b_d(x)^\top Sb_d(x)(\mathrm{mod}I_\mathrm{B}).\) (B.6)

No information is lost in this elimination: any feasible \((\gamma,S)\) of (B.6) has \(C_f-\gamma E_{\emptyset,\emptyset}-S\in\mathrm{ker}(\mathcal{G}_d)\), so Theorem B.1 reconstructs the unique multipliers \(\nu_j\) in (B.5). The SOS Gram matrix _S_ is therefore the standard SDP dual slack. At optimality of an exact relaxation, the optimal slack set is (2.4).

**Lemma B.2** (Trace identity and compactness)**.** _Suppose the relaxation at order d is exact with value f<sub>⋆</sub>. Every_ \(S\in\mathcal{S}_\star\) _satisfies_ \(\mathrm{tr}S=f_\emptyset-f_\star\)_; consequently_ S_<sub>⋆</sub> is compact._

_Proof._ \(\mathrm{tr}S=\langle A_\emptyset,S\rangle\) is the constant coefficient of G_<sub>d</sub>(S_)=_f-f<sub>⋆</sub>_, which is \(f_\emptyset-f_\star\). The set is closed, and \(\|S\|_F\le\mathrm{tr}S\) for PSD matrices, so it is bounded.

## Primal degeneracy.

We now prove Theorem 2.2. Throughout, \(d\ge d_\star(f)\), so \(X_\star=uu^\top=Nqq^\top\) is the unique primal optimum (§2). Primal nondegeneracy of _X<sub>⋆</sub>_ \[AHO97\] means that A_<sub>d</sub>_ is surjective on the tangent space at _X<sub>⋆</sub>_ to the manifold of rank-one PSD matrices. This tangent space is

\(\{qv^\top+vq^\top:v\in\mathbb{R}^N\}=\mathbb{S}(V)^\perp,\text{so nondegeneracy reads}\mathcal{A}_d\big(\mathbb{S}(V)^\perp\big)=\mathbb{R}^m.\) (B.7)

This is a condition on the optimum relative to the constraints, distinct from mere singularity of _X<sub>⋆</sub>_.

_Proof of Theorem 2.2._ By the constant-diagonal identity (4.2), \(\mathrm{ker}(\mathcal{A}_d)\cap\mathbb{S}(V)^\perp=\mathcal{T}_d\cap\mathbb{S}(V)^\perp=\{0\}\), so A_<sub>d</sub>_ is injective on the _N_-dimensional tangent space (B.7); hence nondegeneracy holds if and only if _m=N_. For the dimension formula, R_<sub>d</sub>_+S(_V_)=S_<sup>N</sup>_ because the orthogonal complement of the sum is \(\mathcal{T}_d\cap\mathbb{S}(V)^\perp=\{0\}\); therefore<tbc>

\(\mathrm{dim}\mathcal{L}=\mathrm{dim}\big(\mathcal{R}_d\cap\mathbb{S}(V)\big)=m+\frac{(N-1)N}{2}-\frac{N(N+1)}{2}=m-N,\)

