<tbc>from _F(z_) at \(a_\alpha\) in (2). Finally, conditioned on _X<sub>u</sub>=x<sub>u</sub>_ and the site contexts, \(Pr\{min_{v\in F(z)\backslash\{u\}}d(x_u,X_v)<\varepsilon_\alpha\}\le f_zq_{x,+}\varepsilon_\alpha^{d_X}\); summing over all \(u\in V\) and _z_ (using \(\sum_zf_z=n\)) shows that the minimum separation \(\varepsilon_\alpha\) in (2) holds globally with probability at least \(1-\delta/3\).

## A.5 Proof of Coordinate-Quotient Connectivity (Theorem 3.7)

Proof of Theorem 3.7(b). We first show that the symmetric \(\rho_c\)- radius graph over the active sites \(\{Z_i\in\Omega_c\}\) is connected (and nonempty) except with probability at most \(\delta/6\):

\(\bullet\) _Case 1_ (\(\rho_c\ge diam(\Omega_c)\)): Every pair of active sites in \(\Omega_c\) lies at distance at most \(diam(\Omega_c)\le\rho_c\), so the \(\rho_c\)-radius graph on \(\{Z_i\in\Omega_c\}\) is a complete graph. Moreover, because \(M\pi_c\ge log(6/\delta)\), the probability that no site falls in \(\Omega_c\) is \((1-\pi_c)^M\le e^{-M\pi_c}\le\delta/6\).<tbc>

\(\bullet\) _Case 2_ (\(\rho_c<diam(\Omega_c)\)): By the interior-area regularity in Assumption A.3 (applied at scale \(t\le\rho_c/3<diam(\Omega_c)\)), we can tile the connected region \(\Omega_c\) into at most \(N_\text{cell}\le C_0\lambda_2(\Omega_c)/\rho_c^2\) connected cells of diameter at most \(\rho_c/3\) such that any two points in adjacent cells are within great-circle distance \(\rho_c\), and each cell \(\kappa\) has surface area at least \(c_0\rho_c^2\) (hence site mass at least \(c_0p_{s,-}\rho_c^2\)). Under _M_ independent draws from _p<sub>s</sub>_, a given cell \(\kappa\) is empty with probability at most \((1-c_0p_{s,-}\rho_c^2)^M\le exp(-Mc_0p_{s,-}\rho_c^2)\). Because \(\pi_c\le p_{s,+}\lambda_2(\Omega_c)\), substituting \(\rho_c\) from (2) with \(C_s^2\ge max\{\frac{2p_{s,+}}{c_0p_{s,-}},\frac{2C_0}{3}\}\) and taking a union bound over all _N_cell cells ensures that every cell contains at least one site with failure probability at most \(N_\text{cell}(\delta/(3M))^2\le\delta/6\). When every cell is occupied, the symmetric \(\rho_c\)-radius graph over \(\{Z_i\in\Omega_c\}\) is connected [30, 31].

Next, for any fixed site \(z\in\Omega_c\), the spherical ball \(\mathcal{B}(z,\rho_c)\cap\mathcal{S}\) has surface area at most \(c_1\rho_c^2\), and hence _p<sub>s</sub>_-mass at most \(c_1p_{s,+}\rho_c^2\). Since \(\pi_c\ge p_{s,-}\lambda_2(\Omega_c)\), the expected number of other sites within distance \(\rho_c\) of _z_ is at most \(\mu_s=(M-1)c_1p_{s,+}\rho_c^2\le\frac{c_1p_{s,+}C_s^2}{p_{s,-}}log(3M/\delta)\). Ap plying the multiplicative Chernoff bound and a union bound over all _M_ sites shows that, for \(C_h\ge max\{e^2c_1(p_{s,+}/p_{s,-})C_s^2,2\}\), every site has at most \(h_c=\lceil C_hlog(3M/\delta)\rceil\) other sites within distance \(\rho_c\) except with probability at most \(Me^{-(h_c+1)}\le\delta/6\).

Combining the \(\alpha\)-charge event (failure probability \(\le\delta/3\)), the cell-occupancy event (\(\le\delta/6\)), and the site-crowding event (\(\le\delta/6\)) gives an intersection event of probability at least \(1-2\delta/3\). On this intersection, every active vertex \(u\in\mathcal{A}(c)\) encounters at most _h<sub>c</sub>_ other coordinates within distance \(\rho_c\) and retains at most \(a_\alpha\) edges from each of them (and from its own fiber), so \(L_u(\rho_c)\le a_\alpha(h_c+1)\le B_g\). Therefore, _u_’s nearest-first geographic stream reaches every active coordinate within distance \(\rho_c\) and retains at least one representative from each before exhausting _B<sub>g</sub>_, proving Part (b). Because this holds in both directions for every \(\rho_c\)-close pair of active coordinates, the coordinate quotient contains the connected symmetric \(\rho_c\)-radius site graph and is therefore strongly connected, proving Part (a). \(\square\)

