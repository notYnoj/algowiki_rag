so putting it together with (4.3), (4.4) and (4.7), we get

\(\mathrm{Var}LC_n\ge\frac{pp_{X,\mathrm{min}}(1-\gamma^*)}{8k_0}n.\)

## 4.4 A weaker kind of lower bound

Let us return to the Bernoulli framework with parameter 0_\<p\<_1, and let \(\gamma_n(p)=\mathbb{E}LC_n/n\) and \(\gamma(p)=\mathrm{lim}_{n\rightarrow\infty}\gamma_n(p)\). It seems reasonable to expect that Var_LC<sub>n</sub>/n_ converges when _n_ tends to infinity, but, so far, unfortunately a proof of this result has been elusive. To the best of our knowledge, it is still an open problem to determine whether or not, in the uniform case, the variance tends to infinity. The function \(\gamma\) is clearly symmetric around 1/2, and it is expected to be strictly convex with a minimum at 1/2, but besides numerical simulations there is no proof of this fact yet. The goal of this section is to prove:

**Theorem 4.1.** _Let_ \(p_0\in(0,1/2)\) _be such that_ \(\gamma(p_0)>\gamma(1/2)\)_. Then there exists_ \(p_1\in(p_0,1/2)\) _such that when p=p_<sub>1</sub>,

\(\mathrm{limsup}_{n\rightarrow\infty}\frac{VarLC_n}{n}\ge 2p_0(1-p_0)\left(\frac{\gamma(p_0)-\gamma(1/2)}{1/2-p_0}\right)^2.\)

**Remark 4.2.** _Using the bound_ \(\gamma(1/2)<0.8263\) _from \[20\], and since_ \(\gamma(p)\ge p^2+(1-p)^2\)_, we can apply the above theorem with p_<sub>0</sub>=0.096_, to get for some_ \(p_1\in(0.096,0.5),\mathrm{limsup}_{n\rightarrow\infty}\mathrm{Var}LC_n/n\ge 1.8/10^8\)_. Clearly, by symmetry, this limsup result is also valid for some_ \(p_2=1-p_1\in(0.5,0.904)\).

_Proof._ We have

\(\gamma_n(p_0)-\gamma_n(1/2)=-\int_{p_0}^{1/2}\frac{\mathrm{d}\gamma_n}{\mathrm{d}p}(p)\mathrm{d}p=\int_{p_0}^{1/2}\frac{1}{2n}\sum_{k=1}^{2n}\mathbb{E}_p\left(LC_n^{k,0}-LC_n^{k,1}\right)\mathrm{d}p,\)

using a Russo-Margulis type formula. This is not strictly the Russo-Margulis lemma since _LC<sub>n</sub>_ is not monotone, but the proof of this version is elementary: as in \[8\], we rewrite \(\gamma_n\) as a function of 2_n_ parameters, the parameters of each letter (Bernoulli random variables):

\(\frac{\mathrm{d}\gamma_n}{\mathrm{d}p}(p)=\frac{\mathrm{d}\gamma_n}{\mathrm{d}p}(p,p,\dots,p)=\sum_{k=1}^{2n}\frac{\mathrm{d}\gamma_n}{\mathrm{d}p_k}(p,p,\dots,p),\)

which yields the result. Hence,

\(\gamma(p_0)-\gamma(1/2)=\mathrm{limsup}_{n\rightarrow\infty}\gamma_n(p_0)-\gamma_n(1/2)\)<br>
\(\le\int_{p_0}^{1/2}\mathrm{limsup}_{n\rightarrow\infty}\frac{1}{2n}\sum_{k=1}^{2n}\mathbb{E}_p\left(LC_n^{k,0}-LC_n^{k,1}\right)\mathrm{d}p,\)

so there exists \(p_1\in(p_0,1/2)\) such that

\(\mathrm{limsup}_{n\rightarrow\infty}\frac{1}{2n}\sum_{k=1}^{2n}\mathbb{E}_{p_1}\left(LC_n^{k,0}-LC_n^{k,1}\right)\ge\frac{\gamma(p_0)-\gamma(1/2)}{1/2-p_0}.\)

Let us fix _p=p_<sub>1</sub>. As seen previously,

\(B_{2n}(2n)=\frac{1}{2n}\sum_{k=1}^{2n}\big(\mathbb{E}\left(LC_n(Z^{k,0})-LC_n(Z^{k,1})\right)\big)^2p_1(1-p_1),\)

