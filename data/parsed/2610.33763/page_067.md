Hence, solution of the second-ISP can be written as

\(u(x,y,t)=\sum_{j=1}^\infty\sum_{k=1}^\infty\left(\psi_{j,k}\mathbf{W}_{j,k}(t)+w(t)f_{j,k}(t)*\mathbf{V}_{j,k}(t)\right)X_{j,k}(x,y),\) (5.55)

where _w(t_) remains to be determined. Next, we examine some specific cases of Eq. (5.54) based on the memory kernel \(\varrho(t)\).

**Solution of second-ISP for** _n_**-Tempered FDE:** From Eq. (5.32), we derive the following expression for _U<sub>j,k</sub>(t_) in the second-ISP for the _n_-tempered FDE (5.9)

\(U_{j,k}(t)=\frac{1}{P_1}\psi_{j,k}e^{-pt}E_{\bar{\beta},1}(\cdots\lambda\mathbf{t}\cdots)+\frac{w(t)}{P_1}f_{j,k}(t)*e^{-pt}t^{\beta_1-1}E_{\bar{\beta},\beta_1}(\cdots\lambda\mathbf{t}\cdots).\) (5.56)

• For _p_=0, the equation above matches the expression of _U<sub>j,k</sub>(t_) in second-ISP for solving the multi-term FDE (5.10).<tbc>

• When _p_=0, _P_<sub>1</sub>=1, and \(P_2=P_3=\cdots=P_n=0\), Eq. (5.56) simplifies to the expression of _U<sub>j,k</sub>(t_) in second-ISP for the solution of a mono-FDE.<tbc>

• The expression of _U<sub>j,k</sub>(t_) in second-ISP for the SDE (5.12) can be derived by setting \(\beta_1=1\), _p_=0, _P_<sub>1</sub>=1, and \(P_2=P_3=\cdots=P_n=0\) in Eq. (5.56).

## 5.4.2 The main results of second-ISP

The following section presents a theorem that establishes the conditions necessary for problem second-ISP to have a regular solution.

\(\bullet\) **Existence of second-ISP**

**Theorem 5.3** _Assume the following:_

(_a)_ \(\psi(x,y)\in C^4([0,1]\times[0,1])\) _satisfies conditions (5.20)._<tbc>

(_b)_ \(f(x,y,t)\in C^{0,2,2}(\bar{\Omega})\) _meets the conditions_<tbc>

\(f(x,0,t)=0,\frac{\partial}{\partial y}f(x,1,t)=0,\frac{\partial}{\partial x}f(0,y,t)=0,\)<br>
\(\frac{\partial}{\partial x}f(1,y,t)-d\left(\frac{\partial^2}{\partial x^2}f(1,y,t)+\frac{\partial^2}{\partial y^2}f(1,y,t)\right)=0.\)

_Additionally, if_<tbc>

<tbc>\(\left(\int_0^1\int_0^1f(x,y,t)dxdy\right)^{-1}\le Q_0,\)<tbc>

<tbc>_for some constant Q_<sub>0</sub>_\>_0.<tbc>

(_c)_ \(\mathcal{E}(t)\in AC([0,T])\)_, and satisfies the consistency condition, i.e.,_<tbc>

<tbc>\(\int_0^1\int_0^1\psi(x,y)dxdy=\mathcal{E}(0),\)<tbc>

<tbc>_then a regular solution for second-ISP exists._<tbc>

