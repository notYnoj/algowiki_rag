<tbc>**Algorithm 3.1** NLF fixed-load solve

Require: load \(\alpha\); initial guess \(\phi\); inner-solver state H (Cholesky factor or hierarchy, shared across calls); relative residual tolerance tol (default 10<sup>-9</sup>); forcing parameter \(\eta\) (default 0.05)<br>
\(r\leftarrow\alpha d-B\rho(B^\top\phi)\)<br>
while \(\|r\|>\mathrm{tol}\cdot\alpha\|d\|\) do<br>
   refresh check: if H is empty, or the previous pass reduced \(\|r\|\) by a factor worse than 0.25, or the line search stalled on a stale H, rebuild \(H\leftarrow\) inner setup of \(J(\phi)=B\mathrm{diag}(\rho'(B^\top\phi))B^\top\)<br>
   \(\delta\leftarrow\) approximate solution of the frozen correction equation \(J_H\delta=r\), where \(J_H=B\mathrm{diag}(\rho'(B^\top\phi_\mathrm{build}))B^\top\) is the linearization H was built from: inner solve(s) with H starting from \(\delta=0\), stopped when \(\|r-J_H\delta\|\le\eta\|r\|\)<br>
   line search: for \(\tau=1,\frac{1}{2},\frac{1}{4},\dots,\frac{1}{2^{49}}\) find the first \(\tau\) with \(\left\|\alpha d-B\rho\big(B^\top(\phi+\tau\delta)\big)\right\|\le\|r\|\)<br>
   if line search succeeded then \(\phi\leftarrow\phi+\tau\delta\)<br>
   else if H was stale (built before this iteration) then rebuild H from current<br>
\(J(\phi)\); recompute \(\delta\leftarrow\) inner solve of \(J_H\delta=r\) from \(\delta=0\); repeat line search<br>
   if retry succeeded then \(\phi\leftarrow\phi+\tau\delta\)<br>
   else break \(\triangleright\) fresh-H stall: no improving direction exists; exit<br>
   end if<br>
   else break \(\triangleright\) fresh H already in use; exit<br>
   end if<br>
\(r\leftarrow\alpha d-B\rho(B^\top\phi)\)<br>
end while<br>
return \(\phi\)

<tbc>engages on 11 of 2,003 graphs (0.5%) and restores textbook convergence.

**3.3. Continuation.** Only the saturating/fold class needs continuation. Here \(\alpha\) is the unknown maximizer. A fixed-\(\alpha\) solve is feasible iff \(\alpha<F^*\) (the min-cut value), and as \(\alpha\uparrow F^*\) the solution curve _folds_--\(\alpha(V)\) flattens onto the asymptote _F_<sup>∗</sup> while the potentials grow without bound (Fig. 3.1); at the fold \(\kappa(J)\sim(F^*-\alpha)^{-1}\) and the source-sink gap is \(V=|\phi_s-\phi_t|\sim-\mathrm{log}(F^*-\alpha)\), so \(dV/d\alpha\sim(F^*-\alpha)^{-1}\rightarrow\infty\). Thus \(\alpha\) is a bad continuation parameter: the feasible loads crowd at the fold and the step is forced to zero. The well-conditioned variable is the _cut-mode amplitude_ \(\psi=\chi^\top\phi\sim-\mathrm{log}(F^*-\alpha)\),2 \(\chi\) the (a priori unknown) min-cut indicator. We realize this by pseudo-arclength continuation \[27, 28\] (Algorithm 3.2), which never forms \(\chi\).

The equilibria of (1.1) trace a smooth curve \(\big(\phi(s),\alpha(s)\big)\) as the load is varied; we parametrize it by its own arclength _s_ and write a dot for the derivative along the curve,

2Justification of both asymptotics. Near the fold \(\phi=V\chi+O(1)\), \(\chi\) the source-side indicator, so every cut edge carries gradient _g<sub>e</sub>=V+O_(1). The saturating tail of (2.5) is \(\rho_e(g)=c_e\mathrm{tanh}(g/c_e)=c_e-2c_ee^{-2g/c_e}+O(e^{-4g/c_e})\), and all _s-t_ flow crosses the cut, so \(\alpha=\sum_{e\in\mathrm{cut}}\rho_e(g_e)=F^*-2\sum_{e\in\mathrm{cut}}c_ee^{-2V/c_e}(1+o(1))\). Hence \(F^*-\alpha\unknown e^{-2V/\bar{c}}\), \(\bar{c}\) the largest cut capacity, i.e. \(V=\frac{\bar{c}}{2}\mathrm{log}\frac{1}{F^*-\alpha}+O(1)\) and \(\psi=\chi^\top\phi\propto V\) . The same expansion gives the cut conduc tances \(\rho'_e(g_e)=\mathrm{sech}^2(g_e/c_e)=4e^{-2V/c_e}(1+o(1))\), whence \(\lambda_\mathrm{min}(J)\le\sum_\mathrm{cut}\rho'_e\propto F^*-\alpha\) (here and below \(\lambda_\mathrm{min}\) is the smallest _nonzero_ eigenvalue--_J_ being a graph Laplacian, its zero eigenvalue with constant eigenvector **1** is excluded, and \(\kappa(J)\) is correspondingly the ratio over the nonzero spectrum; the bound is the Rayleigh quotient at \(\chi\), which loads only the cut edges); for a _simple_ fold the next eigenvalue stays \(\Theta(1)\) (the deflated spectral gap) and \(\lambda_\mathrm{max}(J)=\Theta(1)\), so the bound is two-sided and \(\kappa(J)\sim(F^*-\alpha)^{-1}\).

