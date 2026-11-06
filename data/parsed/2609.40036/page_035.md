_Proof of the lower bound in Theorem 5._ Return to a common even distribution \(\theta\), so \(\Theta=\theta_\mathrm{max}\). Let \(\gamma=q/D^{2/3}\le 1/32\), put \(\delta=\delta_\mathrm{cyc}(D,\theta)\), and set \(p=(1-16\gamma)\delta\). Since \(q\ge 2\), we have \(D\ge 512\). The lower bound in (125) and \(\theta_\mathrm{max}\ge 1/(q-1)\) show that<tbc>

\(\delta\le\frac{q}{D^2}<\frac{1}{2},(D-1)Z_\theta(\delta)=1.\) (149)

<tbc>Indeed, at _p=q/D_<sup>2</sup> the lower bound \(2\sqrt{p(1-p)/(q-1)}\) is larger than 1/(_D_-1). Consequently,<tbc>

\(u\le\gamma D^{-1/3}\le\frac{1}{256},K^{1/3}<\frac{4}{3}\gamma,a_*\le\frac{64\gamma^2}{9q}\le\frac{1}{288}.\) (150)

<tbc>By (125), \((D-1)B_\Theta(\delta)\le 1+(D-1)\delta\). Comparing the square-root and linear terms in (124) gives

\(\frac{B_\Theta((1-16\gamma)\delta)}{B_\Theta(\delta)}\le\sqrt{\frac{1-16\gamma}{1-\delta}},\) (151)

\(\mathrm{log}R\le-8\gamma+\frac{\delta}{2(1-\delta)}+(D-1)\delta<-7\gamma.\) (152)

Here \(\delta\le\gamma D^{-4/3}\) and \((D-1)\delta\le\gamma D^{-1/3}\le\gamma/8\). The remaining terms in (142) obey

\(\frac{4a_*}{\gamma}\le\frac{4}{9},\frac{1}{\gamma}\sqrt{\frac{2qa_*}{1-a_*}}<3.8,\Psi(a_*)<5\gamma,\) (153)

and

\(8u+b_0K^{1/3}\le\gamma+\frac{4}{3}b_0\gamma<4\gamma.\) (154)

Thus (142) holds with strict slack, giving recovery and the stronger conclusion of Lemma 6. All its left-hand sides are nondecreasing functions of _p_ in this interval, so the result also holds at every smaller positive _p_. At _p_=0, growing girth gives the conclusion directly.

Finally, at the cycle crossing, (125) gives

\(\frac{1}{D-1}=2\sqrt{\delta(1-\delta)\theta_\mathrm{max}}+O(\delta).\) (155)

Uniformly for _q=o(D_<sup>2/3</sup>), (149) implies \((D-1)\delta=o(1)\) and hence \(\delta=(1+o(1))/(4\theta_\mathrm{max}D^2)\). Combining the lower bound just proved with the strong converse proves (76).

**Lemma 7** (From channel reliability to a cutoff)**.** _Fix independent nonzero-symbol distributions_ \(\theta_1,\dots,\theta_m\) _and use the lexicographically first minimum-Hamming-weight representative of each syndrome. Let R<sub>k</sub> be the probability under P<sub>k</sub> that the decoder fails on at least one word at Hamming distance at most one from the sampled error. Then R<sub>k</sub> is nondecreasing in k. For independent errors with_ \(\mathrm{Pr}(E_i=0)=1-p'\) _and_ \(\mathrm{Pr}(E_i=a)=p'\theta_i(a)\)_, write_ \(R(p')\) _for the same failure probability. If_ \(K\sim\mathrm{Bin}(m,p')\)_, then_

\(\mathrm{max}_{k\le\ell} R_k=R_\ell\le\frac{R(p')}{\mathrm{Pr}(K\ge\ell)}.\) (156)

_In particular, for fixed_ \(p<p'\)_, a vanishing_ \(R(p')\) _implies uniformly vanishing R<sub>k</sub> through_ \(\ell=\lfloor pm\rfloor\).

