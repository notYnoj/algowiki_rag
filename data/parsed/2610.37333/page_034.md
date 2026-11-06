Figure 8 compares the `JIDA` solver of `diff-soup` on the CPU and GPU with the CPU lanes of SUNDIALS, PETSc, `DifferentialEquations.jl`, and MATLAB on both problems.

(a)
t= 0 s
t= 9 s
t= 18 s
t= 27 s
t= 36 s
1.0
n
0.5
10 nm
0.0
(b)
0.007
Exx
(c)
0
Eyy
-0.007
(d)
0.0008
0
Exy
-0.0008

Figure 7: Solution of the Cahn-Hilliard problem with elasticity on its 50 nm square domain at \(256\times 256\) cells, five snapshots from _t_=0 to 36 s. (a) The conserved order parameter \(\eta\) phase separating from the sinusoidal seed. (b, c, d) The strain components \(\varepsilon_{xx}\), \(\varepsilon_{yy}\), and \(\varepsilon_{xy}\) of the displacement that holds the solid in mechanical equilibrium, the normal components on one shared scale and the shear on its own.

