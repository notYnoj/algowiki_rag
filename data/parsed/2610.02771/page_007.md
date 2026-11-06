## 3.1 Fixed clipping bias

The simplest implementation chooses the clipping level from the target accuracy:<tbc>

\(L_\varepsilon:=\frac{2\sigma^2}{\varepsilon},\alpha_\varepsilon:=1+log\frac{L_\varepsilon}{\sigma}=1+log\frac{2\sigma}{\varepsilon}.\)

<tbc>By Lemma 4, the clipping bias is at most \(\varepsilon/4\). The confidence radius from Theorem 5 becomes

\(\beta_\varepsilon(n,\gamma)=\frac{\varepsilon}{4}+2\sqrt{\frac{3\alpha_\varepsilon\sigma^2x_n(\gamma)}{n}}+\frac{2\alpha_\varepsilon\sigma^2x_n(\gamma)}{n\varepsilon}.\)

Algorithm FIXEDCLIP-1BITBAI uses this radius with \(\gamma=\delta/K\). At each round it forms confidence intervals \[LCB_<sub>k</sub>,_UCB_<sub>k</sub>_\] of \(\mu_k\), sets \(B_k=max_{a\neq k}\mathrm{UCB}_a-\mathrm{LCB}_k\), lets \(h\in argmin_kB_k\) and \(\ell\in argmax_{a\neq h}\mathrm{UCB}_a\), stops if \(B_h\le\varepsilon\), and otherwise samples the more uncertain arm in \(\{h,\ell\}\) using the 1-bit tail-integral query at clipping level \(L_\varepsilon\). Detailed pseudocode is given in Algorithm 3 in Appendix E.

From the expression of \(\beta_\varepsilon(n,\gamma)\), the sample requirement is no longer governed only by the usual _n_<sup>-1/2</sup> concentration term. In addition, there is a lower-order \(n^{-1}\varepsilon^{-1}\) term coming from the Bernstein range correction. This term is a direct consequence of the clipping level \(L_\varepsilon\) chosen so that the clipping bias is at most \(\varepsilon/4\), affecting the final sample complexity. This leads to the hardness quantity:

\(H_\mathrm{fix}(\varepsilon):=\alpha_\varepsilon\sum_{k=1}^K\left(\frac{\sigma^2}{\widetilde{\Delta}_k^2}+\frac{\sigma^2}{\varepsilon\widetilde{\Delta}_k}\right).\)

With this hardness quantity, we can state the sample complexity upper bound.

**Theorem 8** (Fixed clipping upper bound)**.** FIXEDCLIP-1BITBAI _is_ \((\varepsilon,\delta)\)_-PAC. With probability at least_ \(1-\delta\)_, its needed number of 1-bit queries satisfies_

\(N_\mathrm{fix}=O\big(H_\mathrm{fix}(\varepsilon)\left[log\frac{K}{\delta}+loglogH_\mathrm{fix}(\varepsilon)\right]\big).\)

The proof of Theorem 8 is given in Appendix C.1. A finite deterministic query bound also holds on every realization for \(\varepsilon>0\), guaranteeing termination even outside the confidence event; together with interval correctness this establishes the PAC guarantee. The deterministic bound and proof are given in Appendix C.3.1.

**Remark 9** (The choice of clipping level _L_)**.** _The fixed choice_ \(L_\varepsilon=2\sigma^2/\varepsilon\) _is simple and ensures bias at most_ \(\varepsilon/4\)_, but it is not instance-optimal, especially when_ \(\varepsilon\checkmark\Delta_k\) _or_ \(\varepsilon=0\)_. For exact best-arm identification_ \(\varepsilon=0\)_, the natural scale is_ \(L_\star=\Theta(\sigma^2/\Delta_{k^\star})\)_; more generally, the oracle arm-wise choice would be_ \(L_k=\Theta(\sigma^2/\widetilde{\Delta}_k)\)_, leading to the gap-adaptive hardness_

\(H_\mathrm{gap}=\sum_{k=1}^K\left(1+log\frac{\sigma}{\overline{\Delta_k}}\right)\frac{\sigma^2}{\overline{\Delta_k^2}}.\)

The phased algorithm below obtains this behavior without knowing the gaps.

## 3.2 Phased adaptive clipping

The intuition behind the phased algorithm is that easy arms should not be estimated at the finest accuracy scale. In FIXEDCLIP-1BITBAI, the clipping level is fixed using the target accuracy \(\varepsilon\), so even an arm with a large gap pays the range cost associated with resolving \(\varepsilon\)-level differences. The phased algorithm instead proceeds from coarse to fine resolutions. At phase _j_, it uses a clipping level matched to the current resolution \(\rho_j\) and eliminates arms that are already distinguishable at that scale. Only statistically competitive arms survive to finer phases. This removes the fixed-clipping mixed term and yields a bound depending on each arm’s own effective gap.

To implement this idea, schedule resolutions<tbc>

\(\rho_j:=2^{-j}\sigma,J:=\lceil log_2(\sigma/\varepsilon)\rceil,j=0,1,\dots,J,\)

