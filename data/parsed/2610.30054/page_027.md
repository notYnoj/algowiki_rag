where we multiply these inequalities and use that _G_<sub>1</sub>=1. The factors (3_k_+2)/(3_k_-1) telescope to (3_n_-1)/2, which gives the first inequality of the claim. For the second, we use that \(\tau\ge 0\), \((3n-1)/2\ge n\), and \((3k+1)/(3k)\ge((k+1)/k)^{1/3}\) by the binomial theorem, so that \(\prod_{k=1}^{n-1}(3k+1)/(3k)\ge n^{1/3}\).

_Proof of Theorem 1.1._ Let \(\phi\in\Delta_\mathbb{F}\), and let \(\tau:=\mathrm{log}\phi(\langle 2,2,2\rangle)\). Since \(\phi(\pi\cdot\mathsf{P}_{n,n})\le 2n-1\) for every \(\pi\in\mathfrak{S}_3\) (Lemma 4.10(i) for \(\phi_\pi\)), Proposition 4.12 gives \(n^{8\tau/3}\le(2n-1)^6<64n^6\) for every integer \(n\ge 1\), so \(8\tau/3\le 6\), that is, \(\phi(\langle 2,2,2\rangle)\le 2^{9/4}\). Since this holds for every \(\phi\in\Delta_\mathbb{F}\), Theorem 4.2 gives \(\omega_\mathbb{F}\le 9/4\).

For a fixed integer \(n\ge 2\), the first inequality of Proposition 4.12 and the upper bound (2_n_-1)<sup>6</sup> give, in the same way,

\(\omega_\mathbb{F}\le\frac{3\mathrm{log}(2n-1)}{\mathrm{log}\big(\frac{3n-1}{2}\prod_{k=1}^{n-1}\frac{3k+1}{3k}\big)}.\)

For example \(\omega_\mathbb{F}<2.74\) for _n_=2, the bound of the example in Section 1.2.3, and \(\omega_\mathbb{F}<2.65\) for _n_=3.

## 4.5 Quadratic constraints on asymptotic spectrum of matrix multiplication

We now extend the analysis in Lemma 4.11 and Proposition 4.12 to the rectangular case, which we will use to prove Theorem 1.2 in Section 4.6. The proof ideas are essentially the same, but we need to take into account the ratios of the "weights" given to the three legs resulting from the definition of \(\omega_\mathbb{F}(a,b,c)\).

The following lemma generalises Lemma 4.11, which is the case _u=v=b_ and _r=s_=1.

**Lemma 4.13.** _Let_ \(a\ge 1\) _be an integer, and let_ \(g,h:\mathbb{Z}_{\ge 1}\rightarrow\mathbb{R}_{>0}\) _be concave functions such that_ \(2g(m)+h(m)\le g(3m+a-1)\) _and_ \(2h(m)+g(m)\le h(3m+a-1)\) _for every integer_ \(m\ge 1\)_. Then for all integers_ \(u,v,r,s\ge 1\),

\(\big(\frac{g(u+r)}{g(u)}\big)^s\big(\frac{h(v+s)}{h(v)}\big)^r\ge\big(\frac{D}{D-\frac{4rs}{r+s}}\big)^{r+s},\)

_where D_:=_u+v+r+s+a_-1.

_Proof._ Let _m_:=max(_u+r,v+s_) and \(\lambda:=\frac{g(m)+h(m)}{2m+a-1}>0\). By concavity and the first hypothesis, for every integer \(1\le k<m\),<tbc>

\(g(k+1)-g(k)\ge\frac{g(3m+a-1)-g(m)}{2m+a-1}\ge\lambda.\)

<tbc>Likewise, \(h(k+1)-h(k)\ge\lambda\). Writing _A_:=_g(u+r_) and _B_:=_h(v+s_), summing these difference bounds gives \(A-g(u)\ge r\lambda\) and \(B-h(v)\ge s\lambda\). Similarly, \(g(m)-A\ge(m-u-r)\lambda\). Doing the same for _h_, and then using that \(g(m)+h(m)=\lambda(2m+a-1)\), we also find<tbc>

\(A+B\le g(m)+h(m)-\lambda(2m-u-r-v-s)=\lambda D.\)

<tbc>By the weighted arithmetic-mean geometric-mean inequality,

\(\big(\frac{g(u)}{A}\big)^{s/(r+s)}\big(\frac{h(v)}{B}\big)^{r/(r+s)}\le\frac{1}{r+s}\big(s\frac{g(u)}{A}+r\frac{h(v)}{B}\big).\) (4.3)

