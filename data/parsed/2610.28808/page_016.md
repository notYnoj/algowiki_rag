## 4.1. Computational complexity: PCG versus deflated CG.

Assume that _S<sub>k</sub>_=\[_s_<sub>1</sub>_,...,s<sub>k</sub>_\] and \(\Lambda_k=\mathrm{diag}(\lambda_1,\dots,\lambda_k)\) are available. Both deflated CG and PCG with \(U^\theta\) use CG as an iterative solver; the main computational difference lies in the cost of applying the deflation projector versus applying the scaled spectral preconditioner.

Deflated CG requires the projector \(P(t)=I_n-V_k(t)\left(S_k^\top V_k(t)\right)^{-1}S_k^\top\), where _V<sub>k</sub>(t_)=_A(t)S<sub>k</sub>_. Constructing this projector requires _k_ products with _A(t_) to form _V<sub>k</sub>(t_), O(_nk_<sup>2</sup>) operations to assemble \(S_k^\top V_k(t)\), and O(_k_<sup>3</sup>) operations to factorize it. Once these quantities are available, applying _P(t_) requires products with \(S_k^\top\) and _V<sub>k</sub>(t_) and the solution of a \(k\times k\) linear system. Deflated CG stores _S<sub>k</sub>_, _V<sub>k</sub>(t_), and the dense matrix \(S_k^\top V_k(t)\). In contrast, PCG with the scaled spectral preconditioner \(U^\theta\) stores only _S<sub>k</sub>_, the associated eigenvalues, and the scalar parameter \(\theta\). Applying \(U^\theta\) requires one multiplication by each of \(S_k^\top\) and _S<sub>k</sub>_, together with a diagonal scaling.

## 4.2. Synthetic data experiments.

We consider the linear system _A(t)x_=(_A+tE)x=b_, where \(A\in\mathbb{R}^{n\times n}\) is diagonal with entries

(4.1) \(\lambda_i=\lambda_n+\frac{n-i}{n-1}\left[\psi+(\lambda_1-\lambda_n-\psi)\rho^{i-1}\right],i=1,\dots,n,\)

where \(0<\rho<1\) controls the exponential decay of the spectrum and \(0<\psi<\lambda_1-\lambda_n\) ensures that the smallest consecutive eigenvalue gap satisfies \(\gamma_0\ge\psi/(n-1)>0\) in exact arithmetic. Setting \(\psi=0\) recovers the spectrum used in \[14\]. In what follows, we fix \(n=4\times 10^3\), \(\lambda_1=10^6\), \(\lambda_n=1\), and \(\psi=1\). Throughout this section, _E_ is a fixed randomly generated symmetric matrix satisfying \(\|E\|_F=1\), and \(b=[1,\dots,1]^\top/\sqrt{n}\). The initial guesses satisfy Assumptions 3.2 and 3.3.

The numerical study is organized in two parts. First, we compare the PCG error with the leading term in Theorem 3.8 and discuss the effect of the omitted remainder. Second, we compare the energy-norm convergence of CG, PCG using \(U^\theta\), and deflated CG for the same family of test matrices. All methods are run with full reorthogonalization. In the supplementary material, we present additional numerical results for a variational data assimilation problem.

## 4.2.1. Comparison with the theoretical bound.

We assess the leading term in the upper bound of Theorem 3.8 by evaluating \(\left\|x^*(t)-x_{\ell+1}^{[P]}(t)\right\|_{A(t)}^2\) and \((\alpha(t,\theta)^2/\theta^2)\left\|x^*(t)-x_\ell^{[\mathrm{D}]}(t)\right\|_{A(t)}^2\), as functions of the perturbation size _t_ for different \(\ell\) and \(\rho\). We set _k_=60 and choose \(\theta_m\) as scaling. For this choice, \(\alpha(t,\theta_m)/\theta_m\approx 0.99<1\) over the tested range of _t_.  4.1 reports, for \(\rho\in\{0.9,0.94\}\), the gap \(\gamma_0\), the ratio \(\lambda_k/\lambda_n\) governing _q<sub>k</sub>_, and the separation of \(\theta_m\) from the nondeflated spectrum.

From  4.1, Assumption 3.1 is satisfied; choosing \(\delta=\gamma_0\) ensures that \(\theta_m\in\Theta_\delta\). The behavior of the omitted remainder in Theorem 3.8 is governed by _q<sub>k</sub>_, whose size is controlled mainly by the ratio \(\lambda_k/\lambda_n\). From  4.1, the ratio \(\lambda_k/\lambda_n>10^3\) for both cases; consequently, the remainder \(\gamma_1q_k^{2\ell}+\gamma_2\ell q_k^{2\ell-1}\) becomes large for large values of \(\ell\).

\begin{tabular}{cccc}
 & \(\gamma_0\) & \(\lambda_k/\lambda_n\) & \(\mathrm{min}_{i=k+1,\dots,n}|\theta_m-\lambda_i|\) \\
\(\rho=0.9\) & \(2.5\times 10^{-4}\) & \(1.969\times 10^3\) & \(4.387\times 10^1\) \\
\(\rho=0.94\) & \(2.5\times 10^{-4}\) & \(2.559\times 10^4\) & \(1.254\times 10^2\) \\
\end{tabular}

4.1

_Diagnostic quantities: the minimum eigenvalue gap_ \(\gamma_0\)_, the ratio_ \(\lambda_k/\lambda_n\) _governing q<sub>k</sub>, and the separation_ \(\mathrm{min}_{i>k}|\theta_m-\lambda_i|\) _of the midrange scaling parameter from the nondeflated spectrum._

