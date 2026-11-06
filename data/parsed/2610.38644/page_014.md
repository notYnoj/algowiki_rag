## 4.2 Comparison with PINNs and FBPINNs

To contextualize the performance of CFKS, we compare it with standard physics-informed neural networks (PINNs) and finite-basis PINNs (FBPINNs). The three ODE benchmarks considered above coincide with those studied by Moseley et al. \[23\], allowing comparison under the same operator families and frequency content.

Standard PINNs exhibit pronounced spectral bias on these problems, particularly for the \(\omega=15\) and multiscale cases. FBPINNs improve the high-frequency representation by decomposing the domain into overlapping subdomains with locally normalized subnetworks, but require the selection of the subdomain layout, overlap, network architecture, and training schedule \[23\]. For the first-order oscillatory problem, the reported FBPINN configuration uses 30 subdomains<tbc>

Solution, w = 15
Absolute error
10-4
0.050
10-6
0.025
10-8
0.000
10-10
-0.025
10-12
-0.050
10-14
-6
-4
-2
0
2
4
6
-6
-4
-2
0
2
4
6
X
X
Kernel solution
Exact
Solution, w = 15
Absolute error
0.004
10-5
0.002
10-7
0.000
10-9
10-11
-0.002
10-13
-0.004
10-15
-6
-4
-2
0
2
4
6
-6
-4
-2
0
2
4
6
X
X
Kernel solution
Exact
Multicscale solution, [w1, 02] = [1, 15]
Absolute error
2
10-3
10-5
1
10-7
0
10-9
10-11
10-13
-2
-6
-4
-2
0
2
4
6
-6
-4
-2
0
2
4
6
X
X
Kernel solution
Exact

Figure 1: ODE benchmarks. Top: first-order oscillatory problem \(u'=cos(15x)\). Middle: second-order oscillatory problem \(u''=sin(15x)\). Bottom: multiscale problem with \([\omega_1,\omega_2]=[1,15]\). In each row, the left panel compares the continuum-feature kernel and exact solutions, while the right panel shows the pointwise absolute error.

