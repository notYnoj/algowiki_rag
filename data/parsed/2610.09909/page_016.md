<tbc>the term _II_ can be bounded as follows:

\(II\le\|e_h\|_{H^2(\Omega_h)}\big(Ch^{k+1}\|f\|_{H^{k-1}(\Omega_h)}+Ch\|e_h\|_{H^1(\Omega_h)}\big)\)<br>
\(\le Ch^{2k}\|f\|_{H^{k-1}(\Omega_h)}^2+Ch^k\|f\|_{H^{k-1}(\Omega_h)}\|e_h\|_{H^1(\Omega_h)}.\) (3.51)

For the first term _I_, we bound the _L_<sup>2</sup>-norm of \(\Delta v_h\) on the narrow band \(\Omega_h\backslash\Omega\) by applying the triangle inequality and the approximation property of the PHT-spline interpolation:

\(\|\Delta v_h\|_{L^2(\Omega_h\backslash\Omega)}\le\|\Delta v\|_{L^2(\Omega_h\backslash\Omega)}+\|\Delta(v_h-v)\|_{L^2(\Omega_h\backslash\Omega)}\)<br>
\(\le\|\Delta v\|_{L^2(\Omega_h\backslash\Omega)}+Ch\|v\|_{H^3(\widetilde{\Omega}_h)}\)<br>
\(\le Ch^{k+1}\|f\|_{H^{k-1}(\Omega_h)}+Ch\|e_h\|_{H^1(\Omega_h)}.\)

Noting that the residual _r_ vanishes identically in the physical domain \(\Omega\), a direct application of (3.24) alongside the Cauchy-Schwarz inequality yields the bound for _I_:

\(I=\big|(r,\Delta v_h)_{L^2(\Omega_h)}\big|\le\|r\|_{L^2(\Omega_h\backslash\Omega)}\|\Delta v_h\|_{L^2(\Omega_h\backslash\Omega)}\)<br>
\(\le Ch^{2k}\|f\|_{H^{k-1}(\Omega_h)}^2+Ch^k\|f\|_{H^{k-1}(\Omega_h)}\|e_h\|_{H^1(\Omega_h)}.\) (3.52)

By virtue of the interpolation estimate in Lemma 3.4 and the established _H_<sup>2</sup>-error bound (3.36), the third term _III_ is controlled as follows:

\(III=\big|(\Delta e_h,\Delta(v-v_h))_{L^2(\Omega_h)}\big|\)<br>
\(\le Ch\|v\|_{H^3(\widetilde{\Omega}_h)}\|e_h\|_{H^2(\Omega_h)}\le Ch^k\|f\|_{H^{k-1}(\Omega_h)}\|e_h\|_{H^1(\Omega_h)}.\) (3.53)

To estimate the fourth term _IV_, we decompose the jump penalty on the interface faces \(F\in\mathcal{F}_h^\Gamma\) into high-order (\(3\le j\le 2k\)) and low-order (_j_=2) contributions. For the high-order jumps, successive applications of the discrete scaled trace and inverse inequalities give:

\(\|\left[\left[\partial_n^jv_h\right]\right]\|_{L^2(F)}\le Ch^{-1/2}\|\partial_n^jv_h\|_{L^2(K)}\)<br>
\(\le Ch^{5/2-j}\|\partial_n^3v_h\|_{L^2(K)}\le Ch^{5/2-j}\|v_h\|_{H^3(K)}.\) (3.54)

Summing this estimate over all relevant faces for \(j\ge 3\), we deduce:

\(\sum_{j=3}^{2k}\sum_{F\in\mathcal{F}_h^\Gamma} h^{2j-3}\|\left[\left[\partial_n^jv_h\right]\right]\|_{L^2(F)}^2\le C\sum_{j=3}^{2k}\sum_{K\in\mathcal{T}_h^\Gamma} h^{2j-3}h^{5-2j}\|v_h\|_{H^3(K)}^2\le Ch^2\|v_h\|_{H_h^3(\Omega_h)}^2.\)

For the low-order jump _j_=2, the assumed regularity \(v\in H^3(\widetilde{\Omega}_h)\) ensures that the exact normal derivative is continuous across the faces, i.e., \(\left[\left[\partial_n^2v\right]\right]_F=0\). Applying the continuous scaled trace inequality to the error function \(\partial_n^2(v_h-v)\in H^1(K)\) in conjunction with the interpolation property (3.21), we obtain:

\(\sum_{F\in\mathcal{F}_h^\Gamma} h\|\left[\left[\partial_n^2v_h\right]\right]\|_{L^2(F)}^2=\sum_{F\in\mathcal{F}_h^\Gamma} h\|\left[\left[\partial_n^2(v_h-v)\right]\right]\|_{L^2(F)}^2\)<br>
\(\le C\sum_{K\in\mathcal{T}_h^\Gamma}\big(\|\partial_n^2(v_h-v)\|_{L^2(K)}^2+h^2\|\nabla\partial_n^2(v_h-v)\|_{L^2(K)}^2\big)\)<br>
\(\le Ch^2\|v\|_{H^3(\widetilde{\Omega}_h)}^2.\)

Combining these estimates for both low- and high-order jump contributions, we arrive at the unified bound for the stabilization penalty associated with the dual interpolant _v<sub>h</sub>_:

\(j_h(v_h,v_h)=\sum_{j=2}^{2k}\sum_{F\in\mathcal{F}_h^\Gamma} h_F^{2j-3}\|\left[\left[\partial_n^jv_h\right]\right]\|_{L^2(F)}^2\)<br>
\(\le Ch^2\|v\|_{H^3(\widetilde{\Omega}_h)}^2+Ch^2\|v_h\|_{H_h^3(\Omega_h)}^2\le Ch^2\|e_h\|_{H^1(\Omega_h)}^2.\) (3.55)

To bound the fourth term _IV_ , we apply the Cauchy-Schwarz inequality to the stabilization bilinear form. Invoking the jump penalty estimate \(j_h^{1/2}(\widetilde{\mathcal{I}}_h\tilde{u},\widetilde{\mathcal{I}}_h\tilde{u})\) from (3.33) alongside the

