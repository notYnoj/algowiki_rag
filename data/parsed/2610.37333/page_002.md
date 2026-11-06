**PROGRAM SUMMARY**

_Program :_ `diff-soup`: differentiable, sparse-oriented unified PDE suite

_CPC Library link to program files:_ (to be added by Technical Editor)

_Developer’s repository link:_ `https://github.com/stmorgenstern/diff-soup`

_Licensing provisions:_ BSD 3-Clause

_Programming language:_ Python, C++

_Supplementary material:_ The program files in the CPC Program Library contain `diff-soup` 1.0.0 together with the companion repository `diff\_soup\_paper`, which holds the benchmark suite, manifests, result stores, figure pipeline and worked examples.

_Nature of problem:_ Computational modeling of time-dependent partial differential equations (PDEs) gives rise to large systems of stiff ordinary differential equations and differential-algebraic equations. Robust and efficient integration of these systems requires implicit variable step, variable order (VSVO) methods such as BDF and NDF, whose predominant cost is the repeated factorization and solution of large sparse linear systems. The established stiff integration libraries run these operations on the CPU, and the general-purpose implicit ODE/DAE time- integration libraries of the `JAX` ecosystem rely on dense linear algebra, so large two- and three-dimensional problems remain out of reach for GPU-native, differentiable simulation. These challenges have limited the adoption of machine learning in general multiphysics modeling workflows.

_Solution method:_ We introduce diff-soup, a general-purpose differentiable, sparse- oriented unified PDE suite for GPU-accelerated multiphysics modeling, simulation, and inference. We provide a user-friendly Recipe API that models complex physical systems in math-like notation on both structured and unstructured domains with the finite difference, finite volume, and finite element methods. For fast simulation, we implement sparse Jacobian assembly by automatic differentiation with graph coloring, three VSVO stiff integrators written natively in `JAX`, and a wrapper to the NVIDIA `cuDSS` sparse direct linear solver on the GPU. All simulations are fully differentiable to second order, enabling large-scale PDE-constrained optimization. Using these derivatives, we provide an inference module for PDE-constrained least- squares problems, from classical frequentist and Bayesian inference to modern deep learning approaches. Both simulation and inference exploit batched solves, data parallelism, and model parallelism to scale to large problems.

_Additional comments including restrictions and unusual features:_ This article describes `diff-soup` 1.0.0. The package runs on Linux x86\_64 with Python 3.12 and `JAX` 0.11. GPU execution requires an NVIDIA GPU with a CUDA 12 or CUDA 13 driver and `cuDSS` 1.0 or newer, which is installed from NVIDIA’s Python wheels.

