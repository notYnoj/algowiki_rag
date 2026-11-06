multiplication tensors and one copy of P<sub>2,2</sub>:

\(\mathsf{P}_{2,2}\otimes\langle 1,1,4\rangle\cong\mathsf{P}_{2,2}\oplus_1\mathsf{P}_{2,2}\oplus_1\mathsf{P}_{2,2}\oplus_1\mathsf{P}_{2,2}\)<br>
\(\supseteq\mathsf{P}_{2,1}\oplus_1\mathsf{P}_{2,3}\oplus_1\mathsf{P}_{2,3}\oplus_1\mathsf{P}_{2,1}\) (D3), _b_=2, twice<br>
\(\supseteq\mathsf{P}_{2,1}\oplus_1\mathsf{P}_{2,2}\oplus_1\mathsf{P}_{2,4}\oplus_1\mathsf{P}_{2,1}\) (D3), _b_=3<br>
\(\supseteq\mathsf{P}_{2,1}\oplus_1\mathsf{P}_{2,2}\oplus_1\mathsf{P}_{2,1}\oplus_1\left((23)\cdot\mathsf{P}_{2,1}\right)\oplus_1\mathsf{P}_{2,1}\oplus_1\mathsf{P}_{2,1}\) (D4), _b_=1<br>
\(\cong\langle 2,1,4\rangle\oplus_1\langle 1,2,1\rangle\oplus_1\mathsf{P}_{2,2},\)

where in the last step, we use that the partial direct sum of the four copies of \(\mathsf{P}_{2,1}\cong\langle 2,1,1\rangle\) is \(\langle 2,1,1\rangle\otimes\langle 1,1,4\rangle\cong\langle 2,1,4\rangle\), and that \((23)\cdot\mathsf{P}_{2,1}\cong\langle 1,2,1\rangle\). The copy of P<sub>2,2</sub> comes back and goes into the next round. So _k_ rounds, followed by removing the last copy of P<sub>2,2</sub>, give

\(\mathsf{P}_{2,2}\otimes\langle 1,1,3k+1\rangle\supseteq\langle 2,1,4k\rangle\oplus_1\langle 1,2,k\rangle.\)

With (1.1), this is (1.2) with _n_=3_k_+1, _s_=4_k_ and _t=k_. Since _a(s+t_)=10_k\>_3_k_+1, we get \(\omega_\mathbb{F}\le 3\mathrm{log}(3)/\mathrm{log}(10k/(3k+1))\), and letting \(k\rightarrow\infty\) gives \(\omega_\mathbb{F}\le 3\mathrm{log}(3)/\mathrm{log}(10/3)<2.74\).

Starting instead from \(\langle 5\rangle\supseteq\mathsf{P}_{2,4}\), ingredient (D4) with _b_=1 gives \(\mathsf{P}_{2,4}\supseteq\langle 2,1,2\rangle\oplus_1\langle 1,2,1\rangle\) in one step, and the same argument, with \(\langle 5\rangle\) in place of \(\langle 3\rangle\), gives the better bound \(\omega_\mathbb{F}\le 3\mathrm{log}5/\mathrm{log}6<2.695\).

Again, this is just an example, but it illustrates components of the actual construction, and it can indeed be extended (by starting with P_<sub>a,a</sub>_ with \(a\rightarrow\infty\)) to explicit combinations of the ingredients whose bounds tend to 9/4.

## 1.3 High-level proof description and role of asymptotic spectrum duality

Our proof of Theorem 1.1 will not combine the ingredients by hand, as the Section 1.2.3 example does. Instead, Strassen’s spectral points turn the search for the best combination of the ingredients, including their tensor powers, into an optimisation problem. Spectral points are semiring homomorphisms \(\phi\) from tensors to the nonnegative real numbers that are monotone under restriction (Definition 4.1). By Strassen’s duality theorem, \(T\lesssim S\) if and only if \(\phi(T)\le\phi(S)\) for every spectral point \(\phi\) \[Str88, Theorem 3.2\]. In particular, \(\omega_\mathbb{F}\) is the maximum of \(\mathrm{log}\phi(\langle 2,2,2\rangle)\) over all spectral points \(\phi\) (Theorem 4.2).

For a spectral point \(\phi\), let _p_<sub>1</sub>, _p_<sub>2</sub> and _p_<sub>3</sub> be the logarithms of \(\phi(\langle 1,1,2\rangle)\), \(\phi(\langle 2,1,1\rangle)\) and \(\phi(\langle 1,2,1\rangle)\). Then \(\mathrm{log}\phi(\langle 2,2,2\rangle)=p_1+p_2+p_3\), so it suffices to show that \(p_1+p_2+p_3\le 9/4\). We will show using ingredient (D2) that if _p_<sub>1</sub>_\>_0, then \(\phi^{1/p_1}\) is superadditive on partial direct sums, whose summands share the first leg (Lemma 4.6). Subsequently, (D3) makes the function \(b\mapsto\phi(\mathsf{P}_{a,b})^{1/p_1}\) concave, and (D4) gives the "tripling inequality"

\(2\phi(\mathsf{P}_{a,b})^{1/p_1}+\phi\big((23)\cdot\mathsf{P}_{a,b}\big)^{1/p_1}\le\phi(\mathsf{P}_{a,3b+a-1})^{1/p_1}\)

(Lemma 4.10). The same holds for the tensors \(\pi\cdot\mathsf{P}_{a,b}\) with permuted legs in place of P_<sub>a,b</sub>_, with \(p_{\pi(1)}\) in place of _p_<sub>1</sub>. From these inequalities, an elementary argument shows that the product of the six numbers \(\phi(\pi\cdot\mathsf{P}_{a,a})\), which is the value of \(\phi\) at the symmetrisation \(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\mathsf{P}_{a,a}\) of Section 1.2, is at least _a_<sup>8(_p_<sub>1</sub>+_p_<sub>2</sub>+_p_<sub>3</sub>)/3</sup> (Proposition 4.12). By ingredient (D1), it is at most (2_a_-1)<sup>6</sup>. Letting \(a\rightarrow\infty\) gives \(p_1+p_2+p_3\le 9/4\) for every spectral point \(\phi\), and hence \(\omega_\mathbb{F}\le 9/4\).

In terms of asymptotic restriction, the above construction leads to a chain in which symmetrised polynomial multiplication is in the middle: For every integer \(a\ge 1\),<tbc>

\(\langle a^4,a^4,a^4\rangle^{\otimes 2}\lesssim\big(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\mathsf{P}_{a,a}\big)^{\otimes 3}\unknown\langle(2a-1)^{18}\rangle,\) (1.6)

