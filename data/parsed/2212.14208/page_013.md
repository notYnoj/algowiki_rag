<tbc>modelling. These DOEs have the form

(5.1) \(E\dot{u}(t)=(J-R)u(t)+f(t),u(0)=u_0,\)

where _E_ is hermitian and positive definite, _J_ is anti-selfadjoint and _R_ is hermitian and positive semidefinite. With a step size of \(\tau>0\), the linear systems to solve at each time step are then of the form

\(Ax=b\text{with}A=E+\frac{\tau}{2}(R-J),\)

and we have \(H=E+\frac{\tau}{2}R\), positive definite, and \(S=-\frac{\tau}{2}J\). Note that implicit integration methods are mandatory in this situation if one wants to preserve the dissipation of energy; see \[14\].

_Example 3._ We take the homonomically constrained spring mass system from \[15\], which is part of the port Hamiltonian system benchmark collection<sup>1</sup>. We refer to \[10\] and \[9\] on how the matrices _E_, _R_ and _J_ arise from the descriptor system formulation of the system. We took the system with \(n=2\cdot 10^6\) as it was also considered in \[9\] and \(\tau/2=0.1\). The numerical results are given in Figure 3. For all choices of \(\varepsilon_\mathrm{cg}\), the norms of the residuals of FGAL and FMR are so close that they are indistinguishable in the plots, which is why we report only the results for FMR. The bounds from Proposition 4.4 again match the convergence behavior quite exactly. Similar to the<tbc>

<sup>1</sup>available at https://algopaul.github.io/PortHamiltonianBenchmarkSystems/

cg tolerance = 0.1
cg tolerance = 0.01
100
FGAL
100
FGAL FMR FMR
a posteriori bound
a posteriori bound
10-5
10-5
10-10
10-10
10-15
10-15
0
10
20
30
40
50
60
70
80
0
10
20
30
40
50
60
70
80
cg tolerance = 0.001
cg tolerance = 1e-12
105
105
FGAL
FGAL FMR FMR
100
a posteriori bound
a posteriori bound
100
10-5
10-5
10-10
10-10
10-15
10-15
10-20
10-20
10-25
0
10
20
30
40
50
60
70
80
0
10
20
30
40
50
60
70
80

Fig. 2. _Results for the unsteady channel domain Stokes problem, Example 2,_ \(\tau/2=10^{-3}\)_, four choices for_ \(\varepsilon_\mathrm{cg}\)

