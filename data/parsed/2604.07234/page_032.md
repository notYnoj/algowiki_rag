<tbc>**Lemma 4.4** (Subexponential number of relevant types)**.** _We have_ \(lim_{M\rightarrow\infty}\frac{1}{N}log|\mathcal{I}_M|=0\).

_Proof._ By Lemma 4.3, any feasible \(\mu\in\mathcal{M}_L\) has \(|supp(\mu)|\le s_M\) where _s<sub>M</sub>_ is the RHS of (4.11). For each \(s\le s_M\), the number of choices of a support set \(D\subseteq\mathcal{A}_M\) of size _s_ is \(\genfrac(){pt}{2}{K_M}{s}\), and given _D_, the number of positive multiplicity vectors \((n_x)_{x\in D}\) with \(\sum_{x\in D}n_x=L\) is \(\genfrac(){pt}{2}{L-1}{s-1}\). Hence the number of possible \(\mu\) satisfies<tbc>

\(|\mathcal{I}_M|\le\sum_{L=1}^M\sum_{s=1}^{\lfloor s_M\rfloor}\genfrac(){pt}{2}{K_M}{s}\genfrac(){pt}{2}{L-1}{s-1}.\)

<tbc>Using \(\genfrac(){pt}{2}{K}{s}\le(eK/s)^s\) and the subadditivity of log yields

\(log|\mathcal{I}_M|\le s_M\cdot O(logM),\)

and since _s<sub>M</sub>=O(M_<sup>2/3</sup>) while \(N=M/\alpha\), we get \((1/N)log|\mathcal{I}_M|\rightarrow 0\). □

## 4.4.3. _Entropy replacement and sum-to-sup._

**Proposition 4.5** (Entropy replacement at scale _N_)**.** _Fix_ \(\alpha\in(0,1)\)_. There exists an explicit deterministic_ \(\delta_M=\delta_M(\alpha)\) _with_ \(\delta_M/N\rightarrow 0\) _such that_<tbc>

(4.13) \(e^{-\delta_M}\widetilde{Z}^{\le M}\le\overline{Z^{\le M}}\le e^{\delta_M}\widetilde{Z}^{\le M}.\)

<tbc>_Proof._ Fix an admissible summand \((L,\mu)\) in (4.7) and write \(D=\{n_{a,b}\ge 1\}\), _s_=|_D_|. By Lemma 4.2,<tbc>

\(log|\mathcal{S}_{L-1}(\mu)|=LH(\mu)+\Delta_L(\mu)\)

<tbc>with \(\Delta_L(\mu)\) given by (4.9). Since \(1\le n_{a,b}\le L\le M\) on _D_, (4.10) implies<tbc>

\(|\Delta_L(\mu)|\le\frac{s+1}{2}log(2\pi M)+\frac{s}{12}+\frac{1}{12}.\)

<tbc>By Lemma 4.3, \(s\le s_M:=\frac{1}{2}(\sqrt{3(N+1)}+2)^2\) for every feasible \(\mu\), so \(|\Delta_L(\mu)|\le\delta_M\) with<tbc>

\(\delta_M:=\frac{s_M+1}{2}log(2\pi M)+\frac{s_M}{12}+\frac{1}{12},\frac{\delta_M}{N}\rightarrow 0.\)

<tbc>Thus, it holds uniformly over all admissible \((L,\mu)\) that

\(e^{-\delta_M}e^{LH(\mu)}\le|\mathcal{S}_{L-1}(\mu)|\le e^{\delta_M}e^{LH(\mu)}.\)

Multiplying by \(e^{L\mathbb{E}_\mu[logw]}\) and summing gives (4.13). □

**Proposition 4.6** (Sum to supremum)**.** _We have_

(4.14) \(\frac{1}{N}log\overline{Z^{\le M}}=sup_{(L,\mu)\in\mathcal{I}_M}\frac{L}{N}\big(H(\mu)+\mathbb{E}_\mu[logw(a,b)]\big)+o(1).\)

_Proof._ Let \(\widetilde{T}_M(L,\mu):=exp(LH(\mu)+L\mathbb{E}_\mu[logw])\). Since all summands are nonnegative,<tbc>

\(sup_{(L,\mu)\in\mathcal{I}_M}\widetilde{T}_M(L,\mu)\le\widetilde{Z}^{\le M}\le|\mathcal{I}_M|\cdot sup_{(L,\mu)\in\mathcal{I}_M}\widetilde{T}_M(L,\mu).\)

<tbc>Taking logs, dividing by _N_, and using Lemma 4.4 yields

\(\frac{1}{N}log\widetilde{Z}^{\le M}=sup_{(L,\mu)\in\mathcal{I}_M}\frac{L}{N}\big(H(\mu)+\mathbb{E}_\mu[logw]\big)+o(1).\)

Combine with Proposition 4.5 and \(\delta_M/N\rightarrow 0\) to replace \(\widetilde{Z}^{\le M}\) by \(\overline{Z^{\le M}}\). □

