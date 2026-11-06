# DEFLATION-BASED SPECTRAL PRECONDITIONING FOR THE CONJUGATE GRADIENT METHOD ON PERTURBED SYSTEMS <sup>∗</sup>

Y. DIOUANE<sup>†</sup>, S. GÜROL<sup>‡</sup>, O. MOUHTAL<sup>‡†</sup>, AND D. ORBAN<sup>†</sup>

**Abstract.** We consider sequences of large symmetric positive-definite linear systems in which spectral information from a reference matrix _A_ is reused to accelerate the solution of a nearby system with perturbed matrix _A(t_)=_A+tE_, where _E_ is symmetric, \(\|E\|_F=1\), and \(t\ge 0\) is the perturbation size. We compare deflated conjugate gradient (deflated CG) with preconditioned CG (PCG) equipped with a scaled spectral preconditioner constructed from the same spectral information of _A_. First, we derive an energy-norm error characterization of deflated CG. We then use perturbation analysis to show that, after one additional PCG iteration, the squared PCG error is bounded, up to terms of order _t_<sup>2</sup>, by an explicit multiple of the squared deflated CG error. This result clarifies the role of the scaling parameter in the preconditioner. Experiments show that the scaled spectral preconditioner recovers much of the convergence improvement provided by deflation while requiring fewer products with _A(t_).

**Key words.** Krylov methods, conjugate gradient, PCG, deflated CG, spectral preconditioner.

**MSC codes.** 65F08, 65F22, 65F15

**1. Introduction.** We consider sequences of large symmetric positive-definite (SPD) linear systems solved by the conjugate gradient (CG) method [15]. Such sequences arise in many applications, such as variational data assimilation [8], where consecutive systems are often closely related. Information generated while solving one system can then be recycled to accelerate subsequent solves; see, for example, [12, 22, 25, 28].

We consider a reference matrix _A_ together with a nearby matrix _A(t_)=_A+tE_, where _E_ is symmetric, \(\|E\|_F=1\), and _t_ is sufficiently small for _A(t_) to remain positive definite. Our goal is to reuse spectral information from _A_ to accelerate CG applied to the perturbed system _A(t)x=b_. This is particularly attractive in large-scale matrix- free settings, where constructing a preconditioner may be prohibitively expensive and only a limited number of matrix-vector products can be afforded.

One important approach for exploiting recycled information is deflated CG. Given a deflation subspace W=Range(_W_), deflated CG splits the solution into a component in W and a complementary component computed by CG on a projected system [9, 21, 24]. Tang et al. [27] mention that, for any deflation subspace, the effective condition number of the deflated system does not exceed that of the original system. A widely used choice for the deflation subspace is a set of approximate eigenvectors obtained from previous Krylov iterations through Ritz or harmonic Ritz projections [22, 24, 25, 29]. In the nonsymmetric setting, SVD-based strategies have also been proposed for recycling Krylov subspaces, in particular for GMRES [1]. Problem-dependent alternatives include coarse spaces arising from domain decomposition and multilevel methods [27]. These approaches seek to construct a low-dimensional subspace that captures the components responsible for slow convergence at moderate additional cost.

<sup>∗</sup>Submitted to the editors DATE. **Funding:** This research was partially funded by the Natural Sciences and Engineering Research Council of Canada (NSERC) Discovery Grants held by Diouane and Urban. Gürol and Mouhtal were partially funded by the French national programme LEFE/INSU. <sup>†</sup>GERAD and Department of Mathematics and Industrial Engineering, Polytechnique Montréal. (youssef.diouane@polymtl.ca, dominique.orban@polymtl.ca, oussama-2.mouhtal@polymtl.ca). <sup>‡</sup>CERFACS / CECI CNRS UMR 5318, Toulouse, France. (gurol@cerfacs.fr).

arXiv:2610.28808v2 [math.NA] 24 Oct 2026

