_Proof._ For every _Y_ , \(\langle Y,\mathsf{Syl}Y\rangle=\mathrm{tr}(Y^\top AY)+\sigma\mathrm{tr}(Y^\top YB)\), and both terms are nonnegative. In case (a) the first term is at least \(a\|Y\|_F^2\), in case (b) the second is at least \(\sigma b\|Y\|_F^2\); Cauchy-Schwarz then gives \(\|\mathsf{Syl}Y\|_F\ge a\|Y\|_F\), respectively \(\ge\sigma b\|Y\|_F\). Injectivity in equal finite dimensions gives invertibility and the bounds.

## C.4 Two-sided tangent and normal cones

For an endpoint \(\bar{Z}=\bar{X}-\sigma\bar{S}\) define the two kernel-supported PSD cones \(\mathcal{K}(\bar{X}):=\{W\in\mathbb{S}_+^p:\mathrm{ran}W\subseteq K_\bar{X}\}\) and \(\mathcal{K}(\bar{S}):=\{W\in\mathbb{S}_+^p:\mathrm{ran}W\subseteq K_\bar{S}\}\).

**Proposition C.4** (Endpoint cones)**.** _Under Theorem 3.1, at_ \(\bar{Z}=\bar{X}-\sigma\bar{S}\in\mathcal{Z}_\star\),

\(T_{\mathcal{X}_\star}(\bar{X})=\{M\in\mathcal{M}:P_{K_\bar{X}}MP_{K_\bar{X}}\unknown 0\},N_{\mathcal{X}_\star}(\bar{X})=\mathcal{M}^\perp-\mathcal{K}(\bar{X}),\) (C.8)

\(T_{\mathcal{S}_\star}(\bar{S})=\{\Lambda\in\mathcal{L}:P_{K_\bar{S}}\Lambda P_{K_\bar{S}}\unknown 0\},N_{\mathcal{S}_\star}(\bar{S})=\mathcal{L}^\perp-\mathcal{K}(\bar{S}),\) (C.9)

\(T_{\mathcal{Z}_\star}(\bar{Z})=T_{\mathcal{X}_\star}(\bar{X})-\sigma T_{\mathcal{S}_\star}(\bar{S}),N_{\mathcal{Z}_\star}(\bar{Z})=\mathcal{D}^\perp-\mathcal{K}(\bar{X})+\mathcal{K}(\bar{S}),\) (C.10)

_where the sums are Minkowski sums and all cones are taken in_ S_<sup>p</sup>._

_Proof._ For the cone supported on _U_, the tangent and ambient normal formulas are

\(T_{\mathbb{S}_+(U)}(\bar{X})=\{H\in\mathbb{S}(U):P_{K_\bar{X}}HP_{K_\bar{X}}\unknown 0\},N_{\mathbb{S}_+(U)}(\bar{X})=\mathbb{S}(U)^\perp-\mathcal{K}(\bar{X}).\)

The tangent condition is necessary, as one sees by evaluating feasible secants on vectors of \(K_\bar{X}\). It is sufficient for the following reason. Adding \(\varepsilon P_{K_\bar{X}}\) to a direction _H_ makes its kernel block positive definite. The Schur complement then shows that \(\bar{X}+t(H+\varepsilon P_{K_\bar{X}})\) is PSD for small _t\>_0. Letting \(\varepsilon\downarrow 0\) closes the cone. The normal formula is the polar: the free cross and range blocks force the corresponding normal blocks to vanish, and the polar of the PSD kernel cone is its negative. For the slice \(\mathcal{X}_\star=(X_\mathrm{sc}+\mathcal{M})\cap\mathbb{S}_+(U)\) the same approximation can be performed inside M. Replace _H_ by \(H+\varepsilon(X_\mathrm{sc}-\bar{X})\), whose kernel block is positive definite because \(X_\mathrm{sc}\succ 0\) on _U_. The relative Slater point _X_<sub>sc</sub> justifies the normal-cone intersection rule \[Roc15\]. Hence \(N_{\mathcal{X}_\star}(\bar{X})=\mathcal{M}^\perp+\mathbb{S}(U)^\perp-\mathcal{K}(\bar{X})=\mathcal{M}^\perp-\mathcal{K}(\bar{X})\), using \(\mathcal{M}\subseteq\mathbb{S}(U)\). This proves (C.8), and (C.9) is the same argument on _V_ with the anchor _S_<sub>sc</sub>.

For the product, the map \((X,S)\mapsto X-\sigma S\) is a linear isomorphism of \(\mathbb{S}(U)\times\mathbb{S}(V)\) onto \(\mathbb{S}(U)\oplus\mathbb{S}(V)\), so it carries the tangent cone of \(\mathcal{X}_\star\times\mathcal{S}_\star\), which is the product of the tangent cones, onto \(T_{\mathcal{X}_\star}(\bar{X})-\sigma T_{\mathcal{S}_\star}(\bar{S})\). For the normal cone, \(H\in N_{\mathcal{Z}_\star}(\bar{Z})\) if and only if \(\langle H,X-\bar{X}\rangle\le 0\) for all \(X\in\mathcal{X}_\star\) and \(\langle H,S-\bar{S}\rangle\ge 0\) for all \(S\in\mathcal{S}_\star\) (take \(S=\bar{S}\) for the first inequality and \(X=\bar{X}\) for the second), that is, \(H\in N_{\mathcal{X}_\star}(\bar{X})\cap\big(-N_{\mathcal{S}_\star}(\bar{S})\big)=(\mathcal{M}^\perp-\mathcal{K}(\bar{X}))\cap(\mathcal{L}^\perp+\mathcal{K}(\bar{S}))\). If _H=Y-W<sub>U</sub>+W<sub>V</sub>_ with \(Y\in\mathcal{D}^\perp\), \(W_U\in\mathcal{K}(\bar{X})\), \(W_V\in\mathcal{K}(\bar{S})\), then _H_ lies in both sets because \(W_V\in\mathbb{S}(V)\subseteq\mathcal{M}^\perp\) and \(W_U\in\mathbb{S}(U)\subseteq\mathcal{L}^\perp\). Conversely, if _H=Y_<sub>1</sub>-_W<sub>U</sub>=Y_<sub>2</sub>+_W<sub>V</sub>_ with \(Y_1\in\mathcal{M}^\perp\), \(Y_2\in\mathcal{L}^\perp\), then \(Y:=H+W_U-W_V=Y_1-W_V=Y_2+W_U\) lies in \(\mathcal{M}^\perp\cap\mathcal{L}^\perp=\mathcal{D}^\perp\), so _H=Y-W<sub>U</sub>+W<sub>V</sub>_. The sign of the slack cone is positive because the fixed-point variable contains \(-\sigma S\), and positive scalars do not change cones.

At a relative-interior endpoint both kernels vanish, so \(T_{\mathcal{Z}_\star}(\bar{Z})=\mathcal{D}\) and \(N_{\mathcal{Z}_\star}(\bar{Z})=\mathcal{D}^\perp\). At a boundary endpoint the two extra cones may be nonzero, and the three summands in (C.10) are _not_ orthogonal in general. This is the precise sense in which the boundary is harder than the interior, and why Theorem D.2 bounds the summands through the anchors rather than through orthogonality.<tbc>

