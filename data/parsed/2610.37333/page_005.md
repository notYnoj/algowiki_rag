linear solver and sparse automatic differentiation in `JAX`. Traditionally, differential equation software has been developed for small model problems and extended to large multiphysics systems afterwards, whereas we take the opposite approach and design every component around the sparse structure of large discretized PDEs. `diff-soup` provides the standard numerical tools of a large-scale stiff solver, including VSVO integrators for stiff ordinary differential equations (ODEs) and index-1 differential-algebraic equations (DAEs) with consistent initialization, event handling, and sparse automatic differentiation, together with finite difference, finite volume, and finite element discretizations on grids and meshes. Beyond these standard tools, `diff-soup` is distinguished from existing stiff solvers by

1. a GPU-native and fully differentiable design that is specialized to problems with sparse structure,<tbc>

2. accelerator-specific techniques for reaching large problems, namely reduced precision, batched solves, and multi-GPU parallelism, and<tbc>

3. end-to-end workflows for PDE-constrained optimization, with second- order optimizers, multiple shooting, and statistical inference, that compose with `JAX` libraries such as `equinox` [51], `optax` [52], and `blackjax` [53] for embedded deep learning models and uncertainty quantification.

The remainder of this paper is organized as follows. Section 2 reviews the computational background on VSVO time integration, sparse methods, and differentiable simulation. Section 3 describes the modeling, simulation, and inference modules of `diff-soup`. In Section 4, we benchmark forward solves and gradients against SUNDIALS, PETSc, `DifferentialEquations.jl`, MATLAB, and `diffrax`, and we examine reduced precision and multi-GPU execution. In Section 5, we demonstrate two end-to-end applications, the Bayesian inference of the constitutive relationships of a phase-separating material from image data and the training of a neural field embedded in a three-dimensional packed bed reactor model.

## 2. Mathematical Background

In this work, we consider time-dependent systems that take the general form of a differential-algebraic equation

\(0=F(y,y',\theta,z(t),t),\) (1)

