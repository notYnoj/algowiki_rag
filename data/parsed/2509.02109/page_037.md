<tbc>To prove local minimality, we compute the Hessian of E<sub>3</sub> at \(\alpha\in[-\frac{1}{6},\frac{1}{6}]^2,\eta\in(-\frac{1}{2},\frac{1}{2})^3\) verifying \(\alpha_1+\alpha_2\le 0\):

\(H^-(\alpha,\eta)=\left(\begin{array}{ c c c c c }
0 & 0 & 2\eta_1 & 0 & -2\eta_3-2 \\
0 & 0 & 0 & 2\eta_2 & -2\eta_3-2 \\
2\eta_1 & 0 & 2\alpha_1+\frac{1}{3} & 0 & 0 \\
0 & 2\eta_2 & 0 & 2\alpha_2+\frac{1}{3} & 0 \\
-2\eta_3-2 & -2\eta_3-2 & 0 & 0 & -2\alpha_1-2\alpha_2+\frac{4}{3}
\end{array}\right).\)

The property of _H_<sup>+</sup>(0<sub>R<sup>2</sup></sub>,0<sub>R<sup>3</sup></sub>) from Eq. (73) is also satisfied by _H_<sup>-</sup>(0<sub>R<sup>2</sup></sub>,0<sub>R<sup>3</sup></sub>), and we conclude likewise that (0<sub>R<sup>2</sup></sub>,0<sub>R<sup>3</sup></sub>) is a local minimum for the problem \(\mathcal{E}_3^-\) defined in Eq. (69).

We conclude that \((\alpha,\eta)=(0_{\mathbb{R}^2},0_{\mathbb{R}^3})\) is a minimum of E<sub>3</sub> on the set \([-\frac{1}{6},\frac{1}{6}]^2\times(-\frac{1}{2},\frac{1}{2})^3\), with value \(\mathcal{E}_3(0_{\mathbb{R}^2},0_{\mathbb{R}^3})=\frac{2}{3}\varepsilon^2>0\) (use Eq. (70) for example).

## A.7.2 Discrete 2-Wasserstein Distance for _n_=2: Proof of Unique Local Minimum

### Unique Local Minimum of the Discrete 2-Wasserstein Distance for _n_=2.

We consider the minimisation of the quadratic Wasserstein cost \(\mu\longmapsto\mathrm{W}_2^2(\mu,\nu)\) when \(\mu\) is restricted to two Dirac atoms,<tbc>

\(\mu_{x,\alpha}=\alpha\delta_{x_1}+(1-\alpha)\delta_{x_2},(x,\alpha)\in\mathbb{R}^{2d}\times[0,1],\)

<tbc>against the fixed target \(\nu=\gamma\delta_{y_1}+(1-\gamma)\delta_{y_2}\) with \(\gamma\in(0,1)\) and \(y_1\neq y_2\). Denoting

\(\mathcal{E}_2(x,\alpha):=\mathrm{W}_2^2(\mu_{x,\alpha},\nu),\) (75)

we show that inside the domain \(\mathcal{D}:=\{(x,\alpha):x_1\neq x_2,\alpha\in(0,1)\}\) every local minimiser of E<sub>2</sub> is such that \(\mu_{x,\alpha}=\nu\), and is thus a global minimiser. We show this result more generally, for costs \(c(x,y):=\phi(x-y)\) where \(\phi\) is convex, C<sup>1</sup>, \(\phi(v)=0\Longleftrightarrow v=0\) and \(\nabla\phi(v)=0\Longleftrightarrow v=0\). Additionally, boundary stationary points can occur when atoms merge, i.e. \(\alpha\in\{0,1\}\) or _x_<sub>1</sub>=_x_<sub>2</sub>; they are local but not global minima. When these weights arise from EM, we can prevent such degeneracies by fixing weights or imposing a hard lower bound on them throughout the iterations.

We now determine all the local minimisers of the energy E<sub>2</sub> defined in Eq. (75) in the domain \(\mathcal{D}:=\{(x,\alpha):x_1\neq x_2,\alpha\in(0,1)\}\). Fix \(\gamma\in(0,1)\), and let _x_<sub>1</sub>, _x_<sub>2</sub>, _y_<sub>1</sub> and _y_<sub>2</sub> in R_<sup>d</sup>_, with \(y_1\neq y_2\). For \(\alpha\in(0,1)\), we consider the measures:

\(\mu(x_1,x_2,\alpha):=\alpha\delta_{x_1}+(1-\alpha)\delta_{x_2},\nu:=\gamma\delta_{y_1}+(1-\gamma)\delta_{y_2}.\)

Consider the ground cost \(c:=(x,y)\in\mathbb{R}^d\times\mathbb{R}^d\longmapsto\phi(x-y)\), with:

• (H1) \(\phi:\mathbb{R}^d\rightarrow\mathbb{R}_+\) convex and C<sup>1</sup>,<tbc>

• (H2) \(\phi(v)=0\Longleftrightarrow v=0\),<tbc>

• (H3) \(\nabla\phi(v)=0\Longleftrightarrow v=0\).

<tbc>For instance, \(\phi\) could be \(\|\cdot\|_p^p\) with _p\>_1. Every feasible coupling between \(\mu(x_1,x_2,\alpha)\) and \(\nu\) can be written under the form:<tbc>

\(\pi(\alpha,t):=\left(\begin{array}{ c c }
\alpha-t & t \\
\gamma-\alpha+t & 1-\gamma-t
\end{array}\right),t\in[t_-(\alpha),t_+(\alpha)],t_-(\alpha):=\mathrm{max}(0,\alpha-\gamma),t_+(\alpha):=\mathrm{min}(\alpha,1-\gamma).\)

<tbc>The interval \([t_-(\alpha),t_+(\alpha)]\) is non-empty for all \(\alpha\in(0,1)\), since \(\gamma\in(0,1)\). The transport cost associated to a plan \(\pi(\alpha,t)\) writes:<tbc>

\(\mathcal{F}(x,\alpha,t):=(\alpha-t)c(x_1,y_2)+(\gamma-\alpha+t)c(x_2,y_2)+tc(x_1,y_2)+(1-\gamma-t)c(x_2,y_2).\) (76)

<tbc>Since \(\mathcal{E}_2(x_1,x_2,\alpha)=\mathrm{min}_{t\in[t_-(\alpha),t_+(\alpha)]}\mathcal{F}(x_1,x_2,\alpha,t)\) and that F is linear in _t_, we obtain:<tbc>

\(\mathcal{E}_2(x_1,x_2,\alpha)=\mathrm{min}\left(\mathcal{E}^-(x_1,x_2,\alpha),\mathcal{E}^+(x_1,x_2,\alpha)\right),\mathcal{E}^-(x_1,x_2,\alpha):=\mathcal{F}(x_1,x_2,\alpha,t_-(\alpha)),\mathcal{E}^+(x_1,x_2,\alpha):=\mathcal{F}(x_1,x_2,\alpha,t_+(\alpha)).\) (77)

