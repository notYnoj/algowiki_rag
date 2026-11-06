DR residual made uniform over the fixed-point set, and by Theorem 3.2 it is equivalent to the stall cone equaling the tangent cone at every endpoint. The companion paper \[KY26b\] studies the failure of this equality at a selected endpoint. There the gap \(\mathcal{C}(\bar{Z})\backslash T_{\mathcal{Z}_*}(\bar{Z})\) consists of the two cross blocks coupling \(\mathrm{ran}\bar{X}\) with \(K_\bar{S}\) and \(K_\bar{X}\) with \(\mathrm{ran}\bar{S}\) (its Proposition 3), and each direction in it carries a nonzero second-order drift (its Proposition 6). Linear growth at \(\bar{Z}\) closes the gap (its Corollary 1(3)). The identities (3.8) say that these cross blocks are empty at every relative-boundary factor, and (iii)\(\Leftrightarrow\)(v) is the setwise converse of that corollary. The one-sided case, a unique primal optimum plus one strictly complementary pair, is the _primal simplicity_ condition of \[DU21, Definition 5\]; the two-sided theorem drops the uniqueness. In general conic programs, ADMM, sGS-ADMM, and PDHG can become arbitrarily slow near degenerate optima \[KY26a, Jia26\]; exact Boolean relaxations exclude this near their optimal set, with instance-dependent constants (§7).

## B The Boolean Moment-SOS tion

Throughout this appendix, fix \(1\le d\le n\) and put _N=N<sub>d</sub>_; recall the index sets (2.1), the XOR-class matrices \(A_\Gamma\), and the moment matrix (2.2). As in §4, set

\(\mathcal{H}_d:=\mathrm{span}\{A_\Gamma:\Gamma\in\mathcal{I}_{2d}\},\mathcal{T}_d:=\mathrm{span}\{A_\Gamma:\emptyset\neq\Gamma\in\mathcal{I}_{2d}\},\mathcal{R}_d:=\mathcal{T}_d^\perp.\) (B.1)

Every \(\Gamma\in\mathcal{I}_{2d}\) occurs as a symmetric difference of two sets in I_<sub>d</sub>_: split it into two parts of size at most _d_. The XOR class of \(\Gamma\) is the set of unordered pairs {_A,B_} with \(A,B\in\mathcal{I}_d\) and \(A\triangle B=\Gamma\), i.e. the support of \(A_\Gamma\). Distinct classes are disjoint, so the matrices \(A_\Gamma\) are Frobenius orthogonal, and \(A_\emptyset=I_N\). Hence \(\mathcal{H}_d=\mathrm{span}\{I_N\}\oplus\mathcal{T}_d\) as in (4.3). Every matrix in T_<sub>d</sub>_ has zero diagonal.

### The Gram-to-polynomial map.

Define the polynomial-valued linear map

\(\mathcal{G}_d(Y):=\sum_{\Gamma\in\mathcal{I}_{2d}}\langle A_\Gamma,Y\rangle x^\Gamma,b_d(x)^\top Yb_d(x)\equiv\mathcal{G}_d(Y)(x)(\mathrm{mod}I_\mathrm{B}),\) (B.2)

so \(\mathrm{ker}(\mathcal{G}_d)=\mathcal{H}_d^\perp\). The canonical representative \(C_f=\sum_\Gamma f_\Gamma A_\Gamma/\|A_\Gamma\|_F^2\) of §2 satisfies G_<sub>d</sub>(C<sub>f</sub>_)=_f_ and \(\langle C_f,M_d(y)\rangle=\sum_\Gamma f_\Gamma y_\Gamma\) by orthogonality of the classes. For moments, let \(L_y(\sum_\Gamma h_\Gamma x^\Gamma):=\sum_\Gamma h_\Gamma y_\Gamma\) be the Riesz functional. For \(g=c^\top b_d\) one has \(L_y(g^2\mathrm{mod}I_\mathrm{B})=c^\top M_d(y)c\). Hence \(M_d(y)\unknown 0\) if and only if \(L_y(g^2\mathrm{mod}I_\mathrm{B})\ge 0\) for every square-free _g_ of degree at most _d_.

### The independent equality encoding.

Let \(E_{A,B}\) (\(A,B\in\mathcal{I}_d\)) be the matrix units, and define the symmetric units _F<sub>A,B</sub>_:=_E<sub>A,A</sub>_ if _A=B_ and \(F_{A,B}:=\frac{1}{2}(E_{A,B}+E_{B,A})\) otherwise. Then \(\langle F_{A,B},X\rangle=X_{A,B}\) and \(\mathcal{G}_d(F_{A,B})=x^{A\triangle B}\), and the _F<sub>A,B</sub>_ with \(A\le B\) (in a fixed total order on I_<sub>d</sub>_) form a basis of S_<sup>N</sup>_. For each XOR class \(\Gamma\) choose one reference pair {_A,B_} (with \(A=B=\emptyset\) for \(\Gamma=\emptyset\)), and write \(F_\Gamma^\circ:=F_{A,B}\) for its symmetric unit. For every other pair {_A,B_} in the class, include the consistency matrix \(D_{A,B}:=F_{A,B}-F_\Gamma^\circ\), where \(\Gamma=A\triangle B\). Listing these as _D_<sub>1</sub>_,...,D_<sub>_m_-1</sub>, define

\(\mathcal{A}_dX:=\big(X_{\emptyset,\emptyset},\langle D_1,X\rangle,\dots,\langle D_{m-1},X\rangle\big),b:=e_1,m=\frac{N(N+1)}{2}-|\mathcal{I}_{2d}|+1.\) (B.3)

**Proposition B.1** (Exact standard SDP encoding)**.** _The matrices D_<sub>1</sub>_,...,D_<sub>_m_-1</sub> _form a basis of_ \(\mathrm{ker}(\mathcal{G}_d)=\mathcal{H}_d^\perp\)_; the operator_ A_<sub>d</sub> has full row rank; and_

\(\{X:\mathcal{A}_dX=e_1\}=I_N+\mathcal{T}_d,\mathrm{ker}(\mathcal{A}_d)=\mathcal{T}_d,\mathrm{ran}(\mathcal{A}_d^*)=\mathcal{R}_d,\mathcal{A}_d^\dagger e_1=I_N.\) (B.4)

