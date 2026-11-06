Since \(\Gamma_j\ge log(K(J+1)/\delta)\), a union bound over all _K(J_+1) arm-phase pairs shows that, with probability at least \(1-\delta\), the above Bernstein bound holds simultaneously for every _k_ and _j_. Taking _C_<sub>0</sub> sufficiently large yields<tbc>

\(2\sqrt{V_{k,j}\Gamma_j}+B_{k,j}\Gamma_j\le\frac{3\rho_j}{64}.\)

<tbc>The clipping bias at level _L<sub>j</sub>_ is<tbc>

\(\big|\mathbb{E}[W_k]-\mathbb{E}[[W_k]_{L_j}]\big|\le\frac{\sigma^2}{2L_j}=\frac{\rho_j}{64}.\)

<tbc>Consequently, on the simultaneous event,

\(\big|\tilde{\mu}_{k,j}^\mathrm{reuse}-\mu_k\big|\le\frac{3\rho_j}{64}+\frac{\rho_j}{64}=\frac{\rho_j}{16}=r_j\)

whenever all slabs \(s\le j\) have been topped up to _m<sub>s,j</sub>_. Thus the reusable estimator certifies the same phase-_j_ radius as the restarted estimator.

It remains to count samples. For a fixed arm _k_, let _j<sub>k</sub>_ be the last phase in which _k_ is sampled by the reusable algorithm. Since samples are retained, the total number of slab samples collected for arm _k_ is bounded by the final top-up target at phase _j<sub>k</sub>_, namely

\(\sum_{s=0}^{j_k}m_{s,j_k}=O\left(\frac{\sigma^2}{\rho_{j_k}^2}\Gamma_{j_k}\sum_{s=0}^{j_k}A_s\right)=O\left(\frac{\alpha_{j_k}\sigma^2}{\rho_{j_k}^2}\Gamma_{j_k}\right).\)

On the same valid-interval event, the stopping and elimination arguments from Lemmas 25-29 apply verbatim, since they only use validity of the confidence intervals and the fact that each completed phase reaches radius _r<sub>j</sub>_. Hence Lemma 29 gives<tbc>

\(\rho_{j_k}\ge c\overline{\Delta_k}.\)

<tbc>Therefore

\(\alpha_{j_k}=1+log\frac{32\sigma}{\rho_{j_k}}=O\big(1+log\frac{\sigma}{\overline{\Delta_k}}\big)=O(\Lambda(\overline{\Delta_k})),\)<br>
\(\frac{\sigma^2}{\rho_{j_k}^2}=O\left(\frac{\sigma^2}{\overline{\Delta_k^2}}\right),\)

and<tbc>

\(\Gamma_{j_k}=O\big(\Gamma(\overline{\Delta_k};K,J,\delta)\big).\)

<tbc>Thus arm _k_ contributes at most

\(O\left(\Lambda(\overline{\Delta_k})\frac{\sigma^2}{\overline{\Delta_k^2}}\Gamma(\overline{\Delta_k};K,J,\delta)\right)\)

queries. Summing over _k_=1_,...,K_ proves the claimed bound.

## C.3 Deterministic finite query bounds

The high-probability bounds above quantify gap-dependent behavior. For positive accuracy, both algorithms also have finite gap-independent query caps on every realization. These bounds establish termination without conditioning on confidence validity. We assume supplied anchors and \(0<\varepsilon\le\sigma\); for larger accuracy one may run the algorithms with target \(\sigma\).

### C.3.1 Fixed clipping

**Proposition 32** (Pathwise fixed-clipping cap)**.** _Let_ \(A_\varepsilon=\alpha_\varepsilon\sigma^2/\varepsilon^2\)_, and let_ \(m_\varepsilon\) _be the smallest nonnegative integer satisfying_<tbc>

\(2^{m_\varepsilon}\ge 768A_\varepsilon log\left(\frac{\pi^2K(m_\varepsilon+1)^2}{3\delta}\right).\)

<tbc>_Set_ \(n_\mathrm{fix}^\circ=2^{m_\varepsilon}\)_. Then on every realization,_<tbc>

\(\tau_\mathrm{fix}\le Kn_\mathrm{fix}^\circ=O\big(KA_\varepsilon\left[log\frac{K}{\delta}+loglog(e^eA_\varepsilon)\right]\big).\)

