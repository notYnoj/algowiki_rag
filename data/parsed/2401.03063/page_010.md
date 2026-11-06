Hence,

\(\mathrm{Var}S=\sum_{k=0}^{n-1}\int_0^1n\genfrac(){pt}{2}{n-1}{k}\alpha^k(1-\alpha)^{n-1-k}B_{k+1}\mathrm{d}\alpha=\sum_{k=0}^{n-1}B_{k+1}.\)

## 2.2 Connection with a semigroup approach

The semigroup approach, as developed in \[18\] for the hypercube, boils down to the same integration along \(\alpha\) trick. We need first to rewrite our results in a more general setup: we assume the _X<sub>i</sub>_’s to be i.i.d. discrete variables, taking a finite number of values and this time, _S_ takes values in a Banach space \((E,\|\cdot\|_E)\). We also consider a continuous convex function \(\Phi:E\rightarrow\mathbb{R}^+\), so instead of considering \(\mathrm{Var}S=\mathbb{E}\|S-\mathbb{E}S\|_E^2=\|S-\mathbb{E}S\|_{E,2}^2\), we consider \(\mathbb{E}\left(\Phi(S-\mathbb{E}S)\right)\). The price to pay is a suboptimal constant, as seen next, and the lack of connection with the _B<sub>k</sub>_’s, which do not seem to have any equivalent in this setup. We hope that making this connection casts a new light on the breakthrough \[18\], but also gives prospects to generalize it: indeed, while it is not clear what would be the adequate semigroup when the _X<sub>i</sub>_’s are not binary variables, our theorem works for all discrete distributions with finite support (and it is straightforward to generalize to all discrete distributions or even bounded continuous distributions). It should also be pointed that, motivated by geometric applications, the case of the biased cube was also recently studied by different methods in \[7\].

**Theorem 2.1.** _For any_ \(\alpha\in(0,1)\)_, let_ \(\varepsilon_1(\alpha),\dots,\varepsilon_n(\alpha)\) _be i.i.d. random variables such that_ \(\mathbb{P}(\xi_i(\alpha)=1)=1-\alpha,\mathbb{P}(\xi_i(\alpha)=-1)=\alpha\)_, and let_ \(\delta_i(\alpha)=(\xi_i(\alpha)-\mathbb{E}\xi_i(\alpha))/\sqrt{Var\xi_i(\alpha)}\)_. Then,_

\(\mathbb{E}(\Phi(S-\mathbb{E}S))\le\int_0^1\mathbb{E}\Phi\left(\pi\sum_{i=1}^n\delta_i(\alpha)d_iS(X)\right)\frac{\mathrm{d}\alpha}{\pi\sqrt{\alpha(1-\alpha)}}.\)

_Proof._ Firstly, without loss of generality, we may assume E_S_=0 (one may check all the following results are true when one adds a constant to _S_). Following \[18\], denoting by \(\Phi^*\) the convex conjugate of \(\Phi\), we note that for any \(x\in E\),

\(\Phi(x)=\mathrm{sup}_{y\in E^*}\left(\langle y,x\rangle-\Phi^*(y)\right),\)

and therefore, since the _X<sub>i</sub>_’s only take a finite number of values,

\(\mathbb{E}(\Phi(S-\mathbb{E}S))=\mathrm{sup}_{T\text{is}\sigma(X_1,\dots,X_n)-\text{measurable, taking values in}E^*}\mathbb{E}(\langle T,S\rangle-\Phi^*(T)).\) (2.4)

We now bound the term \(\mathbb{E}(\langle T,S\rangle-\Phi^*(T))\). As in (2.1),

\(\mathbb{E}(\langle T,S\rangle-\Phi^*(T))=-\int_0^1\frac{\mathrm{d}}{\mathrm{d}\alpha}\left(\mathbb{E}(\langle T,S(X^{(\alpha)})\rangle\right)\mathrm{d}\alpha-\mathbb{E}\Phi^*(T)),\)

and just like in obtaining (2.2), we get<tbc>

\(\mathbb{E}(\langle T,S\rangle-\Phi^*(T))=\int_0^1\mathbb{E}(\langle T,\sum_{i=1}^nS(X^{(\alpha),i})-S(X^{(\alpha),\hat{i}}))\rangle\mathrm{d}\alpha-\mathbb{E}\Phi^*(T).\)

<tbc>Note that<tbc>

\(S(X^{(\alpha),i})-S(X^{(\alpha),\hat{i}})=d_iS(X^{(\alpha),i})-d_iS(X^{(\alpha),\hat{i}}),\)

<tbc>and by independence,<tbc>

\(\mathbb{E}(\langle T,d_iS(X^{(\alpha),\hat{i}})\rangle)=0,\)

<tbc>so

\(\mathbb{E}(\langle T,S\rangle-\Phi^*(T))=\sum_{i=1}^n\int_0^1\mathbb{E}(\langle T,d_iS(X^{(\alpha),i})\rangle\mathrm{d}\alpha-\mathbb{E}\Phi^*(T).\) (2.5)

