We call a function \(h:\mathbb{Z}_{\ge 1}\rightarrow\mathbb{R}\) _concave_ if \(h(m+1)+h(m-1)\le 2h(m)\) for every \(m\ge 2\).

**Lemma 4.10.** _Let_ \(\phi\in\Delta_\mathbb{F}\)_, and let_ \(p:=log\phi(\langle 1,1,2\rangle)\).

(i) _For all_ \(a,b\ge 1\)_, we have_ \(min(a,b)\le\phi(\mathsf{P}_{a,b})\le a+b-1\)_, and_ \(\phi(\mathsf{P}_{a,b})\) _is nondecreasing in a and in b._<tbc>

(ii) _If p\>_0_, then for all_ \(a\ge 1\)_, the function_ \(b\mapsto\phi(\mathsf{P}_{a,b})^{1/p}\) _is concave._<tbc>

(iii) _If p\>_0_, then for all_ \(a,b\ge 1\)_, we have_ \(2\phi(\mathsf{P}_{a,b})^{1/p}+\phi((23)\cdot\mathsf{P}_{a,b})^{1/p}\le\phi(\mathsf{P}_{a,3b+a-1})^{1/p}\).

_Proof._ (i) For _n_=min(_a,b_), the degenerations \(\langle n\rangle\triangleleft\mathsf{P}_{n,n}\le\mathsf{P}_{a,b}\) (Lemma 3.3) give \(n=\phi(\langle n\rangle)\le\phi(\mathsf{P}_{a,b})\) (Lemma 4.3(i) and (ii)), and \(\mathsf{P}_{a,b}\triangleleft\langle a+b-1\rangle\) (Proposition 3.2) gives \(\phi(\mathsf{P}_{a,b})\le a+b-1\). If \(a_1\le a_2\) and \(b_1\le b_2\), then \(\mathsf{P}_{a_1,b_1}\le\mathsf{P}_{a_2,b_2}\), so \(\phi(\mathsf{P}_{a_1,b_1})\le\phi(\mathsf{P}_{a_2,b_2})\).

(ii) and (iii) Suppose that _p\>_0. By Lemma 3.6 and Lemma 3.4, for all integers \(a\ge 1\) and \(b\ge 2\),<tbc>

\(\mathsf{P}_{a,b+1}\oplus_1\mathsf{P}_{a,b-1}\triangleleft\mathsf{P}_{a,b}\otimes\langle 1,1,2\rangle,\)

<tbc>and by Lemma 3.11, for all integers \(a,b\ge 1\),

\(\mathsf{P}_{a,b}\oplus_1((23)\cdot\mathsf{P}_{a,b})\oplus_1\mathsf{P}_{a,b}\triangleleft\mathsf{P}_{a,3b+a-1}.\)

Moreover, \(\phi(\mathsf{P}_{a,b}\otimes\langle 1,1,2\rangle)=2^p\phi(\mathsf{P}_{a,b})\). So Lemma 4.6 and the monotonicity of \(\phi\) under degeneration give (ii) from the first degeneration and (iii) from the second.

In the subsequent sections we will use the following definition as a shorthand:

\(\phi(a,b):=\phi(\mathsf{P}_{a,b}).\) (4.2)

## 4.4 Square matrix multiplication

In this subsection we will prove Theorem 1.1. By Theorem 4.2, it suffices to show that \(\phi(\langle 2,2,2\rangle)\le 2^{9/4}\) for every \(\phi\in\Delta_\mathbb{F}\). For this we will use Lemma 4.10 applied to \(\phi_\pi\) with \(\pi\) ranging over S<sub>3</sub>. In the case that \(p:=log\phi_\pi(\langle 1,1,2\rangle)>0\), we will apply Lemma 4.11 to the functions \(b\mapsto\phi_\pi(a,b)^{1/p}\) and \(b\mapsto\phi_{\pi\circ(23)}(a,b)^{1/p}\) appearing in Lemma 4.10. Roughly speaking, this will then allow us to lower bound the growth of \(n\mapsto\phi_\pi(n,n)\) in terms of _p_. Subsequently, we will obtain a lower bound on \(\phi\) evaluated on \(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\mathsf{P}_{n,n}\) in terms of \(\phi(\langle 2,2,2\rangle)\). The upper bound will then follow from the fact that \(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\mathsf{P}_{a,b}\) has low border rank (Proposition 3.2).

In Sections 4.5 and 4.6 we will treat the rectangular case. Those sections will not rely on any result from this section, and the results there will also recover the results of this section. So, this section can also safely be skipped.

We begin with a general lemma about concave functions.

\begin{tabular}{cc}
Degeneration & Inequality \\
(D1) \(\mathsf{P}_{a,b}\triangleleft\langle a+b-1\rangle\) & \(\phi(\mathsf{P}_{a,b})\le a+b-1\) \\
(D3) \(\mathsf{P}_{a,b+1}\oplus_1\mathsf{P}_{a,b-1}\triangleleft\mathsf{P}_{a,b}\oplus_1\mathsf{P}_{a,b}\), \(b\ge 2\) & \(\phi(\mathsf{P}_{a,b+1})^{1/p}+\phi(\mathsf{P}_{a,b-1})^{1/p}\le 2\phi(\mathsf{P}_{a,b})^{1/p}\) \\
(D4) \(\mathsf{P}_{a,b}\oplus_1((23)\cdot\mathsf{P}_{a,b})\oplus_1\mathsf{P}_{a,b}\triangleleft\mathsf{P}_{a,3b+a-1}\) & \(2\phi(\mathsf{P}_{a,b})^{1/p}+\phi((23)\cdot\mathsf{P}_{a,b})^{1/p}\) \\
 & \(\le\phi(\mathsf{P}_{a,3b+a-1})^{1/p}\) \\
\end{tabular}

1: The ingredients (D1), (D3) and (D4) of Section 1.1 (Proposition 3.2, Lemma 3.6 and Lemma 3.11), for integers \(a,b\ge 1\), and the inequalities that they give for a spectral point \(\phi\in\Delta_\mathbb{F}\), where \(p:=log\phi(\langle 1,1,2\rangle)>0\) in the last two rows.

