<tbc>where the last inequality uses (3.12) and the _H_<sup>2</sup>-stability of the spline interpolation operator. Let \(\mathcal{I}_h\phi\in V_h\) be the interpolation of \(\phi\). Since \(\mathcal{I}_h\phi-\phi_h\in V_h\), the inverse inequality is applicable. Moreover, by Assumption 2.1 (P2) and the standard interpolation estimate,<tbc>

\(\|\phi-\mathcal{I}_h\phi\|_{H^2(\Omega_h)}\le Ch^{k-1}\|\phi\|_{H^{k+1}(\widetilde{\Omega}_h)}\text{for}k\ge 2.\)

<tbc>Therefore,

\(\|\phi-\phi_h\|_{H^2(\Omega_h)}\le\|\phi-\mathcal{I}_h\phi\|_{H^2(\Omega_h)}+\|\mathcal{I}_h\phi-\phi_h\|_{H^2(\Omega_h)}\)<br>
\(\le h^{k-1}\|\phi\|_{H^{k+1}(\widetilde{\Omega}_h)}+h^{-1}\|\mathcal{I}_h\phi-\phi_h\|_{H^1(\Omega_h)}\)<br>
\(\le h^{k-1}\|\phi\|_{H^{k+1}(\widetilde{\Omega}_h)}+h^{-1}\big(\|\mathcal{I}_h\phi-\phi\|_{H^1(\Omega_h)}+\|\phi-\phi_h\|_{H^1(\Omega_h)}\big)\)<br>
\(\le Ch^{k-1},\) (3.15)

where _C_ depends on \(\|\phi\|_{H^{k+1}(\widetilde{\Omega}_h)}\). Substituting (3.15) into (3.14), we arrive at

\(\|T_1\|_{H^2(\Omega_h)}\le Ch^{k-1}\|v\|_{H^3(\widetilde{\Omega}_h)}.\) (3.16)

**Estimate for** _T_<sub>2</sub>**:** For \(T_2=\phi(z-z_h)\), we use the Leibniz rule to estimate the _H<sup>m</sup>_-norm for \(m\in\{1,2\}\) in a unified way. Since \(\phi\in C^{k+1}(\hat{\Omega})\), its derivatives are uniformly bounded, and hence<tbc>

\(\|\phi(z-z_h)\|_{H^m(T)}\le C\big(\|\phi\|_{L^\infty(T)}\|z-z_h\|_{H^m(T)}+\|z-z_h\|_{H^{m-1}(T)}\big).\) (3.17)

<tbc>The second term on the right-hand side can be handled directly. Indeed, by the standard local approximation property of the PHT-spline interpolation operator, we have<tbc>

\(\|z-z_h\|_{H^{m-1}(T)}\le Ch^{k-m+1}\|z\|_{H^k(\omega_T)}.\)

<tbc>Using the uniformly bounded overlap of the patches \(\omega_T\) and the Hardy-type inequality (3.12), we obtain

\(\sum_{T\in\mathcal{T}_h}\|z-z_h\|_{H^{m-1}(T)}^2\le Ch^{2(k-m+1)}\|z\|_{H^k(\widetilde{\Omega}_h)}^2\le Ch^{2(k-m+1)}\|v\|_{H^{k+1}(\widetilde{\Omega}_h)}^2.\) (3.18)

The first term, however, is more delicate. A direct application of the interpolation estimate would involve the quantity \(\|z\|_{H^{k+1}(\widetilde{\Omega}_h)}\), and using the Hardy-type inequality in a straightforward manner would then require higher regularity of _v_ than desired. To avoid this loss of derivatives, we proceed with a more refined argument. Following the approach in \[17, Lemma 6\] and \[24, Lemma 3.5\], we analyze (3.17) by decomposing the mesh T_<sub>h</sub>_ into two disjoint subsets according to the distance of each element from the interface \(\Gamma\). Here, \(\omega_T\) denotes the element patch associated with the local interpolation on _T_.

**Case 1: Interior domain** \(\{T\in\mathcal{T}_h:\text{dist}(\omega_T,\Gamma)\ge 3h\}\).

For any _T_ in this set, the level set function \(\phi\) does not vanish on the patch \(\omega_T\). Since \(\phi\) is Lipschitz continuous and satisfies \(\phi=0\) on \(\Gamma\), there exists a constant _c_<sub>0</sub>_\>_0 such that<tbc>

\(min_{x\in\omega_T}|\phi(x)|\ge c_0h.\)

<tbc>Moreover, the standard interpolation estimate on _T_ gives<tbc>

\(\|z-z_h\|_{H^l(T)}\le Ch^{k+1-l}|z|_{H^{k+1}(\omega_T)},l\le m.\)

<tbc>Applying \[17, (33)\] on the patch \(\omega_T\), we obtain<tbc>

\(|z|_{H^{k+1}(\omega_T)}\le\frac{C}{min_{\omega_T}|\phi|}\big(|v|_{H^{k+1}(\omega_T)}+\|z\|_{H^k(\omega_T)}\big).\)

<tbc>To control the prefactor involving \(\phi\), we note that

\(\frac{\|\phi\|_{L^\infty(T)}}{min_{\omega_T}|\phi|}=1+\frac{\|\phi\|_{L^\infty(T)}-min_{\omega_T}|\phi|}{min_{\omega_T}|\phi|}\le 1+\frac{Ch\|\nabla\phi\|_{L^\infty(T)}}{c_0h}\le\tilde{C},\)

