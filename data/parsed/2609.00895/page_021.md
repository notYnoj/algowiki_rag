**Remark 3.5.** The distinctness assumption on the limits within each parity class excludes configurations in which several of the ratios _n<sub>s</sub>/N_ converge to the same limit within _E_ or within _O_. This is analogous to the trigonometric case considered in \[1\], where a multiplicity \(\alpha\) among the limiting values requires

\(f\in C^{q+\alpha-1}\)

with \(f^{(q+\alpha-1)}\) absolutely continuous.

One expects that (51) and the corresponding _L_<sub>2</sub>-error asymptotics remain valid for clustered configurations when the maximal multiplicity \(\alpha\) is counted separately within each parity class, provided

\(f\in C^{q+\alpha-1}([-1,1];\mathbb{R}^2),\)

with \(f^{(q+\alpha-1)}\) absolutely continuous, and _p,r_ are sufficiently smooth for the asymptotic expansions in (9) to be continued to the required order in 1_/n_.

We do not prove this extension here. As in \[1, Theorem 3.3\], further integrations by parts extending (14) would introduce the additional reduced boundary values

\(g_{q+1}^\pm,\dots,g_{q+\alpha-1}^\pm,\)

which would enter the interpolation equations through higher powers of _x<sub>n<sub>s</sub></sub>_.

## 4 Asymptotic _L_<sub>2</sub> error estimates

As in (15), define<tbc>

\(\widetilde{S}_{q,N}(f):=\widetilde{P}(x)+\sum_{|n|\le N}\widetilde{F}_nv_n(x),\)

<tbc>where<tbc>

\(\widetilde{P}(x):=\sum_{k=0}^{q-1}[G_k(x,1,0)\widetilde{f}_k(1)-G_k(x,-1,0)\widetilde{f}_k(-1)].\)

<tbc>For the reduced boundary values \(\widetilde{g}_k^\pm\) obtained from (28), we choose<tbc>

\(\widetilde{f}_k(\pm 1):=\widetilde{g}_k^\pm\left(\begin{array}{ c }
cos\gamma_\pm \\
-sin\gamma_\pm
\end{array}\right),\gamma_+=\beta,\gamma_-=\alpha,\)

<tbc>so that, consistently with (8),<tbc>

\(\left(cos\gamma_\pm-sin\gamma_\pm\right)\widetilde{f}_k(\pm 1)=\widetilde{g}_k^\pm.\)

<tbc>We then set<tbc>

\(\widetilde{P}_n:=\langle\widetilde{P},v_n\rangle_{L_2},\widetilde{F}_n:=c_n-\widetilde{P}_n.\)

<tbc>The _KEG-D error_ is defined by

\(\widetilde{R}_{q,N}(f):=f-\widetilde{S}_{q,N}(f).\)

### 4.1 Main theorem

**Theorem 4.1.** _Under the hypotheses of Theorem 3.4 (in particular, the strict parity balance q<sub>e</sub>=q<sub>o</sub>=q),_

\(lim_{N\rightarrow\infty} N^{2q+1}\|\widetilde{R}_{q,N}(f)\|^2=\frac{2^{2q}}{\pi^{2q+2}}[(A+B)^2J_E+(A-B)^2J_O],\) (52)

_where A,B are the Dirac jump constants_ (17) _and_<tbc>

\(J_E:=\int_{-1}^1\prod_{s\in E}\big(x-\frac{1}{c_s}\big)^2dx,J_O:=\int_{-1}^1\prod_{s\in O}\big(x-\frac{1}{c_s}\big)^2dx.\)

