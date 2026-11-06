Using the definition of statistical distance,

\(\Delta\big(D_0,\frac{D_0+D_1}{2}\big)=\frac{1}{2}\sum_x\big|D_0(x)-\frac{D_0(x)+D_1(x)}{2}\big|,\)<br>
\(=\frac{1}{4}\sum_x|D_0(x)-D_1(x)|,\)<br>
\(=\frac{1}{2}\Delta(D_0,D_1),\)<br>
\(\le\frac{\epsilon}{2}.\)

Therefore,

\(\Delta(P,Q)\le\sum_{k=0}^{n-1}\frac{\epsilon}{2}=\frac{n\epsilon}{2}.\)

Notice that the hypothesis of Vafa and Vaikuntanathan \[VV25\] considered SIVP, whereas Hypothesis 2 concerns nSMP. We show that these hypotheses are tightly related. Suppose there exist constants \(\eta,c_1,c_2>0\) such that nSMP with approximation factor \(2^{(c_1n^{1/2-\eta})}\) can be solved in time \(2^{(c_2n^{1/2-\eta})}\). Then, by Theorem B.3, this implies a polynomial-time reduction to SIVP with an approximation factor<tbc>

\(\sqrt{n}\cdot 2^{(c_1n^{1/2-\eta})}=2^{(c_1n^{1/2-\eta}+logn/2)},\)

<tbc>and running time

\(\mathrm{poly}(n)\cdot 2^{(c_2n^{1/2-\eta})}\le 2^{(c_2n^{1/2-\eta}+c'_2\mathrm{log}n)}\)

for some constant \(c'_2>0\). In particular, for all sufficiently large _n_, this yields an algorithm for \(2^{2c_1n^{(1/2)-\eta}}\) approximate SIVP running in time \(2^{(2c_2n^{1/2-\eta})}\).

## D Additional Proofs for Section 6

### D.1 Proof of Claim 6.0.1

_Proof._ Both \(\mathbf{w},\mathbf{w}'\) lie in \(\{0,\pm 1\}^n\) and are non-zero, since \(\mathbf{u}_i\neq\mathbf{u}_j\) and \(\mathbf{u}_l\neq\mathbf{u}_k\).

_A counting identity._ For \(\mathbf{c}\in\mathbb{Z}_r^n\), the inner product \(\mathbf{c}\cdot\mathbf{a}^{(r)}\) is uniform on Z_<sub>r</sub>_ if some _c<sub>t</sub>_ is a unit mod _r_. Hence, in general, the map \(\mathbf{a}^{(r)}\mapsto(\mathbf{w}\cdot\mathbf{a}^{(r)},\mathbf{w}'\cdot\mathbf{a}^{(r)})\) is a group homomorphism \(\mathbb{Z}_r^n\rightarrow\mathbb{Z}_r^2\). Under the uniform distribution on \(\mathbb{Z}_r^n\), the probability that it maps to (0,0) equals 1/|Im|, and |Im|=_r_<sup>2</sup>_/N_, where

\(N:=\#\{(x,y)\in\mathbb{Z}_r^2:x\mathbf{w}+y\mathbf{w}'\equiv_r\mathbf{0}\}\)

(the image and this annihilator are dual to each other). Thus _P=N/r_<sup>2</sup>.

_Computing N._ Fix a coordinate _s_ with \(w_s=\sigma\in\{\pm 1\}\) and let \(b:=w'_s\in\{0,\pm 1\}\). The _s_-th coordinate of \(x\mathbf{w}+y\mathbf{w}'\equiv\mathbf{0}\) forces \(x\equiv-\sigma by\). Substituting this into coordinate _t_ gives \(m_ty\equiv_r0\), where

\(m_t:=w'_t-\sigma bw_t\in\{0,\pm 1,\pm 2\}\)

(up to sign, _m<sub>t</sub>_ is the \(2\times 2\) minor of rows \(\mathbf{w},\mathbf{w}'\) on columns _s,t_). Therefore \(N=\#\{y\in\mathbb{Z}_r:m_ty\equiv_r0\forall t\}=\mathrm{gcd}(g,r)\), where _g_:=gcd_<sub>t</sub>(m<sub>t</sub>,r_).

