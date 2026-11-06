<tbc>Theorem 3.8. _Let Assumption_ 3.1 _hold and fix_ \(\delta\in(0,\gamma_0]\)_. Consider_ \(k\in\{1,\dots,n-1\}\) _and_ \(\theta\in\Theta_\delta\)_. Let z_<sub>0</sub> _and y_<sub>0</sub> _be as in Assumptions_ 3.2 _and_ 3.3_. Then, there exist_ \(t^*\in(0,\lambda_n/\|E\|_2)\), \(\gamma_1>0\) _, and_ \(\gamma_2>0\) _such that, for every_ \(1\le\ell\le n-k\) _and_ \(t\in[0,t^*]\) _such that_ \(x_{\ell+1}^{[P]}(t)=U^\theta y_{\ell+1}\) _and_ \(x_\ell^{[\mathrm{D}]}(t)\) _exist,_

(3.26) \(\left\|x^*(t)-x_{\ell+1}^{[P]}(t)\right\|_{A(t)}^2\le\frac{\alpha(t,\theta)^2}{\theta^2}\left\|x^*(t)-x_\ell^{[\mathrm{D}]}(t)\right\|_{A(t)}^2+\left(\gamma_1q_k^{2\ell}+\gamma_2\ell q_k^{2\ell-1}\right)t^2,\)

_where_ \(\alpha(t,\theta):=\mathrm{max}_{k+1\le i\le n}\left|\widehat{\lambda}_i(t)-\theta\right|\) _and_ \(q_k:=\frac{\lambda_k+t^*\|E\|_2}{\lambda_n-t^*\|E\|_2}-1\).

_Proof._ The proof proceeds in three steps: (1) we split the PCG error into a clustered and a nonclustered contribution using an admissible test polynomial; (2) we bound the clustered contribution; and (3) we bound the nonclustered contribution using Lemma 3.6. Let _t_<sub>0</sub>_\>_0 be chosen as in Lemma 3.7. A value _t_<sup>∗</sup>_\>_0 that is uniform in _k_ and in \(\theta\in\Theta_\delta\) is obtained by taking the minimum of _t_<sub>0</sub> and the finitely many positive thresholds associated, for \(1\le k\le n-1\), with Lemmas 3.3, 3.5 and 3.6.

Fix \(1\le\ell\le n-k\) and \(t\in[0,t^*]\) for which both iterates exist. For _i_=1_,...,n_, set \(\widetilde{\beta}_i^\theta(t):=s_i^\theta(t)^\top\left(U^\theta b-A^\theta(t)y_0\right)\) and let _y_<sup>∗</sup>(_t_) be the exact solution of \(A^\theta(t)y=U^\theta b\). Then, \(x^*(t)=U^\theta y^*(t)\) and \(\left\|x^*(t)-U^\theta y\right\|_{A(t)}^2=\left\|y^*(t)-y\right\|_{A^\theta(t)}^2\) for any _y_. The standard CG minimization property therefore gives

(3.27) \(\left\|x^*(t)-x_{\ell+1}^{[P]}(t)\right\|_{A(t)}^2=\mathrm{min}_{q\in\mathbb{P}_{\ell+1}(0)}\sum_{i=1}^n\frac{\widetilde{\beta}_i^\theta(t)^2}{\lambda_i^\theta(t)}q\left(\lambda_i^\theta(t)\right)^2.\)

Consider \(q_{\ell+1}^{(t)}(\lambda)=(1-\lambda/\theta)p_\ell^{(t)}(\lambda)\in\mathbb{P}_{\ell+1}(0)\). Using this polynomial in (3.27) and separating the sum over the eigenvalues of \(A^\theta(t)\) into the clustered indices _i_=1_,...,k_ (close to \(\theta\)) and the nonclustered indices _i=k_+1_,...,n_ gives

(3.28) \(\left\|x^*(t)-x_{\ell+1}^{[P]}(t)\right\|_{A(t)}^2\le T_\mathrm{c}^\theta(t)+T_\mathrm{n}^\theta(t),\)

where \(T_\mathrm{c}^\theta(t)=\sum_{i=1}^k\widetilde{\beta}_i^\theta(t)^2f_{\ell,t}^\theta(\lambda_i^\theta(t))\) and \(T_\mathrm{n}^\theta(t)=\sum_{i=k+1}^n\widetilde{\beta}_i^\theta(t)^2f_{\ell,t}^\theta(\lambda_i^\theta(t))\) with \(f_{\ell,t}^\theta(\lambda):=\frac{1}{\lambda}\left(1-\frac{\lambda}{\theta}\right)^2p_\ell^{(t)}(\lambda)^2\). For conciseness, define \(\underline{\mu}:=\lambda_n-t^*\|E\|_2\) and \(\overline{\mu_j}:=\lambda_j+t^*\|E\|_2\) for \(j\in\{k,k+1\}\).

We first bound \(T_\mathrm{c}^\theta(t)\). Let \(p_\ell^{(t)}(\lambda)=\prod_{j=1}^\ell\left(1-\frac{\lambda}{\xi_j(t)}\right)\), where \(\xi_1(t),\dots,\xi_\ell(t)\) are the Ritz values. Since these Ritz values lie in \([\underline{\mu},\overline{\mu_{k+1}}]\), for every \(\lambda\in[\underline{\mu},\overline{\mu_k}]\),

(3.29) \(\left|p_\ell^{(t)}(\lambda)\right|\le\mathrm{max}_{\lambda\in[\underline{\mu},\overline{\mu_k}]\xi\in[\underline{\mu},\overline{\mu_{k+1}}]}\left|1-\frac{\lambda}{\xi}\right|^\ell=\left(\frac{\lambda_k+t^*\|E\|_2}{\lambda_n-t^*\|E\|_2}-1\right)^\ell=q_k^\ell,\)

The equality follows from the fact that the maximum is attained at \(\lambda=\overline{\mu_k}\) and \(\xi=\underline{\mu}\) (using \(\underline{\mu}>0\) and \(\overline{\mu_k}\ge\overline{\mu_{k+1}}\)). For \(i\le k\), Weyl’s inequality gives \(|\lambda_i^\theta(t)-\theta|\le t\); since \(\theta\ge\lambda_n\), this yields \(\left|1-\frac{\lambda_i^\theta(t)}{\theta}\right|^2\le\frac{t^2}{\theta^2}\le\frac{t^2}{\lambda_n^2}\). Using (3.29), gives

\(T_\mathrm{c}^\theta(t)\le\left(\sum_{i=1}^k\frac{\widetilde{\beta}_i^\theta(t)^2}{\lambda_i^\theta(t)}\right)q_k^{2\ell} t^2/\lambda_n^2\le\frac{\left\|U^\theta\left(b-A(t)z_0\right)\right\|_2^2}{\underline{\mu}\lambda_n^2}q_k^{2\ell} t^2\)<br>
\(\le\frac{\mathrm{max}_{0\le s\le t^*}\|b-A(s)z_0\|_2^2}{\underline{\mu}\lambda_n^2}q_k^{2\ell} t^2=:c_{1,k}q_k^{2\ell} t^2.\)

