<tbc>**Theorem 8.7** _Let_ \(P\in\{\widetilde{P}_{\unknown,\mathbf{n},M},\widehat{P}_{\unknown,\mathbf{n},M}\}\) _be defined as in_ (8.39) _and as in_ (8.40)_, respectively. Set_ \(U=F_\mathbf{n}\otimes I_M\)_. Then P is unitarily similar to a block diagonal matrix_<tbc>

\(U^*PU=\mathrm{blkdiag}\big(d\lambda_jI_M+Q_{\theta,M}\big)_{j=1}^{N_1N_2},\)

<tbc>_where_ \(\lambda_j\) _are the eigenvalues of_ \(C_{\unknown,\mathbf{n}}\)_, j_=1_,...,N_<sub>1</sub>_N_<sub>2</sub>_. Each diagonal block_

\(D_j=d\lambda_jI_M+Q_{\theta,M},j=1,\dots,N_1N_2,\)

_is an invertible lower triangular Toeplitz matrix._

**Remark 8.4** _The computation of a vector P_<sup>-1</sup>_v is carried out in three steps._

1. _Step 1: compute_ \(\dot{v}=(F_\mathbf{n}^*\otimes I_M)v\)_. This requires O(N_<sub>1</sub>_N_<sub>2</sub>_M_log(_N_<sub>1</sub>_N_<sub>2</sub>)) _operations._<tbc>

_2._ _Step 2: compute_ \(\ddot{v}=\mathrm{blkdiag}\big(D_j^{-1}\big)_{j=1}^{N_1N_2}\dot{v}\),<br>
_where each system involves an ILTT matrix. The first column of each inverse can be computed in O(M_log_M_) _operations. The total cost is O(N_<sub>1</sub>_N_<sub>2</sub>_M_log_M). All systems are independent and can be solved in parallel._<tbc>

_3._ _Step 3: compute_ \(v=(F_\mathbf{n}\otimes I_M)\ddot{v}\)_, with cost O(N_<sub>1</sub>_N_<sub>2</sub>_M_log(_N_<sub>1</sub>_N_<sub>2</sub>)).

_Therefore, computing P_<sup>-1</sup>_v requires O(N_<sub>1</sub>_N_<sub>2</sub>_M_log(_N_<sub>1</sub>_N_<sub>2</sub>)+_N_<sub>1</sub>_N_<sub>2</sub>_M_log_M_) _, which is nearly linear in the problem size._<br>
_Furthermore, in line with the arguments in Remark 8.3, for solving N_<sub>1</sub>_N_<sub>2</sub> _linear systems with coefficient matrices D<sub>j</sub>, j_=1_,...,N_<sub>1</sub>_N_<sub>2</sub>_, the related cost is reduced from_ O(_N_<sub>1</sub>_N_<sub>2</sub>_M_log_M_) _to_ O(_N_<sub>1</sub>_N_<sub>2</sub>_M)._

**Theorem 8.8** _Let_ \(P\in\{\widetilde{P}_{\unknown,\mathbf{n},M},\widehat{P}_{\unknown,\mathbf{n},M}\}\)_, as defined in_ (8.39) _and in_ (8.40)_, respectively. Then,_<tbc>

\(\{P_{\mathbf{n},M}\}_{\mathbf{n},M}\sim_\mathrm{GLT}\hat{d}(\gamma_1^*f_{\alpha_1}(\xi_1)+\gamma_2^*f_{\alpha_2}(\xi_2))+q_\theta(\xi_3),\)

<tbc>_with_ \(\hat{d}=\int_\Omega a(x_1,x_2)\) _and d=d**<sub>n</sub>** converging to_ \(\hat{d}\) _as **n** tends to infinity, and_

\(\{P_{\mathbf{n},M}^{-1}A_{\mathbf{n},M}\}_{\mathbf{n},M}\sim_\mathrm{GLT}\frac{\gamma^*a(x_1,x_2)(\gamma_1^*f_{\alpha_1}(\xi_1)+\gamma_2^*f_{\alpha_2}(\xi_2))+q_\theta(\xi_3)}{\gamma^*\hat{d}(\gamma_1^*f_{\alpha_1}(\xi_1)+\gamma_2^*f_{\alpha_2}(\xi_2))+q_\theta(\xi_3)},\)

_where necessarily_ \(\gamma_2^*=0\) _if_ \(\alpha_1>\alpha_2\) _and alternatively_ \(\gamma_1^*=0\) _if_ \(\alpha_2>\alpha_1\).

## 8.4 Numerical experiments

We conclude our analysis by numerically evaluating the performance of the proposed preconditioning strategy. The objective is to examine its capability to cluster the eigenvalues around 1, reduce the condition number, and enhance the efficiency of the GMRES method in terms of iteration counts and CPU time.<br>
All numerical experiments were conducted in MATLAB R2022b on a laptop equipped with an 11th Gen Intel(R) Core(TM) i5-1155G7 CPU @ 2.50GHz, 16GB RAM, running Windows 11 Pro (version 23H2, build 22631.5189).

