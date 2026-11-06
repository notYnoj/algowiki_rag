<tbc>_K_=6 components, when weights are allowed to vary, some components of the optimised mixture (in red) are trapped between two target components (in blue).

## Choice of the number of components _K_.

We choose _K_=10 Gaussian components in our colour transfer experiments. Taking _K_=1, i.e. one Gaussian per source and target, is equivalent to applying the following affine map to source pixels:<tbc>

\(T:x\in\mathbb{R}^d\longmapsto m_t+A(x-m_s),\)

<tbc>where _m<sub>s</sub>_ and _m<sub>t</sub>_ are the empirical means of source and target colour distributions, and where

\(A=\Sigma_s^{-1/2}\left(\Sigma_s^{1/2}\Sigma_t\Sigma_s^{1/2}\right)^{1/2}\Sigma_s^{-1/2}=A^\top.\)

This map performs a coarser colour transfer than the optimisation with _K_=10, as compared in Fig. 25: the contrast is better preserved with higher values of _K_. We always set \(\varepsilon_r=10^{-3}\) in this experiment.

Measure 1
Measure 2
Measure 3
Projected Barycentre
Projected Barycentre
Projected Barycentre

B
G
R
(a)
(b)

Figure 23: 3D barycentre (left) and its projections (right).

Figure 24: Final GMMs in RGB space with (a) variable weights and (b) fixed weights. Target is in blue and optimised mixture is in red. In (a) we are stuck in a local minimum, in (b) we converged.

