<tbc>energy norm bound for \(\xi_h\) from (3.34), we deduce:<tbc>

\(IV\le\big(j_h^{1/2}(\widetilde{\mathcal{I}}_h\tilde{u},\widetilde{\mathcal{I}}_h\tilde{u})+j_h^{1/2}(\xi_h,\xi_h)\big)j_h^{1/2}(v_h,v_h)\le Ch^k\|f\|_{H^{k-1}(\Omega_h)}\|e_h\|_{H^1(\Omega_h)}.\) (3.56)

<tbc>For the boundary integral term _V_ , an application of the Cauchy-Schwarz inequality on the interface \(\Gamma\) yields:<tbc>

\(V=\big|\int_\Gamma e_h\partial_ne_hds\big|\le\|e_h\|_{L^2(\Gamma)}\|\partial_ne_h\|_{L^2(\Gamma)}.\) (3.57)

<tbc>The boundary trace of the normal derivative is bounded by combining the standard scaled trace inequality with the prior _H_<sup>2</sup>-error estimate (3.36):

\(\|\partial_ne_h\|_{L^2(\Gamma)}\le Ch^{-1/2}\|e_h\|_{H^1(\Omega_h)}+Ch^{1/2}\|e_h\|_{H^2(\Omega_h)}\)<br>
\(\le Ch^{-1/2}\|e_h\|_{H^1(\Omega_h)}+Ch^{k-1/2}\|f\|_{H^{k-1}(\Omega_h)}.\) (3.58)

Substituting the previously derived bound for \(\|e_h\|_{L^2(\Gamma)}\) from (3.48) and the normal derivative estimate (3.58) into (3.57), we obtain:

\(V\le\big(Ch^{k+1/2}\|f\|_{H^{k-1}(\Omega_h)}+Ch^{k-1}\|e_h\|_{H^1(\Omega_h)}\big)\)<br>
\(\times\big(Ch^{-1/2}\|e_h\|_{H^1(\Omega_h)}+Ch^{k-1/2}\|f\|_{H^{k-1}(\Omega_h)}\big)\)<br>
\(\le Ch^k\|f\|_{H^{k-1}(\Omega_h)}\|e_h\|_{H^1(\Omega_h)}+Ch^{2k}\|f\|_{H^{k-1}(\Omega_h)}^2+Ch^{k-3/2}\|e_h\|_{H^1(\Omega_h)}^2.\) (3.59)

Finally, collecting the individual estimates (3.51), (3.52), (3.53), (3.56), and (3.59), we arrive at the following comprehensive bound for the gradient error over the physical domain \(\Omega\):

\(\|\nabla e_h\|_{L^2(\Omega)}^2\le I+II+III+IV+V\)<br>
\(\lesssim h^k\|f\|_{H^{k-1}(\Omega_h)}\|e_h\|_{H^1(\Omega_h)}+h^{2k}\|f\|_{H^{k-1}(\Omega_h)}^2+h^{k-3/2}\|e_h\|_{H^1(\Omega_h)}^2.\) (3.60)

To extend the optimal _H_<sup>1</sup>-estimate to the entire computational domain \(\Omega_h\), we leverage the discrete extension property of the ghost penalty operator \[6\] in conjunction with a generalized Poincaré-Friedrichs inequality on the physical domain \(\Omega\). We then substitute the gradient bound (3.60), the ghost penalty energy estimate (3.34), and the interfacial _L_<sup>2</sup>-norm estimate (3.48). By further bounding the interpolation trace error via the standard continuous trace inequality \(\|\rho\|_{L^2(\Gamma)}\le C\|\rho\|_{H^1(\Omega)}\le Ch^k\|f\|_{H^{k-1}(\Omega_h)}\), we uniformly estimate the discrete component \(\xi_h\in S_h\) using the triangle inequality and Corollary 1 to obtain:

\(\|\xi_h\|_{H^1(\Omega_h)}^2\le C\big(\|\nabla\xi_h\|_{L^2(\Omega)}^2+\|\xi_h\|_{L^2(\Gamma)}^2+h^2j_h(\xi_h,\xi_h)\big)\)<br>
\(\le C\big(\|\nabla e_h\|_{L^2(\Omega)}^2+\|e_h\|_{L^2(\Gamma)}^2+h^2\big|\big|\big|\xi_h\big|\big|^2+\|\rho\|_{H^1(\Omega_h)}^2+\|\rho\|_{L^2(\Gamma)}^2\big)\)<br>
\(\le C\big(h^k\|e_h\|_{H^1(\Omega_h)}\|f\|_{H^{k-1}(\Omega_h)}+h^{2k}\|f\|_{H^{k-1}(\Omega_h)}^2+h^{k-3/2}\|e_h\|_{H^1(\Omega_h)}^2\big),\)

where the sub-optimal error term \(h^{2k-2}\|e_h\|_{H^1(\Omega_h)}^2\) is asymptotically dominated and thus safely absorbed by the leading-order component \(h^{k-3/2}\|e_h\|_{H^1(\Omega_h)}^2\) for any polynomial degree \(k\ge 2\). Applying Young’s inequality with an arbitrarily small parameter \(\varepsilon>0\) to decouple the cross term, and subsequently reverting to the total error \(e_h=\xi_h+\rho\), we deduce:

\(\|e_h\|_{H^1(\Omega_h)}^2\le 2\|\xi_h\|_{H^1(\Omega_h)}^2+2\|\rho\|_{H^1(\Omega_h)}^2\)<br>
\(\le C_1\varepsilon^{-1}h^{2k}\|f\|_{H^{k-1}(\Omega_h)}^2+C_2(\varepsilon+h^{k-3/2})\|e_h\|_{H^1(\Omega_h)}^2.\)

Because the polynomial degree \(k\ge 2\) guarantees a strictly positive exponent _k_-3/2, we can select a sufficiently small \(\varepsilon\) and assume an adequately refined mesh size _h_ to ensure that \(C_2(\varepsilon+h^{k-3/2})<1\). This permits the rigorous absorption of the remaining _H_<sup>1</sup>-error terms into the left-hand side, thereby completing the proof of the optimal global estimate \(\|e_h\|_{H^1(\Omega_h)}\le Ch^k\|f\|_{H^{k-1}(\Omega_h)}\). □

