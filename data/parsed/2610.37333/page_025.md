or optionally a dense solver, and handles the global variables through the Schur complement of Section 2.2. Finally, events interrupt the integration when a user-specified condition is met to terminate the solve or modify the state and controls before continuing.

The `pdesolve` function is compatible with the standard `JAX` transformations including JIT compilation, automatic differentiation, and batching through `jax.vmap`. The compiled solve is cached for each problem and solver configuration, so the time interval, initial conditions, parameters, and controls can change without recompilation. To differentiate through the solve, we employ the discretize-then-optimize approach of Section 2.3 with a frozen controller. By default, forward mode automatic differentiation propagates one tangent per input direction through the adaptive loop, with batching used when possible. Reverse mode uses a discrete checkpointed adjoint to compute the gradient of a scalar objective with respect to all parameters in

import jax
import numpy as np
y0 = spec.assemble_state({}) # the initial state
solver = ds.JIDA() # VSVO DAE engine
ts = np.linspace(0.02, 0.1, 5)
sol = ds.pdesolve(problem, solver, (0.0, 0.1), y0, saveat=ds.SaveAt(ts=ts))
sol.ys, sol.ok, sol.stats # (5, 64) states, outcome, stats
theta = ds.default_theta(problem) # the parameter pytree
def final_state(theta):
return ds.pdesolve(problem, solver, (0.0, 0.1), y0, theta=theta).ys[-1]
S = jax.jacfwd(final_state)(theta) # forward mode (default)
def loss(theta):
sol = ds.pdesolve(problem, solver, (0.0, 0.1), y0, theta=theta,
adjoint=ds.CheckpointAdjoint()) # checkpointed reverse mode
return sol.ys[-1].sum()
g = jax.grad(loss)(theta) # one backward sweep
H = jax.hessian(loss)(theta) # forward over reverse

Listing 2: A solve and differentiation of the running heat equation example given in Eq. (15). The JIDA solver integrates the problem of Listing 1 to five output times, forward mode differentiates the final state with respect to the parameters at the default settings, and the checkpointed adjoint enables the reverse-mode gradient and the forward-over-reverse Hessian of a scalar loss.

