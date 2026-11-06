<tbc>Testing the numerical error _e<sub>h</sub>_ against the Laplacian of the dual solution \(\Delta v\) over the physical domain \(\Omega\), and noting that \(\Delta v=e_h\) from (3.37), we deduce:

\(-\int_\Omega\Delta e_he_h=-\int_\Omega\Delta e_h\Delta v\)<br>
\(=-(\Delta e_h,\Delta v)_{L^2(\Omega_h)}+(\Delta e_h,\Delta v)_{L^2(\Omega_h\backslash\Omega)}\)<br>
\(=-(\Delta e_h,\Delta v_h)_{L^2(\Omega_h)}-(\Delta e_h,\Delta(v-v_h))_{L^2(\Omega_h)}+(\Delta e_h,\Delta v)_{L^2(\Omega_h\backslash\Omega)}\)<br>
\(=(r,\Delta v_h)_{L^2(\Omega_h)}-(\Delta e_h,\Delta(v-v_h))_{L^2(\Omega_h)}+(\Delta e_h,\Delta v)_{L^2(\Omega_h\backslash\Omega)}\)<br>
\(-\big(j_h(\widetilde{\mathcal{I}}_h\tilde{u},v_h)-j_h(\xi_h,v_h)\big),\)

where the last equality follows from the error equation (3.27), and \(v_h:=\widetilde{\mathcal{I}}_hv\in S_h\) denotes the modified interpolant defined in (3.8). By Corollary 2, it satisfies \(\|v-v_h\|_{H_h^3(\Omega_h)}\le C\|v\|_{H^3(\widetilde{\Omega}_h)}\). Hence, by the triangle inequality,

\(\|v_h\|_{H_h^3(\Omega_h)}\le C\|v\|_{H^3(\widetilde{\Omega}_h)}\le C\|e_h\|_{H^1(\Omega_h)},\) (3.39)

where the last inequality follows from (3.38).

Applying integration by parts to the left side \(-\int_\Omega\Delta e_he_h\), we obtain

\(\|\nabla e_h\|_{L^2(\Omega)}^2\le\underbrace{\big|(r,\Delta v_h)_{L^2(\Omega_h)}\big|}_I+\underbrace{\big|(\Delta e_h,\Delta v)_{L^2(\Omega_h\backslash\Omega)}\big|}_II\)<br>
\(+\underbrace{\big|(\Delta e_h,\Delta(v-v_h))_{L^2(\Omega_h)}\big|}_{III}+\underbrace{\big|j_h(\widetilde{\mathcal{I}}_h\tilde{u},v_h)\big|+\big|j_h(\xi_h,v_h)\big|}_IV+\big|\underbrace{\int_\Gamma e_h\partial_ne_h\big|}_V.\)

In what follows, we systematically estimate the terms _I_ through _V_ .

As a first step, we establish an upper bound for the error on the boundary, denoted by \(\|e_h\|_{L^2(\Gamma)}\). Note that the exact solution extension satisfies \(\tilde{u}=0\) precisely on the continuous boundary \(\Gamma\). Thus, the error on the interface simplifies to \(e_h=\tilde{u}-u_h=-u_h\). By introducing the auxiliary variables \(w=\tilde{u}/\phi\) and \(w_h=u_h/\phi_h\), we can rewrite the error on \(\Gamma\) as \(e_h=(\phi-\phi_h)w_h\). Splitting this expression yields:

\(\|e_h\|_{L^2(\Gamma)}=\|(\phi_h-\phi)\big[(w_h-w)+w\big]\|_{L^2(\Gamma)}\)<br>
\(\le\|\phi_h-\phi\|_{L^2(\Gamma)}\|w\|_{L^\infty(\Gamma)}+\|\phi_h-\phi\|_{L^\infty(\Gamma)}\|w_h-w\|_{L^2(\Gamma)}.\)

By virtue of the Hardy inequality and the Sobolev embedding theorem for dimension \(d\in\{2,3\}\), the \(L^\infty\)-norm of _w_ is uniformly bounded by the regularity of \(\tilde{u}\):

\(\|w\|_{L^\infty(\Omega_h)}\le C\|\tilde{u}\|_{W^{1,\infty}(\widetilde{\Omega}_h)}\le C\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}.\) (3.40)

Applying the scaled trace inequality, the \(L^2(\Gamma)\)-norms can be controlled by:

\(\|w_h-w\|_{L^2(\Gamma)}\le C\left(h^{-1/2}\|w_h-w\|_{L^2(\Omega_h)}+h^{1/2}\|w_h-w\|_{H^1(\Omega_h)}\right),\) (3.41)

\(\|\phi_h-\phi\|_{L^2(\Gamma)}\le C\left(h^{-1/2}\|\phi_h-\phi\|_{L^2(\Omega_h)}+h^{1/2}\|\phi_h-\phi\|_{H^1(\Omega_h)}\right)\le Ch^{k+1/2}.\) (3.42)

To estimate the geometric error in the \(L^\infty(\Gamma)\)-norm, combining the inverse inequality with standard Sobolev embeddings for \(d\le 3\) yields:

\(\|\phi_h-\phi\|_{L^\infty(\Gamma)}\le\|\phi_h-\mathcal{I}_h\phi\|_{L^\infty(\Omega_h)}+\|\phi-\mathcal{I}_h\phi\|_{L^\infty(\Omega_h)}\)<br>
\(\le Ch^{-1/2}\|\phi_h-\mathcal{I}_h\phi\|_{L^6(\Omega_h)}+Ch^{k-1/2}\)<br>
\(\le Ch^{-1/2}\|\phi_h-\mathcal{I}_h\phi\|_{H^1(\Omega_h)}+Ch^{k-1/2}\le Ch^{k-1/2}.\) (3.43)

Applying the Hardy inequality on \(\Omega_h\) to \(\phi_h(w_h-w)\) and substituting the identity \(\phi_h(w_h-w)=u_h-\phi_hw=-e_h+(\phi-\phi_h)w\), we deduce:

\(\|w_h-w\|_{L^2(\Omega_h)}\le C\|\phi_h(w_h-w)\|_{H^1(\Omega_h)},\)<br>
\(\le\|e_h\|_{H^1(\Omega_h)}+\|(\phi-\phi_h)w\|_{H^1(\Omega_h)}\)

