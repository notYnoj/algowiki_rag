Note that \(0\in\mathrm{Sym}(A;\alpha)\) and \(\mathrm{Sym}(A;\alpha)=-\mathrm{Sym}(A;\alpha)\). Moreover, it holds that

\(|\mathrm{Sym}(A;\alpha)|\le\frac{|A|}{\alpha},\)

which follows readily from \(\sum_{x\in A-A}r_{A-A}(x)=|A|^2\). In the notation from before one can equivalently express the symmetry set as a set of popular differences, \(\mathrm{Sym}(A;\alpha)=\mathrm{Pop}(A,-A;\alpha|A|)\).

We need the following lemma corresponding to \[TV06, Lemma 2.34\].

**Lemma 7.2** (Dyadic Pigeonhole Principle)**.** _Let_ \(0<\alpha<1\) _and let_ \(A,D\subseteq\mathbb{Z}\) _be such that_<tbc>

\(\sum_{x\in D}r_{A-A}(x)\ge\alpha|A|^2.\)

<tbc>_Then there is a subset_ \(D'\subseteq D\) _such that, for every_ \(x\in D'\),

\(r_{A-A}(x)\ge\Omega\left(\frac{\alpha}{1+\mathrm{log}\frac{1}{\alpha}+\mathrm{log}(1+\frac{|D|}{|A|})}\cdot\frac{|A|^2}{|D'|}\right).\)

_Moreover, there is a randomized algorithm that, given A,_ \(\alpha\) _and D, computes such a set_ \(D'\) _in time_ \(\widetilde{O}(|A|+|D|/\alpha)\).

**Proof.** We first call Lemma 2.5 on the sets _A,-A,D_ with parameter \(\epsilon=\mathrm{min}(\frac{\alpha|A|}{8|D|},1)\) to approximate the multiplicities _r_<sub>_A-A_</sub>(_x_) for all \(x\in D\) by \(0\le\tilde{r}(x)\le|A|\) within additive error<tbc>

\(|r_{A-A}(x)-\tilde{r}(x)|\le\epsilon|A|=\frac{\alpha|A|^2}{8|D|}.\)

<tbc>Let<tbc>

\(D^*=\left\{x\in D:\tilde{r}(x)\ge\frac{\alpha|A|^2}{4|D|}\right\}.\)

<tbc>This set is chosen so that for all \(x\in D^*\) we have \(r_{A-A}(x)\ge\tilde{r}(x)/2\). Further observe that

\(\sum_{x\in D^*}\tilde{r}(x)\ge\sum_{x\in D}\tilde{r}(x)-\sum_{x\in D\backslash D^*}\tilde{r}(x)\)<br>
\(\ge\sum_{x\in D}\tilde{r}(x)-|D|\cdot\frac{\alpha|A|^2}{4|D|}\)<br>
\(\ge\sum_{x\in D}r_{A-A}(x)-|D|\cdot\frac{\alpha|A|^2}{8|D|}-|D|\cdot\frac{\alpha|A|^2}{4|D|}\)<br>
\(\ge\frac{\alpha|A|^2}{2}.\)

Now let _L_ be the smallest integer with \(2^{-L}<\frac{\alpha|A|}{2|D|}\), and consider the partition of _D_<sup>∗</sup> into _D_<sub>1</sub>_,...,D<sub>L</sub>_ defined by<tbc>

\(D_\ell=\left\{x\in D^*:\frac{|A|}{2^\ell}<\tilde{r}(x)\le\frac{|A|}{2^{\ell-1}}\right\}.\)

