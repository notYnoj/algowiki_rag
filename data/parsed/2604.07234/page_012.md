<tbc>_skips_ that the _i_th bit of _Y_ plays over the greedy algorithm when constructing \(\sigma\). This mapping from \(S_{X^\prime,Y}\) to skip vectors \(v\in\mathbb{N}^M\) is evidently injective. Furthermore, for each \(s\in\mathbb{N}\), we define<tbc>

\(\mathcal{V}_s:=\left\{v\in\mathbb{N}^M:\sum_{i=1}^Mv_i=s\right\}.\)

<tbc>It similarly follows that for any \(v\in\mathcal{V}_s\), the event that _v_ is a skip vector corresponding to a configuration in \(S_{X^\prime,Y}\) is the event that the sum of _M+s_ i.i.d. Geom(1/2) random variables is at most _N_. Here, each Geom(1/2) random variable corresponds to the number of bits of \(X'\) necessary to advance the candidate embedding with skip vector _v_ by one step. We conclude that

\(Z_{X^\prime,Y}=\sum_{s=0}^{(1/\alpha-1)M}\sum_{v\in\mathcal{V}_s}\unknown\left\{v\text{corresponds to an elmt. of}S_{X^\prime,Y}\right\}\ge\sum_{s=0}^{\left(\frac{1}{2\alpha}-1\right)M}\sum_{v\in\mathcal{V}_s}\unknown\left\{\sum_{i=1}^{M+s}\text{Geom}(1/2)\le N\right\}\ge e^{-o_p(N)}\sum_{s=0}^{\left(\frac{1}{2\alpha}-1\right)M}\left|\mathcal{V}_s\right|\approx e^{-o_p(N)}\big|\mathcal{V}_{\left(\frac{1}{2\alpha}-1\right)M}\approx e^{-o_p(N)}exp\left(M\cdot\frac{h(2\alpha)}{2\alpha}\right)=e^{-o_p(N)}exp\left(N\cdot\frac{h(2\alpha)}{2}\right),\text{(2.1)}\)

where the latter inequality of (2.1) follows from Cramér’s theorem applied to the Geom(1/2) law and Markov’s inequality to control the number of "bad summands." The lower bound of (1.8) follows.

It remains to prove (1.7). Our strategy is guided by the observation that \(Z_{X^\prime,Y}\) exhibits an approximate superadditivity due to its self-replicating structure. For large integers _M_<sub>1</sub> and _M_<sub>2</sub>, the inequality

(2.2) \(logZ_{X_{1:N_1+N_2}^\prime Y_{1:M_1+M_2}}\ge logZ_{X_{1:N_1}^\prime,Y_{1:M_1}}+logZ_{X_{N_1+1:N_1+N_2}^\prime,Y_{M_1+1:M_1+M_2}},\)

holds whenever each partition function in (2.2) is positive. We partition \(S_{X^\prime,Y}\) by partitioning \(X'\) and _Y_ into contiguous blocks and grouping embeddings according to how blocks of _Y_ are matched to blocks of \(X'\). To handle dependencies across these classes, we restrict to an extremal class of this partition and argue that this choice is enough to fully capture the typical exponential behavior of \(Z_{X^\prime,Y}\).

We define the collection of _assignments_, corresponding to weak compositions of _N_ into \(\sqrt{M}\) parts, via<tbc>

\(\mathcal{A}=\mathcal{A}_N:=\left\{\mu:[\sqrt{M}]\rightarrow[N]\big|\sum_{i=1}^{\sqrt{M}}\mu(i)=N\right\}.\)

<tbc>Corresponding to \(\mu\in\mathcal{A}\) is a decomposition of \(X'\) given by<tbc>

\(X'=X'_\mu^\prime(1)X'_\mu^\prime(2)\cdots X'_\mu^\prime(\sqrt{M}).\)

<tbc>For \(i\in[\sqrt{M}]\), the _block_ \(X'_\mu^\prime(i)\) induced by \(\mu\) is a contiguous sequence of \(\mu(i)\) bits of \(X'\), with the superscript respecting the order in which the bits appear in _Y_ . Letting \(\bar{\nu}:[\sqrt{M}]\rightarrow[M]\) denote the map with \(\bar{\nu}(i)=\sqrt{M}\) for all \(i\in[M]\), we may decompose _Y_ analogously. For \(\mu\in\mathcal{A}\), the number of embeddings of _Y_ as a subsequence of \(X'\) for which \(Y_\bar{\nu}^{(i)}\) is _assigned_ to \(X'_\mu^\prime(i)\) is then

(2.3) \(Z_{X^\prime,Y}(\mu):=\prod_{i=1}^{\sqrt{M}}Z_{X_\mu^\prime(i),Y_\bar{\nu}^{(i)}}.\)

We focus on the following two kinds of assignments.

\(\bullet\) We let \(\mu^*\) denote the (random) extremal assignment maximizing \(Z_{X^\prime,Y}(\mu)\).<tbc>

\(\bullet\) We let \(\bar{\mu}\) denote a "baseline" for which \(\bar{\mu}(i)=N/\sqrt{M}\) for all \(i\in[\sqrt{M}]\).

