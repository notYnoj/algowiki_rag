<tbc>Then \(\widetilde{x}(s)=[I_n,0,\dots,0]\mathcal{L}_0^{-1}\mathcal{U}_my_s\) approximates _x<sub>q</sub>(s_).

The name _infinite GMRES_ comes from extending this construction to an infinite- dimensional companion linearization \[10\]. The starting vector \(\mathrm{vec}_0(z)/\|z\|_2\) has only its first block nonzero. Multiplication by \(\mathcal{L}_1\mathcal{L}_0^{-1}\) increases the number of potentially nonzero blocks by at most one, and Arnoldi orthogonalization preserves the remaining zero blocks. Thus, in exact arithmetic, the first _p_ Arnoldi steps are identical for every _q_ greater than or equal to _p_, up to appending zero blocks to the basis vectors. The reduced least-squares problems and the recovered approximations \(\widetilde{x}(s)\) are consequently independent of _q_ as well. We may therefore formally let \(q\rightarrow\infty\) and interpret these iterates as GMRES applied to the infinite companion linearization of the full Taylor series. Each iteration still requires only finitely many active blocks and Taylor coefficients, so the infinite matrix is never formed. Omitting the zero tails introduces no truncation error into these iterates.

## 3. Toeplitz infinite GMRES.

### 3.1. Block Toeplitz motivation.

The preconditioned companion matrix is

\(\mathcal{L}_1\mathcal{L}_0^{-1}=\left[\begin{array}{ c c c c c c }
0 & 0 & 0 & \cdots & 0 \\
A_0^{-1} & -A_0^{-1}A_1 & -A_0^{-1}A_2 & \cdots & -A_0^{-1}A_q \\
I & 0 &  &  &  \\
 &  & \ddots & \ddots &  \\
 &  &  & I & 0
\end{array}\right].\)

Now we consider the structure of \(\mathcal{K}_m(\mathcal{L}_1\mathcal{L}_0^{-1},\mathrm{vec}_0(z))\). Define

(3.1) \(a_1:=A_0^{-1}z,a_m:=-A_0^{-1}\sum_{j=1}^{m-1}A_ja_{m-j},\forall m\ge 2.\)

Direct multiplication gives

\(\mathcal{K}_m(\mathcal{L}_1\mathcal{L}_0^{-1},\mathrm{vec}_0(z))=\mathrm{Range}\left[\begin{array}{ c c }
z & 0 \\
0 & V_{m-1} \\
0 & 0
\end{array}\right],\)

where

\(V_m:=\left[\begin{array}{ c c c c c c }
a_1 & a_2 & a_3 & \cdots & a_m \\
a_1 & a_2 & \cdots & a_{m-1} \\
 & \ddots & \ddots & \vdots \\
 &  & a_1 & a_2 \\
 &  &  & a_1
\end{array}\right]\in\mathbb{C}^{mn\times m},\forall m.\)

Because \(a_1\neq 0\), so _V<sub>m</sub>_ has full column rank. We use its unique thin QR factorization _V<sub>m</sub>=Q<sub>m</sub>R<sub>m</sub>_, with a positive real diagonal in _R<sub>m</sub>_. These factorizations are nested because the first _m_-1 columns of _V<sub>m</sub>_ equal \([V_{m-1}^T,0]^T\).

This structure already reduces infGMRES to QR factorization of Toeplitz matrix _V<sub>m</sub>_. Using the coordinates under _V<sub>m</sub>_, we can prove that the reduced least-squares problem and approximate solution in infGMRES are

(3.2) \(\mathrm{min}_{y\in\mathbb{C}^m}\left\|\left[\begin{array}{ c c c }
\|z\|_2 & 0 \\
0 & R_m
\end{array}\right]\left(\left[\begin{array}{ c }
I_m \\
0_{1\times m}
\end{array}\right]-s\left[\begin{array}{ c }
0_{1\times m} \\
I_m
\end{array}\right]\right)y-\|z\|_2e_1\right\|_2,\widetilde{x}(s)=[a_1,\dots,a_m]y.\)

