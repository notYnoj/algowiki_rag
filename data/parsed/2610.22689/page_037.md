<tbc>Tracking the filtration depth through this chain reveals that \(P_{ZZ}^{b,k}\in\mathcal{F}_{2k-1}^{a_{P_n,\mathrm{free}}}\). Similarly, by applying up to two additional commutations with single-qubit _X_-generators at the boundaries, we find that

\(P_{YZ}^{b,k},P_{ZY}^{b,k}\in\mathcal{F}_{2k}^{\mathbf{a}_{P_n,\mathrm{free}}},P_{YY}^{b,k}\in\mathcal{F}_{2k+1}^{\mathbf{a}_{P_n,\mathrm{free}}}.\)

Because the maximum path length of a non-trivial contiguous block within _n_ sites is bounded by _n_-1, the maximum filtration level required to span the algebra cannot exceed 2_n_-1. Therefore, \(\mathcal{D}_{a_{P_n,\mathrm{free}}}\le 2n-1\) and \(\mathcal{D}_{a_{C_n,\mathrm{free}}}\le 2n-1\), completing the proof.

**Complete Graphs.** We denote by _x(P_), _y(P_), _z(P_), and _i(P_) the number of _X_-, _Y_-, _Z_-, and identity factors in a Pauli string _P_, respectively, so that<tbc>

\(x(P)+y(P)+z(P)+i(P)=n.\) (C3)

<tbc>By Theorem 1 in \[17\], the free DLA g<sub>_K<sub>n</sub>,_free</sub> admits a basis consisting of Pauli strings _P_ satisfying

\(\left\{\begin{array}{ c c }
y(P)+z(P)\equiv 0 & (\mathrm{mod}2), \\
x(P)\neq n, & 
\end{array}\right.\) (C4)

We establish degree bounds for every such basis element _P_ based on its constituents.

**Case 1: strings with no** _X_ **factors (**_x(P_)=0).** Let \(s:=y(P)+z(P)\ge 2\) denote the support size of non-_X_ factors (which is even, \(s\in 2\mathbb{Z}_{>0}\)). We prove by induction on _s_ that \(iP\in\mathcal{F}_{2s-1}^{\mathbf{a}_{K_n,\mathrm{free}}}\) (i.e., \(\mathrm{deg}(iP)\le 2s-1\)).

For the base case _s_=2, two-body strings of type _ZZ_, _ZY/YZ_, and _YY_ have generation degrees 1, 2, and at most 3, respectively.

Assume \(s\ge 4\) is even and that the claim holds for all valid Pauli strings with non-_X_ support strictly smaller than _s_.

We select a pivot site \(j\in\mathrm{supp}(P)\) as follows: if \(y(P)\ge 1\), choose _j_ such that _P<sub>j</sub>=Y_ ; otherwise (_y(P_)=0), select any site _j_ in the support, so _P<sub>j</sub>=Z_. Next, choose two distinct sites \(a,b\in\mathrm{supp}(P)\backslash\{j\}\) and define \(P'\) by replacing _P<sub>a</sub>_ and _P<sub>b</sub>_ with identity operators _I<sub>a</sub>_ and _I<sub>b</sub>_, so that \(s(P')=s-2\ge 2\).

For each \(v\in\{a,b\}\), define the auxiliary operator<tbc>

\(A_v:=\left\{\begin{array}{ c c }
iP_vZ_j, & \text{if}P_j=Y_j, \\
iP_vY_j, & \text{if}P_j=Z_j.
\end{array}\right.\) (C5)

<tbc>We verify that \(\mathrm{deg}(A_v)\le 2\) for all \(v\in\{a,b\}\) as follows:<tbc>

\(iZ_aY_j\propto[iX_j,iZ_aZ_j],iZ_bY_j\propto[iX_j,iZ_bZ_j],\)

<tbc>Evaluating the iterated Lie bracket confirms that _iP_ is recovered (up to a non-zero scalar factor) via the nested commutator:

\(iP\propto[A_b,[A_a,iP']].\) (C6)

Applying the inductive hypothesis \(\mathrm{deg}(iP')\le 2(s-2)-1\) together with the filtration bracket compatibility property (33), we obtain

\(\mathrm{deg}(iP)\le\mathrm{deg}(iP')+\mathrm{deg}(A_a)+\mathrm{deg}(A_b)\)<br>
\(\le(2(s-2)-1)+2+2\)<br>
\(=2s-5+4=2s-1,\) (C7)

which completes the inductive step and establishes \(iP\in\mathcal{F}_{2s-1}\).

**Case 2: strings with** _X_ **factors and** \(y(P)+z(P)\ge 2\)**.** Let _s_:=_x(P_)+_y(P_)+_z(P_) denote the total support size of _P_. We prove by induction on \(x(P)\ge 1\) that \(\mathrm{deg}(iP)\le 2s-1\). The base case _x(P_)=0 is established by Case 1.

