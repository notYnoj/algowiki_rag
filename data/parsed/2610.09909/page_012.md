<tbc>error estimate in the energy norm; next, we derive the _H_<sup>2</sup>-error estimate; and finally, we recover the optimal _H_<sup>1</sup>-error bound via a duality argument.

_Proof._ Recall that \(\tilde{u}\) is an extension of _u_ satisfying \(\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\le C\|u\|_{H^{k+1}(\Omega)}\) and \(\Omega\subset\Omega_h\). Combining this extension estimate with the elliptic regularity for the source problem \(-\Delta u=f\) in \(\Omega\), we obtain the following bound:<tbc>

\(\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}\le C\|u\|_{H^{k+1}(\Omega)}\le C\|f\|_{H^{k-1}(\Omega)}\le C\|f\|_{H^{k-1}(\Omega_h)}.\) (3.23)

<tbc>We define the residual \(r:=-\Delta\tilde{u}-f\) in the extended domain \(\Omega_h\). Since \(\tilde{u}=u\) in \(\Omega\), it follows that the residual vanishes identically in \(\Omega\). Furthermore, because \(\tilde{u}\in H^{k+1}(\Omega_h)\) and \(f\in H^{k-1}(\Omega_h)\), we have \(r\in H^{k-1}(\Omega_h)\). Therefore, by applying Lemma 3.1 to the residual _r_ and invoking the estimate (3.23), we obtain

\(\|r\|_{L^2(\Omega_h)}=\|r\|_{L^2(\Omega_h\backslash\Omega)}\le Ch^{k-1}\|r\|_{H^{k-1}(\Omega_h\backslash\Omega)}\)<br>
\(\le Ch^{k-1}\big(\|\Delta\tilde{u}\|_{H^{k-1}(\Omega_h\backslash\Omega)}+\|f\|_{H^{k-1}(\Omega_h\backslash\Omega)}\big)\)<br>
\(\le Ch^{k-1}\big(\|\tilde{u}\|_{H^{k+1}(\Omega_h)}+\|f\|_{H^{k-1}(\Omega_h)}\big)\)<br>
\(\le Ch^{k-1}\|f\|_{H^{k-1}(\Omega_h)}.\) (3.24)

Let \(\widetilde{\mathcal{I}}_h\tilde{u}\in S_h\) be the spline interpolant defined in Lemma 3.4. We decompose the finite element error \(e_h:=\tilde{u}-u_h\) into the interpolation error \(\rho:=\tilde{u}-\widetilde{\mathcal{I}}_h\tilde{u}\) and the discrete error \(\xi_h=\widetilde{\mathcal{I}}_h\tilde{u}-u_h\in S_h\):<tbc>

\(e_h=(\tilde{u}-\widetilde{\mathcal{I}}_h\tilde{u})+(\widetilde{\mathcal{I}}_h\tilde{u}-u_h)=\rho+\xi_h.\) (3.25)

<tbc>We now derive the error equation for the discrete component \(\xi_h\). From the definition of the bilinear form \(a_h(\cdot,\cdot)\) and the discrete scheme (1.3), for any test function \(v_h\in S_h\), we have:<tbc>

\(a_h(\xi_h,v_h)=a_h(\widetilde{\mathcal{I}}_h\tilde{u},v_h)-a_h(u_h,v_h)\)<br>
\(=(\Delta\widetilde{\mathcal{I}}_h\tilde{u},\Delta v_h)_{L^2(\Omega_h)}+j_h(\widetilde{\mathcal{I}}_h\tilde{u},v_h)+(f,\Delta v_h)_{L^2(\Omega_h)}.\) (3.26)

<tbc>Recall the continuous identity \(-\Delta\tilde{u}=f+r\) in the extended domain \(\Omega_h\), which yields \(f=-\Delta\tilde{u}-r\). Substituting this relation into (3.26), we obtain<tbc>

\(a_h(\xi_h,v_h)=(\Delta\widetilde{\mathcal{I}}_h\tilde{u}-\Delta\tilde{u},\Delta v_h)_{L^2(\Omega_h)}-(r,\Delta v_h)_{L^2(\Omega_h)}+j_h(\widetilde{\mathcal{I}}_h\tilde{u},v_h)\)<br>
\(=-(\Delta\rho,\Delta v_h)_{L^2(\Omega_h)}-(r,\Delta v_h)_{L^2(\Omega_h)}+j_h(\widetilde{\mathcal{I}}_h\tilde{u},v_h).\) (3.27)

<tbc>Choosing \(v_h=\xi_h\in S_h\) in (3.27), we have<tbc>

\(\big\|\xi_h\big\|^2=-(\Delta\rho,\Delta\xi_h)_{L^2(\Omega_h)}-(r,\Delta\xi_h)_{L^2(\Omega_h)}+j_h(\widetilde{\mathcal{I}}_h\tilde{u},\xi_h).\) (3.28)

<tbc>We bound the three terms on the right-hand side using the Cauchy-Schwarz inequality and the definition of the energy norm:<tbc>

\(|(\Delta\rho,\Delta\xi_h)_{L^2(\Omega_h)}|\le\|\Delta\rho\|_{L^2(\Omega_h)}\|\Delta\xi_h\|_{L^2(\Omega_h)}\le\|\Delta\rho\|_{L^2(\Omega_h)}\big\|\big\|\xi_h\big\|,\)<br>
\(|(r,\Delta\xi_h)_{L^2(\Omega_h)}|\le\|r\|_{L^2(\Omega_h)}\|\Delta\xi_h\|_{L^2(\Omega_h)}\le\|r\|_{L^2(\Omega_h)}\big\|\big\|\xi_h\big\|,\)<br>
\(|j_h(\widetilde{\mathcal{I}}_h\tilde{u},\xi_h)|\le j_h^{1/2}(\widetilde{\mathcal{I}}_h\tilde{u},\widetilde{\mathcal{I}}_h\tilde{u})j_h^{1/2}(\xi_h,\xi_h)\le j_h^{1/2}(\widetilde{\mathcal{I}}_h\tilde{u},\widetilde{\mathcal{I}}_h\tilde{u})\big\|\big\|\xi_h\big\|.\)

<tbc>Substituting these bounds into (3.28) and dividing both sides by \(\big\|\big\|\xi_h\big\|\), we obtain the stability estimate for the discrete component:<tbc>

\(\big\|\big\|\xi_h\big\|\big\|\le\|\Delta\rho\|_{L^2(\Omega_h)}+\|r\|_{L^2(\Omega_h)}+j_h^{1/2}(\widetilde{\mathcal{I}}_h\tilde{u},\widetilde{\mathcal{I}}_h\tilde{u}).\) (3.29)

<tbc>To bound the right-hand side of (3.29), we estimate each term separately. First, by the standard approximation properties of the spline interpolant given in Lemma 3.4, the Laplacian of the interpolation error is bounded by

\(\|\Delta\rho\|_{L^2(\Omega_h)}^2\le C\|\rho\|_{H^2(\Omega_h)}^2\le Ch^{2k-2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}^2,\) (3.30)

and the residual term is known to satisfy the estimate \(\|r\|_{L^2(\Omega_h)}^2\le Ch^{2k-2}\|\tilde{u}\|_{H^{k+1}(\widetilde{\Omega}_h)}^2\).

