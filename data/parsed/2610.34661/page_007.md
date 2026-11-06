The truncated ionic charge density and its primitive are defined by

\(\rho_\tau(\xi):=-\beta\sum_{i=1}^nZ_i\bar{c}_iE_\tau(-Z_i\xi),P_\tau(\xi):=\int_0^\xi\rho_\tau(\eta)\mathrm{d}\eta,\xi\in\mathbb{R}.\) (20)

Let _Z_<sub>max</sub>:=max_<sub>i</sub>|Z<sub>i</sub>_|.

**Lemma 3.2.** _Let_ (3) _hold and_ \(\tau>0\)_. Then_ \(\rho_\tau\in C^2(\mathbb{R})\) _and the following hold._

(i) \(\rho_\tau(0)=0\) _and_ \(\rho'_\tau(\xi)=\beta\sum_{i=1}^nZ_i^2\bar{c}_iE'_\tau(-Z_i\xi)>0\) _for all_ \(\xi\in\mathbb{R}\)_; hence_ \(\rho_\tau\) _is strictly increasing,_ \(P_\tau\) _is convex and_ \(P_\tau\ge 0\).<tbc>

(ii) _There are constants C_<sub>0</sub>_,C_<sub>1</sub>_,C_<sub>2</sub>_\>_0 _depending only on_ \(\tau,\beta,Z_\mathrm{max}\) _and_ \(\bar{c}\) _such that for all_ \(\xi\in\mathbb{R}\),<tbc>

\(|\rho_\tau(\xi)|\le C_0(1+|\xi|)^2,0<\rho'_\tau(\xi)\le C_1(1+|\xi|),|\rho''_\tau(\xi)|\le C_2,0\le P_\tau(\xi)\le C_0(1+|\xi|)^3.\text{(21)}\)

(iii) \(\rho_\tau(\xi)=\rho(\xi)\), \(\rho'_\tau(\xi)=\rho'(\xi)\) _and_ \(\rho''_\tau(\xi)=\rho''(\xi)\) _whenever_ \(Z_\mathrm{max}|\xi|\le\tau\).<tbc>

<tbc>_Proof._ (i) By (3) and \(E_\tau(0)=1\), \(\rho_\tau(0)=-\beta\sum_iZ_i\bar{c}_i=0\). The formula for \(\rho'_\tau\) follows from the chain rule and \(\rho'_\tau>0\) from Lemma 3.1(i), since \(\bar{c}_i\ge 0\) and \(\bar{c}>0\). Convexity of \(P_\tau\) follows from \(P''_\tau=\rho'_\tau>0\), and \(P_\tau\ge 0\) from \(P_\tau(0)=0\), \(P'_\tau(0)=\rho_\tau(0)=0\) and convexity. (ii) The bounds on \(\rho_\tau\) and \(\rho'_\tau\) follow from (19) and \((1+|Z_i\xi|)\le(1+Z_\mathrm{max})(1+|\xi|)\); for instance<tbc>

\(C_0=\beta e^\tau Z_\mathrm{max}\bar{c}(1+Z_\mathrm{max})^2,C_1=\beta e^\tau Z_\mathrm{max}^2\bar{c}(1+Z_\mathrm{max})\)

<tbc>will do. Since

\(\rho''_\tau(\xi)=-\beta\sum_{i=1}^nZ_i^3\bar{c}_iE''_\tau(-Z_i\xi),\)

Lemma 3.1(i) gives \(|\rho''_\tau(\xi)|\le C_2:=\beta e^\tau Z_\mathrm{max}^3\bar{c}\). The bound on \(P_\tau\) follows by integrating the bound on \(\rho_\tau\). (iii) If \(Z_\mathrm{max}|\xi|\le\tau\) then \(-Z_i\xi\le\tau\) for all _i_, and Lemma 3.1(ii) applies.

_Remark_ 3.3. In the symmetric 1:1 case, \(\rho_\tau(\xi)=\kappa^2\mathrm{sinh}_\tau(\xi)\) and \(\rho'_\tau(\xi)=\kappa^2\mathrm{cosh}_\tau(\xi)\) with

\(\mathrm{sinh}_\tau(\xi):=\frac{1}{2}\big(E_\tau(\xi)-E_\tau(-\xi)\big),\mathrm{cosh}_\tau(\xi):=\frac{1}{2}\big(E'_\tau(\xi)+E'_\tau(-\xi)\big).\) (22)

They are _C_<sup>2</sup> counterparts of the modified hyperbolic functions \(\widetilde{\mathrm{sinh}}\) and \(\widetilde{\mathrm{cosh}}\) of \[34, Eq. (49)\], which are obtained by freezing sinh and cosh at the values \(\pm\mathrm{sinh}\tau\) and \(\mathrm{cosh}\tau\) for \(|\xi|\ge\tau\); those functions are continuous but not differentiable at \(\pm\tau\), and \(\widetilde{\mathrm{cosh}}\) is not the derivative of \(\widetilde{\mathrm{sinh}}\). The functions in (22) coincide with sinh and cosh for \(|\xi|\le\tau\), \(\mathrm{cosh}_\tau=\mathrm{sinh}'_\tau\), and \(\mathrm{sinh}_\tau\) is odd, increasing and of quadratic growth.

## 3.2 The truncated problem and its well-posedness

For \(\tau>0\) consider the truncated version of (15): find \(\Phi_\tau\in H_0^1(\Omega)\) such that<tbc>

\(a(\Phi_\tau,v)+\big(\rho_\tau(U+\Phi_\tau),v\big)_{D_s}=0\forall v\in H_0^1(\Omega).\) (23)

<tbc>By Assumption 2.1 and (21), for \(\Phi\in H_0^1(\Omega)\) we have \(|\rho_\tau(U+\Phi)|\le C_0(1+M_U+|\Phi|)^2\in L^3(D_s)\) because \(\Phi\in L^6(\Omega)\), so that the nonlinear term in (23) is well defined for every \(v\in H_0^1(\Omega)\subset L^{3/2}(\Omega)\). Let

\(J_\tau(v):=\frac{1}{2}a(v,v)+\int_{D_s}P_\tau(U+v)\mathrm{d}\mathbf{r},v\in H_0^1(\Omega),\) (24)

which is finite by (21) since \(H_0^1(\Omega)\subset L^3(\Omega)\).

