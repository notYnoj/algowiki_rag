**Claim 2.8.** _If an edge_ \((s,x)\in E^\star\) _is a_ \(\beta'\)_-navigation from s to a point_ \(v\in\mathcal{U}_{i,s}\)_, then_ \(v\in B(x,\rho_i)\).

_Proof of claim._ Since \(v\in\mathcal{U}_{i,s}\), there exists a pair \((C,p)\in\mathcal{G}_i\) such that \(v\in C\) and \(p\in A_i(s)\). Hence \(\mathsf{d}(p,v)\le\rho_i\). By triangle inequality,<tbc>

\(\mathsf{d}(s,v)\le\mathsf{d}(s,p)+\mathsf{d}(p,v)\le r_{i+1}+2\rho_i=r_i\left(1+\delta+\frac{2}{\alpha+2}\right).\)

<tbc>If (_s,x_) is a \(\beta'\)-navigation from _s_ to _v_, then

\(\mathsf{d}(x,v)<\frac{\mathsf{d}(s,v)}{\beta'}\le\frac{r_i\left(1+\delta+\frac{2}{\alpha+2}\right)}{(1+\delta)(\alpha+2)+2}=\frac{r_i}{\alpha+2}=\rho_i.\)

Thus \(v\in B(x,\rho_i)\).

For each level _i_, define<tbc>

\(E_{s,i}^\star=\left\{(s,x)\in E_s^\star\middle|\exists v\in\mathcal{U}_{i,s}\text{such that}\mathsf{d}(x,v)<\frac{\mathsf{d}(s,v)}{\beta'}\right\}.\)

<tbc>By the \(\beta'\)-navigability of _G<sup>⋆</sup>_ and Claim 2.8, the balls \(\{B(x,\rho_i)\cap\mathcal{U}_{i,s}|(s,x)\in E_{s,i}^\star\}\) cover U_<sub>i,s</sub>_. Therefore,<tbc>

\(\mathsf{OPT}_{i,s}\le|E_{s,i}^\star|.\)

<tbc>It remains to show that each edge of \(E_s^\star\) belongs to only constantly many sets \(E_{s,i}^\star\). Suppose \((s,x)\in E_{s,i}^\star\). Then there exists \(v\in\mathcal{U}_{i,s}\) such that \(\mathsf{d}(x,v)<\mathsf{d}(s,v)/\beta'\). Choose a pair \((C,p)\in\mathcal{G}_i\) with \(v\in C\) and \(p\in A_i(s)\). Since \(\mathsf{d}(p,v)\le\rho_i\),<tbc>

\(\mathsf{d}(s,v)\le r_{i+1}+2\rho_i=r_i\left(1+\delta+\frac{2}{\alpha+2}\right),\)

<tbc>and<tbc>

\(\mathsf{d}(s,v)>r_i-2\rho_i=r_i\left(1-\frac{2}{\alpha+2}\right).\)

<tbc>Consequently,<tbc>

\(r_i\left(1-\frac{2}{\alpha+2}\right)\left(1-\frac{1}{\beta'}\right)<\mathsf{d}(s,x)<r_i\left(1+\delta+\frac{2}{\alpha+2}\right)\left(1+\frac{1}{\beta'}\right).\)

<tbc>Thus, for a fixed edge (_s,x_), the relevant values of _r<sub>i</sub>_ lie in an interval whose ratio is at most

\(R_{\beta^\prime}=\frac{\left(1+\delta+\frac{2}{\alpha+2}\right)\left(1+\frac{1}{\beta'}\right)}{\left(1-\frac{2}{\alpha+2}\right)\left(1-\frac{1}{\beta'}\right)}\)<br>
\(=\frac{\alpha^2+5\alpha+2}{\alpha^2}\cdot\frac{\alpha+6+\frac{2}{\alpha}}{\alpha+4+\frac{2}{\alpha}}\)<br>
\(\le\left(1+\frac{1}{\alpha}\right)^5\cdot\left(1+\frac{1}{\alpha}\right)^2=\left(1+\frac{1}{\alpha}\right)^7.\)

