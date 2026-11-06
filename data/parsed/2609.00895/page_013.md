## 3.3 Parity classification and kernel basis

By (9),

\(\kappa_n^{(+)}=(-1)^nK_0+O\left(\frac{1}{n}\right),-\kappa_n^{(-)}=-K_0+O\left(\frac{1}{n}\right),\) (34)

where \(K_0=1/\sqrt{2}\). We partition the selected indices according to parity:<tbc>

\(E:=\{s\in[2q]:n_s\text{is even}\},O:=\{s\in[2q]:n_s\text{is odd}\},\)

<tbc>and set<tbc>

\(q_e:=|E|,q_o:=|O|,q_e+q_o=2q.\)

<tbc>We now examine the leading-order structure of the KEG-D coefficient matrix \(\Lambda_N\). In view of (34), define

\(\Lambda_0:=K_0\left(\begin{array}{ c c c c c c c c }
(-1)^{n_1} & (-1)^{n_1}x_{n_1} & \cdots & (-1)^{n_1}x_{n_1}^{q-1} & -1 & -x_{n_1} & \cdots & -x_{n_1}^{q-1} \\
\vdots & \vdots &  & \vdots &  & \vdots &  & \vdots \\
(-1)^{n_{2q}} & (-1)^{n_{2q}}x_{n_{2q}} & \cdots & (-1)^{n_{2q}}x_{n_{2q}}^{q-1} & -1 & -x_{n_{2q}} & \cdots & -x_{n_{2q}}^{q-1}
\end{array}\right).\)

Thus, \(\Lambda_0\) is obtained from \(\Lambda_N\) by replacing \(\kappa_{n_s}^{(+)}\) and \(-\kappa_{n_s}^{(-)}\) by their leading terms

\((-1)^{n_s}K_0\text{and}-K_0,\)

respectively. The notation \(\Lambda_0\) refers to this leading-order replacement; the matrix still depends on _N_ through the nodes _x<sub>n<sub>s</sub></sub>_.

We determine which parity distribution makes \(\Lambda_0\) non-singular. For each exponent _j_=0_,...,q_-1, consider the corresponding pair of columns

\(K_0\big((-1)^{n_s}x_{n_s}^j\big)_{s=1}^{2q},-K_0\big(x_{n_s}^j\big)_{s=1}^{2q},\)

and replace them by their sum and difference. The determinant of each such two-column transformation is -2, so the rank is unchanged.

For the sum, the _s_-th component is<tbc>

\(K_0\big((-1)^{n_s}-1\big)x_{n_s}^j=\left\{\begin{array}{ c c }
0, & s\in E, \\
-2K_0x_{n_s}^j, & s\in O,
\end{array}\right.\)

<tbc>whereas for the difference it is<tbc>

\(K_0\big((-1)^{n_s}+1\big)x_{n_s}^j=\left\{\begin{array}{ c c }
2K_0x_{n_s}^j, & s\in E, \\
0, & s\in O.
\end{array}\right.\)

<tbc>Hence, after a permutation of rows and columns, the transformed matrix has the block-diagonal form

\(\left(\begin{array}{ c c }
-2K_0V_O & 0 \\
0 & 2K_0V_E
\end{array}\right),\)

where _V<sub>O</sub>_ is the \(q_o\times q\) Vandermonde matrix on the nodes _x<sub>n<sub>s</sub></sub>_, \(s\in O\), and _V<sub>E</sub>_ is the \(q_e\times q\) Vandermonde matrix on the nodes _x<sub>n<sub>s</sub></sub>_, \(s\in E\).

For \(\Lambda_0\) to have full rank 2_q_, both _V<sub>O</sub>_ and _V<sub>E</sub>_ must have rank _q_. Hence necessarily<tbc>

\(q_o\ge q,q_e\ge q.\)

<tbc>Since<tbc>

\(q_e+q_o=2q,\)

