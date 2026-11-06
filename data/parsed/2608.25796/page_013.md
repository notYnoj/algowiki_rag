so that, by Axiom **GLT3**, part 3, we deduce<tbc>

\(\{P_N^{-1}A_N\}_N\sim_\mathrm{GLT}=1\)

<tbc>if _a(x_) is a constant function and

\(\{P_N^{-1}A_N\}_N\sim_\mathrm{GLT}\frac{\ell_0-\gamma a(x)f_\alpha(\theta)}{\ell_0-\gamma df_\alpha(\theta)}\)

when _a(x_) is Riemann integrable. Finally the corresponding singular value distributions follow directly from Axiom **GLT1**.

## 5.1.2. GLT analysis of the preconditioning for Technique 2

By Theorem 4.3, we have \(B_M=T_N(g_\beta)\) with \(g_\beta\) belonging to the Wiener class. Following the literature on Toeplitz preconditioning \[11, 39\], we know that the natural circulant and the natural \(\omega\)-circulant approximations _P<sub>M</sub>_ ensure a strong singular value clustering at zero for {_B<sub>M</sub>-P<sub>M</sub>}<sub>M</sub>_ in the sense of Definition 2.3. Hence, taking into account Remark 2.4, \(\{B_M-P_M\}_M\sim_\sigma 0\) and the latter is equivalent to

\(\{B_M-P_M\}_M\sim_\mathrm{GLT}0,\) (15)

by Axiom **GLT1**.

Relation (15) is the basis for proving the following result.

**Theorem 5.2.** _Let_ \(\beta\in(1,2)\) _and let_ \(P_M\in\left\{\widehat{C}_{\beta,M},\widehat{C}_{\omega,\beta,M}\right\}\)_. Then_

• \(\{P_M\}_M\sim_{\mathrm{GLT},\sigma} g_\beta(\theta_2)\);<tbc>

• \(\{P_M^{-1}B_N\}_N\sim_{\mathrm{GLT},\sigma} 1\).

_Proof._ The proof is a simplified version of that of Theorem 5.1, which has been given with all the details, and hence we omit it.

Joining the information in the last two theorem we can prove the following result, which is essentially based on Axiom **GLT4** on tensor product matrix sequences.

**Theorem 5.3.** _Let_ \(\alpha,\beta\in(1,2)\)_. Then_

• \(\{P_{\alpha,\beta,NM}\}_{N,M}\sim_{\mathrm{GLT},\sigma}\gamma^*df_\alpha(\theta_1)+g_\beta(\theta_2)\);<tbc>

• \(\{P_{\alpha,\beta,NM}^{-1}\mathcal{A}_{N,M}\}_{N,M}\sim_{\mathrm{GLT},\sigma} 1\) _when a is a constant;_<tbc>

• \(\{P_{\alpha,\beta,NM}^{-1}\mathcal{A}_{N,M}\}_{N,M}\sim_{\mathrm{GLT},\sigma}\frac{\gamma^*da(x)f_\alpha(\theta_1)+g_\beta(\theta_2)}{\gamma^*df_\alpha(\theta_1)+g_\beta(\theta_2)}\)<tbc>

<tbc>_for a general Riemann integrable coefficient a(x)._

_Proof._ The proof amounts in combining Theorem 5.1, Theorem 5.2 with the tensor product Axiom **GLT4**.

