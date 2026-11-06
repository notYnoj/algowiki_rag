For \(0<\nu<1\), since

\(P''_1(t)=128(1-\nu)^2\ge 0,P'_1(t_*)=32(\nu-1)(\nu^2-\sqrt{5}\nu+\sqrt{5})<0,\) (C.31)

we conclude that \(P'_1(t)<0\) for \(0\le t\le t_*\). Thus _P_<sub>1</sub> is decreasing on \[0_,t_<sub>∗</sub>\] and

\(P_q(t)\ge P_1(t)\ge P_1(t_*)=4\nu^2\left[\nu^2+(1-2\sqrt{5})\nu+2\sqrt{5}-1\right]>0,\forall t\in[0,t_*].\)

Therefore, when \(0<|k\Delta x|\le 2\pi/5\), every factor on the right-hand side of (C.28) is positive, which proves (C.21).

## Appendix C.5. First-order correction for \(\gamma_1=1\)

The first-order correction to the amplification factor can be derived in a manner similar to the leading-order analysis. Here we first claim that along an eigenvalue branch with a nonzero limit, the error \(e_{4,j}^{n,r}\) has order \(O(\varepsilon^2)\) when \(M\ge 4\). Taking the fifth component of the equation (C.3), we obtain

\(\left(1+\frac{\omega}{\varepsilon}\right)e_{4,j}^{n,s+1/2}=(1-\nu)e_{4,j}^{n,s}+\frac{\nu}{2}e_{4,j-1}^{n,s+1/2}+\frac{\nu}{2}e_{4,j+1}^{n,s}+\frac{\nu}{2C_{M+1}}(e_{3,j-1}^{n,s+1/2}-e_{3,j+1}^{n,s})+\frac{5\nu}{2C_{M+1}}(e_{5,j-1}^{n,s+1/2}-e_{5,j+1}^{n,s}),\)

where the terms involving \(e_{5,j\pm 1}\) are omitted when _M_=4 and the right-hand side is \(O(\varepsilon)\) due to (C.13). Since \(1+\omega/\varepsilon=O(\varepsilon^{-1})\), it follows that \(e_{4,j}^{n,s+1/2}=O(\varepsilon^2)\). Similarly, the fifth component of (C.4) gives \(e_{4,j}^{n,s+1}=O(\varepsilon^2)\). Since \(e_{4,j}^{n,\gamma_1}=e_{4,j}^{n+1,0}\), below we will also assume \(e_{4,j}^{n,0}\) to be \(O(\varepsilon^2)\). This conclusion enables us to derive the first-order correction to the amplification factor by considering only the first four components of the error vector \(\delta\mathbf{u}_j^{(n)}\), as other components are not coupled to these four components up to the first order in \(\varepsilon\).

For simplicity, we set \(\gamma_1=1\) in this subsection. For a fixed wave number _k_, we write<tbc>

\(\mathbf{H}_j^{n,r}=\widehat{\mathbf{H}}^{n,r}(\varepsilon,k)e^{\mathrm{i}jk\Delta x},e_{3,j}^{n,r}=\widehat{e}_3^{n,r}(\varepsilon,k)e^{\mathrm{i}jk\Delta x},r\in\left\{0,\frac{1}{2},1\right\}.\) (C.32)

<tbc>Applying the results of the leading-order analysis, we know that along the leading-order eigenvalue branch \(\mu\), the first three components of an eigenvector of \(\mathbf{T}(\varepsilon,k)\), together with the intermediate amplitudes obtained during the moment sweeps, can be expanded as<tbc>

\(\widehat{\mathbf{H}}^{n,0}(\varepsilon,k)=a\mathbf{v}_\mu+\varepsilon\widehat{\mathbf{H}}^{n,0,(1)}(k)+O(\varepsilon^2),\) (C.33)

\(\widehat{\mathbf{H}}^{n,1/2}(\varepsilon,k)=a\phi_\mu^{(0)}(k)\mathbf{v}_\mu+\varepsilon\widehat{\mathbf{H}}^{n,1/2,(1)}(k)+O(\varepsilon^2),\) (C.34)

\(\widehat{\mathbf{H}}^{n,1}(\varepsilon,k)=a\mathcal{G}_\mu^{(0)}(k)\mathbf{v}_\mu+\varepsilon\widehat{\mathbf{H}}^{n,1,(1)}(k)+O(\varepsilon^2),\) (C.35)

<tbc>and for the fourth component, we let \(\widehat{e}_3^{n,r}(\varepsilon,k)=a\varepsilon\xi_r(k)+O(\varepsilon^2)\) for \(r\in\{0,1/2,1\}\). Since the leading-order eigenvalue of \(\mathbf{T}(\varepsilon,k)\) is \(\Lambda_\mu^{(0)}(k)=[\mathcal{G}_\mu^{(0)}(k)]^{\gamma_2+1}\), and the hydrodynamic stage does not change \(e_{3,j}^{n,r}\), we have<tbc>

\(\xi_1(k)=[\mathcal{G}_\mu^{(0)}(k)]^{\gamma_2+1}\xi_0(k).\) (C.36)

<tbc>Without loss of generality, we may assume the first-order term in (C.33) has no component along \(\mathbf{v}_\mu\):

\(\widehat{\mathbf{H}}^{n,0,(1)}(k)=\sum_{\mu^\prime\in\{-\sqrt{3},0,\sqrt{3}\backslash\{\mu\}}}c_{\mu^\prime}^{(1)}(k)\mathbf{v}_{\mu^\prime}.\) (C.37)

Substituting (C.33), (C.34) and (C.37) into the first four equations of (C.3) and collecting the \(O(\varepsilon)\) terms in the first three equations and the _O_(1) terms in the fourth, we obtain

\(\left[\mathbf{I}-\frac{\nu}{2}\left(\mathbf{I}+\frac{\mathbf{A}_h}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x}\right]\widehat{\mathbf{H}}^{n,1/2,(1)}(k)\)<br>
\(=\sum_{\mu^\prime\in\{-\sqrt{3},0,\sqrt{3}\backslash\{\mu\}}}\left[1-\nu+\frac{\nu}{2}\left(1-\frac{\mu'}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x}\right]c_{\mu^\prime}^{(1)}(k)\mathbf{v}_{\mu^\prime}+\frac{a\nu}{2C_{M+1}}\mathbf{b}\left[\xi_{1/2}(k)e^{-\mathrm{i}k\Delta x}-\xi_0(k)e^{\mathrm{i}k\Delta x}\right],\) (C.38)

\(\omega\xi_{1/2}(k)=\frac{\nu}{2C_{M+1}}\left[\phi_\mu^{(0)}(k)e^{-\mathrm{i}k\Delta x}-e^{\mathrm{i}k\Delta x}\right].\) (C.39)

