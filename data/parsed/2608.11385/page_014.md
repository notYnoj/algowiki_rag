_Proof._ Differentiating (36) gives<tbc>

\(F_G^{(r)}(\phi)=\sum_{k=-D}^D(ik)^ra_ke^{ik\phi}.\)

<tbc>Choose _M\>_2_D_, let \(\omega=e^{2\pi i/M}\), and set \(\phi_j=2\pi j/M\). Orthogonality of the _M_th roots of unity yields<tbc>

\(\frac{1}{M}\sum_{j=0}^{M-1}F_G^{(r)}(\phi_j)\omega^{-jk}=(ik)^ra_k.\)

<tbc>Since _D<sub>⋆</sub>\>_0 and \(a_{D_\star}\neq 0\), the derivative coefficient (_iD<sub>⋆</sub>)<sup>r</sup>a<sub>D<sub>⋆</sub></sub>_ is nonzero. Consequently, the largest exponent with nonzero recovered derivative coefficient is again _D<sub>⋆</sub>_; no oracle for _F<sub>G</sub>_ itself is required. The extreme coefficient is recovered exactly as

\(a_{D_\star}(G)=\frac{1}{(iD_\star)^rM}\sum_{j=0}^{M-1}F_G^{(r)}(\phi_j)\omega^{-jD_\star},\)

where the value _D<sub>⋆</sub>_ is recovered as in the proof of Thm. 1.2. Applying this identity to G(_H_) and using Theorem 2.4 recovers |#MC(_H_)| in polynomial time.

The full gradient and Hessian determine the phase derivatives, so their exact computation inherits the preceding hardness.

**Corollary 3.2** (Hardness of the full gradient and Hessian)**.** _Consider the depth-two QAOA for MaxCut objective_ \(\mathcal{F}_G(\gamma_1,\gamma_2,\beta_1,\beta_2):=\langle C_G\rangle\)_. Exact computation of the full gradient_ \(\nabla\mathcal{F}_G\) _and of the full Hessian_ \(\nabla^2\mathcal{F}_G\) _is_ #P_-hard under deterministic polynomial-time Turing reductions. The same conclusion holds for single correlators._

_Proof of Corollary 3.2._ On the affine line \(\theta(\phi)=(\phi,\phi,\beta_1,\beta_2)\), the chain rule gives

\(F'_G(\phi)=v_\gamma^\mathsf{T}\nabla\mathcal{F}_G(\theta(\phi)),F''_G(\phi)=v_\gamma^\mathsf{T}\nabla^2\mathcal{F}_G(\theta(\phi))v_\gamma,\)

for \(v_\gamma=(1,1,0,0)^T\). The conclusion follows from Theorem 3.1 with _r_=1 and _r_=2.

**Remark 3.3.** _The result establishes hardness of the tied-phase directional derivative and curvature, and hence of returning the full gradient or Hessian. It does not by itself imply hardness of each individual gradient coordinate or Hessian entry separately._

The derivative hardness also survives exponentially small additive errors, by the same coefficient recovery argument used for expectation values.

**Corollary 3.4** (Exponentially precise derivative approximation)**.** _For the mixer angles of The orem 1.2 and every fixed_ \(r\ge 1\)_, there exists a constant c\>_0 _such that approximating_ \(F_G^{(r)}(\phi)\) _to additive error at most_ 2<sup>-_cN_</sup>_, where N_=|_V(G_)|_, is_ #P_-hard under deterministic polynomial-time Turing reductions. In particular, this applies to the tied-phase first and second derivatives._

_Proof._ The Fourier transform of the derivative oracle yields approximations to (_ik)<sup>r</sup>a<sub>k</sub>_. As in Corollary 2.8, for every _k\>D<sub>⋆</sub>_ the true coefficient vanishes, whereas the coefficient at _k=D<sub>⋆</sub>_ exceeds a known computable threshold in magnitude. Scanning the recovered coefficients from the largest exponent downward therefore identifies _D<sub>⋆</sub>_.

