then the selected columns of _B_ occur in the order<tbc>

\(\alpha_{t_1}\mathbf{e}_{t_1},\dots,\alpha_{t_q}\mathbf{e}_{t_q},\beta_{u_1}\mathbf{e}_{u_1},\dots,\beta_{u_q}\mathbf{e}_{u_q}.\)

<tbc>The sign of the corresponding permutation is<tbc>

\(\varepsilon(T)=(-1)\sum_{k=1}^q(t_k-k).\)

<tbc>Hence<tbc>

\(det(B_{[:,S]})=\varepsilon(T)\left(\prod_{i\in T}\alpha_i\right)\left(\prod_{j\in T^c}\beta_j\right),\)

<tbc>while

\(det(C_{[S,:]})=det(V_T)det(V_{T^c}).\)

Summing over all subsets \(T\subseteq[2q]\) with |_T_|=_q_ gives (21).

**Corollary 2.3.** _The matrix_ \(\Lambda\) _is invertible if and only if the right-hand side of_ (21) _is non-zero. In particular,_ \(\Lambda\) _is singular whenever_ \(\alpha_i=\beta_i\) _for all i._

_Proof._ The invertibility criterion follows immediately from Theorem 2.2. If \(\alpha_i=\beta_i\) for all _i_, then the _j_-th columns of the two blocks in (19) coincide, so \(\Lambda\) is singular. (Note that this is not visible term by term in (21): the terms of _T_ and _T<sup>c</sup>_ cancel in pairs only for odd _q_, since \(\varepsilon(T^c)=(-1)^q\varepsilon(T).\))

## 2.2 Inverse via polynomial interpolation

**Theorem 2.4.** _Suppose that_ \(det(\Lambda)\neq 0\)_, and write_<tbc>

\(\Lambda^{-1}=\genfrac(){pt}{2}{Y}{Z},Y,Z\in\mathbb{C}^{q\times 2q}.\)

<tbc>_For each j_=1_,...,_2_q, define the polynomials_<tbc>

\(Y_j(x):=\sum_{k=0}^{q-1}Y_{k+1,j}x^k,Z_j(x):=\sum_{k=0}^{q-1}Z_{k+1,j}x^k.\)

<tbc>_Then_ (_Y<sub>j</sub>,Z<sub>j</sub>_) _is the unique pair of polynomials of degree at most q_-1 _satisfying_

\(\alpha_iY_j(x_i)+\beta_iZ_j(x_i)=\delta_{ij},i=1,\dots,2q.\) (22)

_Proof._ Let **y**_<sub>j</sub>_ and **z**_<sub>j</sub>_ denote the _j_-th columns of _Y_ and _Z_, respectively. The _j_-th column of the identity \(\Lambda\Lambda^{-1}=I_{2q}\) gives<tbc>

\(D_\alpha V_q\mathbf{y}_j+D_\beta V_q\mathbf{z}_j=\mathbf{e}_j.\)

<tbc>By the definitions of _Y<sub>j</sub>_ and _Z<sub>j</sub>_, the _i_-th component of this identity is

\(\alpha_iY_j(x_i)+\beta_iZ_j(x_i)=\delta_{ij},\)

which proves (22).

Conversely, any pair of polynomials of degree at most _q_-1 satisfying (22) determines coefficient vectors \(\mathbf{y},\mathbf{z}\in\mathbb{C}^q\) satisfying

\(\Lambda\genfrac(){pt}{2}{\mathbf{y}}{\mathbf{z}}=\mathbf{e}_j.\)

Since \(\Lambda\) is invertible, this system has a unique solution. Hence the pair (_Y<sub>j</sub>,Z<sub>j</sub>_) is unique.

