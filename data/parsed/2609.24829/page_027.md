_Proof._ Note that for every edge _e_ we have \(t_e^O\sim\text{Bin}(t_e,p)\), so \(\mathbb{E}\left[t_E^O\right]=pt_e\). Suppose \(t_e^O<p\gamma\) yet \(t_e>2\gamma\). Then \(t_e^O<p\gamma\) implies \(t_e^O<(1/2)t_ep\) and by Chernoff,

\(Pr\left[t_e^O<p\gamma\right]\le Pr\left[t_e^O<(1/2)t_ep\right]\le exp\left(-\frac{(1/2)^2}{2}t_ep\right)\)<br>
\(\le exp\left(-\frac{1}{4}p\gamma\right)\le exp\left(-\frac{50\varepsilon^{-2}log(n)}{4}\right)\le n^{-10}.\)

On the other hand, suppose oracle(_e_)=H. We first show that _t<sub>e</sub>_ must be large. Suppose \(t_e<\gamma/2\), and therefore \(\mu:=\mathbb{E}\left[t_e^O\right]\le p\gamma/2\). We write \(p\gamma=(1+\kappa)\mu\) for a fitting \(\kappa>1\). Therefore by Chernoff

\(Pr\left[t_e^O\ge p\gamma\right]\le Pr\left[t_e^O\ge(1+\kappa)\mu\right]\le exp\left(-\frac{\kappa\mu}{3}\right)=exp\left(-\frac{p\gamma-\mu}{3}\right)\)<br>
\(\le exp\left(-\frac{p\gamma}{6}\right)\le exp\left(-\frac{50\varepsilon^{-2}log(n)}{6}\right)\le n^{-7}\)

so with high probability, \(t_e\ge\gamma/2\). The following follows from a standard two sided Chernoff bound conditioned on the above calculation:

\(Pr\left[|t_e^O-\mu|\ge\varepsilon\mu\right]\le 2exp\left(-\frac{\varepsilon^2}{3}\mu\right)\le 2exp\left(-\frac{50}{3}log(n)\right)\le n^{-7}\)

concluding the proof.

**Lemma A.1** (Oracle Guarantees)**.** With high probability, \(t_e^O=(1\pm\varepsilon)t_ep\) for all heavy edges _e_ and \(t_e\le 2\sqrt{\tau}\) for all light edges.

_Proof._ Note that for any edge _e_, we have \(t_e^O\sim\text{Bin}(t_e,p)\) where _p_ was defined to be \(p_{log(\sqrt{\tau})}=10\delta^{-1}\varepsilon^{-2}(logn)/\sqrt{\tau}\). The result follows from the Chernoff bound as in 4.2 and then taking the union bound over all edges.

The next lemma establishes that _P_, the set of potentially heavy edges we construct, will contain most of the edges that ultimately will be defined to be heavy by the oracle.

**Lemma A.2** (Missing Heavy Edges)**.** \(\sum_{e\in E^\mathbb{H}\backslash P}t_e\le\varepsilon T\) with probability at least \(1-\delta\).

_Proof._ First note that \(|E_\mathbb{H}|\le 4T/\sqrt{\tau}\) since, by Lemma A.1, if _e_ is heavy then \(t_e\ge p\sqrt{\tau}/(p(1+\varepsilon))=\sqrt{\tau}/(1+\varepsilon)\) and summing _t<sub>e</sub>_ over all heavy edges is at most 3_T_. Next we consider the probability a heavy edge is not in _P_. To do this, let \(i=\lceil log_2(\tau/(\delta^{-1}\varepsilon^{-2}t_e))\rceil\) and note that if _e_ does not appear within the first _q<sub>i</sub>im_ edges of the stream then the probability _e_ is not added to _P_ is at most

\((1-q_i^2p_i)^{t_e}\le e^{-t_eq_i^2p_i}\le e^{-t_e10\delta^{-1}\varepsilon^{-2}(logn)2^i/\tau}\le 1/n^{10}\)

because the events that different triangles are formed between _e_ and edges in _E<sub>i</sub>_ are negatively associated.

Therefore, the probability that we do not include heavy edge _e_ in _P_ is

\(Pr\left[e\in E^\mathbb{H}\backslash P\right]\le 1/n^{10}+Pr\left[e\text{appears in a prefix of length}q_im\right]\) (10)

\(=1/n^{10}+2^i/\sqrt{\tau}\le 2\cdot\frac{2\delta\sqrt{\tau}}{\varepsilon^{-2}t_e},\)

where we used the fact that 1_/n_<sup>10</sup> was dominated by the second term for sufficiently large _n_.

