equation on the unit interval with diffusivity _D_,

\(\frac{\partial u}{\partial t}=D\nabla^2u,x\in(0,1),t>0,u(0,t)=u(1,t)=0,u(x,0)=x(1-x),\text{(15)}\)

which translates to the following `diff-soup` Recipe:

First, the user specifies the domain on which the physical system will be simulated. `diff-soup` provides a flexible domain and discretization system with support for both structured grids through FDM, FVM, and FEM, and unstructured meshes through FEM. Once a domain is registered, the unknowns are declared on it as fields, scalar- or vector-valued variables that are specified as differential or algebraic variables. The user then writes the PDE system in strong form as a plain Python closure over an access object _q_, composing the field values, the declared parameters, and the differential operators of the domain. `diff-soup` maintains a readily extendable library of common differential operators for science and engineering, with each operator declaring the induced sparsity pattern for composition into the sparse<tbc>

import numpy as np
import diff_soup as ds
from diff_soup.domains import cartesian_grid_1d
n = 64
spec = ds.problem("heat") # open the builder
spec.domain("rod", cartesian_grid_1d(n, 0.0, 1.0, method="fvm")) # 64 cells
spec.field("u", mass="differential", scale=1.0, init=lambda x: x * (1.0 - x))
D = spec.param("D", value=0.1, learnable=True, bounds=(0.01, 2.0)) # learnable
@spec.equation(writes="u", reads=("u",))
def heat(q):
return q.p.D * q.ops.laplacian(q.u) # du/dt = D lap(u)
spec.bc.dirichlet("u", node_indices=np.array([0, n - 1]), value=0.0)
problem = spec.build() # lower the recipe

Listing 1: The heat equation of Eq. (15) declared through the Recipe API. The unit interval is discretized on 64 finite-volume cells, the diffusivity is declared as a learnable parameter with box bounds, both ends are pinned to zero, and `build` lowers the recipe into the problem that the simulation module consumes.

