## A Basic lemmas

**Lemma 2.12.** _Let_ \(f:D\rightarrow\mathbb{R}_{\ge 0}\cup\{\infty\}\) _be a function. For any set_ \(S\subseteq D\) _where_ (G_<sub>f</sub>_)<sub>|_S_</sub> _is defined, it is the unique choice that minimizes_ E<sub>_x_∼D<sub>|_S_</sub></sub>\[_f(x_)\]-S(D<sub>|_S_</sub>) _over all distributions supported on S._

_Proof._ Observe that

\(\mathbb{E}_{x\sim\mathcal{D}_{|S}}[f(x)]-\mathcal{S}(\mathcal{D}_{|S})=\mathbb{E}_{x\sim\mathcal{D}_{|S}}[f(x)+log_{\mathcal{D}_{|S}}Pr[x]]\)<br>
\(=\mathbb{E}_{x\sim\mathcal{D}_{|S}}[log(Pr_{\mathcal{D}_{|S}}[x]/2^{-f(x)})]\)<br>
\(=\mathbb{E}_{x\sim\mathcal{D}_{|S}}[log(Pr_{\mathcal{D}_{|S}}[x]/Pr_{(\mathcal{G}_f)_{|S}}[x])]-log\left(\sum_{x\in S}2^{-f(x)}\right)\)<br>
\(=D_\text{KL}(\mathcal{D}_{|S}||(\mathcal{G}_f)_{|S})-log\left(\sum_{x\in S}2^{-f(x)}\right).\)

By Proposition 2.10, we know that _D_<sub>KL</sub>(D<sub>|_S_</sub>||(G_<sub>f</sub>_)<sub>|_S_</sub>) and hence E<sub>D<sub>|_S_</sub></sub>\[_f(x_)\]-S(D<sub>|_S_</sub>) is minimized exactly when Pr<sub>D<sub>|_S_</sub></sub>\[_x_\]=Pr<sub>(G_<sub>f</sub>_)<sub>|_S_</sub></sub>\[_x_\] for every \(x\in S\).

**Lemma 2.22.** _Let g be a gate in a circuit computing a function_ \(f:D\rightarrow R\)_. A heat function_ \(Q:D\rightarrow\mathbb{R}_{\ge 0}\cup\{\infty\}\) _is valid for g if and only if, for every_ \(y\in R\),<tbc>

\(\sum_{x\in f^{-1}(y)}2^{-Q(x)}\le 1.\)

<tbc>_Proof._ By Definition 2.21 we know that _Q_ is valid precisely when<tbc>

\(max_\mathcal{D}\sum_{x\in supp(\mathcal{D})}Pr_\mathcal{D}[x]\left(log(Pr_{f(\mathcal{D})}[f(x)])-log(Pr_\mathcal{D}[x])-Q(x)\right)\le 0.\)

<tbc>Or equivalently when<tbc>

\(max_\mathcal{D}\sum_{y\in supp(f(\mathcal{D}))}Pr_{f(\mathcal{D})}[y]\left(\mathcal{S}(\mathcal{D}_{|f^{-1}(y)})-\mathbb{E}_{\mathcal{D}_{|f^{-1}(y)}}[Q(x)]\right)\le 0.\)

<tbc>By convexity, we can assume without loss of generality that the maximum D has Pr<sub>_f_(D)</sub>\[_y_\]=1 for some fixed choice of _y_. We can also assume that the maximum D has no probability mass on any _x_ where \(Q(x)=\infty\) unless _Q_ is \(\infty\) on every point and the validity condition is trivial. Additionally, by Lemma 2.12 we know that the maximal D<sub>|_f_<sup>-1</sup>(_y_)</sub> is (G_<sub>Q</sub>_)<sub>|_f_<sup>-1</sup>(_y_)</sub>. Thus the above is equivalent to the claim

\(max_ylog\left(\sum_{x\in f^{-1}(y)}2^{-Q(x)}\right)\le 0.\)

Taking 2 to the power of both sides of this inequality proves our desired bound.

