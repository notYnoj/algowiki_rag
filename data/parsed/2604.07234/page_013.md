<tbc>We work under the convention that log0:=0. It will suffice to derive the weak law in this setting, as it can be easily shown that the probability that \(Z_{X^\prime,Y}=0\) vanishes. Altogether, we have that

(2.4) \(Z_{X^\prime,Y}=O\left(|\mathcal{A}|\right)\cdot Z_{X^\prime,Y}(\mu^*)=e^{\tilde{O}\big(\sqrt{N}\big)}\prod_{i=1}^{\sqrt{M}}Z_{X_{\mu^*}^{^\prime(i)},Y_\tilde{\nu}^{(i)}}.\)

For \(i\in[\sqrt{M}]\), the event \(Z_{X_\tilde{\mu}^{^\prime(i)},Y_\tilde{\nu}^{(i)}}=0\) corresponds to the event that a sum of \(\sqrt{M}\) i.i.d. Geom(1/2) random variables is greater than \(N/\sqrt{M}=\sqrt{M}/\alpha\). Thus, where the following (2.5) relies crucially on the assumption that \(\alpha<1/2\),

(2.5) \(\mathbb{P}\left(\bigcup_{i\in[\sqrt{M}]}\left\{Z_{X_\tilde{\mu}^{^\prime(i)},Y_\tilde{\nu}^{(i)}}=0\right\}\right)^{(\text{Hoeffding})}e^{-\Omega(\sqrt{N})}\checkmark 1.\)

Rearranging (2.4) and invoking (2.5) yields, where the _o<sub>p</sub>_(1) term is _O_(1),

(2.6) \(\frac{1}{M}logZ_{X^\prime,Y}=\frac{1}{M}\sum_{i=1}^{\sqrt{M}}logZ_{X_\tilde{\mu}^{^\prime(i)},Y_\tilde{\nu}^{(i)}}+\frac{1}{M}\underbrace{\left(logZ_{X^\prime,Y}(\mu^*)-logZ_{X^\prime,Y}(\bar{\mu})\right)}_{\ge 0}+\tilde{O}\big(N^{-1/2}\big)+o_p(1).\)

**Remark 2.1.** We comment that fractional lengths (e.g., note that \(\bar{\nu}(i)=\sqrt{M}\) may not be an integer) are a benign issue throughout the argument and do not affect the asymptotics. The adjustment to the argument presented below is to take floors for every fractional length and to have the final multiplicand in (2.3) become a larger "remainder block." We omit the routine modifications here. \(\triangle\)

We are now ready to prove Lemma 2.2, an analogous convergence result in expectation.

**Lemma 2.2.** _The expression_ \(\frac{1}{N}\mathbb{E}[logZ_{X^\prime,Y}]\) _converges to a constant._

_Proof of Lemma 2.2._ It suffices to prove Lemma 2.2 when normalizing by _M_ instead of _N_. We first restrict our attention to those values of _M_ in the collection<tbc>

\(\mathcal{S}:=\{2,4,16,256,\dots\}.\)

<tbc>From (2.5) and (2.6), it follows for \(M\ge 4\) from S that

(2.7) \(\frac{1}{M}\mathbb{E}\left[logZ_{X^\prime,Y}\right]\ge\frac{\sqrt{M}}{M}\mathbb{E}\left[logZ_{X_\tilde{\mu}^{^\prime(1)},Y_\tilde{\nu}^{(1)}}\right]-e^{-\Omega(\sqrt{N})}=\frac{1}{\sqrt{M}}\mathbb{E}\left[logZ_{X_{1:\sqrt{M}/\alpha}^\prime,Y_{1:\sqrt{M}}}\right]-e^{-\Omega(\sqrt{N})}.\)

Let _C,c\>_0 be such that the exponential term in the RHS of (2.7) is at most \(Ce^{-c\sqrt{M}}\) for all _M_ considered. It follows that for \(M\in\mathcal{S}\), the sequence<tbc>

\(\frac{1}{M}\mathbb{E}\left[logZ_{X^\prime,Y}\right]+\sum_{M^\prime\in\mathcal{S}:M^\prime\le M}Ce^{-c\sqrt{M^\prime}}\)

<tbc>is increasing. This sequence is also uniformly bounded since \(e^{-\Omega(\sqrt{N})}\) is summable and

\(\frac{1}{M}\mathbb{E}\left[logZ_{X^\prime,Y}\right]\le\frac{1}{M}log\genfrac(){pt}{2}{N}{M}=O(1),\)

so it converges. We conclude that the sparse subsequence \(\frac{1}{M}\mathbb{E}[logZ_{X^\prime,Y}]\) on \(M\in\mathcal{S}\) converges.

We now extend the result to all values of _M_. We define the iterated square root

\(\phi(M)=\left\{\begin{array}{ c c }
0 & M\le 2 \\
1+\phi(\sqrt{M}) & M>2
\end{array}\right.\)

