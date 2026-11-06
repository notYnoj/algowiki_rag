<tbc>of the finite-section approximation, we compare the truncated value gradient and feedback of Theorem 2,

\(U_N(x)=2\sum_{i=1}^N\pi_{i+1}(\mathbf{P})x^i,u_N=-\frac{1}{r}\unknown_N^\top\unknown_N\mathbf{g}_N\) (38)

against the closed-form solution (12) where the truncated vector \(\mathbf{g}_N=\left[g_0,\dots,g_{N-1}\right]^\top\). We denote by _J<sub>N</sub>_ the cost in (3) along the closed loop under _u<sub>N</sub>_. We consider three nonlinear systems, where the algorithm in Theorem 2 was written as a MATLAB program to solve their lifted HJB equation.

_Example 1: Polynomial drift with rational input_

Consider the nonlinear system<tbc>

\(\dot{x}=x+x^2+u(1-(x/3))^{-1}\) (39)

<tbc>with weight _r_=1 and state cost function _q(x_)=_x_<sup>2</sup>. The drift function _f(x_)=_x+x_<sup>2</sup> and the control function _g(x_)=(1-_x/_3)<sup>-1</sup> satisfy (8) and (9). The gradient of the value function and the optimal control law are given by<tbc>

\(V_x=\frac{2(3x-x^2)}{9}\big(3+2x-x^2+\sqrt{9+(3+2x-x^2)^2}\big)\)

<tbc>and \(u^*=-\frac{x}{3}(3+2x-x^2+\sqrt{9+(3+2x-x^2)^2})\) respectively, and the corresponding dynamical system (1) with optimal control becomes

\(\dot{x}=-\frac{x\sqrt{9+(3+2x-x^2)^2}}{3-x}\)

In Fig. 2, the truncation order _N_ is held constant, and the closed-loop trajectories are simulated using the truncated controller _u<sub>N</sub>_. The left panel in Fig. 2 shows the Linear Quadratic Regulator (LQR) approximation, while the improvement is visible in the right panel, where the truncation order is increased to _N_=10 and more coefficients \(\pi_m\) enter \(\unknown_N\). It is observed that the approximation yields accurate estimates across different initial conditions for large truncation order _N_. We remark that _V<sub>x</sub>_ is analytic on a complex disc \(|z|<\sqrt{6-3\sqrt{2}}\approx 1.326\).

_Example 2: Trigonometric drift and input_

Consider the nonlinear system studied by \[3\]<tbc>

\(\dot{x}=tan(x)+(sec(x))u\)

<tbc>with _q(x_)=(1/2)sin<sup>2</sup>(_x_) and _r_=1/2, for which the closed- form value function and optimal control are

\(V=\frac{1+\sqrt{2}}{2}sin^2(x),u^*=-\big(1+\sqrt{2}\big)sin(x)\)

In this case, _f_<sub>1</sub>=1, _g_<sub>0</sub>=1, and \(\Delta=2>0\). Thus, by Theorem 2, we have \(\pi_2(\mathbf{P})=(1+\sqrt{2})/2\). While _f,g_, and _q_ are analytic on \(|x|<\pi/2\), the poles of tan(_x_) and sec(_x_) at \(\pm\pi/2\) cancel against the factor 2_r/g_<sup>2</sup>=cos<sup>2</sup>(_x_) in (12) for this example, giving \(V_x=\big(1+\sqrt{2}\big)sin(x)cos(x)\), which is analytic everywhere. To verify the approximation, Fig. 3 (left) shows that the truncated gradient _U<sub>N</sub>(x_) represents _V<sub>x</sub>(x_) more accurately over the state space as the truncation order is increased. In Fig. 3 (right), it is observed that the normalized error between the closed-loop cost of the truncated controller and the optimal cost decreases with more truncations for the listed initial conditions. We note that, since _f_ is odd and both _g_ and _q_ are even, _V<sub>x</sub>_ is an odd function, and \(\pi_m(\mathbf{P})=0\) for odd _m_. Thus, even truncations equal the preceding odd ones in Fig. 3 (right).

_Example 3: Fast-intermediate glycolysis model with PFK enzyme activity as input_

Consider the autocatalytic glycolysis model studied by \[29\] where the dynamics are given by<tbc>

\(\dot{y}=u\gamma(y)-c,\gamma(y)=\frac{2y^a}{1+y^{2h}}\)

<tbc>Here, _u_ is the PFK activity, \(\gamma\) is the ATP production per unit activity, and _c\>_0 is the ATP consumption rate, with \(\gamma(1)=1\). With _x=y_-1 and _u=c+v_, this is the general form (1) with \(f=c(\gamma-1),g=\gamma\), and _q=wx_<sup>2</sup>, where _w\>_0. With \(J=\int_0^\infty\left[w(y-1)^2+rv^2\right]dt\), we have \(g_0=\gamma(1)=1\) and \(\Delta=c^2(a-h)^2+w/r>0\), so the conditions in (8) and (9) hold and the HJB optimal controls have the following closed-form<tbc>

\(u^*(y)=\frac{c-sgn(y-1)S(y)}{\gamma(y)},S=\sqrt{f^2+\frac{w}{r}\gamma^2(y-1)^2}\)

1.5
1.5
xo = -1.5
xo = 1
xo = -1.5
xo = 1
1
1
xo = -1
xo = 1.5
xo = -1
xo = 1.5
xo = -0.5
optimal
xo = -0.5
optimal
0.5
xo = 0.5
0.5
xo = 0.5
0
0
-0.5
-0.5
-1
-1
N = 1
N = 10
-1.5
-1.5
0
2
4
0
2
4
t
t

4
100
2
10-10
0
-2
N = 1
N = 7
xo = 0.5
xo = 1
N = 3
N = 9
10-20
xo = 1.5
N = 5
exact
-4
π/2
0
π/2
1
2
3
4
5
6
7
8
9
10
X
N

Fig. 2. Trajectories of the closed-loop system for Example 1 using _N_=1 (left) and _N_=10 (right) for different initial conditions.

Fig. 3. Truncated solution to the HJB compared to the exact solution represented by the dashed line, for different _N_ (left). Log-scale normalized closed-loop cost error against _N_ for different initial conditions (right).

