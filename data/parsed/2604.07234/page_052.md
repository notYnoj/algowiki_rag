<tbc>As the sufficient statistic of this exponential family is (_a,b_), which is not contained in an affine line, the family is thus minimal. Additionally, since \(p_\theta\) has discrete support, it follows from Theorem E.1 that the mean parameter space is<tbc>

\(\mathcal{M}:=\left\{(\alpha,\beta)\in\mathbb{R}^2:1\le\beta\le\alpha\right\}\Longrightarrow\mathcal{M}^\circ=\left\{(\alpha,\beta)\in\mathbb{R}^2:1<\beta<\alpha\right\}.\)

<tbc>It follows from Lemma 4.10 (whose proof does not rely on the preceding Lemma 4.9) and (4.32) that<tbc>

\(\Omega:=\left\{(\theta_1,\theta_2)\in\mathbb{R}^2:A(\theta)<\infty\right\}=\left\{(\theta_1,\theta_2)\in(-\infty,0)^2:e^{\theta_1}(1+e^{\theta_2/2})^2<1\right\}.\)

<tbc>It readily follows from this description of \(\Omega\) that for any \(\gamma=(\gamma_1,\gamma_2)\in\Omega\), there exists an open box \(I\subset\Omega\) such that \(\gamma\in I\) and uniformly over \(\theta\in I\),<tbc>

\(\sum_{a,b}\frac{\partial p_\theta(a,b)}{\partial\theta_1}=\sum_{a,b}a\cdot p_\gamma(a,b)<\infty;\sum_{a,b}\frac{\partial p_\theta(a,b)}{\partial\theta_2}=\sum_{a,b}b\cdot p_\gamma(a,b)\le\sum_{a,b}a\cdot p_\gamma(a,b)<\infty.\)

<tbc>It thus follows that this family satisfies, for all \(\theta\in\Omega\), that

(E.1) \(\nabla_\theta A(\theta)=\left(\mathbb{E}_\theta[a],\mathbb{E}_\theta[b]\right),\)

which we want to be equal to \((1/(\alpha\rho),1/\rho)\in\mathcal{M}^\circ\). Altogether, Theorem E.2 yields the existence of \((\theta_1^*,\theta_2^*)\) for which (E.1) is satisfied. Letting \(\left(\lambda_1^*,\lambda_2^*\right)=(-\theta_1^*,-\theta_2^*)\), we may then set \(\lambda_0^*\) via<tbc>

\(e^{1+\lambda_0^*}=\sum_{a,b}w(a,b)e^{-\lambda_1^*a-\lambda_2^*b}.\)

<tbc>We conclude that this system of equations has a solution. We now let \(\nu^*\), _Z_<sup>∗</sup>, \(\lambda_1^*\), and \(\lambda_2^*\) denote the corresponding quantities for such a solution. It holds that

(E.2) \(\mathrm{log}\nu^*(a,b)=\mathrm{log}w(a,b)-\lambda_1^*a-\lambda_2^*b-\mathrm{log}Z^*.\)

For any probability measure \(\nu\), the objective functional may be expressed via

\(H(\nu)+\mathbb{E}_\nu\left[\mathrm{log}w\right]=-\sum_{a,b}\nu(a,b)\mathrm{log}\nu(a,b)+\sum_{a,b}\nu(a,b)\mathrm{log}w(a,b)=-\sum_{a,b}\nu(a,b)\mathrm{log}\nu(a,b)+\sum_{a,b}\nu(a,b)\mathrm{log}\nu^*+\sum_{a,b}\nu\lambda_1^*a+\sum\nu(a,b)\lambda_2^*b+\sum_{a,b}\nu(a,b)\mathrm{log}Z^*=-\sum_{a,b}\nu(a,b)\mathrm{log}\frac{\nu(a,b)}{\nu^*(a,b)}+\frac{c\lambda_1}{\rho}+\frac{\lambda_2}{\rho}+\mathrm{log}Z^*=\frac{c\lambda_1}{\rho}+\frac{\lambda_2}{\rho}+\mathrm{log}Z^*-D_\mathrm{KL}\left(\nu\left\|\nu^*\right\right\rangle\) (E.3)

where the first equality in the third line is due to the normalization and mean constraints applied to the solution. Since \(D_\mathrm{KL}\left(\nu\left\|\nu^*\right\rangle\ge 0\), we conclude that \(\nu^*\) is a global maximizer of the objective functional.

## References

\[Ale94\] K. S. Alexander. The Rate of Convergence of the Mean Length of the Longest Common Subsequence. _The Annals of Applied Probability_ 4.4 (1994), pp. 1074-1082.

\[Bou99\] J. Boutet de Monvel. Extensive Simulations for Longest Common Subsequences: Finite Size Scaling, a Cavity Solution, and Configuration Space Properties. _The European Physical Journal B_ 7 (1999), pp. 293-308.

\[Che19\] M. Cheraghchi. Capacity upper bounds for deletion-type channels. _Journal of the ACM (JACM)_ 66.2 (2019), pp. 1-79.

\[CS75\] V. Chvátal and D. Sankoff. Longest Common Subsequences of Two Random Sequences. _Journal of Applied Probability_ 12.2 (1975), pp. 306-315.

\[CSS15\] I. Corwin, T. Seppäläinen, and H. Shen. The strict-weak lattice polymer. _Journal of Statistical Physics_ 160.4 (2015), pp. 1027-1053.

\[Dek79\] J. G. Deken. Some Limit Results for Longest Common Subsequences. _Discrete Mathematics_ 26.1 (1979), pp. 17-31.

