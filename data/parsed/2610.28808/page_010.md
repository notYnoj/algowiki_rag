<tbc>Lemma 3.5. _Let Assumption_ 3.1 _hold and fix_ \(\delta\in(0,\gamma_0]\)_. Let_ \(1\le k\le n-1\)_. For sufficiently small_ \(t\ge 0\)_, the eigenpairs of the preconditioned matrix indexed by i=k_+1_,...,n admit the following expansions, uniformly in_ \(\theta\in\Theta_\delta\),<tbc>

\(\lambda_i^\theta(t)=\lambda_i(t)+O(t^2),s_i^\theta(t)=s_i+t\underline{S_i}T_i^\theta\underline{S_i^\top} Es_i+O(t^2),\)

<tbc>_where_ \(T_i^\theta\) _is an_ \((n-1)\times(n-1)\) _diagonal matrix such that_<tbc>

\([T_i^\theta]_{jj}=\left\{\begin{array}{ c c }
\sqrt{\theta}/(\sqrt{\lambda_j}(\lambda_i-\theta)), & \text{\textit{for}}j=1,\dots,k \\
1/(\lambda_i-\lambda_j), & \text{\textit{for}}j=k+1,\dots,n:j\neq i.
\end{array}\right.\)

<tbc>_Proof._ Since \(A^\theta(t)=U^\theta AU^\theta+tU^\theta EU^\theta\), the first-order perturbation (3.5) gives<tbc>

\(\lambda_i^\theta(t)=\lambda_i^\theta(0)+ts_i^\top U^\theta EU^\theta s_i+O(t^2)=\lambda_i+ts_i^\top Es_i+O(t^2)=\lambda_i(t)+O(t^2),\)

<tbc>where we used \(U^\theta s_i=s_i\) and \(\lambda_i^\theta(0)=\lambda_i\) for _i=k_+1_,...,n_. Applying the eigenvector expansion gives,

(3.21) \(s_i^\theta(t)=s_i+t\underline{S_i}\left(\lambda_iI_{n-1}-\Omega_i\right)^{-1}\underline{S_i^\top} U^\theta EU^\theta s_i+O(t^2),\)

where \(\Omega_i=\text{diag}(\underbrace{\theta,\dots,\theta}_{k\text{times}},\lambda_{k+1},\dots,\lambda_{i-1},\lambda_{i+1},\dots,\lambda_n)\). Using \(U^\theta s_i=s_i\) and \(U^\theta\underline{S_i}=\underline{S_i}\text{diag}(\frac{\sqrt{\theta}}{\sqrt{\lambda_1}},\dots,\frac{\sqrt{\theta}}{\sqrt{\lambda_k}},\underbrace{1,\dots,1}_{n-k-1\text{times}})\), (3.21) becomes \(s_i^\theta(t)=s_i+t\underline{S_i}T_i^\theta\underline{S_i^\top} Es_i+O(t^2)\).

For every _i\>k_ and every \(\theta\in\Theta_\delta\), the distance from \(\lambda_i\) to the remaining spectrum of \(U^\theta AU^\theta\) is at least \(\delta\). Moreover, \(\|U^\theta EU^\theta\|_2\le\|U^\theta\|_2^2\|E\|_2\le 1\). Hence Proposition 3.1, applied with the common gap \(\delta\), provides a common perturbation radius and \(\theta\)- independent constants in the eigenvalue and eigenvector remainders. □

## 3.4. Comparison between PCG and deflated CG.

This section presents the main comparison between the energy-norm errors of PCG and deflated CG. To connect the two error representations, we first compare their residual coefficients and then establish spectral bounds used in the main comparison theorem.

Throughout this section, we use the following assumptions.

Assumption 3.2. _The initial guess z_<sub>0</sub> _when solving_ (3.2) _is chosen such that_ \(S_k^\top r_0=0\)_, with r_<sub>0</sub>=_b-Az_<sub>0</sub>_. A possible choice is_ \(z_0=S_k\Lambda_k^{-1}S_k^\top b\).

Assumption 3.3. _The initial guess for the preconditioned system_ (3.4) _is chosen such that_ \(z_0=U^\theta y_0\).

Lemma 3.6. _Let Assumption_ 3.1 _hold and fix_ \(\delta\in(0,\gamma_0]\)_. Let_ \(1\le k\le n-1\)_. For_ \(i\in\{k+1,\dots,n\}\)_, define_

\(\widetilde{\zeta}_i(t):=\widehat{s}_i(t)^\top\left(\widehat{b}(t)-\widehat{A}(t)z_0\right)\text{\textit{and}}\widetilde{\beta}_i^\theta(t):=s_i^\theta(t)^\top\left(U^\theta b-A^\theta(t)y_0\right).\)

_Then, under Assumptions_ 3.2 _and_ 3.3_, for a_ \(t\ge 0\) _sufficiently small,_ \(\widetilde{\zeta}_i(t)^2=\widetilde{\beta}_i^\theta(t)^2+O(t^2)\) _uniformly in_ \(\theta\in\Theta_\delta\).

_Proof._ Using Lemma 3.3,

\(\widetilde{\zeta}_i(t)=\widehat{s}_i(t)^\top(\widehat{b}(t)-\widehat{A}(t)z_0)\)<br>
\(=(s_i+t\underline{S_i}D_i\underline{S_i^\top} Es_i)^\top(\overline{S_k}\overline{S_k^\top} r_0-t\overline{S_k}\overline{S_k^\top} ES_k\Lambda_k^{-1}S_k^\top b-t\overline{S_k}\overline{S_k^\top} E\overline{S_k}\overline{S_k^\top} z_0)+O(t^2)\)<br>
\(=s_i^\top r_0+t\left(s_i^\top E\underline{S_i}D_i\underline{S_i^\top} r_0-s_i^\top ES_k\Lambda_k^{-1}S_k^\top b-s_i^\top E\overline{S_k}\overline{S_k^\top} z_0\right)+O(t^2)\)<br>
\(=s_i^\top r_0+t\left(s_i^\top E\underline{S_i}D_i\underline{S_i^\top} r_0-s_i^\top ES_kS_k^\top x^*-s_i^\top E\overline{S_k}\overline{S_k^\top} z_0\right)+O(t^2).\)

