## 4.5. The limiting variational formula.

For \(\rho\in(0,1)\) define

\(\Phi(\rho):=sup\big\{H(\nu)+\mathbb{E}_\nu[logw(a,b)]:\text{supp}(\nu)\subseteq\{(a,b):1\le b\le a\},\) (4.15)

\(|\text{supp}(\nu)|<\infty,\mathbb{E}_\nu[a]=\frac{1}{\alpha\rho},\mathbb{E}_\nu[b]=\frac{1}{\rho}\big\}.\)

**Lemma 4.7** (Bounded-atom correction)**.** _Fix_ \(\alpha\in(0,1)\)_. The following holds for all sufficiently large M. Let_ \(L\in\{1,\dots,M\}\) _and let_ \((X_1,\dots,X_L)\in\mathcal{S}_{L-1}(N,M)\)_, with X<sub>k</sub>_=(_a<sub>k</sub>,b<sub>k</sub>_) _and empirical measure_ \(\mu=\frac{1}{L}\sum_{k=1}^L\delta_{X_k}\)_. Then there exists an index k<sub>⋆</sub> with_

(4.16) \(2\le b_{k_\star}\le a_{k_\star}.\)

_Define a modified tuple_ \(\big(X'_1,\dots,X'_L\big)\) _by setting_<tbc>

\(X'_{k_\star}:=\big(a_{k_\star}-1,b_{k_\star}-1\big);X'_k:=X_k\text{\textit{for}}k\neq k_\star,\)

<tbc>_and let_ \(\widehat{\mu}\) _be its empirical measure. Then_<tbc>

\(\mathbb{E}_\widehat{\mu}[a]=\frac{N}{L};\mathbb{E}_\widehat{\mu}[b]=\frac{M}{L}.\)

<tbc>_Moreover, writing_ \(K_M:=\frac{(N+1)(N+2)}{2}\) _for the alphabet size, we have_

(4.17) \(\big|H(\widehat{\mu})-H(\mu)\big|\le\frac{1}{L}log(K_M-1)+h\left(1/L\right),\)

_and_

(4.18) \(\big|\mathbb{E}_\widehat{\mu}[logw]-\mathbb{E}_\mu[logw]\big|\le\frac{1}{L}max_{2\le b\le a\le N+1}\big|logw(a,b)-logw(a-1,b-1)\big|.\)

_In particular, uniformly over_ \(L\in\{1,\dots,M\}\)_, as_ \(M\rightarrow\infty\),

(4.19) \(\frac{L}{N}\big(H(\widehat{\mu})+\mathbb{E}_\widehat{\mu}[logw]\big)=\frac{L}{N}\big(H(\mu)+\mathbb{E}_\mu[logw]\big)+o(1).\)

_Proof._ The existence of an atom satisfying (4.16) follows since \(L\le M\) and

\(\sum_{k=1}^Lb_k=M+1.\)

Replacing (_a,b_) by (_a_-1_,b_-1) decreases the total sums by (1,1), hence changes (_N_+1_,M_+1) to (_N,M_), giving the mean identities. For (4.17), note that \(\mu\) and \(\widehat{\mu}\) are supported on an alphabet of size \(\le K_M\) and differ in total variation by at most 1_/L_ (one count is moved from one symbol to another), so the explicit Fannes-Audenaert bound gives the stated inequality. Since only one atom is changed, (4.18) is immediate. Finally, using _K<sub>M</sub>=O(M_<sup>2</sup>),

\(max_{2\le b\le a\le N+1}\big|logw(a,b)-logw(a-1,b-1)\big|=O(logM),\)

and \(h(1/L)\checkmark(logL)/L\), we obtain

\(\frac{L}{N}\big|H(\widehat{\mu})-H(\mu)\big|\le\frac{1}{N}log(K_M-1)+\frac{L}{N}h(1/L)=o(1),\)<br>
\(\frac{L}{N}\big|\mathbb{E}_\widehat{\mu}[logw]-\mathbb{E}_\mu[logw]\big|\le\frac{1}{N}max_{2\le b\le a\le N+1}\big|logw(a,b)-logw(a-1,b-1)\big|=o(1),\)

which yields (4.19). □

