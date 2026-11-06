## 3.1. Modeling

In this subsection, we describe the modeling module, the primary user entry point in `diff-soup`, and its lowering to an internal representation (IR) system used for simulations. We have designed the Recipe API as a user-friendly workflow for specifying physical equations in math-like notation without needing a symbolic algebra system. For example, consider the heat<tbc>

diff-
Modeling
Simulation
Inference
MSE
D(c)
iteration
c
grids and meshes
sparse Jacobian
simulated physics with adaptive time steps
optimization
learned function
spec = ds.problem("heat") solver = ds.JIDA()
measurement = ds.inference.Measurement( "u", times=ts, values=data, ...)
sol = ds.pdesolve(problem, solver, (0.0, 0.1), y0)
experiment = ds.inference.Experiment( (measurement,))
spec.domain("bowl", mesh)
spec.field("u", mass="differential")
problem, solver, (0.0, 0.1), y0,
def loss(theta):
est = ds.inference.InferenceProblem( def heat(q):
sol = ds.pdesolve(, theta=theta,
experiment, parameters=D)
fit = ds.inference.optsolve(est,
return sol.ys[-1].sum()
def.inference.NewtonTrustRegion())
return q.p.D * q.ops.laplacian(q.u)
spec.bc.dirichlet("u", value=0.0)
g = jax.grad(loss)(theta)
posterior = ds.inference.laplace(
problem = spec.build()
H = jax.hessian(loss)(theta)
est, fit)
grids and meshes: FDM, FVM, FEM
VSVO integrators: JIDA, JBDF, JNDF
solvers: Newton trust-region, Levenberg-Marquardt, L-BFGS
operators with sparsity patterns
consistent initialization, events
nonlinear boundary conditions
modified Newton nonlinear solver
multiple shooting and data assimilation
global constraints and controls
sparse direct and dense linear solvers
classical and neural function approximation
learnable parameters and functions
direct authoring from the residual
discrete forward and adjoint sensitivities
statistical estimation and uncertainty quantification
JIT compilation automatic differentiation
cuDSS batched solves
JAX
GPU
vectorization optax, equinox, blackjax
reduced precision multi-GPU parallelism

Figure 3: Visual overview of the three primary modules of `diff-soup` for modeling, differentiable simulation, and inference.

