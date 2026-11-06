Here \(Z_\mathbf{C}=\mathbf{w}^\dagger Q_\mathcal{S}\mathbf{w}\ge 1-\varepsilon\). Invariance makes the cross terms under \(\widetilde{\mathbf{S}}_\mathrm{err}\) vanish. Since \(\|Q_\mathcal{S}\mathbf{w}\|^2\ge(1-\varepsilon)Z_\mathbf{C}\), every allowed **w** satisfies<tbc>

\(\left\langle\widetilde{\mathbf{S}}_\mathrm{err}\right\rangle_{\Gamma_\mathcal{S}}\le\lambda_\ell\frac{\|Q_\mathcal{S}\mathbf{w}\|^2}{Z_\mathbf{C}}+m\left(1-\frac{\|Q_\mathcal{S}\mathbf{w}\|^2}{Z_\mathbf{C}}\right)\le(1-\varepsilon)\lambda_\ell+m\varepsilon.\) (43)

<tbc>For the lower bound, choose **w** to be a top eigenvector of \(T_{\rho,\ell}\). The component of _Q_<sub>S</sub>**w** along **w** is _Z_**<sub>C</sub>**w**. Since \(T_{\rho,\ell}\unknown 0\), orthogonality gives \(\mathbf{w}^\dagger Q_\mathcal{S}T_{\rho,\ell} Q_\mathcal{S}\mathbf{w}\ge\lambda_\ell Z_\mathbf{C}^2\), with the matrices restricted to the occupied shells. The orthogonal term in (42) is nonnegative, so<tbc>

\(\left\langle\widetilde{\mathbf{S}}_\mathrm{err}\right\rangle_{\Gamma_\mathcal{S}}\ge\lambda_\ell Z_\mathbf{C}\ge(1-\varepsilon)\lambda_\ell.\) (44)

<tbc>Combining Eqs. (34), (40), (43) and (44) proves

\(f_\ell^*\ge(1-\varepsilon)\frac{\lambda_\ell}{m}-\frac{\sqrt{(q-1)\rho(1-\rho)}\varepsilon}{1-\varepsilon},f_\ell^*\le(1-\varepsilon)\frac{\lambda_\ell}{m}+\varepsilon+\frac{\sqrt{(q-1)\rho(1-\rho)}\varepsilon}{1-\varepsilon}.\) (45)

Finally, we bound the spectral edge \[Jor+25\]:

\(F_\rho(p_\ell)-m^{-1/2}\le\frac{\lambda_\ell}{m}\le F_\rho(p_\ell).\) (46)

For the upper bound, let \(x=m^{-1}\sum_kk|w_k|^2\le\ell/m\). Positivity bounds the off-diagonal entry of the one-qubit reduced density matrix of \(\sum_kw_k|D_k^m\rangle\) by \(\sqrt{x(1-x)}\). (26) then gives \(\mathbf{w}^\dagger T_\rho\mathbf{w}/m\le F_\rho(x)\le F_\rho(p_\ell)\).

The case \(\ell=0\) is exact. For the lower bound with \(\ell>0\), consider the binomial amplitudes<tbc>

\(w_k^{(p)}:=\sqrt{\genfrac(){pt}{2}{m}{k}p^k(1-p)^{m-k}},0\le k\le m,0<p<1.\) (47)

<tbc>Their qubit state is \((\sqrt{1-p}|0\rangle+\sqrt{p}|1\rangle)^{\otimes m}\), so (26) gives<tbc>

\(\frac{(\mathbf{w}^{(p)})^\dagger T_\rho\mathbf{w}^{(p)}}{m}=F_\rho(p).\) (48)

<tbc>Truncate \(\mathbf{w}^{(p_\ell)}\) at \(\ell\) and normalize. For \(\ell>0\),<tbc>

\(\frac{\lambda_\ell}{m}\ge\rho+(F_\rho(p_\ell)-\rho)R_\ell,R_\ell:=\frac{\mathrm{Pr}[\mathrm{Bin}(m-1,p_\ell)\le\ell-1]}{\mathrm{Pr}[\mathrm{Bin}(m,p_\ell)\le\ell]}.\) (49)

<tbc>Indeed, both the mean weight divided by _m_ and the adjacent-shell contribution are their untruncated values multiplied by \(R_\ell\), using (27). For \(K\sim\mathrm{Bin}(m,p_\ell)\) we therefore have \(\mathbb{E}[K|K\le\ell]=mp_\ell R_\ell\). Since \(\ell\ge mp_\ell\), the binomial median bound of \[KB78, Theorem 3\] gives \(\mathrm{Pr}[K\le\ell]\ge 1/2\). Thus<tbc>

\(mp_\ell(1-R_\ell)\le\frac{\mathbb{E}[(mp_\ell-K)_+]}{\mathrm{Pr}[K\le\ell]}\le\sqrt{mp_\ell(1-p_\ell)},\) (50)

