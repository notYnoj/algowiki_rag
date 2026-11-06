<tbc>\[toc\] A DEFLATION-BASED PRECONDITIONER FOR PCG 15<tbc>

<tbc>where \(c_5:=nc_\beta c_2+c_\zeta c_\lambda c_3\) and \(c_6:=c_\zeta c_\lambda c_4\). Using \(\left|1-\widehat{\lambda}_i(t)/\theta\right|^2\le\alpha(t,\theta)^2/\theta^2\) and the deflated CG error representation in Theorem 3.2, we obtain

(3.37) \(T_\mathrm{n}^\theta(t)\le\frac{\alpha(t,\theta)^2}{\theta^2}\left\|x^*(t)-x_\ell^{[\mathrm{D}]}(t)\right\|_{A(t)}^2+\left(c_5q_k^{2\ell}+c_6\ell q_k^{2\ell-1}\right)t^2.\)

The result follows from (3.28), (3.30), and (3.37) with \(\gamma_1:=c_1+c_5\) and \(\gamma_2:=c_6\). \(\square\)

Theorem 3.8 provides an explicit second-order comparison between PCG with \(U^\theta\) and deflated CG. After one additional PCG iteration, the squared energy-norm error is bounded by the squared deflated CG error multiplied by \((\alpha(t,\theta)/\theta)^2\), plus a remainder of order _t_<sup>2</sup>. The quantity \(\alpha(t,\theta)\) is the largest distance from \(\theta\) to the nonzero eigenvalues of \(\widehat{A}(t)\); by Lemma 3.3, these eigenvalues agree with the corresponding eigenvalues of _A(t_) up to _O(t_<sup>2</sup>). Thus, if \(\alpha(t,\theta)/\theta<1\), the leading term is contractive.

The explicit factor \(\gamma_1q_k^{2\ell}+\gamma_2\ell q_k^{2\ell-1}\) describes how the perturbation remainder depends on the iteration index. When _q<sub>k</sub>\>_1, this upper bound can grow rapidly with \(\ell\) and can be pessimistic; when 0_\<q<sub>k</sub>\<_1, its behavior is different and it may decrease as \(\ell\) grows. This concerns only the quality of the perturbation estimate and does not imply that either iterative method has increasing error. Increasing _k_ removes more eigenvalues from the nondeflated spectrum and may reduce _q<sub>k</sub>_.

Following Diouane et al. \[6\], the next proposition introduces two scaling choices and shows that both yield a contractive leading factor for sufficiently small perturbations.

Proposition 3.9. _Suppose the assumptions of Theorem_ 3.8 _hold._

(i) _Then, for sufficiently small_ \(t\ge 0\)_, the bound_ (3.26) _holds with_ \(\theta=\lambda_k\) _and its leading factor is contractive, i.e.,_ \(\alpha(t,\lambda_k)/\lambda_k<1\).<tbc>

(ii) _Suppose, in addition, that_ \(\lambda_n\) _is known, and let_ \(\theta_m:=(\lambda_k+\lambda_n)/2\) _with_ \(\theta_m\notin\{\lambda_{k+1},\dots,\lambda_n\}\)_. Then, for sufficiently small_ \(t\ge 0\)_, the bound_ (3.26) _also holds with_ \(\theta=\theta_m\)_, and its leading factor is strictly smaller than the one in_ (i)_, i.e.,_ \(\alpha(t,\theta_m)/\theta_m<\alpha(t,\lambda_k)/\lambda_k<1\).

_Proof._ Indeed, since \(\lambda_k-\lambda_i\ge\lambda_k-\lambda_{k+1}\ge\gamma_0\) for every _i\>k_, we have \(\lambda_k\in\Theta_{\gamma_0}\). Let _t_<sup>∗</sup>_\>_0 be the threshold supplied by Theorem 3.8 when it is applied with \(\delta=\gamma_0\), i.e., for any \(t\le t^*\), the bound (3.26) holds with \(\theta=\lambda_k\). At _t_=0, the nonzero eigenvalues of \(\widehat{A}(0)\) are \(\lambda_{k+1},\dots,\lambda_n\), and hence \(\alpha(0,\lambda_k)/\lambda_k=(\lambda_k-\lambda_n)/\lambda_k<1\). Since the eigenvalues of \(\widehat{A}(t)\) depend continuously on _t_, and hence so does \(t\mapsto\alpha(t,\lambda_k)\). Therefore, there exists \(\bar{t}>0\) such that \(\alpha(t,\lambda_k)/\lambda_k<1\) for every \(t\in[0,\bar{t}]\). Hence, by taking \(\tau:=\mathrm{min}\{t^*,\bar{t}\}\) proves (i).

To prove (ii), suppose that \(\lambda_n\) is known and that \(\theta_m\notin\{\lambda_{k+1},\dots,\lambda_n\}\). Set \(\delta:=\mathrm{min}\left\{\gamma_0,\mathrm{min}_{i=k+1,\dots,n}|\theta_m-\lambda_i|\right\}\). Then, \(0<\delta\le\gamma_0\) and \(\theta_m\in\Theta_\delta\). Let \(t_m^*>0\) be the threshold supplied by Theorem 3.8 for this \(\delta\), i.e., for any \(t\le t_m^*\), the bound (3.26) holds with \(\theta=\theta_m\). At _t_=0,

(3.38) \(\frac{\alpha(0,\theta_m)}{\theta_m}=\frac{\lambda_k-\lambda_n}{\lambda_k+\lambda_n}<\frac{\lambda_k-\lambda_n}{\lambda_k}=\frac{\alpha(0,\lambda_k)}{\lambda_k}<1.\)

By continuity, there exists \(\bar{t}_m>0\) such that the strict inequalities in (3.38) remain valid for every \(t\in[0,\bar{t}_m]\). Taking \(\tau_m:=\mathrm{min}\{\tau,t_m^*,\bar{t}_m\}\) proves (ii). \(\square\)

We note that the choice \(\theta=\theta_m\) is particularly practical in applications such as variational data assimilation, where \(\lambda_n\) is often known a priori.

**4. Numerical experiments.**

