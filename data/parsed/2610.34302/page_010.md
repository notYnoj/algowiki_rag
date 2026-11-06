_Proof of claim._ Suppose that two distinct centers \(p,p'\in A_i(s)\) at level _i_ are both mapped to the same edge \((s,x)\in E_s^\star\). By triangle inequality,<tbc>

\(\mathsf{d}(p,p')\le\mathsf{d}(p,x)+\mathsf{d}(x,p')<\frac{\mathsf{d}(s,p)}{\beta}+\frac{\mathsf{d}(s,p')}{\beta}.\)

<tbc>Since \(p,p'\in A_i(s)\),<tbc>

\(\mathsf{d}(s,p),\mathsf{d}(s,p')\le r_{i+1}+\frac{r_i}{\alpha+2},\)

<tbc>and therefore<tbc>

\(\mathsf{d}(p,p')<\frac{2\left((1+\delta)+\frac{1}{\alpha+2}\right)r_i}{\beta}.\)

<tbc>On the other hand, the centers returned by Algorithm 2.1 at level _i_ are separated by distance more than \(r_i/(\alpha+2)\). Hence<tbc>

\(\frac{r_i}{\alpha+2}<\mathsf{d}(p,p')<\frac{2\left((1+\delta)+\frac{1}{\alpha+2}\right)r_i}{\beta},\)

<tbc>which implies

\(\beta<2(1+\delta)(\alpha+2)+2.\)

This contradicts the definition of \(\beta\).

**Claim 2.5.** _For every edge_ \((s,x)\in E_s^\star\)_, there are at most_ 5 _indices i for which some p with_ \((s,p)\in E_s^i\) _satisfies_ \(\phi_s(i,p)=(s,x)\).

_Proof of claim._ Suppose that \(p\in A_i(s)\) is a level-_i_ center and \(\phi_s(i,p)=(s,x)\). By definition of \(\phi_s\),<tbc>

\(\mathsf{d}(p,x)<\frac{\mathsf{d}(s,p)}{\beta}.\)

<tbc>Using \(p\in A_i(s)\) and triangle inequality,<tbc>

\(\mathsf{d}(s,x)<\left(1+\frac{1}{\beta}\right)\left(r_{i+1}+\frac{r_i}{\alpha+2}\right),\)

<tbc>and<tbc>

\(\mathsf{d}(s,x)>\left(1-\frac{1}{\beta}\right)\left(r_i-\frac{r_i}{\alpha+2}\right)=r_i\cdot\frac{\alpha+1}{\alpha+2}\left(1-\frac{1}{\beta}\right).\)

<tbc>Thus, for a fixed edge (_s,x_), the relevant values of _r<sub>i</sub>_ lie in an interval whose ratio is at most

\(R_\beta=\frac{\left((1+\delta)+\frac{1}{\alpha+2}\right)\left(1+\frac{1}{\beta}\right)}{\frac{\alpha+1}{\alpha+2}\left(1-\frac{1}{\beta}\right)}\)<br>
\(=\frac{\alpha^2+4\alpha+2}{\alpha(\alpha+1)}\cdot\frac{2\alpha+9+\frac{4}{\alpha}}{2\alpha+7+\frac{4}{\alpha}}\)<br>
\(\le\left(1+\frac{1}{\alpha}\right)^3\cdot\left(1+\frac{1}{\alpha}\right)\le\left(1+\frac{1}{\alpha}\right)^4.\)

Since consecutive values of _r<sub>i</sub>_ differ by a factor of \(1+1/\alpha\), there are at most \(1+\mathrm{log}_{1+1/\alpha} R_\beta\le 5\) such levels.

