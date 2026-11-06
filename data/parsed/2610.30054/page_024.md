_Proof._ Let \(\phi\in\Delta_\mathbb{F}\), and let _p_<sub>1</sub>, _p_<sub>2</sub> and _p_<sub>3</sub> be the logarithms of \(\phi(\langle 1,1,2\rangle)\), \(\phi(\langle 2,1,1\rangle)\) and \(\phi(\langle 1,2,1\rangle)\). Let \(\pi\in\mathfrak{S}_3\), and let \((i,j,k)=(\pi(1),\pi(2),\pi(3))\). By Lemma 4.3(iv), we have that \(\phi_\pi(\langle q,1,1\rangle)=q^{p_j}\), \(\phi_\pi(\langle 1,q,1\rangle)=q^{p_k}\) and \(\phi_\pi(\langle 1,1,2\rangle)=2^{p_i}\) (this can be most easily seen by considering which leg of \(\pi\cdot T\) is one-dimensional, with _T_ the tensor where \(\phi_\pi\) is evaluated).

If _p<sub>i</sub>\>_0, then the AM-GM inequality, Lemma 4.6 for \(\phi_\pi\), and \(\mathrm{Str}_q\unknown\langle q+1\rangle\) give

\(2q^{(p_j+p_k)/(2p_i)}\le q^{p_j/p_i}+q^{p_k/p_i}\le\phi_\pi(\mathrm{Str}_q)^{1/p_i}\le(q+1)^{1/p_i}.\)

So \(2^{p_i}q^{(p_j+p_k)/2}\le q+1\). This also holds if _p<sub>i</sub>_=0, since \(p_j,p_k\le 1\). Multiplying these three inequalities, one for each value of _i_, gives \((2q)^{p_1+p_2+p_3}\le(q+1)^3\). Since the maximum of _p_<sub>1</sub>+_p_<sub>2</sub>+_p_<sub>3</sub> over all \(\phi\in\Delta_\mathbb{F}\) is \(\omega_\mathbb{F}\) (Theorem 4.2 and Lemma 4.3(iv)), this proves the claim.

From the same tensor, Strassen’s laser method \[Str87, Corollary 7.5\] (see also \[Blä13, Section 8 and Corollary 8.8\]) gives \(4q^{\omega_\mathbb{F}}\le(q+1)^3\) for every integer \(q\ge 2\). This is best for _q_=5, where it gives \(5^{\omega_\mathbb{F}}\le 54\), equivalently \(\omega_\mathbb{F}<2.48\).

The proof of Proposition 4.8 is easily generalized to obtain Lemma 4.9 below, which we use in Section 1.2 for illustrative purposes. We will not need it for the remainder of the text, so it may be skipped. We recover Proposition 4.8 by setting \(S=\langle q,1,1\rangle\) and _s=t_=1, and applying \(\mathrm{Str}_q\unknown\langle q+1\rangle\).

**Lemma 4.9** (Symmetrised partial direct sums)**.** _Let S be a tensor over_ F_, and let_ \(s,t\ge 1\) _be integers. Then_<tbc>

\(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\big(S\otimes\langle 1,1,s+t\rangle\big)\lesssim\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\big(\big(S\otimes\langle 1,1,s\rangle\big)\oplus_1\big(((23)\cdot S)\otimes\langle 1,1,t\rangle\big)\big).\)

<tbc>_Proof._ Let \(T:=(S\otimes\langle 1,1,s\rangle)\oplus_1(((23)\cdot S)\otimes\langle 1,1,t\rangle)\), and let \(\phi\in\Delta_\mathbb{F}\). By Strassen’s duality theorem \[Str88, Theorem 3.2\], and since \(\phi\) is multiplicative and the six permutations form three pairs \(\{\pi,\pi\circ(23)\}\), it suffices to show that<tbc>

\(\phi_\pi(T)\phi_{\pi\circ(23)}(T)\ge\phi_\pi\big(S\otimes\langle 1,1,s+t\rangle\big)\phi_{\pi\circ(23)}\big(S\otimes\langle 1,1,s+t\rangle\big)\)

<tbc>for every \(\pi\in\mathfrak{S}_3\). Fix \(\pi\), and let \(p:=\mathrm{log}\phi_\pi(\langle 1,1,2\rangle)\), \(x:=\phi_\pi(S)\) and \(y:=\phi_{\pi\circ(23)}(S)\). Since \((23)\cdot\langle 1,1,2\rangle\cong\langle 1,1,2\rangle\), also \(\phi_{\pi\circ(23)}(\langle 1,1,2\rangle)=2^p\), so \(\phi_\pi(\langle 1,1,m\rangle)=\phi_{\pi\circ(23)}(\langle 1,1,m\rangle)=m^p\) for every integer \(m\ge 1\) (Lemma 4.3(iv) and (v)). So the right-hand side is (_s+t_)<sup>2_p_</sup>_xy_. Moreover, \(\phi_\pi((23)\cdot S)=y\) and \(\phi_{\pi\circ(23)}((23)\cdot S)=x\). If _p\>_0, then Lemma 4.6 for \(\phi_\pi\) and for \(\phi_{\pi\circ(23)}\) gives

\(\phi_\pi(T)^{1/p}\ge sx^{1/p}+ty^{1/p}\text{and}\phi_{\pi\circ(23)}(T)^{1/p}\ge sy^{1/p}+tx^{1/p},\)

and \((sx^{1/p}+ty^{1/p})(sy^{1/p}+tx^{1/p})\ge(s+t)^2(xy)^{1/p}\), since the difference is _st(x_<sup>1_/p_</sup>-_y_<sup>1_/p_</sup>)<sup>2</sup>. Raising to the power _p_ gives the claim. If _p_=0, then the restriction \(T\ge S\otimes\langle 1,1,s\rangle\) gives \(\phi_\pi(T)\ge x\) and \(\phi_{\pi\circ(23)}(T)\ge y\), which is the claim.

## 4.3 Concavity and tripling for each leg

In this subsection we will bound the values \(\phi(\mathsf{P}_{a,b})\) of a spectral point \(\phi\) at the polynomial multiplication tensors. We will show that, if \(p:=\mathrm{log}\phi(\langle 1,1,2\rangle)>0\), then \(b\mapsto\phi(\mathsf{P}_{a,b})^{1/p}\) is concave and satisfies a tripling inequality (Lemma 4.10). The results follows directly from the degenerations of Section 3, combined with Lemma 4.6, see  1.

