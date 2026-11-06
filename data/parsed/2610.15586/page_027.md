synthesis of a register unitary costs exponentially in the register size. Separability alone therefore does not give an efficient algorithm asymptotically.

For the lens, the source is generally not exactly rank two. A Schmidt truncation with retained rank _r<sub>b</sub>_ has relative amplitude tail \(\unknown_b=\big(\sum_{j>r_b}s_j^2/\sum_js_j^2\big)^{1/2}\), where _s<sub>j</sub>_ are its singular values. A truncated preparation must report this tail and its effect on the sampling law. The pilot uses exact state preparation and exact DST-I register unitaries. Resource estimates that assume a power-of-two QFT or a rank-two source do not apply to it.

A compiled resource table should state the software versions, synthesis seed, time schedule, Trotter refinement, gate set, number of active qubits, and whether the counts are logical or native to the backend. We do not report lens gate counts here, because they require a construction consistent with this grid and preparation, and we make no claim of hardware feasibility.

### B.5 IonQ outcome laws

Figure 5 shows the circuit laws and the measured IonQ frequencies for the six six-qubit circuits of Sec. 6.

## C Proof of Lemma 9

By writing \(|b\rangle=\sum_\lambda P_\lambda|b\rangle\), we obtain \(\langle z|_Fe^{-i\lambda k\Delta t}|b\rangle=\sum_\lambda a_\lambda(z)e^{-i\lambda k\Delta t}\). Hence

\(q(z)=\frac{1}{d}\sum_{k=0}^{d-1}\big|\sum_\lambda a_\lambda(z)e^{-i\lambda k\Delta t}\big|^2=\sum_{\lambda,\mu} a_\lambda(z)\overline{a_\mu(z)}D_d\big((\lambda-\mu)\Delta t\big).\) (37)

The terms with \(\lambda=\mu\) give \(q^\infty(z)\), since _D<sub>d</sub>_(0)=1. The remaining terms give Eq. (17). The geometric sum gives \(|D_d(\theta)|=|sin(d\theta/2)|/(d|sin(\theta/2)|)\le 1/(d|sin(\theta/2)|)\), and \(|D_d|\le 1\) holds trivially.

## D Discretization of the duct examples

For the elliptic duct we use the cell centers \(\mu_i=(i+\frac{1}{2})\Delta\mu\) and \(\nu_j=(j+\frac{1}{2})\Delta\nu\) with \(\Delta\mu=\mu_0/N\) and \(\Delta\nu=\pi/(2N)\). The Neumann condition at \(\mu=0\) is imposed by the mirror ghost value _w_<sub>-1</sub>=_w_<sub>0</sub>, and the Dirichlet condition at \(\mu_0\) by the antisymmetric ghost value _w<sub>N</sub>_=-_w_<sub>_N_-1</sub>. The resulting tridiagonal matrix<tbc>

Ellipse, k = 0 (38 2Q, p = 0.38)
Ellipse, k = 1 (39 2Q, p = 0.28)
Ellipse, k = 2 (39 2Q, p = 0.23)
0.5
circuit law
0.3
0.25
IonQ Forte-1
0.4
0.20
0.3
0.2
0.15
0.2
0.1
0.10
probability
0.1
0.05
0.0
0.0
0.00
Lens, k = 0 (78 2Q, p = 0.41)
Lens, k = 1 (194 2Q, p = 0.64)
Lens, k = 2 (315 2Q, p = 0.88)
0.5
0.5
0.20
0.4
0.4
0.15
0.3
0.3
0.2
0.10
0.2
probability
0.1
0.05
0.1
0.0
0.00
0.0
0
10
20
30
40
50
60
0
10
20
30
40
50
60
0
10
20
30
40
50
60
mode index k1N + k2
mode index k1N + k2
mode index k1N + k2

**Figure 5:** Circuit laws (gray) and measured frequencies on IonQ Forte-1 (blue, 500 shots) for the six circuits. The titles give the number of two-qubit gates and the fitted replacement probability _p_. For the lens, the shaded indices lie outside the odd-odd sector and are removed by the parity filter.

