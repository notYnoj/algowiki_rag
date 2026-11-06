(v) \(\phi_\pi\in\Delta_\mathbb{F}\).

_Proof._ Part (i) is \[Str87, Proposition 5.10\] and \[Str88, Theorem 3.1\]. Part (ii) holds since \(\langle n\rangle\) is the direct sum of _n_ copies of \(\langle 1\rangle\), and part (iii) follows since \(\langle 1\rangle\le T\) for every nonzero tensor _T_ (Lemma 2.1(i)). The formula in part (iv) is \[Str88, Proposition 4.3\]. The bounds on the three values follow from parts (i)-(iii), since each of the tensors \(\langle 1,1,2\rangle\), \(\langle 2,1,1\rangle\) and \(\langle 1,2,1\rangle\) is nonzero and a restriction of \(\langle 2\rangle\). The last claim is the formula for _n_<sub>1</sub>=_n_<sub>2</sub>=_n_<sub>3</sub>=_m_, together with the formula for _n_<sub>1</sub>=_n_<sub>2</sub>=_n_<sub>3</sub>=2. Part (v) follows since permuting the legs of a tensor commutes with direct sums and tensor products, fixes \(\langle 1\rangle\) and preserves restriction (Lemma 2.1(iv)).

Strassen also expressed the exponents of rectangular matrix multiplication as a maximum over spectral points.

**Lemma 4.4** (Strassen \[Str88, Proposition 4.5\])**.** _Let_ \(a,b,c\ge 0\) _be real numbers. Then_

\(2^{\omega_\mathbb{F}(a,b,c)}=\mathrm{max}_{\phi\in\Delta_\mathbb{F}}\phi(\langle 2,1,1\rangle)^a\phi(\langle 1,2,1\rangle)^b\phi(\langle 1,1,2\rangle)^c.\)

_Proof._ For _a,b,c\>_0, this follows directly from \[Str88, Propositions 4.5 and 3.3\].

If one of _a_, _b_ and _c_ is 0, say _c_=0, then both sides equal 2<sup>_a+b_</sup>, since the tensor rank of \(\langle n_1,n_2,1\rangle\) is _n_<sub>1</sub>_n_<sub>2</sub>, and \(\mathrm{R}_{(1)}\in\Delta_\mathbb{F}\) satisfies \(\mathrm{R}_{(1)}(\langle 2,1,1\rangle)=\mathrm{R}_{(1)}(\langle 1,2,1\rangle)=2\).

## 4.2 Superadditivity on partial direct sums

In this subsection we will show that, for every \(\phi\in\Delta_\mathbb{F}\) with \(p:=\mathrm{log}\phi(\langle 1,1,2\rangle)>0\), the function \(\phi^{1/p}\) is superadditive on partial direct sums (Lemma 4.6). We will first treat isomorphic summands using Proposition 3.5 (Lemma 4.5), and then remove the hypothesis that the summands are isomorphic by applying this case to tensor powers. As a first application, we will obtain \(\omega_\mathbb{F}<2.3212\) from a tensor of Strassen (Proposition 4.8).

**Lemma 4.5** (Isomorphic summands)**.** _Let_ \(\phi\in\Delta_\mathbb{F}\)_, and suppose that_ \(p:=\mathrm{log}\phi(\langle 1,1,2\rangle)\) _is positive. Let_ \(r\ge 1\) _be an integer, and let_ \(S=S_1\oplus_1\cdots\oplus_1S_r\) _be a partial direct sum in which each S<sub>i</sub> is isomorphic to S_<sub>1</sub>_. Then_<tbc>

\(\phi(S)\ge\frac{1}{2}r^p\phi(S_1).\)

<tbc>_Proof._ We have<tbc>

\((S_1\oplus\cdots\oplus S_r)\otimes\mathsf{P}_{1,r}\unknown S\otimes\mathsf{P}_{r,r}\unknown S\otimes\langle 2r-1\rangle.\)

<tbc>The first degeneration is Proposition 3.5 with _m=t=r_. The second follows by tensoring the border rank bound \(\mathsf{P}_{r,r}\unknown\langle 2r-1\rangle\) (Proposition 3.2) with _S_. The left-hand side is isomorphic to \(\langle r\rangle\otimes S_1\otimes\langle 1,1,r\rangle\), since \(S_1\oplus\cdots\oplus S_r\cong\langle r\rangle\otimes S_1\) and \(\mathsf{P}_{1,r}\cong\langle 1,1,r\rangle\). The spectral point \(\phi\) is multiplicative and monotone under degeneration, \(\phi(\langle n\rangle)=n\) for every integer \(n\ge 1\), and \(\phi(\langle 1,1,r\rangle)=r^p\) (Lemma 4.3(i), (ii) and (iv)). So

\(r^{1+p}\phi(S_1)\le(2r-1)\phi(S).\)

Since \(r/(2r-1)\ge 1/2\), it follows that \(\phi(S)\ge\frac{1}{2}r^p\phi(S_1)\).

**Lemma 4.6** (Superadditivity)**.** _Let_ \(\phi\in\Delta_\mathbb{F}\)_, and suppose that_ \(p:=\mathrm{log}\phi(\langle 1,1,2\rangle)\) _is positive. Let_ \(m\ge 1\) _be an integer. For_ \(\ell\in[m]\)_, let_ \(T_\ell\in U\otimes V_\ell\otimes W_\ell\) _be tensors over_ F_. Then_<tbc>

\(\phi(T_1\oplus_1\cdots\oplus_1T_m)^{1/p}\ge\phi(T_1)^{1/p}+\cdots+\phi(T_m)^{1/p}.\)

