<tbc>We split the summation in \(j_h(\widetilde{\mathcal{I}}_h\tilde{u},\widetilde{\mathcal{I}}_h\tilde{u})\) into low-order (\(2\le j\le k\)) and high-order (\(k+1\le j\le 2k\)) contributions. For the low-order jumps, since the extended exact solution \(\tilde{u}\in H^{k+1}(\widetilde{\Omega}_h)\), the traces of its normal derivatives are continuous across internal faces, meaning \(\left\unknown\partial_n^j\tilde{u}\right\unknown\equiv 0\). Thus, we can insert \(\tilde{u}\) to obtain \(\left\unknown\partial_n^j\widetilde{\mathcal{I}}_h\tilde{u}\right\unknown=\left\unknown\partial_n^j(\widetilde{\mathcal{I}}_h\tilde{u}-\tilde{u})\right\unknown=-\left\unknown\partial_n^j\rho\right\unknown\). Applying the standard continuous scaled trace inequality and the approximation properties of \(\rho\), we have

\(\sum_{j=2}^k\sum_{F\in\mathcal{F}_h^\Gamma} h_F^{2j-3}\|\left\unknown\partial_n^j\widetilde{\mathcal{I}}_h\tilde{u}\right\unknown\|_{L^2(F)}^2=\sum_{j=2}^k\sum_{F\in\mathcal{F}_h^\Gamma} h_F^{2j-3}\|\left\unknown\partial_n^j\rho\right\unknown\|_{L^2(F)}^2\)<br>
\(\le C\sum_{j=2}^kh^{2j-3}\big(h^{-1}h^{2(k+1-j)}\big)\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}^2\)<br>
\(\le Ch^{2k-2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}^2.\) (3.31)

For the high-order jumps, the exact solution lacks sufficient regularity but we can directly apply the discrete trace inequality followed by the inverse inequality to reduce the order of derivatives from _j_ down to _k_+1,

\(\sum_{j=k+1}^{2k}\sum_{F\in\mathcal{F}_h^\Gamma} h_F^{2j-3}\|\left\unknown\partial_n^j\widetilde{\mathcal{I}}_h\tilde{u}\right\unknown\|_{L^2(F)}^2\le C\sum_{j=k+1}^{2k}\sum_{F\in\mathcal{F}_h^\Gamma} h^{2j-3}\big(h^{2(k+1-j)-1}\|\widetilde{\mathcal{I}}_h\tilde{u}\|_{H^{k+1}(K)}^2\big)\)<br>
\(\le Ch^{2k-2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}^2\) (3.32)

where we use the _H_<sup>_k_+1</sup>-stability of the spline interpolant \(\|\widetilde{\mathcal{I}}_h\tilde{u}\|_{H_h^{k+1}(\Omega_h)}\le C\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\).

Combining (3.31) and (3.32), the total penalty term satisfies

\(j_h(\widetilde{\mathcal{I}}_h\tilde{u},\widetilde{\mathcal{I}}_h\tilde{u})\le Ch^{2k-2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}^2.\) (3.33)

Finally, substituting this bound along with (3.30) into (3.29), we achieve the optimal energy norm estimate for \(\xi_h\):

\(\left\unknown\left\unknown\xi_h\right\unknown\right\unknown^2\le Ch^{2k-2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}^2\le Ch^{2k-2}\|f\|_{H^{k-1}(\Omega_h)}^2,\) (3.34)

where the last step follows from (3.23).

We exploit the error decomposition \(e_h=\rho+\xi_h\) and apply the triangle inequality:

\(\|e_h\|_{H^2(\Omega_h)}\le\|\rho\|_{H^2(\Omega_h)}+\|\xi_h\|_{H^2(\Omega_h)}\le Ch^{k-1}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}+\|\xi_h\|_{H^2(\Omega_h)}\) (3.35)

with the interpolation error estimate (3.9).

By Lemma 3.3, the discrete error component \(\xi_h\in S_h\) satisfies<tbc>

\(\|\xi_h\|_{H^2(\Omega_h)}^2\le C\big(\|\Delta\xi_h\|_{L^2(\Omega_h)}^2+j_h(\xi_h,\xi_h)\big)=C\left\unknown\left\unknown\xi_h\right\unknown\right\unknown^2.\)

<tbc>Consequently, we obtain the final optimal _H_<sup>2</sup>-norm error estimate:

\(\|e_h\|_{H^2(\Omega_h)}\le Ch^{k-1}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\le Ch^{k-1}\|f\|_{H^{k-1}(\Omega_h)}.\) (3.36)

We now establish the optimal _H_<sup>1</sup>-error estimate by employing a standard duality argument. Let _v_ be the solution to the dual problem:

\(\left\{\begin{array}{ c c }
-\Delta v=-e_h & \text{in}\Omega, \\
v=0 & \text{on}\Gamma.
\end{array}\right.\) (3.37)

Extending the dual solution _v_ from \(\Omega\) to the extended domain \(\widetilde{\Omega}_h\), elliptic regularity on the fixed domain \(\Omega\), followed by boundedness of this extension, gives

\(\|v\|_{H^3(\widetilde{\Omega}_h)}\le C\|v\|_{H^3(\Omega)}\le C\|e_h\|_{H^1(\Omega_h)}.\) (3.38)

