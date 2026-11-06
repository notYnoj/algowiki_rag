\(\le\|e_h\|_{H^1(\Omega_h)}+\|\phi-\phi_h\|_{H^1(\Omega_h)}\|w\|_{L^\infty(\Omega_h)}+\|\phi-\phi_h\|_{L^\infty(\Omega_h)}\|w\|_{H^1(\Omega_h)}\)<br>
\(\le\|e_h\|_{H^1(\Omega_h)}+Ch^{k-1/2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\) (3.44)

\(\|w_h-w\|_{H^1(\Omega_h)}\le C\|\phi_h(w_h-w)\|_{H^2(\Omega_h)}\)<br>
\(\le\|e_h\|_{H^2(\Omega_h)}+\|(\phi-\phi_h)w\|_{H^2(\Omega_h)}\)<br>
\(\le\|e_h\|_{H^2(\Omega_h)}+\|\phi-\phi_h\|_{H^2(\Omega_h)}\|w\|_{W^{1,\infty}(\Omega_h)}\)<br>
\(+\|\phi-\phi_h\|_{L^\infty(\Omega_h)}\|w\|_{H^2(\Omega_h)}\)<br>
\(\le\|e_h\|_{H^2(\Omega_h)}+Ch^{k-1}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\) (3.45)

where the last inequality uses the estimate from (3.15). Substituting these bounds back into the trace inequality (3.41) yields:

\(\|w_h-w\|_{L^2(\Gamma)}\le Ch^{-1/2}\big(\|e_h\|_{H^1(\Omega_h)}+Ch^{k-1/2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\big)\)<br>
\(+Ch^{1/2}\big(\|e_h\|_{H^2(\Omega_h)}+Ch^{k-1}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\big)\)<br>
\(\le C\big(h^{-1/2}\|e_h\|_{H^1(\Omega_h)}+h^{1/2}\|e_h\|_{H^2(\Omega_h)}+h^{k-1}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\big).\) (3.46)

Consequently, returning to the initial splitting of \(\|e_h\|_{L^2(\Gamma)}\) and expanding the terms with (3.46), we obtain:

\(\|e_h\|_{L^2(\Gamma)}\le\|\phi_h-\phi\|_{L^2(\Gamma)}\|w\|_{L^\infty(\Gamma)}+\|\phi_h-\phi\|_{L^\infty(\Gamma)}\|w_h-w\|_{L^2(\Gamma)}\)<br>
\(\le Ch^{k+1/2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\)<br>
\(+Ch^{k-1/2}\big(h^{-1/2}\|e_h\|_{H^1(\Omega_h)}+h^{1/2}\|e_h\|_{H^2(\Omega_h)}+h^{k-1}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\big)\)<br>
\(\le Ch^{k+1/2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}+Ch^k\|e_h\|_{H^2(\Omega_h)}+Ch^{k-1}\|e_h\|_{H^1(\Omega_h)}.\) (3.47)

For polynomial degree \(k\ge 2\), the explicitly known high-order term _h_<sup>2_k_-3/2</sup>∥_u_∥<sub>_H_<sup>_k_+1</sup></sub> is asymptotically dominated by the leading-order error \(h^{k+1/2}\|\tilde{u}\|_{H^{k+1}}\) (since \(2k-3/2\ge k+1/2\)) and can thus be absorbed. Furthermore, by invoking the previously established _H_<sup>2</sup>- error bound (3.36), the term involving the _H_<sup>2</sup>-error can be controlled as \(h^k\|e_h\|_{H^2(\Omega_h)}\le Ch^{2k-1}\|f\|_{H^{k-1}(\Omega_h)}\). Since \(2k-1\ge k+1/2\) for \(k\ge 2\), this term is also bounded by the leading-order term and subsequently absorbed. Finally, applying the standard elliptic regularity \(\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\le C\|f\|_{H^{k-1}(\Omega_h)}\), the remaining unabsorbed terms yield the fundamental boundary estimate:<tbc>

\(\|e_h\|_{L^2(\Gamma)}\le Ch^{k+1/2}\|f\|_{H^{k-1}(\Omega_h)}+Ch^{k-1}\|e_h\|_{H^1(\Omega_h)}.\) (3.48)

<tbc>By \[27, Lemma 3.1\], for any sufficiently smooth function \(\zeta\in H^1(\Omega_h\backslash\Omega)\),<tbc>

\(\|\zeta\|_{L^2(\Omega_h\backslash\Omega)}\le C\big(h^{1/2}\|\zeta\|_{L^2(\Gamma)}+h\|\nabla\zeta\|_{L^2(\Omega_h\backslash\Omega)}\big).\) (3.49)

<tbc>Applying (3.49) to \(\zeta=\Delta v\), we note that the dual problem (3.37) ensures \(-\Delta v=-e_h\) up to the continuous boundary \(\Gamma\), yielding the exact trace identity \(\Delta v=e_h\) on \(\Gamma\). Furthermore, the gradient of the Laplacian is controlled by the _H_<sup>3</sup>-regularity of the dual extension, such that \(\|\nabla(\Delta v)\|_{L^2(\Omega_h\backslash\Omega)}\le C\|v\|_{H^3(\widetilde{\Omega}_h)}\le C\|e_h\|_{H^1(\Omega_h)}\). Consequently, we obtain

\(\|\Delta v\|_{L^2(\Omega_h\backslash\Omega)}\le C\big(h^{1/2}\|\Delta v\|_{L^2(\Gamma)}+h\|\nabla(\Delta v)\|_{L^2(\Omega_h\backslash\Omega)}\big)\)<br>
\(\le Ch^{1/2}\|e_h\|_{L^2(\Gamma)}+Ch\|v\|_{H^3(\widetilde{\Omega}_h)}\)<br>
\(\le Ch^{k+1}\|f\|_{H^{k-1}(\Omega_h)}+Ch\|e_h\|_{H^1(\Omega_h)},\) (3.50)

where, assuming \(k\ge 2\), the higher-order term \(h^{k-1/2}\|e_h\|_{H^1(\Omega_h)}\) is asymptotically dominated and hence safely absorbed by the leading-order term \(h\|e_h\|_{H^1(\Omega_h)}\). Utilizing this estimate,

