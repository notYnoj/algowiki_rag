iteration numbers and wall-clock time. Nevertheless, even with \(\gamma_2=1\), FIM-3 still provides noticeable acceleration, with both the iteration numbers and wall-clock time reduced by roughly half compared with the IMEX-SGS iteration.

As in the first-order case, the performance of FIM-3 can be further improved by increasing \(\gamma_2\). However, the appropriate choice of \(\gamma_2\) varies considerably with the Knudsen number, and the values reported in  3 are selected<tbc>

1.04
Kn = 0.1, DUGKS
Kn = 0.01, M = 7
1.03
Kn = 0.1, M = 10
Kn = 0.001, DUGKS
Kn = 0.1, M = 9
Kn = 0.001, M = 6
Kn = 0.01, DUGKS
Kn = 0.001, M = 5
1.02
Kn = 0.01, M = 8
1.01
1
0.99
0.98
-0.4
-0.2
0
0.2
0.4

1.08
1.07
1.06
1.05
1.04
1.03
1.02
1.01
1
-0.4
-0.2
0
0.2
0.4

0.8
0.6
0.4
0.2
0
-0.2
-0.4
-0.6
-0.8
-0.4
-0.2
0
0.2
0.4

0.05
0.04
0.03
0.02
0.01
0
-0.01
-0.02
-0.03
-0.04
-0.05
-0.4
-0.2
0
0.2
0.4

10-1
Kn = 0.1, M = 9, p
Kn = 0.001, M = 5, p
Kn = 0.1, M = 9, 0
Kn = 0.001, M = 5, 0
Kn = 0.01, M = 7, p
First-order ref
10-2
Kn = 0.01, M = 7, 0
10-3
10-4
10-5
10-3
10-2
AX

10-2
Kn = 0.1, M = 9, p
Kn = 0.001, M = 5, p
Kn = 0.1, M = 9, 0
Kn = 0.001, M = 5, 0
10-3
Kn = 0.01, M = 7, p
Second-order ref
Kn = 0.01, M = 7, 0
10-4
10-5
10-6
10-7
10-8
10-3
10-2
AX

(a) Density, \(\rho\)

(b) Temperature, \(\theta\)

(c) Velocity, _u_<sub>2</sub>

(d) Heat flux, _q_<sub>1</sub>

Figure 1: Numerical solutions of the planar Couette flow with _N<sub>x</sub>_=128.

(a) First-order scheme

(b) Second-order scheme

Figure 2: The errors of the FIM method with various _Kn_ for planar Couette flow.

