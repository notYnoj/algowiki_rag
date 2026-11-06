**Lemma 4.11.** _Let_ \(a\ge 1\) _be an integer, and let_ \(g,h:\mathbb{Z}_{\ge 1}\rightarrow\mathbb{R}_{>0}\) _be concave functions such that_ \(2g(m)+h(m)\le g(3m+a-1)\) _and_ \(2h(m)+g(m)\le h(3m+a-1)\) _for every integer_ \(m\ge 1\)_. Then for every integer_ \(b\ge 1\),<tbc>

\(\frac{g(b+1)}{g(b)}\frac{h(b+1)}{h(b)}\ge\big(\frac{2b+a+1}{2b+a-1}\big)^2.\)

<tbc>_Proof._ Let _D_=2_b+a_-1 and _S=g(b_)+_h(b_). Since _g_ is concave, its differences _g(k_+1)-_g(k_) do not increase with _k_. So _g(b_+1)-_g(b_) is at least the average of the _D_ differences _g(j_+1)-_g(j_) with \(b\le j<3b+a-1\), and the first hypothesis with _m=b_ gives<tbc>

\(g(b+1)-g(b)\ge\frac{g(3b+a-1)-g(b)}{D}\ge\frac{S}{D}.\)

<tbc>Likewise, the second hypothesis gives \(h(b+1)-h(b)\ge S/D\). Since \(S^2\ge 4g(b)h(b)\), we find<tbc>

\(g(b+1)h(b+1)\ge\big(g(b)+\frac{S}{D}\big)\big(h(b)+\frac{S}{D}\big)=g(b)h(b)+\frac{S^2}{D}+\frac{S^2}{D^2}\ge g(b)h(b)\big(1+\frac{2}{D}\big)^2.\)

<tbc>**Proposition 4.12.** _Let_ \(\phi\in\Delta_\mathbb{F}\)_, and let_ \(\tau:=log\phi(\langle 2,2,2\rangle)\)_. Then for every integer_ \(n\ge 1\),<tbc>

\(\prod_{\pi\in\mathfrak{S}_3}\phi(\pi\cdot\mathsf{P}_{n,n})\ge\big(\frac{3n-1}{2}\prod_{k=1}^{n-1}\frac{3k+1}{3k}\big)^{2\tau}\ge n^{8\tau/3}.\)

<tbc>_Proof._ Let _p_<sub>1</sub>, _p_<sub>2</sub> and _p_<sub>3</sub> be the logarithms of \(\phi(\langle 1,1,2\rangle)\), \(\phi(\langle 2,1,1\rangle)\) and \(\phi(\langle 1,2,1\rangle)\), so that \(\tau=p_1+p_2+p_3\) (Lemma 4.3(iv)). For every integer \(n\ge 1\), let \(G_n:=\prod_{\pi\in\mathfrak{S}_3}\phi_\pi(n,n)\), the left-hand side of the claim. Since \(\phi_\pi(1,1)=1\) (Lemma 4.10(i) for \(\phi_\pi\)), we have _G_<sub>1</sub>=1. Now fix an integer \(n\ge 1\), and let \(\pi\in\mathfrak{S}_3\). Using that \(\phi_\pi(n+1,n)=\phi_{\pi\circ(12)}(n,n+1)\) and \(\phi_\pi(n,n)=\phi_{\pi\circ(12)}(n,n)\), since \(\phi_\pi(a,b)=\phi_{\pi\circ(12)}(b,a)\), we obtain<tbc>

\(\frac{\phi_\pi(n+1,n+1)}{\phi_\pi(n,n)}=\frac{\phi_\pi(n+1,n+1)}{\phi_\pi(n+1,n)}\cdot\frac{\phi_{\pi\circ(12)}(n,n+1)}{\phi_{\pi\circ(12)}(n,n)}.\)

<tbc>We multiply over \(\pi\in\mathfrak{S}_3\). Since \(\pi\mapsto\pi\circ(12)\) is a bijection of S<sub>3</sub>, this gives<tbc>

\(\frac{G_{n+1}}{G_n}=\prod_{a\in\{n,n+1\}}\prod_{\sigma\in\mathfrak{S}_3}\frac{\phi_\sigma(a,n+1)}{\phi_\sigma(a,n)}.\)

<tbc>The six permutations form three pairs \(\{\sigma,\sigma\circ(23)\}\), one for each \(i\in\{1,2,3\}\), with \(\sigma(1)=i\). Let \(a\in\{n,n+1\}\). If _p<sub>i</sub>\>_0, then by Lemma 4.10, applied to \(\phi_\sigma\) and \(\phi_{\sigma\circ(23)}\), the functions \(m\mapsto\phi_\sigma(a,m)^{1/p_i}\) and \(m\mapsto\phi_{\sigma\circ(23)}(a,m)^{1/p_i}\) satisfy the hypotheses of Lemma 4.11. Here we use that both spectral points take the value 2_<sup>p<sub>i</sub></sup>_ at \(\langle 1,1,2\rangle\), since \(\sigma\) and \(\sigma\circ(23)\) move its one- dimensional first leg to leg _i_, and that \(\phi_\sigma((23)\cdot T)=\phi_{\sigma\circ(23)}(T)\) and \(\phi_{\sigma\circ(23)}((23)\cdot T)=\phi_\sigma(T)\) for every tensor _T_, since \(\pi\cdot(\rho\cdot T)=(\pi\circ\rho)\cdot T\) for all \(\pi,\rho\in\mathfrak{S}_3\). That lemma with _b=n_, raised to the power _p<sub>i</sub>_, gives<tbc>

\(\frac{\phi_\sigma(a,n+1)}{\phi_\sigma(a,n)}\cdot\frac{\phi_{\sigma\circ(23)}(a,n+1)}{\phi_{\sigma\circ(23)}(a,n)}\ge\big(\frac{2n+a+1}{2n+a-1}\big)^{2p_i}.\)

<tbc>If _p<sub>i</sub>_=0, this holds as well, since the left-hand side is at least 1: \(\phi_\sigma\) and \(\phi_{\sigma\circ(23)}\) are nondecreasing in the second argument (Lemma 4.10(i)). Multiplying over the three pairs and the two values of _a_ gives<tbc>

\(\frac{G_{n+1}}{G_n}\ge\big(\frac{(3n+1)(3n+2)}{(3n-1)3n}\big)^{2\tau},\text{so}G_n\ge\big(\prod_{k=1}^{n-1}\frac{(3k+1)(3k+2)}{(3k-1)3k}\big)^{2\tau},\)

