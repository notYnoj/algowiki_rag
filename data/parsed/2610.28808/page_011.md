<tbc>\[toc\] A DEFLATION-BASED PRECONDITIONER FOR PCG 11<tbc>

<tbc>Set \(\eta_i:=s_i^\top r_0\). Then, squaring the expression of \(\widetilde{\zeta}_i(t)\) gives<tbc>

(3.22) \(\widetilde{\zeta}_i(t)^2=\eta_i^2+2t\eta_i\left(s_i^\top E\underline{S_i}D_i\underline{S_i^\top} r_0-s_i^\top ES_kS_k^\top x^*-s_i^\top E\overline{S_k}\overline{S_k^\top} z_0\right)+O(t^2).\)

<tbc>Let \(\widehat{T}_i^\theta\) be an \((n-1)\times(n-1)\) diagonal matrix such that<tbc>

\([\widehat{T}_i^\theta]_{jj}=\left\{\begin{array}{ c c }
\theta/(\lambda_j(\lambda_i-\theta)), & \text{for}j=1,\dots,k, \\
1/(\lambda_i-\lambda_j), & \text{for}j=k+1,\dots,n:j\neq i.
\end{array}\right.\)

<tbc>Then, by Assumption 3.3, the preconditioned initial residual satisfies<tbc>

\(U^\theta b-A^\theta(t)y_0=U^\theta\left(b-A(t)z_0\right)=U^\theta r_0-tU^\theta Ez_0.\)

<tbc>Using this identity, the expression for \(\widehat{T}_i^\theta\), and Lemma 3.5, we obtain

\(\widetilde{\beta}_i^\theta(t)=s_i^\theta(t)^\top\left(U^\theta b-A^\theta(t)y_0\right)\)<br>
\(=\left(s_i+t\underline{S_i}T_i^\theta\underline{S_i^\top} Es_i+O(t^2)\right)^\top\left(U^\theta r_0-tU^\theta Ez_0\right)\)<br>
\(=s_i^\top r_0+t\left(s_i^\top E\underline{S_i}\widehat{T}_i^\theta\underline{S_i^\top} r_0-s_i^\top Ez_0\right)+O(t^2)\)<br>
\(=s_i^\top r_0+t\left(s_i^\top E\underline{S_i}\widehat{T}_i^\theta\underline{S_i^\top} r_0-s_i^\top ES_kS_k^\top z_0-s_i^\top E\overline{S_k}\overline{S_k^\top} z_0\right)+O(t^2).\)

Squaring this expression gives

(3.23) \(\widetilde{\beta}_i^\theta(t)^2=\eta_i^2+2t\eta_i\left(s_i^\top E\underline{S_i}\widehat{T}_i^\theta\underline{S_i^\top} r_0-s_i^\top ES_kS_k^\top z_0-s_i^\top E\overline{S_k}\overline{S_k^\top} z_0\right)+O(t^2).\)

From (3.22) and (3.23),

\(\widetilde{\beta}_i^\theta(t)^2-\widetilde{\zeta}_i(t)^2=2t\eta_i\left(s_i^\top E\underline{S_i}(\widehat{T}_i^\theta-D_i)\underline{S_i^\top} r_0+s_i^\top ES_kS_k^\top\left(x^*-z_0\right)\right)+O(t^2)\)<br>
\(=2t\eta_i\left(s_i^\top E\underline{S_i}(\widehat{T}_i^\theta-D_i)\underline{S_i^\top} r_0+s_i^\top ES_kS_k^\top A^{-1}r_0\right)+O(t^2)\)<br>
\(=2t\eta_i\left(s_i^\top ES_k\widehat{D}_i^\theta S_k^\top r_0+s_i^\top ES_k\Lambda_k^{-1}S_k^\top r_0\right)+O(t^2)\)<br>
\(=2t\eta_i\left(s_i^\top ES_k\left(\widehat{D}_i^\theta+\Lambda_k^{-1}\right)S_k^\top r_0\right)+O(t^2),\)

where we used \(\underline{S_i}(\widehat{T}_i^\theta-D_i)\underline{S_i^\top}=S_k\widehat{D}_i^\theta S_k^\top\), with \(\widehat{D}_i^\theta:=\mathrm{diag}\left(\frac{\theta}{\lambda_j(\lambda_i-\theta)}\right)_{j=1,\dots,k}\). By Assumption 3.2, \(S_k^\top r_0=0\), so the entire coefficient of _t_ vanishes. It remains to verify that the resulting _O(t_<sup>2</sup>) estimate is uniform in \(\theta\). In fact, first, Definition 3.4 gives \(\lambda_n\le\theta\le\lambda_k\) and \(|\lambda_i-\theta|\ge\delta\) for _i=k_+1_,...,n_. Consequently, for any \(j\le k\), \(\left|\frac{\theta}{\lambda_j(\lambda_i-\theta)}\right|\le\frac{1}{\delta}\), and \(\left|\frac{\sqrt{\theta}}{\sqrt{\lambda_j(\lambda_i-\theta)}}\right|\le\frac{1}{\delta}\), because \(\theta\le\lambda_k\le\lambda_j\). Thus, the matrices \(\widehat{T}_i^\theta\) and \(T_i^\theta\) are uniformly bounded for any \(\theta\in\Theta_\delta\). Second, \(\|U^\theta\|_2\le 1\) uniformly. Third, the second-order eigenvector remainder in Lemma 3.5 is uniform over \(\Theta_\delta\). All factors produced when the two expansions are multiplied and squared are therefore bounded independently of \(\theta\). Moreover, by Proposition 3.1 and the argument in Lemma 3.5, the threshold underlying the eigenvector remainder is independent of \(\theta\); hence the threshold for the resulting _O(t_<sup>2</sup>) estimate is independent of \(\theta\). □

The following lemma is useful for the proof of the main result.

Lemma 3.7. _Let Assumption_ 3.1 _hold and fix_ \(\delta\in(0,\gamma_0]\)_. Let_ \(1\le k\le n-1\) _and t_<sub>0</sub>_\>_0_, such that_ \(t_0\|E\|_2<\lambda_n\)_. Then for every_ \(0\le t\le t_0\):

**Cahier du GERAD G-2026-70**

