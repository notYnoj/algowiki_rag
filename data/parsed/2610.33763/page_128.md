2. _Step 2: compute_ \(\ddot{v}=\mathrm{blkdiag}\left(D_j^{-1}\right)_{j=1}^N\dot{v},D_j=\gamma d\lambda_jI_M+Q_{\theta,M}\).<tbc>

_3._ _Step 3: compute_ \(\ddot{v}=(F_N\otimes I_M)\ddot{v}\).

_The resulting total cost is of the order O(NM_log(_N_)) _which is optimal in our setting, since it is the same order of the cost of a matrix-vector product with the original coefficient matrix._<br>
_From Theorem 8.5, both Steps 1 and 3 involve Fourier transforms in the spatial dimension and can be performed in_ O(_NM_log_N_) _operations using FFT. Step 2 requires solving N independent systems with coefficient matrices D<sub>j</sub>, which are ILTT matrices. Since the inverse of an ILTT matrix is also ILTT, its first column can be computed in_ O(_M_log_M_) _operations by the divide-and-conquer inversion algorithm \[28\]. Therefore, Step 2 can be carried out in_ O(_NM_log_M_) _operations. In total, applying P_<sup>-1</sup>_v requires_ O(_NM_log_N+NM_log_M), which is nearly linear in the problem size. Moreover, the N systems in Step 2 are completely independent and can be solved in parallel, making the preconditioner highly efficient in practice. Of course, if the matrix_ \(Q_{\theta,M}\) _is not stored explicitly as in (8.16), then it can be viewed as_ \(H_{\theta,M}^{-1}H_M\) _so that_

\(D_j=H_{\theta,M}^{-1}\left(\gamma d\lambda_jH_{\theta,M}+H_M\right),\)

_which leads to a more efficient computation since_ \(H_{\theta,M}\) _and_ \(\gamma d\lambda_jH_{\theta,M}+H_M\)_, j_=1_,...,N, are all lower bidiagonal. With this choice, for solving n linear systems with coefficient matrices D<sub>j</sub>, j_=1_,...,N, the related cost is reduced from_ O(_NM_log_M_) _to_ O(_NM)._

We conclude the current section with a GLT/clustering analysis of the preconditioned matrix sequences.

**Theorem 8.6** _Let_ \(P_{N,M}\in\{\widetilde{P}_{\alpha,N,M},\widehat{P}_{\alpha,N,M}\}\)_, as defined in_ (8.35) _and in_ (8.36)_, respectively. Then,_<tbc>

\(\{P_{N,M}\}_{N,M}\sim_\mathrm{GLT}\gamma^*\hat{d}f_\alpha(\xi_1)+q_\theta(\xi_3),\)

<tbc>_with_ \(\hat{d}=\int_\Omega a(x)\) _and d=d<sub>N</sub> converging to_ \(\hat{d}\) _as N tends to infinity and_<tbc>

\(\{P_{N,M}^{-1}A_{\alpha,N,M}\}_{N,M}\sim_\mathrm{GLT}\frac{\gamma^*a(x)f_\alpha(\xi_1)+q_\theta(\xi_3)}{\gamma^*\hat{d}f_\alpha(\xi_1)+q_\theta(\xi_3)}.\)

<tbc>**Proof:** From the literature \[27, 35\], it is known that \(\{\overline{G_{\alpha,N}}-\widetilde{C}_{\alpha,N}\}_N\sim_\sigma 0\). The same clustering at zero is true for \(\{\overline{G_{\alpha,N}}-\widehat{C}_{\alpha,N}\}_N\) since the approximation is even better (the only neglected coefficient is \(g_N^{(\alpha)}\)). In both cases the clustering is strong since the generating function is continuous and \(2\pi\)-periodic \[27, 35\]. Now by axiom GLT 2, part 3, \(\{\overline{G_{\alpha,N}}-C_{\alpha,N}\}_N\sim_\sigma 0\) if and only if \(\{\overline{G_{\alpha,N}}-C_{\alpha,N}\}_N\sim_\mathrm{GLT}0\), \(C_{\alpha,N}\in\{\widetilde{C}_{\alpha,N},\widehat{C}_{\alpha,N}\}\). Since \(\{\overline{G_{\alpha,N}}\}_N\) is also a GLT matrix sequence, by axiom GLT 3, part 3, it is clear that both the approximating matrix sequences \(\{\widetilde{C}_{\alpha,N}\}_N\), \(\{\widehat{C}_{\alpha,N}\}_N\) are both GLT matrix sequences with the same GLT symbol as \(\{\overline{G_{\alpha,N}}\}_N\), as in Theorem 8.1 and Remark 8.1.<br>
By following the very same steps as in the proof of Theorem 8.1, Theorem 8.3 and of the reasoning in Remark 8.1, we end up with the conclusion<tbc>

\(\{P_{N,M}\}_{N,M}\sim_\mathrm{GLT}\gamma^*\hat{d}f_\alpha(\xi_1)+q_\theta(\xi_3)\)

