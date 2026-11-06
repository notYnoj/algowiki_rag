<tbc>where we have used the Lipschitz continuity of \(\phi\). Therefore, combining the above estimates, we arrive at

\(\|\phi\|_{L^\infty(T)}\|z-z_h\|_{H^m(T)}\le Ch^{k+1-m}\|\phi\|_{L^\infty(T)}\|z\|_{H^{k+1}(\omega_T)}\)<br>
\(\le Ch^{k+1-m}\big(\|v\|_{H^{k+1}(\omega_T)}+\|z\|_{H^k(\omega_T)}\big).\) (3.19)

**Case 2: Strip domain** \(\{T\in\mathcal{T}_h:\mathrm{dist}(\omega_T,\Gamma)<3h\}\).<br>
For any _T_ in this set, the patch \(\omega_T\) lies within a strip of width O(_h_) around the interface \(\Gamma\). Since \(\phi=0\) on \(\Gamma\) and \(\|\nabla\phi\|_{L^\infty(\widehat{\Omega})}\) is bounded, it follows that \(\|\phi\|_{L^\infty(T)}\lesssim h\). This provides an additional factor of _h_, and therefore the standard approximation estimate for the PHT-spline interpolation is sufficient to control the term \(\|\phi\|_{L^\infty(T)}\|z-z_h\|_{H^m(T)}\) using only \(\|z\|_{H^k(\omega_T)}\). Consequently,

\(\|\phi\|_{L^\infty(T)}\|z-z_h\|_{H^m(T)}\le Ch\cdot h^{k-m}\|z\|_{H^k(\omega_T)}.\) (3.20)

By summing the estimates (3.18)-(3.20) over all elements \(T\in\mathcal{T}_h\), for \(m\in\{1,2\}\), and then applying the Hardy-type inequality to \(z=v/\phi\) on \(\widetilde{\Omega}_h\), we obtain the optimal estimates

\(\|T_2\|_{H^1(\Omega_h)}\le Ch^k\|v\|_{H^{k+1}(\widetilde{\Omega}_h)},\|T_2\|_{H^2(\Omega_h)}\le Ch^{k-1}\|v\|_{H^{k+1}(\widetilde{\Omega}_h)}.\)

Finally, combining the above bounds for _T_<sub>2</sub> with those already derived for _T_<sub>1</sub>, we conclude the proof of (3.9). □

By arguing as in the proof of Lemma 3.4, using the local approximation property of the PHT-spline interpolation operator on each element and standard inverse inequalities, one obtains the corresponding interpolation estimates. Passing from these element-wise estimates to the global bound in the broken Sobolev norm is then justified by the uniformly bounded overlap of the patch family \(\{\omega_T\}_{T\in\mathcal{T}_h}\) and the Hardy-type inequality. Therefore, the following corollary is immediate, and its proof is omitted.

**Corollary 2.** Let \(3\le r\le k+1\) be an integer and assume that \(v\in H^{k+1}(\widetilde{\Omega}_h)\) with \(v|_\Omega\in H_0^1(\Omega)\). Under the geometric and mesh assumptions of Lemma 3.4, for \(1\le j\le\mathrm{min}\{k,r\}\),<tbc>

\(\|v-\widetilde{\mathcal{I}}_hv\|_{H_h^j(\Omega_h)}\le Ch^{r-j}\|v\|_{H^r(\widetilde{\Omega}_h)},\) (3.21)

<tbc>where the broken Sobolev norm is defined by

\(\|w\|_{H_h^j(\Omega_h)}^2:=\sum_{T\in\mathcal{T}_h}\|w\|_{H^j(T)}^2.\) (3.22)

## 3.2. Stability and well-posedness.

We now establish the well-posedness of the discrete scheme (1.3). To this end, we introduce the bilinear form \(a_h(\cdot,\cdot)\) and the linear functional \(L_h(\cdot)\) on _S<sub>h</sub>_ by<tbc>

\(a_h(u_h,v_h):=(\Delta u_h,\Delta v_h)_{L^2(\Omega_h)}+j_h(u_h,v_h),L_h(v_h):=-(f,\Delta v_h)_{L^2(\Omega_h)}.\)

<tbc>By (3.3), the bilinear form \(a_h(\cdot,\cdot)\) is symmetric and positive definite on _S<sub>h</sub>_. It therefore defines an inner product on _S<sub>h</sub>_, with the induced energy norm given by<tbc>

\(\big\|\big\|v_h\big\|^2:=a_h(v_h,v_h)=\|\Delta v_h\|_{L^2(\Omega_h)}^2+j_h(v_h,v_h).\)

<tbc>Since _S<sub>h</sub>_ is finite-dimensional, it follows that (_S<sub>h</sub>_, \(\big\|\cdot\big\|\)) is a Hilbert space. On the other hand, when extended to the larger space \(H^2(\Omega_h)\), the quantity \(\big\|\cdot\big\|\) is in general only a semi-norm. Moreover, the linear functional \(L_h(\cdot)\) is continuous on _S<sub>h</sub>_, since, by the Cauchy-Schwarz inequality,

\(|L_h(v_h)|\le\|f\|_{L^2(\Omega_h)}\|\Delta v_h\|_{L^2(\Omega_h)}\le\|f\|_{L^2(\Omega_h)}\big\|\big\|v_h\big\|.\)

Therefore, by the Riesz representation theorem, the variational problem (1.3) admits a unique solution \(u_h\in S_h\).

## 3.3. _H_<sup>1</sup>-error estimate.

Before presenting the detailed proof of Theorem 2.4, we briefly outline the main strategy. The proof proceeds in three main steps: first, we establish an

