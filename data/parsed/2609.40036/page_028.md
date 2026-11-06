i.e. with probability tending to 1). It proceeds in up to _D_-2 successive _rounds_, where round \(k\in\{3,\dots,D\}\) corresponds to adding a random matching _M_<sub>_k_-2</sub> appearing in (64). If completed, this round takes the process from a (_k_-1)-regular graph to a _k_-regular graph.

We require the following uniform lower bound on the degree of vertices in _H<sub>t</sub>_. Its proof relies on various intermediate results in \[LS20\].

**Lemma 1** (Uniform density along a round)**.** _Consider a round from degree k_-1 _to degree k, where_ \(3\le k\le D\)_. For any a\>_0_, let_ A_<sub>n</sub> denote the event that every state of the round satisfies_

\(d_{\mathscr{A}_t}(v)\ge(1-\zeta_n)(|W_t|-1)(v\in W_t),\zeta_n=n^{-a}.\) (99)

_Then, there exists a constant a=a(D,c)\>_0 _such that_ Pr\[A_<sub>n</sub>_\]=1-_o_(1) _uniformly over all_ (_k_-1)_-regular graphs of girth at least g at the start of the round. Moreover,_ A_<sub>n</sub> implies saturation._

**Remark 1.** _The proof of the Lemma mirrors the general strategy employed in the proof of \[LS20, Proposition 2.1\]. It splits the round into intervals using a finite sequence of moments t_<sub>0</sub>_,t_<sub>1</sub>_,...,t<sub>m</sub> engineered so that_ \(|W_{t_{j+1}}|=|W_{t_j}|n^{-\alpha}\)_. This is achieved by exploiting the fact that if the process is not frozen, then_ |_W<sub>t</sub>_|=_n_-2_t. To prove the process does not freeze before the end of the round, the proof uses induction and the notion of C-path-boundedness, introduced in \[LS20, Definition 2.10\]. Note that this conclusion cannot be obtained by conditioning on saturation, which is a future event._

_Proof._ Set

\(c_0=\frac{1+c}{2},\epsilon=\frac{c_0(1-c_0)}{3},\alpha=\frac{\epsilon}{1000},a=\frac{\epsilon}{3},\) (100)

so that \(g\le c_0log_{k-1}n\) and _c_<sub>0</sub>_\>_1/2. We split the round into intervals, one initial, one terminal, and \(m=\left\lceil\frac{c_0}{\alpha}\right\rceil\le\frac{1}{\alpha}=O(1)\) intervening ones, that meet at times _t<sub>j</sub>_, defined recursively as

\(t_0=\left\lceil\frac{1}{2}\left(n-n^{c_0+\epsilon}\right)\right\rceil,t_j=\left\lceil\frac{1}{2}\left(n-(n-2t_{j-1})n^{-\alpha}\right)\right\rceil\) (101)

for _j_=1_,...,m_. We will prove that (99) holds w.h.p. for all times in each interval.

Fix \(t\in\{0,\dots,t_0\}\) in the first interval. A pair \(\{u,v\}\subset W_t\) is available in A_<sub>t</sub>_ if and only if \(\delta_{G_t}(u,v)\ge g-1\). But _G<sub>t</sub>_ has maximum vertex degree _k_, so the number of forbidden partners for \(v\in W_t\) satisfies the Moore bound, \[LS20, Observation 2.2\]<tbc>

\(|W_t\backslash\mathscr{A}_t(v)|\le\sum_{\ell=0}^{g-3}k(k-1)^\ell=O_k((k-1)^{g-2})=O_k(n^{c_0}).\) (102)

<tbc>By \[LS20, Lemma 2.3\], we have \(|W_{t_0}|=n-2t_0=n^{c_0+\epsilon}-O(1)\), so<tbc>

\(\frac{|W_t\backslash\mathscr{A}_t(v)|}{|W_t|-1}\le\frac{O(n^{c_0})}{n^{c_0+\epsilon}-O(1)}=O(n^{-\epsilon})\le\zeta_n\) (103)

<tbc>and thus

\(d_{\mathscr{A}_t}(v)\ge(1-\zeta_n)(|W_t|-1)\) (104)

for all \(t\in\{0,\dots,t_0\}\). Moreover, by \[LS20, Lemma 2.9\], _G_<sub>_t_<sub>0</sub></sub> is _C_<sub>0</sub>-path-bounded with _C_<sub>0</sub>=3 w.h.p.

Fix \(j\in\{0,\dots,m-1\}\) and assume _G<sub>t<sub>j</sub></sub>_ is _C<sub>j</sub>_-path-bounded. For any \(t\in\{t_j,\dots,t_{j+1}\}\) and \(v\in W_t\), a vertex \(u\in W_t\) is forbidden for _v_ in _G<sub>t</sub>_ only if \(\delta_{G_t}(u,v)\le g-2\), which occurs only if<tbc>

