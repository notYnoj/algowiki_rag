By choosing the eigenvectors

\(\mathbf{v}_{-\sqrt{3}}=\left(\begin{array}{ c }
1 \\
-\sqrt{3} \\
1
\end{array}\right),\mathbf{v}_0=\left(\begin{array}{ c }
-2 \\
0 \\
1
\end{array}\right),\mathbf{v}_{\sqrt{3}}=\left(\begin{array}{ c }
1 \\
\sqrt{3} \\
1
\end{array}\right),\) (C.40)

we have \(\mathbf{b}=\mathbf{v}_{-\sqrt{3}}+\mathbf{v}_0+\mathbf{v}_{\sqrt{3}}\), and \(\widehat{\mathbf{H}}^{n,1/2,(1)}(k)\) and \(\xi_{1/2}(k)\) can be solved from the equations (C.38) and (C.39) as

\(\widehat{\mathbf{H}}^{n,1/2,(1)}(k)=\alpha_\mu^{(1)}(k)\mathbf{a}\mathbf{v}_\mu+\sum_{\mu^\prime\neq\mu}\alpha_{\mu^\prime}^{(1)}(k)\mathbf{v}_{\mu^\prime},\xi_{1/2}(k)=\frac{1}{2\Delta x}\left[\phi_\mu^{(0)}(k)e^{-\mathrm{i}k\Delta x}-e^{\mathrm{i}k\Delta x}\right],\) (C.41)

where

\(\alpha_\mu^{(1)}(k)=\frac{\nu(e^{-\mathrm{i}k\Delta x}\xi_{1/2}(k)-e^{\mathrm{i}k\Delta x}\xi_0(k))}{2C_{M+1}\left[1-\frac{\nu}{2}\left(1+\frac{\mu}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x}\right]},\) (C.42)

and \(\alpha_{\mu^\prime}^{(1)}(k)\) for \(\mu'\neq\mu\) are not needed in the subsequent calculation. Applying a similar procedure to the backward sweep (C.4), we obtain \(\widehat{\mathbf{H}}^{n,1,(1)}(k)\) and \(\xi_1(k)\) as follows:

\(\widehat{\mathbf{H}}^{n,1,(1)}(k)=\beta_\mu^{(1)}(k)\mathbf{a}\mathbf{v}_\mu+\sum_{\mu^\prime\neq\mu}\beta_{\mu^\prime}^{(1)}(k)\mathbf{v}_{\mu^\prime},\xi_1(k)=\frac{1}{2\Delta x}\left[\phi_\mu^{(0)}(k)e^{-\mathrm{i}k\Delta x}-\mathcal{G}_\mu^{(0)}(k)e^{\mathrm{i}k\Delta x}\right],\) (C.43)

where

\(\beta_\mu^{(1)}(k)=\frac{\psi_\mu^{(0)}(k)\nu(e^{-\mathrm{i}k\Delta x}\xi_{1/2}(k)-e^{\mathrm{i}k\Delta x}\xi_0(k))}{2C_{M+1}\left[1-\frac{\nu}{2}\left(1+\frac{\mu}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x}\right]}+\frac{\nu(e^{-\mathrm{i}k\Delta x}\xi_{1/2}(k)-e^{\mathrm{i}k\Delta x}\xi_1(k))}{2C_{M+1}\left[1-\frac{\nu}{2}\left(1-\frac{\mu}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x}\right]}.\) (C.44)

and \(\beta_{\mu^\prime}^{(1)}(k)\) for \(\mu'\neq\mu\) are insignificant in the present calculation. Here we recall that the definitions of \(\xi_0(k)\), \(\xi_{1/2}(k)\) and \(\xi_1(k)\) are given in (C.36), (C.41) and (C.43), respectively.

We now consider the hydrodynamic stage, which changes only the first three components. Assume

\(\mathbf{E}_j^{n,\ell}=\widetilde{\mathbf{E}}^{n,\ell}(\varepsilon,k)e^{\mathrm{i}jk\Delta x},\widetilde{\mathbf{E}}^{n,\ell}(\varepsilon,k)=a[\mathcal{G}_\mu^{(0)}(k)]^{\ell+1}\mathbf{v}_\mu+\varepsilon\widetilde{\mathbf{E}}^{n,\ell,(1)}(k)+O(\varepsilon^2),\ell=0,1,\dots,\gamma_2.\)

Let

\(\widetilde{\mathbf{E}}^{n,\ell,(1)}(k)=\gamma_\mu^{\ell,(1)}(k)\mathbf{a}\mathbf{v}_\mu+\sum_{\mu^\prime\neq\mu}\gamma_{\mu^\prime}^{\ell,(1)}(k)\mathbf{v}_{\mu^\prime},\ell=0,1,\dots,\gamma_2.\)

The initialization of the hydrodynamic stage gives \(\gamma_\mu^{0,(1)}(k)=\beta_\mu^{(1)}(k)\), and the error evolution equations (C.7)-(C.8) yield the recurrence relation:

\(\gamma_\mu^{\ell+1,(1)}(k)=\mathcal{G}_\mu^{(0)}(k)\gamma_\mu^{\ell,(1)}(k)+J_\mu(k)\xi_1(k),\ell=0,1,\dots,\gamma_2-1,\)

with

\(J_\mu(k)=-\mathrm{i}\frac{\nu}{C_{M+1}}\mathrm{sin}k\Delta x\left[\frac{\psi_\mu^{(0)}(k)}{1-\frac{\nu}{2}\left(1+\frac{\mu}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x}}+\frac{1}{1-\frac{\nu}{2}\left(1-\frac{\mu}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x}}\right].\) (C.45)

The coefficient \(\gamma_\mu^{\gamma_2,(1)}(k)\) is the first-order correction to the leading-order amplification factor \(\Lambda_\mu^{(0)}(k)\) (see (39)). Solving this recurrence yields the following expression for \(\Lambda_\mu^{(1)}(k)\):

\(\Lambda_\mu^{(1)}(k)=\gamma_\mu^{\gamma_2,(1)}(k)=[\mathcal{G}_\mu^{(0)}(k)]^{\gamma_2}\beta_\mu^{(1)}(k)+\frac{1-[\mathcal{G}_\mu^{(0)}(k)]^{\gamma_2}}{1-\mathcal{G}_\mu^{(0)}(k)}J_\mu(k)\xi_1(k).\) (C.46)

