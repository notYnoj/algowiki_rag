# A Two-Grid Finite Element Method for the Nonlinear Poisson-Boltzmann Equation Based on a Solution Decomposition

**Abstract**

The nonlinear Poisson-Boltzmann equation (PBE) is a widely used implicit-solvent model for the electrostatics of biomolecules in ionic solvent. Its numerical solution is complicated by the point charges, the dielectric jump across the molecular surface, and the exponential nonlinearity. We study a two-grid finite element method for the PBE built on the solution decomposition \(u=G+\Psi+\widehat{\Phi}\) of Xie [J. Comput. Phys. 275 (2014) 294-309], in which _G_ carries the singularities analytically, \(\Psi\) solves a linear interface problem, and \(\widehat{\Phi}\) solves a semilinear interface problem for an arbitrary number of ionic species. The nonlinear problem for \(\widehat{\Phi}\) is solved on a coarse mesh only, followed by a single Newton correction on the fine mesh, so that only symmetric positive definite linear systems are solved on the fine mesh. The analysis uses a _C_<sup>2</sup> truncation of the exponential that grows quadratically beyond a level \(\tau\); for \(\tau\) above an explicit bound the truncated problem has the same solution as the original one, and no discrete maximum principle or mesh-angle condition is needed. Under standard piecewise regularity assumptions we prove quasi-optimal energy and _L_<sup>2</sup> estimates and an _L_<sup>4</sup> estimate for the finite element approximation of \(\widehat{\Phi}\), and for the two-grid solution we prove \(|||u-u_h^\text{tg}|||\le C\big(h^{s-1}+H^{2(s-1)+t/2}\big)\) in three dimensions, where \(t=min\{s,\sigma\}-1\). Whenever the dual problem is at least as regular as the primal one (\(\sigma\ge s\)), the coarse mesh can be chosen as _H∼h_<sup>2/5</sup> without loss of accuracy. A manufactured-solution test confirms the predicted rates and the quadratic dependence of the two-grid correction on the coarse error.

**Keywords:** Poisson-Boltzmann equation; solution decomposition; semilinear interface problem; two-grid method; finite element method; a priori error estimates; biomolecular electrostatics.

**MSC 2020:** 65N30, 65N15, 35J61, 92C40.

### 1 Introduction

The Poisson-Boltzmann equation (PBE) is a standard continuum model for the electrostatic potential of a biomolecule in an ionic solvent [32, 14, 4, 26]. It is solved by finite difference and finite element packages such as APBS [5], DelPhi [30] and MIBPB [16], and by boundary integral methods [25, 15]. From the numerical point of view the PBE is an elliptic interface problem with three difficulties: the source is a sum of Dirac distributions at the atomic centers, so the potential is singular there; the dielectric coefficient jumps across the molecular surface; and the ionic charge density depends exponentially on the potential. We refer to the surveys [26] and [34] for the literature on each of these issues.

<sup>1</sup>Department of Mathematics, Western Washington University, Bellingham, WA 98225, USA. Corresponding author: **chaoz2@wwu.edu.** <sup>2</sup>College of Earth and Mineral Sciences, The Pennsylvania State University, University Park, PA 16802, USA. <sup>3</sup>Department of Mathematical Sciences, University of Wisconsin–Milwaukee, Milwaukee, WI 53211, USA.

Zhen Chao<sup>1</sup>

Jingchun Chen<sup>2</sup>

Cong He<sup>3</sup>

arXiv:2610.34661v1 [math.NA] 26 Oct 2026

