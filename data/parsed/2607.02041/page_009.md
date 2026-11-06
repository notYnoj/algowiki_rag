<tbc>\(\dot{\cdot})\equiv d(\cdot)/ds\), so the tangent \((\dot{\phi},\dot{\alpha})\) is a unit vector, \(\|\dot{\phi}\|^2+\dot{\alpha}^2=1\). Differentiating (1.1) along _s_ gives:

(3.1) \(J\dot{\phi}=\dot{\alpha}d\Longrightarrow\dot{\phi}=J^+d,\dot{\alpha}=1,\text{then rescale to}\|(\dot{\phi},\dot{\alpha})\|=1.\)

As \(\alpha\rightarrow F^*\), \(J^+d\propto\chi/\lambda_\mathrm{min}\) (the pseudoinverse _J_<sup>+</sup> acts on \(\mathbf{1}^\perp\), so \(\lambda_\mathrm{min}\) is again the smallest nonzero eigenvalue), so the tangent rotates onto the cut mode by itself-- stepping in _s_ becomes stepping in \(\psi\), the well-conditioned direction.

Each continuation step is a _predictor_ that advances a fixed arclength \(\Delta s\) along the tangent, \((\phi,\alpha)+=\Delta s(\dot{\phi},\dot{\alpha})\), then a _corrector_ that drives two residuals to zero: the _equilibrium residual_ \(r=\alpha d-B\rho(B^\top\phi)\) of (1.1) (as in Algorithm 3.1) and the _arclength residual_

(3.2) \(N=\dot{\phi}^\top(\phi-\phi_0)+\dot{\alpha}\left(\alpha-\alpha_0\right)-\Delta s,\)

how far the point has advanced along the tangent past the previous solution \((\phi_0,\alpha_0)\), minus the target \(\Delta s\). Setting _r_=0 holds the point on the equilibrium curve; _N_=0 fixes how far along it (hence "pseudo"-arclength: the exact arclength sphere \(\|\delta\phi\|^2+\delta\alpha^2=\Delta s^2\) is linearized to its tangent plane _N_=0.) One Newton step on (_r,N_)=0 is the bordered linear system<tbc>

(3.3) \(\left[\begin{array}{ c c }
J & -d \\
\dot{\phi}^\top & \dot{\alpha}
\end{array}\right]\left[\begin{array}{ c }
\delta\phi \\
\delta\alpha
\end{array}\right]=\left[\begin{array}{ c }
r \\
-N
\end{array}\right].\)

<tbc>Block elimination of \(\delta\alpha\) gives

(3.4) \(\delta\alpha=-\frac{\dot{\phi}^\top w+N}{\dot{\alpha}+\dot{\phi}^\top u},\delta\phi=\delta\alpha u+w,\)

where _u=J_<sup>+</sup>_d_ and _w=J_<sup>+</sup>_r_ are computed by two applications of the inner Laplacian solver. Both \(u,w\in\) range\((J^+)=\chi^\perp\): the near-null cut component of the solution (the \(\chi\) direction) is pinned by the scalar arclength row (3.2), not by these solves. The border keeps the system nonsingular through the fold (\(\kappa=\mathcal{O}(10^3)\) while \(\kappa(J)\rightarrow\infty\)), so the inner Laplacian solver stays fast (approximate Cholesky PCG and LAMG+ cycle ACF both ≈0.01).

The refresh policy of §3.2 is woven into the corrector as a staleness safeguard (Algorithm 3.2). Both _u_ and _w_ computations reuse one frozen hierarchy; since the cut conductances drain exponentially in the cut amplitude, that hierarchy ages faster as the fold sharpens, and the monitor rebuilds it more often -- about every 4 arclength steps at 0.97_F_<sup>∗</sup>, every 2 at 0.995_F_<sup>∗</sup>. The predictor’s tangent \(\dot{\phi}=J^+d\), the single direction most sensitive to _J_’s drift, is instead recomputed on a fresh hierarchy once per accepted step. The fixed-load solution remains machine-precise as close to the fold as \(\alpha=0.995F^*\) (a fixed-\(\alpha\) equilibrium is well-posed only for \(\alpha<F^*\)), while the arclength continuation tracks through the fold to the exact F\* without stalling ( 5.1).

**4. Transportation: undirected congestion equilibrium.** This is NLF’s sharpest result: on convex congestion flow--which has no combinatorial competitor and whose operator never folds--NLF is an empirically linear-time solver, verified against a state-of-the-art interior-point method on real road-network topologies.

