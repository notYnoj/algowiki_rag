diff-soup: GPU-native Differentiable Simulation and Inference for Large-scale Stiff Dynamical Systems

Samuel Degnan-Morgenstern<sup>a</sup>, Martin Z. Bazant<sup>a,b,∗</sup>

<sup>_a_</sup>_Department of Chemical Engineering, Massachusetts Institute of Technology, 25 Ames St., Cambridge, MA 02139, USA_

<sup>_b_</sup>_Department of Mathematics, Massachusetts Institute of Technology, 182 Memorial Dr., Cambridge, MA 02139, USA_

**Abstract**

Learning physical models from spatiotemporal data requires simulating systems of partial differential equations (PDEs) and differentiating through their solution. Upon spatial discretization, these models give rise to stiff dynamical systems that require repeatedly solving large, sparse linear systems. Traditional scientific computing frameworks are largely CPU-based and require problem-specific tuning to accelerate, scale, and differentiate. In this work, we introduce diff-soup, a differentiable, sparse-oriented, unified PDE suite for GPU-native simulation and inference of large, stiff dynamical systems. Built in JAX, diff-soup provides 1) a fully differentiable design for problems with sparse structure, 2) scaling to large problems through the NVIDIA cuDSS sparse direct solver with model and data multi-GPU parallelism, and 3) end-to-end PDE-constrained optimization, from classical statistical inference to embedded deep learning. On stiff PDE benchmarks, diff-soup outperforms established CPU- and GPU-based frameworks by one to two orders of magnitude in both forward solves and gradients. We demonstrate both a classical Bayesian inference workflow, identifying constitutive relationships, and a modern deep learning workflow, training a neural field for the catalyst activity of a three-dimensional packed bed reactor. We provide diff-soup as an open-source repository to facilitate research in computational science and engineering.

<sup>∗</sup>Corresponding author. _E-mail address:_ bazant@mit.edu

