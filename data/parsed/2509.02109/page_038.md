<tbc>In particular, any local optimum of E<sub>2</sub> in \(\mathcal{D}:=\{(x_1,x_2,\alpha)\in\mathbb{R}^d\times\mathbb{R}^d\times(0,1):x_1\neq x_2\}\) must be a local optimum of E<sup>-</sup> or E<sup>+</sup>. Straightforward computation yields the following symmetrical expression:<tbc>

\(\forall x_1,x_2\in\mathbb{R}^d,\forall\alpha\in(0,1),\forall t\in\mathbb{R},\mathcal{F}(x_1,x_2,\alpha,t)=\mathcal{F}(x_2,x_1,1-\alpha,1-\gamma-t),\)

<tbc>which can be understood as exchanging the roles of _x_<sub>1</sub> and _x_<sub>2</sub>. For any \(\alpha\in(0,1)\), we have \(1-\gamma-t_-(\alpha)=t_+(\alpha)\), concluding a symmetrical relationship between E<sup>-</sup> and E<sup>+</sup>:<tbc>

\(\forall x_1,x_2\in\mathbb{R}^d,\forall\alpha\in(0,1),\mathcal{E}^+(x_2,x_1,1-\alpha)=\mathcal{E}^-(x_1,x_2,\alpha).\) (78)

<tbc>As a consequence, any local optimum \((x_1,x_2,\alpha)\in\mathcal{D}\) of E<sup>+</sup> is such that \((x_2,x_1,1-\alpha)\) is a local optimum of E<sup>-</sup>, and conversely. To determine the local minima of E<sub>2</sub> in D, we can focus on the local minima of E<sup>-</sup> in D. We split D intro three sub-regions wherein E<sup>-</sup> has an explicit expression: consider<tbc>

\(\mathcal{R}_<:=\{0<\alpha<\gamma\}\cap\mathcal{D},\mathcal{R}_=:=\{\alpha=\gamma\}\cap\mathcal{D},\mathcal{R}_>:=\{\gamma<\alpha<1\}\cap\mathcal{D},\)

<tbc>we have the following expressions for E<sup>-</sup> at \((x_1,x_2,\alpha)\in\mathcal{D}\):<tbc>

\(\mathcal{E}^-(x_1,x_2,\alpha)=\left\{\begin{array}{ c c }
\alpha c(x_1,y_1)+(\gamma-\alpha)c(x_2,y_1)+(1-\gamma)c(x_2,y_2) & \text{if}(x_1,x_2,\alpha)\in\mathcal{R}_<\cup\mathcal{R}_= \\
\gamma c(x_1,y_1)+(\alpha-\gamma)c(x_1,y_2)+(1-\alpha)c(x_2,y_2) & \text{if}(x_1,x_2,\alpha)\in\mathcal{R}_=\cup\mathcal{R}_>
\end{array}\right..\) (79)

<tbc>**No local minimum in** R_<sub>\<</sub>_**.** For \((x_1,x_2,\alpha)\in\mathcal{R}_<\), consider<tbc>

\(\mathcal{E}_<^-(x_1,x_2,\alpha):=\alpha c(x_1,y_1)+(\gamma-\alpha)c(x_2,y_1)+(1-\gamma)c(x_2,y_2).\)

<tbc>A local optimum \((x_1,x_2,\alpha)\in\mathcal{R}_<\) of E<sup>-</sup> must satisfy the stationarity conditions:

\(0=\frac{\partial\mathcal{E}_<^-}{\partial x_1}=\alpha\nabla\phi(x_1-y_1)\Longrightarrow_{(\mathrm{H}3)}x_1=y_1,\)<br>
\(0=\frac{\partial\mathcal{E}_<^-}{\partial\alpha}=\underbrace{c(x_1,y_1)}_{=0\text{by}(\mathrm{H}2)}-c(x_2,y_1)\Longrightarrow_{(\mathrm{H}2)}x_2=y_1.\)<br>
\(0=\frac{\partial\mathcal{E}_<^-}{\partial x_2}=(\gamma-\alpha)\underbrace{\nabla\phi(x_2-y_1)}_{=0\text{by}(\mathrm{H}2)}+(1-\gamma)\nabla\phi(\underbrace{x_2}_{=y_1}-y_2)=(1-\gamma)\nabla\phi(y_1-y_2).\)

By (H3), since \(y_1\neq y_2\), we have \(\nabla c(y_1,y_2)\neq 0\), hence E<sub>-</sub> has no local minimum in R_<sub>\<</sub>_.

**No local minimum in** R_<sub>\<</sub>_**.** For \((x_1,x_2,\alpha)\in\mathcal{R}_>\), consider<tbc>

\(\mathcal{E}_>^-(x_1,x_2,\alpha):=\gamma c(x_1,y_1)+(\alpha-\gamma)c(x_1,y_2)+(1-\alpha)c(x_2,y_2).\)

<tbc>Likewise, a local minimum \((x_1,x_2,\alpha)\in\mathcal{R}_>\) of E<sup>-</sup> must verify:

\(0=\frac{\partial\mathcal{E}_>^-}{\partial x_1}=(1-\alpha)\nabla\phi(x_2-y_2)\Longrightarrow_{(\mathrm{H}3)}x_2=y_2,\)<br>
\(0=\frac{\partial\mathcal{E}_>^-}{\partial\alpha}=c(x_1,y_2)-\underbrace{c(x_2,y_2)}_{=0\text{by}(\mathrm{H}2)}\Longrightarrow_{(\mathrm{H}2)}x_1=y_2.\)<br>
\(0=\frac{\partial\mathcal{E}_>^-}{\partial x_2}=\gamma\nabla\phi(\underbrace{x_1}_{=y_2}-y_1)+(\alpha-\gamma)\underbrace{\nabla\phi(x_2-y_2)}_{=0\text{by}(\mathrm{H}2)}=\gamma\nabla\phi(y_2-y_1)\neq 0.\)

As before, this system cannot hold, and thus E<sub>-</sub> has no local minimum in R_<sub>\<</sub>_.

