<tbc>Fix \(v\in V(\Gamma)\). A closed depth-first traversal of a spanning tree starting and ending at _v_ visits every vertex, forming a walk of length 2(_n_-1). Applying the propagation identity along this walk gives<tbc>

\(iZ_vQ_{V\backslash\{v\}}\big|_{W_\mathcal{F}}=iE_{0,0}-iE_{e_v,e_v}\in\mathcal{L}_{3+2\cdot 2(n-1)}=\mathcal{L}_{4n-1}.\)

<tbc>Consequently,<tbc>

\(A_{0,e_v}=-\frac{1}{2}\big[iZ_vQ_{V\backslash\{v\}}\big|_{W_\mathcal{F}},i\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\big]\in\mathcal{L}_{4n},B_{0,e_v}=\frac{1}{2}[iZ_v,A_{0,e_v}]\in\mathcal{L}_{4n+1}.\) (C18)

<tbc>We proceed by induction on _k_=|_x_| to prove that for every nonempty independent set _x_ of size _k_,<tbc>

\(A_{0,x},B_{0,x}\in\mathcal{L}_{d_k},d_k:=4n+2k-1.\)

<tbc>The base case _k_=1 is established by (C18). For \(k\ge 2\), choose \(v\in x\) and let _y=x_\\{_v_}. The mixer matching relations from Ref. \[30, Eq. (B24)\] provide the identities<tbc>

\(C_A:=\left[B_{0,y},i\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\right]=-A_{0,x}-A_{y,e_v},C_B:=\left[A_{0,y},i\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\right]=B_{0,x}-B_{y,e_v}.\)

<tbc>Since both pairs (0_,x_) and (_y,e<sub>v</sub>_) exhibit a _Z<sub>v</sub>_-eigenvalue difference of 2, we have<tbc>

\([iZ_v,A_{p,q}]=2B_{p,q},[iZ_v,B_{p,q}]=-2A_{p,q}\)

<tbc>for these pairs, allowing us to invert the relations as

\(A_{0,x}=-\frac{1}{2}C_A-\frac{1}{4}[iZ_v,C_B],B_{0,x}=\frac{1}{2}C_B-\frac{1}{4}[iZ_v,C_A].\)

By the induction hypothesis, \(C_A,C_B\in\mathcal{L}_{d_{k-1}+1}\), which places these expressions in L<sub>_d_<sub>_k_-1</sub>+2</sub>=L_<sub>d<sub>k</sub></sub>_.

Set \(m:=\alpha(\Gamma)\) and \(\delta:=d_m=4n+2m-1\). Then every vacuum transition _A_<sub>0_,x_</sub>_,B_<sub>0_,x_</sub> resides in \(\mathcal{L}_\delta\). Taking commutators of two such transitions generates _A<sub>x,y</sub>_ and _B<sub>x,y</sub>_ for all distinct nonzero \(x,y\in\mathcal{F}\). Furthermore, the relation

\(\frac{1}{2}[A_{0,x},B_{0,x}]=i(E_{0,0}-E_{x,x})\)

implies that \(\mathfrak{su}(W_\mathcal{F})\subseteq\mathcal{L}_{2\delta}\).

Finally, for any edge {_v,w_}, the generator combination \(i(Z_v+Z_w)\big|_{W_\mathcal{F}}\in\mathcal{L}_1\) has a strictly positive trace. Indeed, since \(\Gamma\) is connected and has at least two vertices, Tr_<sub>W<sub>F</sub></sub>(Z<sub>v</sub>)\>_0 for every vertex _v_: removing _v_ defines a non-surjective one-to-one map from independent sets containing _v_ to those omitting it. Consequently, Tr_<sub>W<sub>F</sub></sub>(Z<sub>v</sub>+Z<sub>w</sub>)\>_0. As its traceless component is a linear combination of diagonal operators already contained in \(\mathcal{L}_{2\delta}\), the identity operator satisfies \(iI_{W_\mathcal{F}}\in\mathcal{L}_{2\delta}\) as well, yielding

\(\mathcal{L}_{2\delta}=\mathfrak{u}(W_\mathcal{F}),D_{\mathfrak{Br},\mathfrak{free},\mathcal{F}}\le 2\delta=8n+4m-2.\)

## Appendix D: Theoretical Derivations of Bounds on Circuit Depth for Orbit Generation and Global Element Synthesis

In this appendix, we prove Theorems VIII.2, VIII.4, VIII.5, and VIII.8.

For Theorem VIII.2, the factorization in Eqs. (81)-(85) comprises \(\genfrac(){pt}{2}{D}{2}\) two-level flows and \(\genfrac(){pt}{2}{D}{2}+1\) diagonal factors, thereby establishing Eq. (86). Next, we prove the basis-to-state bound (87) for the reference state \(|e_1\rangle\); the corresponding result for an arbitrary reference state \(|e_r\rangle\) follows immediately by relabeling the basis.

_Proof of Theorem VIII.2._ The global unitary bound in (86) follows directly from the factorizations given in Eq. (81) through (85). It remains to prove assertions 2 and 3. We first establish the basis-to-state transition synthesis bound (87) for \(|e_1\rangle\); the result for any arbitrary basis state follows by relabeling. Expressing the target state as

\(|\phi\rangle=\sum_{j=1}^DC_j|e_j\rangle,p_j:=|c_j|,\)

