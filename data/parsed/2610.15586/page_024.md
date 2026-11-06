## A Elements of Riemannian geometry

This appendix summarizes the notions of Riemannian geometry used in Sec. 4. Standard references are Refs. \[10, 11, 21\]. We use the summation convention.

### Metric and volume.

A Riemannian manifold \((\Omega,g)\) is a smooth manifold with a positive-definite symmetric tensor _g<sub>ij</sub>_ in local coordinates _u<sup>i</sup>_. The line element is _ds_<sup>2</sup>=_g<sub>ij</sub>du<sup>i</sup>du<sup>j</sup>_, and _g<sup>ij</sup>_ denotes the inverse matrix. The volume element is \(d\mu_g=\sqrt{g}du^1\cdots du^n\) with \(\sqrt{g}=\sqrt{\mathrm{det}g_{ij}}\). For a map \(\Phi:R\rightarrow\Omega\subset\mathbb{R}^n\) from a coordinate domain, the induced metric is \(g_{ij}=\partial_i\Phi\cdot\partial_j\Phi\).

### Gradient, divergence, and the Laplace-Beltrami operator.

The gradient of a function is \((\nabla_gw)^i=g^{ij}\partial_jw\), and the divergence of a vector field is \(\mathrm{div}_gV=g^{-1/2}\partial_i(\sqrt{g}V^i)\). The weighted operator of Eq. (18) is

\(-\nabla_g\cdot(\rho\nabla_gw)=-\frac{1}{\sqrt{g}}\partial_i\big(\rho\sqrt{g}g^{ij}\partial_jw\big).\) (30)

For \(\rho=1\) it is the Laplace-Beltrami operator \(-\Delta_g\). By multiplying Eq. (30) by a test function _v_ that vanishes on the wall and integrating with \(d\mu_g\), we obtain the left side of Eq. (18). The integrand \(\rho g^{ij}\partial_iw\partial_jv\sqrt{g}\) is a density, so the weak form does not depend on the choice of coordinates.

### Conformal metrics in two dimensions.

If \(g_{ij}=h^2\delta_{ij}\), then \(\sqrt{g}=h^2\) and \(\sqrt{g}g^{ij}=\delta^{ij}\), so that \(\Delta_g=h^{-2}\Delta\) and the Dirichlet energy \(\int g^{ij}\partial_iw\partial_jwd\mu_g\) equals its flat value. This is the content of Proposition 12. The Gaussian curvature of a conformal metric is \(\mathcal{K}=-h^{-2}\Delta\mathrm{ln}h\). A metric induced by a conformal map of a planar domain is flat, so ln_h_ is harmonic. For the elliptic coordinates, \(h^2=\ell_g^2|\mathrm{sinh}(\mu+i\nu)|^2\), and for the bipolar coordinates, \(h=\ell_g/|\mathrm{cosh}\tau-\mathrm{cos}\sigma|\); in both cases ln_h_ is the real part of the logarithm of an analytic function. This identity provides a simple check of a numerically computed metric factor.

### Lie derivative.

Let _X_ be a vector field with flow \(\phi_s\). The Lie derivative of a tensor field _T_ is<tbc>

\(\left.\mathcal{L}_XT=\frac{d}{ds}\right|_{s=0}\phi_s^*T.\) (31)

<tbc>For a function, \(\mathcal{L}_Xw=X^i\partial_iw\). For a vector field, L_<sub>X</sub>Y_=\[_X,Y_\]. For the metric,

\((\mathcal{L}_Xg)_{ij}=X^k\partial_kg_{ij}+g_{kj}\partial_iX^k+g_{ik}\partial_jX^k=\nabla_iX_j+\nabla_jX_i,\) (32)

where \(\nabla\) is the Levi-Civita connection. The trace is _g<sup>ij</sup>_(L_<sub>X</sub>g_)<sub>_ij_</sub>=2div_<sub>g</sub>X_. Pull-back commutes with _d/ds_, so \(\frac{d}{ds}\phi_s^*T=\phi_s^*\mathcal{L}_XT\) for all _s_.

### Killing and conformal Killing fields.

A Killing field satisfies L_<sub>X</sub>g_=0. Its flow consists of isometries, and it commutes with \(\Delta_g\). Examples are \(\partial_\theta\) for a disk in polar coordinates and translations along a straight duct. A conformal Killing field satisfies \(\mathcal{L}_Xg=2\sigma g\) for a function \(\sigma\). In two dimensions every analytic function \(\zeta(u^1+iu^2)\) defines a conformal Killing field of the flat metric, which is why conformal maps are so plentiful in the plane. Proposition 13 uses Killing fields and discrete isometries, and Proposition 16 uses the trace-free part of L_<sub>V</sub>g_, which vanishes exactly for conformal Killing fields.

### Variations of the metric.

For a variation \(\delta g_{ij}\),

\(\delta g^{ij}=-g^{ik}\delta g_{kl}g^{ij},\delta\sqrt{g}=\frac{1}{2}\sqrt{g}g^{kl}\delta g_{kl}.\) (33)

With \(\delta g=s\mathcal{L}_Vg\) these formulas give Eq. (23). A moving wall, as in a pulsating vessel, can be treated in the same way: if the wall moves with velocity _V_ , the pulled-back metric evolves as \(\partial_tg=\mathcal{L}_Vg\), which is the geometric content of an arbitrary Lagrangian-Eulerian formulation.

