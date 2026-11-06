or equivalently

\(Z_\theta(p)=\mathrm{max}_{a\neq 0}\left\{2\sqrt{p(1-p)\theta(a)}+p\sum_{z\notin\{0,a\}}\sqrt{\theta(z)\theta(z-a)}\right\},\) (70)

which is non-decreasing for \(0\le p\le 1/2\). Hence, the natural branching condition is

\((D-1)Z_\theta(p).\) (71)

When this quantity is below one, the total contribution of long cycle-like competitors is summable, and reliability can hold. When it is above one, the graph contains exponentially many sufficiently independent cycle competitors, and their aggregate likelihood overwhelms the true error, giving a strong converse. This motivates the following definition.

\(\delta_\mathrm{cyc}(D,\theta):=\mathrm{inf}\{p\in[0,1/2]:(D-1)Z_\theta(p)\ge 1\},\) (72)

with value 1/2 if this set is empty.

We now prove the condition under which the whole-word decoding error rate goes to unity or vanishes. Define the _reliability threshold_

\(\delta_\mathrm{rel}(D,\theta):=\mathrm{sup}\left\{p\in[0,1/2]:\mathrm{lim}_{n\rightarrow\infty}\unknown_{G\sim\mathcal{L}_{n,D,c}}P_\mathrm{W}^\mathrm{ML}(G,p,\theta)=0\right\}.\) (73)

The limit is taken with _n_ even and other parameters fixed. For uniform \(\theta\), write \(\delta_\mathrm{rel}(D,q)\).

**Theorem 4** (ML strong converse)**.** _Fix_ \(D\ge 3\)_, a finite field_ \(\unknown_q\), \(c\in(0,1)\)_, and an even replacement distribution_ \(\theta\)_. For the Linial-Simkin ensemble and independent errors with distribution (58),_

\((D-1)Z_\theta(p)>1\Longrightarrow\unknown_GP_\mathrm{S}^\mathrm{ML}(G,p,\theta)\rightarrow 0,0<p\le 1/2.\) (74)

_In particular,_ \(\delta_\mathrm{rel}(D,\theta)\le\delta_\mathrm{cyc}(D,\theta)\)_. For uniform replacement, the same strong converse holds throughout_ \(\delta_\mathrm{cyc}(D,q)<p\le 1-q^{-1}\).

**Theorem 5** (Small-alphabet ML reliability)**.** _Fix_ \(c\in(0,1)\) _and an even replacement distribution_ \(\theta\) _on_ \(\unknown_q^\times\)_. For the Linial-Simkin ensemble, if_ \(\gamma=q/D^{2/3}\le 1/32\)_, then_

\((1-16\gamma)\delta_\mathrm{cyc}(D,\theta)\le\delta_\mathrm{rel}(D,\theta)\le\delta_\mathrm{cyc}(D,\theta).\) (75)

_Throughout the lower interval, a minimum-Hamming-weight syndrome decoder recovers the errors with probability tending to one, as does the optimal ML decoder. As_ \(D\rightarrow\infty\)_, uniformly over even_ \(\theta\) _and finite fields with q=o(D_<sup>2/3</sup>),

\(\frac{\delta_\mathrm{rel}(D,\theta)}{\delta_\mathrm{cyc}(D,\theta)}\rightarrow 1,\delta_\mathrm{rel}(D,\theta)=\frac{1+o(1)}{4\theta_\mathrm{max}D^2}.\) (76)

Both proofs are in Appendix A. The recovery proof also shows that, with probability tending to one, every word differing from the error in at most one coordinate is uniquely recovered by the minimum-weight decoder; see Lemma 6.

