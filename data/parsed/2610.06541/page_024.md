(3) _If_ \(\Lambda(s)\) _has spectral width at most_ \(5\pi/3\) _on_ \[0,1\]_, then, for every integer_ \(T\ge 1\)_, with_ \(U_\Lambda\) _the evolution of_ \(\Lambda(t/T)\),<tbc>

<tbc>\(\left\|e^{-i\Lambda((T-1)/T)}\cdots e^{-i\Lambda(0)}-e^{i\Lambda(1)/2}U_\Lambda(T)e^{-i\Lambda(0)/2}\right\|\le\frac{(4c_0\rho_1+16c_1\rho_1^2+6c_2\rho_2)a^2}{T}.\)<tbc>

<tbc>_Adding J_<sub>1</sub>_/T from (2) gives at most Ka_<sup>2</sup>_/T._<tbc>

(4) _At width_ \(5\pi/3\), \(\mathcal{B}'\le 6.6027\), \(c_0\le 0.6538\), \(c_1\le 0.3577\), \(c_2\le 0.4872\)_, and_ \(K<3.1\cdot 10^4\).

<tbc>_Proof._ Differentiating _f_ gives \(f'=\omega(1+rs)^{-3}\) and \(|f''|=3r\omega(1+rs)^{-4}\le p\). The bounds \(1\le a\le\omega=2a^2/(a+1)\le 2a\) give \(f'^2/p=\omega/[3a(1+rs)^2]\le 2/3\) for \(s\ge 0\), and \(\alpha^2=2(f-1/2)^2+1/2\ge 1/2\). Hence, \(\|\Lambda'\|\le\rho_1f'/\alpha^2\le 2\rho_1f'\) and, with \(\alpha^{-4}\le 2\alpha^{-2}\),

\(\|\Lambda''\|\le\frac{\rho_1}{\alpha^2}\left(|f''|+\left(\frac{4}{\sqrt{3}}+2+4\mathcal{B}'\right)f'^2\right)\le\frac{\rho_1p}{\alpha^2}\left(1+\frac{2}{3}\left(\frac{4}{\sqrt{3}}+2+4\mathcal{B}'\right)\right)=\frac{\rho_2p}{\alpha^2}\le 2\rho_2p\)

for \(s\in[0,1]\), where \(f'\) and _p_ decrease from \(f'(0)=\omega\le 2a\) and \(p(0)=3a\omega\le 6a^2\).

For _J_<sub>1</sub>, \(\alpha^2g^2=\beta^2(1+rs)^{-4}\), \(f'/(\alpha^2g^2)=\omega(1+rs)/\beta^2\), \(p/(\alpha^2g^2)=3a\omega/\beta^2\), and \(f'^2/(\alpha^4g^3)=\omega^2/(\beta^3\alpha)\). Integrating over \[0,1\] gives

\(J_1=\frac{\rho_1f'(0)}{\alpha(f(0))^2g(0)^2}+\frac{\rho_1f'(1)}{\alpha(f(1))^2g(1)^2}+\int_0^1\left(\frac{\rho_2p}{\alpha^2g^2}+\frac{7\rho_1^2f'^2}{\alpha^4g^3}\right)ds\)<br>
\(=\frac{\rho_1\omega(2+r)+3\rho_2a\omega}{\beta^2}+\frac{7\rho_1^2\omega^2}{\beta^3}\int_0^1\frac{ds}{\alpha}\)<br>
\(\le\left(\frac{4\rho_1+6\rho_2}{\beta^2}+\frac{28\sqrt{2}\rho_1^2}{\beta^3}\right)a^2,\)

where the inequality uses \(\omega\le 2a\), \(2+r\le 2a\), and \(1/\alpha\le\sqrt{2}\). Substituting the bounds \(4\rho_1a\) on \(\|\Lambda'\|\) and \(6\rho_2a^2\) on \(\|\Lambda''\|/2\) into Theorem 6.4 and using \(a\le a^2\) gives (3).

Finally, \(\sum_{k\ge 1}|B_{2k}|w^{2k}/(2k)!=1-\frac{w}{2}cot\frac{w}{2}\) gives the closed form \(\mathcal{B}(w)=2+\frac{w}{2}-\frac{w}{2}cot\frac{w}{2}\) , while \(\mathcal{N}(w)=(1-\frac{w}{2}cot\frac{w}{2})/w^2\) by definition. Put \(\mathcal{C}(w)=\frac{1}{2}+w\mathcal{N}(w)=(\mathcal{B}(w)-1)/w\), so that \(\mathcal{C}'=\mathcal{N}+w\mathcal{N}'\). At \(w=5\pi/3\), where \(cot\frac{w}{2}=-\sqrt{3}\) and \(sin^2\frac{w}{2}=\frac{1}{4}\), evaluation and differentiation give

\(\mathcal{B}'=\frac{1}{2}+\frac{\sqrt{3}}{2}+\frac{5\pi}{3},\mathcal{C}=\frac{1}{2}+\frac{\sqrt{3}}{2}+\frac{3}{5\pi},\mathcal{C}'=1-\frac{9}{25\pi^2}.\)

The bounds \(3.14159<\pi<3.14160\) and \(1.73205<\sqrt{3}<1.73206\) give \(\mathcal{B}'\le 6.6027\), \(1.55\le\mathcal{C}\le 1.55702\), and \(\mathcal{C}'\le 0.96353\). Substituting these into N=(C-1/2)_/w_ and \(\mathcal{N}'=(\mathcal{C}'-\mathcal{N})/w\) gives \(0.2005\le\mathcal{N}\le 0.2019\) and \(\mathcal{N}'\le 0.1458\), and substitution into _c_<sub>0</sub>=1/4+2N, \(c_1=1/64+\mathcal{N}/4+2\mathcal{N}'\), and _c_<sub>2</sub>=1/12+2N gives the three bounds. The definitions, these bounds, and \(1.41421<\sqrt{2}<1.41422\) give \(\rho_1\le 5.236\), \(\rho_2\le 112.5\), and \(\beta\ge 0.35355\). Each term of _K_ increases with its nonnegative numerator factors and decreases with \(\beta\), so

\(K\le\frac{4\cdot 5.236+6\cdot 112.5}{0.35355^2}+\frac{28\cdot 1.4143\cdot 5.236^2}{0.35355^3}+4\cdot 0.6538\cdot 5.236+16\cdot 0.3577\cdot 5.236^2+6\cdot 0.4872\cdot 112.5<3.1\cdot 10^4.\)

□

### A.4. Outlook.

The encoding affects the constant _K_ chiefly through the quadratic term \(28\sqrt{2}\rho_1^2/\beta^3\) of _J_<sub>1</sub>. A wider free arc lowers the inverse bound (_w/_2)/sin(_w/_2) defining \(\rho_1\), and retaining more of the gap under compression lowers \(1/\beta^3\), both matters of the encoding rather than of the comparison.

I intend to extend this construction to further examples.

## References

