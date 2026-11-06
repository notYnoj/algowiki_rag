## B.4 Proof of Theorem 5 (Confidence sequence for the 1-bit estimator)

We split the proof into four lemmas. The first lemma records the mean, variance, and range properties of the centered 1-bit variables. The second lemma turns these properties into an exponential supermartingale. The third lemma derives an epoch-wise Bernstein boundary by combining Ville’s inequality with an explicit optimization over the exponential parameter. The fourth lemma stitches the epoch-wise bounds into a genuine time-uniform confidence sequence for the clipped target. The theorem then follows by adding the clipping-bias term.

**Lemma 15** (Centered process properties)**.** _Fix_ \(L\ge\sigma\)_, and define_<tbc>

\(\theta_L:=\mathbb{E}[[W]_L],X_i:=Z_i-\theta_L,S_n:=\sum_{i=1}^nX_i.\)

<tbc>_Then X_<sub>1</sub>_,X_<sub>2</sub>_,... are i.i.d. and mean-zero, and satisfy_<tbc>

\(\mathbb{E}[X_i]=0,\mathrm{Var}(X_i)\le v_L,|X_i|\le b_L\text{\textit{a.s.}},\)

<tbc>_where_<tbc>

\(v_L:=3\alpha_L\sigma^2,b_L:=3\alpha_LL.\)

<tbc>_Proof._ By Lemma 3(i),<tbc>

\(\mathbb{E}[Z_i]=\mathbb{E}[[W]_L]=\theta_L,\)

<tbc>and therefore<tbc>

\(\mathbb{E}[X_i]=\mathbb{E}[Z_i-\theta_L]=0.\)

<tbc>Since subtracting a constant does not change the variance, Lemma 3(ii) gives<tbc>

\(\mathrm{Var}(X_i)=\mathrm{Var}(Z_i)\le 3\alpha_L\sigma^2=v_L.\)

<tbc>It remains to prove the range bound. By Lemma 3(iii),<tbc>

\(|Z_i|\le 2\alpha_LL\text{a.s.}\)

<tbc>Also, since \(|[W]_L|\le L\),<tbc>

\(|\theta_L|=|\mathbb{E}[[W]_L]|\le\mathbb{E}[[W]_L|\le L.\)

<tbc>Hence

\(|X_i|=|Z_i-\theta_L|\le|Z_i|+|\theta_L|\le 2\alpha_LL+L\le 3\alpha_LL=b_L,\)

where we used \(\alpha_L\ge 1\). This proves the claim.

**Lemma 16** (Bernstein supermartingale)**.** _For every_ \(\lambda\in[0,3/b_L)\)_, define_

\(\psi_L(\lambda):=\frac{v_L\lambda^2}{2(1-b_L\lambda/3)},M_n(\lambda):=\mathrm{exp}\big(\lambda S_n-n\psi_L(\lambda)\big).\)

_Then_ \(\{M_n(\lambda)\}_{n\ge 0}\) _is a nonnegative supermartingale._

_Proof._ Since E\[_X<sub>i</sub>_\]=0, \(\mathrm{Var}(X_i)\le v_L\), and \(|X_i|\le b_L\) by Lemma 15, the standard Bernstein mgf bound yields

\(\mathbb{E}[e^{\lambda X_i}]\le\mathrm{exp}\big(\frac{v_L\lambda^2}{2(1-b_L\lambda/3)}\big)=e^{\psi_L(\lambda)}\text{for all}\lambda\in[0,3/b_L).\)

Therefore, conditioning on _X_<sub>1</sub>_,...,X_<sub>_n_-1</sub>,

\(\mathbb{E}[M_n(\lambda)|X_1,\dots,X_{n-1}]=\mathbb{E}\big[\mathrm{exp}\big(\lambda S_{n-1}+\lambda X_n-n\psi_L(\lambda)\big)|X_1,\dots,X_{n-1}\big]\)<br>
\(=M_{n-1}(\lambda)e^{-\psi_L(\lambda)}\mathbb{E}[e^{\lambda X_n}]\)<br>
\(\le M_{n-1}(\lambda).\)

Thus \(\{M_n(\lambda)\}_{n\ge 0}\) is a supermartingale. Since \(M_n(\lambda)\) is an exponential of a real-valued random variable, it is strictly positive almost surely, hence nonnegative.

