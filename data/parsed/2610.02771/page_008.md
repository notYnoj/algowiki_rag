and at phase _j_ set \(L_j:=32\sigma^2/\rho_j\), \(\alpha_j:=1+log(32\sigma/\rho_j)\), and \(r_j:=\rho_j/16\). With \(\gamma=\delta/[K(J+1)]\),

\(\beta_j(n)=\frac{\rho_j}{64}+2\sqrt{\frac{3\alpha_j\sigma^2x_n(\gamma)}{n}}+\frac{32\alpha_j\sigma^2x_n(\gamma)}{\rho_jn}.\)

The choice of _L<sub>j</sub>_ makes the clipping bias of phase _j_ at most \(\rho_j/64\), while \(r_j=\rho_j/16\) is the target statistical radius at that resolution. Thus, phase _j_ should be viewed as a test of whether the currently active arms can already be separated at scale \(\rho_j\). If the confidence intervals are still too wide, the algorithm continues sampling; if all active arms have confidence radius at most _r<sub>j</sub>_, then arms that are clearly suboptimal at this scale can be safely removed.

Algorithm RESTARTPHASEDCLIP-1BITBAI implements this idea using fresh estimators at every phase; detailed pseudocode is given in Algorithm 4 in Appendix E. Within phase _j_, it adaptively samples active arms until either some arm is certified to be \(\varepsilon\)-optimal or all active arms have confidence radius at most _r<sub>j</sub>_. In the latter case, it eliminates every arm whose UCB is below the best LCB by more than \(\varepsilon\), and then moves to the next, finer phase _j_+1.

**Theorem 10** (Phased adaptive clipping upper bound)**.** RESTARTPHASEDCLIP-1BITBAI _is_ \((\varepsilon,\delta)\)_- PAC. With probability at least_ \(1-\delta\)_, the needed number of 1-bit queries satisfies_

\(\tau=O\big(H_\mathrm{gap}\left[log\frac{K}{\delta}+loglog\frac{\sigma}{\varepsilon}\right]\big),\)

The proof of Theorem 10 is given in Appendix C.2. A finite deterministic query bound also holds on every realization for \(\varepsilon>0\), guaranteeing termination even outside the confidence event; together with interval correctness this establishes the PAC guarantee. The deterministic bound and proof are given in Appendix C.3.2.

**Remark 11** (Reuse instead of restart)**.** _The restart version is chosen for proof clarity. In practice one can reuse samples across clipping levels using_

\([W]_{L_j}=\sum_{s=0}^j\int_{I_s}\big(\mathbf{1}\{W\ge t\}-\mathbf{1}\{W\le-t\}\big)dt,I_0=[0,L_0],I_s=(L_{s-1},L_s](s\ge 1).\)

_Thus, when moving from phase j_-1 _to phase j, it suffices to introduce the new slab I<sub>j</sub> and top up only those old slabs whose sample counts are still deficient for the finer phase-j target radius. Lemma 31 shows that this reuse strategy preserves the same order as Theorem 10._

## 3.3 Discussion of the sample complexity

### Fixed clipping vs Phased clipping.

The fixed method is simpler and fully anytime, but it pays the mixed term \(\sigma^2/(\varepsilon\widetilde{\Delta}_k)\) because the range of the 1-bit statistic is proportional to \(L_\varepsilon=\Theta(\sigma^2/\varepsilon)\). This term is unavoidable for a globally fixed clipping level, but it is wasteful for arms with \(\Delta_k\gg\varepsilon\). The phased method matches _L<sub>j</sub>_ to the current resolution \(\rho_j\), so the range term is balanced at the scale where the arm is actually distinguished; its cost is essentially \((1+log(\sigma/\overline{\Delta_k}))\sigma^2/\overline{\Delta_k^2}\) per arm.

### Compared with unquantized fixed-confidence BAI.

The distribution-free hardness of unquantized BAI is \(\sum_k\sigma^2/\widetilde{\Delta}_k^2\) (\[7\]), 1-bit feedback introduces the additional logarithmic factor \(1+log(\sigma/\overline{\Delta_k})\) in the phased bound. The lower bound in Section 4 shows that this logarithmic penalty is inevitable in the finite-variance regime.

### Lau-Scarlett \[21\] with phased successive elimination.

At each resolution \(\rho_j\), run their fixed- target estimator on each active arm with accuracy \(\rho_j/8\) and confidence \(1-\delta/[K(J+1)]\), then retain estimates within \(\rho_j/2\) of the maximum. Simultaneous confidence control yields total cost \(O(H_\mathrm{gap}log(K(J+1)/\delta))\), matching our leading rate. Appendix C.4 gives the correctness and counting argument.

### Total sample complexity.

If the anchors are not initially available but the means lie in \([-\lambda,\lambda]\), running MEDIANEST for each arm adds an additional \(O\big(K(log\frac{\lambda}{\sigma}+log\frac{K}{\delta})\big)\) term to the sample complexity, which does not scale with \(\varepsilon\) or the gaps \(\Delta_k\).

