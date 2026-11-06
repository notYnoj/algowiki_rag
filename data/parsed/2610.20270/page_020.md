<tbc>own directional derivative \(\Pi_+(\widetilde{H}_{KK})\). The formula is valid with repeated eigenvalues, because on any pair of repeated-eigenvalue eigenspaces the multiplier is constant, so changes of eigenbasis give the same ambient derivative after conjugation by _Q_. For \(E:=\Pi'_+(\bar{Z};H)\) and \(F:=\Pi'_-(\bar{Z};H)\) we read off

\(E+F=H,\langle E,\bar{S}\rangle=0,\langle F,\bar{X}\rangle=0,\langle E,F\rangle=2\sum_{i\in+,j\in-}\Omega_{ij}(1-\Omega_{ij})|(\widetilde{H}_{+-})_{ij}|^2\ge 0,\) (C.5)

since _E_ has zero -- block, _F_ has zero ++ block, the _KK_ parts pair as \(\langle\Pi_+(M),\Pi_-(M)\rangle=0\), and only the -- overlap survives. Also \(\|E\|_F,\|F\|_F\le\|H\|_F\), because \(\Pi_\pm\) are nonexpansive and a directional derivative is a limit of difference quotients, and

\(\delta'_\sigma(\bar{Z};H)=-\mathsf{P}E-\mathsf{P}^\perp F,\|\delta'_\sigma(\bar{Z};H)\|_F^2=\|\mathsf{P}E\|_F^2+\|\mathsf{P}^\perp F\|_F^2.\) (C.6)

### Three kinds of endpoints in the fixed coarse coordinates.

Whenever \(K_\bar{X}=\{0\}\) or \(K_\bar{S}=\{0\}\), the same derivative reads, in the fixed bases _B<sub>U</sub>,B<sub>V</sub>_,

\([B_UB_V]^\top\Pi'_+(\bar{Z};H)[B_UB_V]=\left[\begin{array}{ c c }
H_{UU}^\sharp & Y \\
Y^\top & H_{VV}^\sharp
\end{array}\right],\bar{X}_{UU}Y+\sigma Y\bar{S}_{VV}=\bar{X}_{UU}H_{UV}.\) (C.7)

We call this \(U\oplus V\) block description _coarse_, in contrast with the eigen-chart (C.3), which refines _U_ and _V_ by the moving kernels. Here \(H_{UU}^\sharp\) is _H<sub>UU</sub>_ with its \(K_\bar{X}K_\bar{X}\) block replaced by the positive part of that block. Similarly, \(H_{VV}^\sharp\) is the positive part of the \(K_\bar{S}K_\bar{S}\) block of _H<sub>VV</sub>_, embedded in _V_ . The cross block _Y_ is the unique solution of the displayed Sylvester equation. Indeed, in eigencoordinates the equation reads \((\xi_i+\sigma s_j)\widetilde{Y}_{ij}=\xi_i\widetilde{H}_{ij}\) with \(\xi_i\ge 0\) on _U_ and \(s_j\ge 0\) on _V_ . This reproduces the +-, +_K_, and _K_- blocks of (C.4). It is uniquely solvable exactly when \(\xi_i+\sigma s_j>0\) for all pairs, that is, when \(K_\bar{X}=\{0\}\) or \(K_\bar{S}=\{0\}\). When both kernels are nontrivial, the \(K_\bar{X}K_\bar{S}\) part of \(\Pi_+(\widetilde{H}_{KK})\) has no such description, and we never use the coarse form there. Three cases are used:

(a) _Interior endpoints_ \((\bar{X}_{UU}\succ 0\), \(\bar{S}_{VV}\succ 0)\): _K_={0}, \(\Pi_+\) is Fréchet differentiable at \(\bar{Z}\), and \(J_{\bar{X},\bar{S}}:=\Pi'_+(\bar{Z};\cdot)\) is the linear map \(H\mapsto\left[\begin{array}{ c }
H_{UU} \\
Y^\top
\end{array}\right]\) of (3.5).<tbc>

(b) _Primal-anchored endpoints_ \(\bar{Z}=X_\mathrm{sc}-\sigma\bar{S}\): \(K=K_\bar{S}\), \(H_{UU}^\sharp=H_{UU}\), and the Sylvester equation has \(X_\mathrm{sc}|_U\succ 0\) on the left.<tbc>

(c) _Dual-anchored endpoints_ \(\bar{Z}=\bar{X}-\sigma S_\mathrm{sc}\): \(K=K_\bar{X}\), \(H_{VV}^\sharp=0\), and the Sylvester equation has \(S_\mathrm{sc}|_V\succ 0\) on the right.

## C.3 Two uniform Sylvester estimates

**Lemma C.3** (Sylvester estimates)**.** _Let_ \(A\in\mathbb{S}_+(U)\) _and_ \(B\in\mathbb{S}_+(V)\) _be given in the fixed bases, and let_ \(\mathsf{Syl}:Y\mapsto AY+\sigma YB\) _act on_ \(\mathrm{dim}U\times\mathrm{dim}V\) _matrices._

(a) _If_ \(A\unknown aI\) _with a\>_0_, then_ Syl _is invertible and_ \(\|\mathsf{Syl}^{-1}\|_{F\rightarrow F}\le a^{-1}\)_, uniformly over all_ \(B\unknown 0\).<tbc>

(b) _If_ \(B\unknown bI\) _with b\>_0_, then_ Syl _is invertible and_ \(\|\mathsf{Syl}^{-1}\|_{F\rightarrow F}\le(\sigma b)^{-1}\)_, uniformly over all_ \(A\unknown 0\).

_In particular, let_ \(a_X:=\lambda_\mathrm{min}(X_\mathrm{sc}|_U)\) _and_ \(a_S:=\lambda_\mathrm{min}(S_\mathrm{sc}|_V)\)_. The Sylvester operators of the primal- anchored endpoints have inverse norm at most_ \(a_X^{-1}\) _for every_ \(\bar{S}\in\mathcal{S}_\star\)_. Those of the dual-anchored endpoints have inverse norm at most_ \((\sigma a_S)^{-1}\) _for every_ \(\bar{X}\in\mathcal{X}_\star\).

