## B.2 Proof of Theorem 2.6

We first show a main lemma which will be used recursively.

**Lemma B.7.** _There exists a universal constant C\>_0 _such that the following is true. Let G be a weighted undirected graph with n vertices, m edges, and edge weights bounded by W. Let_ \(\lambda\) _be such that_ \(\omega(n^{-\frac{1}{2}})\le\lambda\le o(1)\)_. There is an_ \(\sqrt{\frac{Cnlogn}{\lambda m}}-\)_spectral sparsifier of G with_ \(m\cdot\left(\frac{1}{2}\pm\lambda\right)\) _edges and edge weights bounded by_ 2_W._

_Proof._ Consider the following random procedure.

1. Let \(E_\mathrm{low}\subseteq E\) be a set of edges for which \(w_eR_e\le\frac{n}{\lambda m}\). Also let _E_<sub>high</sub>=_E_\\_E_<sub>low</sub>. Then due to Theorem B.3, we have \(|E_\mathrm{low}|\ge(1-\lambda)m\).<tbc>

2. For each \(e\in E_\mathrm{low}\), draw \(z_e\in\{0,1\}\) uniformly at random.<tbc>

3. Let _Y_ be a graph consisting of \(e\in E_\mathrm{low}\) such that _z<sub>e</sub>_=1 and double the weight to 2_w<sub>e</sub>_.<tbc>

4. Output \(H=Y\cup E_\mathrm{high}\).

<tbc>We claim that the output graph _H_ is the desired sparsifier with non-zero probability. First of all, let’s count number of edges in _H_. This is<tbc>

\(|E_\mathrm{high}|+B(|E_\mathrm{low}|,\frac{1}{2})=m-|E_\mathrm{low}|+B(|E_\mathrm{low}|,\frac{1}{2})\equiv m-B(|E_\mathrm{low}|,\frac{1}{2}).\)

<tbc>Via Chebychev inequality, we have the followings with constant probability.

\(B(|E_\mathrm{low}|,\frac{1}{2})\le\frac{|E_\mathrm{low}|}{2}+4\sqrt{|E_\mathrm{low}|}\le\frac{m}{2}+4\sqrt{m}\le m\cdot(\frac{1}{2}+\lambda)\)

and

\(B(|E_\mathrm{low}|,\frac{1}{2})\ge\frac{|E_\mathrm{low}|}{2}-4\sqrt{|E_\mathrm{low}|}\ge\frac{(1-\lambda)m}{2}-4\sqrt{m}\ge m\cdot(\frac{1}{2}-\lambda).\)

Hence, with constant probability, the number of edges of _H_ lies within \(m\cdot\left(\frac{1}{2}\pm\lambda\right)\).

Next, we will analyze the approximation error. For any \(e\in E_\mathrm{low}\), denote a random vector \(y_e:=\sqrt{2w_ez_e}\cdot L_G^{+/2}\chi_e\) and an \(n\times n\) random matrix \(Y_e:=y_ey_e^\top\). Similarly, for any \(e\in E_\mathrm{high}\), denote a vector \(y_e:=\sqrt{w_e}\cdot L_G^{+/2}\chi_e\) and an \(n\times n\) matrix \(Y_e:=y_ey_e^\top\). Notably, randomness is _not_ involved in those _Y<sub>e</sub>_ of \(e\in E_\mathrm{high}\) and every _Y<sub>e</sub>_ is psd and symmetric.

By basic calculations, we can show that \(\sum_{e\in E}Y_e=L_G^{+/2}L_HL_G^{+/2}\), \(\mathbb{E}\left(\sum_{e\in E}Y_e\right)=\Pi\), and \(\lambda_1(Y_e)\le\frac{2n}{\lambda m}\) for every \(e\in E_\mathrm{low}\). We defer these calculations to via Fact B.8 and Fact B.9 which will come up shortly. Applying the extended matrix Chernoff bound (Theorem B.6), the random matrix \(L_G^{+/2}L_HL_G^{+/2}\) has all non-zero eigenvalues between \(1\pm\varepsilon\) except probability \(2n\cdot\mathrm{exp}(-\frac{\varepsilon^2\lambda m}{6n})\). By setting \(\varepsilon=\sqrt{\frac{Cnlogn}{\lambda m}}\) for suitably large constant _C_, such error probability is at most _n_<sup>-10</sup>.

When it is the case that \(L_G^{+/2}L_HL_G^{+/2}\) has all eigenvalues lied between \(1\pm\varepsilon\), we claim that _H_ is a spectral sparsifier of _G_. To see this, take any vector \(v\in\mathbb{R}^n\) and let \(u=L_G^{+/2}v\). If \(u=\vec{0}\), it means \(v=\vec{1}\) which appears to be the corner case.<sup>10</sup> Otherwise, we have:<tbc>

<sup>10</sup>\(v=\vec{1}\) is in the kernel of both _L<sub>G</sub>_ and _L<sub>H</sub>_. As a result, we have \(v^\top L_Gv=v^\top L_Hv=0\) which satisfies the bounds \(1-\varepsilon\le\frac{v^\top L_Hv}{v^\top L_Gv}\le 1+\varepsilon\) if we were to abuse that \(\frac{0}{0}=1\).

