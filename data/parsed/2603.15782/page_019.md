**Lemma 20** (Lipschitz approximation of Gaussian projections)**.** _There exists function_ \(L=L(c,\Delta,\theta,\Gamma,\beta)\) _with_ \(L=\Theta_{c,\Delta,\theta,\Gamma}(\sqrt{\beta})\) _with the following property: for a given set of parameters_ \(c,\Delta,\theta,\Gamma,\beta,\mu\) _there exists a set_ \(\widehat{S}\subseteq S^*\) _with_ \(|\widehat{S}|\ge(1-\theta)|S^*|\) _such that, for a standard Gaussian vector u_∼N(0_,I<sub>d</sub>), there is an L-Lipschitz function_ \(H_u:(V,\varrho)\rightarrow\mathbb{R}\) _satisfying_

\(\mathbb{E}_u\big|H_u(x)-\langle u,x\rangle\big|\le 2\sqrt{\Delta}(x\in\widehat{S}).\) (13)

_In particular, if_ \(w(e)=\infty\) _for all_ \(e\in E\)_, it suffices that_ \(\beta_v(G)\le\beta\).

_Proof._ Note first that if \(w(e)=\infty\) for all \(e\in E\), then \(\eta_{xy}=0\) for all \(xy\in E\) since (9) is finite (and hence \(\varrho\) has edge lengths \(\xi_{xy}=\eta_x+\eta_y\)).

Put \(r=\Gamma/4\). Apply the padding bound to \((V,\varrho)\) with diameter bound _D_=1/2. Call a terminal padded if its entire \(\varrho\)-ball of radius 2_r_ lies in its part. The padding bound gives this event probability at least \(e^{-\Gamma\beta}\), since \(2r=\Gamma/2\); using radius _r_ for the cores below leaves positive slack. Take \(M=\lceil e^{\Gamma\beta} ln(1/\theta)\rceil\) independent partitions. Each terminal is unpadded in all of them with probability at most \((1-e^{-\Gamma\beta})^M\le\theta\). Hence there exist _M_ partitions of _V_ such that at least \((1-\theta)|S^*|\) terminals of _S_<sup>∗</sup> are padded in at least one partition. Denote these fixed partitions by P<sub>1</sub>_,...,_P_<sub>M</sub>_, and let \(\widehat{S}\) be the set of such terminals.

Set<tbc>

\(L=\frac{2\sqrt{8ln(16M/(c\Delta))}}{r\sqrt{c}}=\Theta(\sqrt{\beta}),b=Lr/2.\)

<tbc>For every part \(P\in\bigcup_{j=1}^M\mathcal{P}_j\), define its _core_ by<tbc>

\(P^\text{\texttt{core}}=\{x\in P\cap S^*:\varrho(x,V-P)\ge r\}\)

<tbc>Let<tbc>

\(\Pi:=\left\{P\in\bigcup_{j=1}^M\mathcal{P}_j:P^\text{\texttt{core}}\neq\varnothing\right\},\)

<tbc>and choose a representative \(x_P\in P^\text{\texttt{core}}\) for each \(P\in\Pi\). Since each part has \(\varrho\)-diameter at most 1/2, (12) gives<tbc>

\(\|x-x_P\|<\sqrt{\Delta}(P\in\Pi,x\in P\cap S^*).\)

<tbc>Let _h<sub>P</sub>_ be \(\langle u,x_P\rangle\) clipped to \[-_b,b_\], and define

\(H_u(x)=\frac{1}{2}min_{P\in\Pi}\{h_P+L\varrho(x,P^\text{\texttt{core}})\}+\frac{1}{2}max_{P\in\Pi}\{h_P-L\varrho(x,P^\text{\texttt{core}})\}.\) (14)

Both envelopes defining _H<sub>u</sub>_ are _L_-Lipschitz, and thus so is their midpoint _H<sub>u</sub>_.

Fix \(x\in\widehat{S}\) and let \(\Pi_x=\{P\in\Pi:x\in P\}\). Each of the _M_ partitions has exactly one part containing _x_, and thus \(1\le|\Pi_x|\le M\).

We claim that each extremum in (14) is attained at a possibly different part \(P\in\Pi_x\). Indeed, since _x_ is padded in some partition, there is \(\tilde{P}\in\Pi_x\) with \(x\in\tilde{P}^\text{\texttt{core}}\). We have \(h_\tilde{P}\pm L\varrho(x,\tilde{P}^\text{\texttt{core}})=h_\tilde{P}\pm 0\in[-b,b]\) for this \(\tilde{P}\). Now consider \(P\in\Pi-\Pi_x\). Pick \(y\in P^\text{\texttt{core}}\). We have \(x\in V-P\), so \(\varrho(x,y)\ge\varrho(y,V-P)\ge r\) by the definition of a core. Therefore, \(h_P+L\varrho(x,P^\text{\texttt{core}})\ge-b+Lr=b\) and \(h_P-L\varrho(x,P^\text{\texttt{core}})\le b-Lr=-b\). The claim follows.

Put \(d_P=L\varrho(x,P^\text{\texttt{core}})\) and define the unclipped local midpoint<tbc>

\(\widetilde{H}_u(x)=\frac{1}{2}min_{P\in\Pi_x}\{\langle u,x_P\rangle+d_P\}+\frac{1}{2}max_{P\in\Pi_x}\{\langle u,x_P\rangle-d_P\}.\)

<tbc>We have<tbc>

\(|H_u(x)-\langle u,x\rangle|\le\underbrace{|\widetilde{H}_u(x)-\langle u,x\rangle|}_{A(u)}+\underbrace{max_{P\in\Pi_x}(|\langle u,x_P\rangle|-b)_+}_{B(u)}.\)

