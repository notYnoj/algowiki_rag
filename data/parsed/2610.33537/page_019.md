<tbc>generally converge more slowly than in the first-order case, while providing higher spatial accuracy. As in the first- order case, FIM-3 requires empirical tuning of \(\gamma_2\) to achieve satisfactory performance, whereas FIM-4 employs one Newton-multigrid step in each alternating iteration. Compared with the tuned FIM-3, FIM-4 is substantially more efficient at small Knudsen numbers, achieving speedups exceeding 4 at _Kn=_0.01 and about 3 at _Kn=_0.001. At _Kn=_0.1, FIM-4 is moderately less efficient than the tuned FIM-3, which may be partly related to the higher computational cost associated with the full Jacobian system. This cost could potentially be reduced by simplifying the Jacobian matrix. In the problems studied in \[41\], such a strategy reduced the Jacobian-related computational cost by<tbc>

1
275
0.8
274.75
274.5
274.25
274
0.6
273.75
273.5
273.25
0.4
273
273.75
272.5
0.2
272.25
272
0
0
0
0.2
0.4
0.6
0.8
1
X

1
0.8
0.6
0.4
0.2
0
0
0.2
0.4
0.6
0.8
1
X

1
0.8
0.6
0.4
0.2
0
0
0.2
0.4
0.6
0.8
1
X

1
0.8
0.6
0.4
0.2
0
0
0.2
0.4
0.6
0.8
1
X

1
DUGKS
0.8
FIM, M = 7
FIM, M = 8
0.6
u2u
u2u
0.4
u2u
u2u
0.2
0
-0.2
0
0.2
0.4
0.6
0.8
1
X, y

1
DUGKS
0.8
FIM, M = 5
FIM, M = 6
0.6
u2u
u2u
0.4
u2u
u2u
0.2
0
-0.2
-0.4
0
0.2
0.4
0.6
0.8
1
X, y

1
0.8
0.6
u2u
u2u
0.4
0.2
0
0
0.2
0.4
0.6
0.8
1
X

1
DUGKS
0.8
FIM, 2 nd, N = N = 64
FIM, 1 st, N = N = 128
FIM, 1 st, N = N = 256
0.6
FIM, 1 st, N = N = 512
FIM, 1 st, N = N = 1024
FIM, 1 st, N = N = 2048
0.4
u2u
u2u
u2u
u2u
u2u
0.2
0
-0.2
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
X, y

1
0.8
0.6
u2u
u2u
u2u
0.4
u2u
u2u
0.2
0
-0.2
-0.4
-0.6
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
X, y

(a) Temperature (K), _M=_10

(b) Velocity streamlines, _M=_8

(c) Velocity streamlines, _M=_6

(d) Heat flux streamlines, _M=_10

(e) _u_<sub>1</sub>, _u_<sub>2</sub> along centerlines

(f) _u_<sub>1</sub>, _u_<sub>2</sub> along centerlines

Figure 6: Numerical solutions of the lid-driven cavity flow with \(N_x\times N_y=64\times 64\). _Left column_: results at _Kn=_0.1, with dashed and red lines representing DUGKS solutions; _Middle column_: velocity streamlines and normalized velocity profiles (_u_<sub>1</sub> along the vertical centerline, _u_<sub>2</sub> along the horizontal centerline) at _Kn=_0.01; _Right column_: corresponding velocity results at _Kn=_0.001.

(a)

(b)

(c)

Figure 7: Numerical solutions of the lid-driven cavity flow with _M=_6 at _Kn=_0.001. _Left_: velocity streamlines with _N<sub>x</sub>=N<sub>y</sub>=_512 and first-order discretization; _Middle_: _u_<sub>1</sub> (_u_<sub>2</sub>) along _x=_1/4 (_y=_1/4); _Right_: _u_<sub>1</sub> (_u_<sub>2</sub>) along _x=_3/4 (_y=_3/4).