## A.6 Explicit Finite-Sample Connectivity Bound

Theorem 3.7 sets the annulus scale \(\varepsilon_\alpha\), the site linking radius \(\rho_c\), and the crowding bound _h<sub>c</sub>_ to their asymptotic logarithmic forms. Leaving these three scales as free parameters yields a non-asymptotic finite-sample failure bound in terms of the problem parameters.

Let _C_<sub>0</sub>_,c_<sub>0</sub>_,c_<sub>1</sub>_\>_0 be the spherical domain constants defined in Appendix A.5. For any \(0<\varepsilon\le min\{r_x,D_x/2\}\), \(0<\rho\le diam(\Omega_c)\), and integer \(h_\rho\ge 0\), define

\(a(\varepsilon)=min\big\{K_f,P_\alpha\left(1+\left\lceil log_2(D_x/\varepsilon)\right\rceil\right)\big\},\)<br>
\(\mu_s(\rho)=(M-1)c_1p_{s,+}\rho^2,\)

and the four-term failure sum

\(\Pi(c)=n^2q_{x,+}\varepsilon^{d_X}+C_0\frac{\lambda_2(\Omega_c)}{\rho^2}exp\big(-Mc_0p_{s,-}\rho^2\big)\)<br>
\(+M\left(\frac{e\mu_s(\rho)}{h_\rho+1}\right)^{h_\rho+1}+\sum_{i=1}^M\delta_{\text{fib},i},\) (6)

where \(\delta_{\text{fib},i}\) is given by (5) at scale _r<sub>i</sub>_ for non-singleton fibers and \(\delta_{\text{fib},i}=0\) for singleton fibers (_f<sub>i</sub>_=1). The four terms in (6) correspond one-to-one to the four failure modes: (1) violation of the per-coordinate charge bound \(a(\varepsilon)\), (2) an empty cell in the geographic \(\rho\)-tiling of \(\Omega_c\), (3) more than \(h_\rho\) sites within radius \(\rho\) of some site, and (4) loss of internal connectivity in some multi-object fiber.

Theorem A.5 (Explicit Finite-Sample Connectivity Bound). _Conditioned on any multiplicity vector_ (_f_<sub>1</sub>_,...,f<sub>M</sub>), suppose that_ \(0<\rho\le diam(\Omega_c)\), \(3r_i\le r_x\) _for all i_, \(h_\rho+1\ge\mu_s(\rho)\)_, and the quotas satisfy_

\(B_g\ge a(\varepsilon)(h_\rho+1),K_f+1\ge max_{1\le i\le M}\big\{(f_i-1)q_{x,+}(3r_i)^{d_X}\big\}.\)

_Then the complete active projection is strongly connected with probability at least_

\(Pr\big\{G[\mathcal{A}(c)]\text{\textit{is strongly connected}}\big\}\ge 1-\Pi(c).\)

Proof. By the derivations in Appendices A.4 and A.5, the four bad events fail with probabilities bounded by the four respective summands of \(\Pi(c)\) in (6). On the complement of their union, every coordinate charges at most \(a(\varepsilon)\) edges, every site has at most \(h_\rho\) neighbors within distance \(\rho\), the \(\rho\)-radius graph on active sites is connected, and every active fiber is internally strongly connected. Because \(B_g\ge a(\varepsilon)(h_\rho+1)\), both conditions of Theorem 3.5 hold, and the union bound yields \(1-\Pi(c)\). Substituting \(\varepsilon=\varepsilon_\alpha\), \(\rho=\rho_c\), and \(h_\rho=h_c\) recovers Theorem 3.7. \(\square\)

## A.7 Route Diameter on Broader Disks

When a query disk is broader than a single geographic budget radius (\(diam(\Omega_c)>\rho_c\)), the active projection _G_[A(_c_)] still possesses a bounded directed diameter: a path can first walk across the geographic site backbone in \(O(\Delta(s_u,s_v)/\rho_c)\) hops to reach the target’s fiber _F(s<sub>v</sub>_), and then contract in vector space inside _F(s<sub>v</sub>_) in at most \(1+\lceil log_\alpha(D_x/\varepsilon_\alpha)\rceil\) hops.

Proposition A.6 (Two-Phase Route Length Bound). _On the intersection event of Theorem 3.7 (with_ \(K_f\ge|F(s_v)|-1\)_), for every pair of active vertices_ \(u,v\in\mathcal{A}(c)\) _separated by geodesic distance D within_ \(\Omega_c\)_, the active projection G_[A(_c_)] _contains a directed path_

