<tbc>Theorem F.6 makes the right-hand side strictly larger than \(c(t^\star,\delta)\). Therefore \(\tau_\delta\le t^\star\) on E, and the stated high-probability bound follows by expanding \(s_{\delta,\eta}\) and absorbing constants.

Now assume that _t<sub>U</sub>_ admits a summable upper-quantile bound _u<sub>U</sub>_. Let<tbc>

\(L_\delta:=\mathrm{log}\frac{1}{\delta},A_\delta:=T_\beta^\star(\mu)L_\delta.\)

<tbc>The high-probability part just proved gives constants \(D_0,D_1,D_2,D_3<\infty\) such that, for every \(\zeta\in(0,1]\),<tbc>

\(\mathbb{P}_\mu\left(\tau_\delta\le A_\delta+R_\delta(\zeta)\right)\ge 1-\zeta,\)

<tbc>where

\(R_\delta(\zeta)=D_0u_U(\zeta/4)+D_1\sqrt{L_\delta\left(\mathrm{log}\frac{4K}{\zeta}+\mathrm{loglog}\frac{e}{\delta}\right)}\)<br>
\(+D_2\left(\mathrm{log}\frac{4K}{\zeta}+\mathrm{loglog}\frac{e}{\delta}\right)+D_3.\)

This follows by applying the high-probability bound with \(\eta=\zeta/4\) and intersecting it with the event \(\{t_U\le u_U(\zeta/4)\}\).

Let \(R_\delta^\downarrow\) be the monotone envelope of \(R_\delta\). Theorem F.3 gives<tbc>

\(\mathbb{E}_\mu[\tau_\delta]\le A_\delta+\sum_{k\ge 0}2^{-k}R_\delta^\downarrow(2^{-k}).\)

<tbc>By Lemma F.4, we may replace _u<sub>U</sub>_ by the upper-tail quantile upper-quantile bound of _t<sub>U</sub>_. Consequently, \(R_\delta(\zeta)\) is nonincreasing in \(\zeta\), and hence \(R_\delta^\downarrow=R_\delta\). Thus, without loss of generality, _u<sub>U</sub>_ is nonincreasing and satisfies<tbc>

\(\sum_{k\ge 0}2^{-k}u_U(2^{-k-2})<\infty.\)

<tbc>The term \(C\sqrt{L_\delta}\) is dominated by \(C\sqrt{L_\delta\mathrm{loglog}(e/\delta)}\) for \(\delta\in(0,1/2]\). Similarly,

\(\sum_{k\ge 0}2^{-k}\left(\mathrm{log}(4K)+k\mathrm{log}2+\mathrm{loglog}\frac{e}{\delta}\right)\le C\mathrm{loglog}\frac{e}{\delta}+C.\)

Combining these bounds yields

\(\mathbb{E}_\mu[\tau_\delta]\le T_\beta^\star(\mu)\mathrm{log}(1/\delta)+C'_{\mu,1}(U)\sqrt{\mathrm{log}(1/\delta)\mathrm{loglog}(e/\delta)}+C'_{\mu,2}(U)\mathrm{loglog}(e/\delta)+C'_{\mu,3}(U).\)

This completes the proof.

## G Guarantees Under a Unique Best Arm

### G.1 Separation implies permanent leader correctness

_Proof of Proposition 6.1._ Fix \(t\ge t_\mathrm{sep}(\eta)\) and any \(j\neq i^\star\). By definition, \(N_{t,i^\star}\ge n_\star(\eta)\ge n_j(\eta)\) and \(N_{t,j}\ge n_j(\eta)\). Hence<tbc>

\(r(N_{t,i^\star},\eta)\le\frac{\mu_{i^\star}-\mu_j}{4},r(N_{t,j},\eta)\le\frac{\mu_{i^\star}-\mu_j}{4}.\)

<tbc>On the armwise confidence event this yields

\(\widehat{\mu}_{t,i^\star}\ge\mu_{i^\star}-\frac{\mu_{i^\star}-\mu_j}{4},\widehat{\mu}_{t,j}\le\mu_j+\frac{\mu_{i^\star}-\mu_j}{4}.\)

Thus \(\widehat{\mu}_{t,i^\star}>\widehat{\mu}_{t,j}\). Since this holds for every \(j\neq i^\star\), the empirical leader is permanently correct from time _t_ onward.

