Certainly, when \(\alpha\) is small, computations involving \(D_\alpha^{-1}\) may introduce stability concerns as extensively studied in \[13, 42\]. However, as examined in \[32\], it appears that this does not significantly impact convergence when a Krylov subspace method is used with a properly chosen small \(\alpha\) independent of the meshes. The stability implications of small \(\alpha\) warrant further investigation, which we will address in our future research.

## 3. Numerical examples

In this section, we demonstrate the effectiveness of our proposed preconditioner. All numerical experiments are carried out using Octave 8.2.0 on a Dell R640 server equipped with dual Xeon Gold 6246R 16-Cores 3.4GHz CPUs, 512GB RAM running Ubuntu 20.04 LTS. The CPU time in seconds is measured using the Octave built-in functions **tic/toc**. Both Steps 1 & 3 in Section 2.3 are implemented by the functions **dst** (discrete sine transform) and **fft** (fast Fourier transform). Furthermore, the MINRES solver used is implemented using the built-in function **minres** on Octave. We choose a zero initial guess and a stopping tolerance of 10<sup>-6</sup> based on the reduction in relative residual norms for the MINRES solver tested unless otherwise indicated.

We adopt the notation MINRES-\(\mathcal{P}_\alpha\) to represent the MINRES solver with the proposed preconditioner \(\mathcal{P}_\alpha\). We will test our proposed MINRES-\(\mathcal{P}_\alpha\) method for wave equation compare its performance against MINRES-P<sub>1</sub> proposed in \[37\] and MINRES-_I<sub>mn</sub>_ (i.e., the non- preconditioned case). We set \(\alpha\) to 10<sup>-6</sup> for MINRES-\(\mathcal{P}_\alpha\), a value empirically chosen based on a series of experiments aimed at optimizing performance. The stopping criterion of for all MINRES solvers tested in this section is set as \(\|\mathbf{r}_k\|_2\le 10^{-6}\), where **r**_<sub>k</sub>_ denotes the residual vector at _k_-th iteration step.

Denote by ‘Iter’, the iteration numbers for solving a linear system by an iterative solver. Denote by ‘CPU’, the computational time in unit of second. Denote by ‘DoF’, the degree of freedom, i.e., the number of unknowns. For ease of statement, we take the same spatial step size _h_ for each spatial direction in all examples appearing in this section. We define the error as

\(\mathrm{E}_{\tau,h}:=\mathrm{max}_{1\le k\le n}h^{d/2}\|(\mathbf{u}_\mathrm{iter}^{(k)}-u(\mathcal{G}_h,k\tau)\|_2,\)

where _d_ is the spatial dimension, _h_ denotes the spatial step size along each spatial direction, \(\mathbf{u}_\mathrm{iter}^{(k)}\) denotes the iterative solution of the linear system at _k_-th time level, and \(u(\mathcal{G}_h,k\tau)\) denotes the values of exact solution \(u(\cdot,k\tau)\) on the spatial grids.

In the following two examples, as discussed, the concerned wave equations is discretized using the finite difference scheme proposed in \[31\], which was shown to be unconditionally convergent with a second-order accuracy without imposing the CFL condition.

