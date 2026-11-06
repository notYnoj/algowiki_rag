_Proof._ By 4.2 with the threshold \(\gamma=n^{1/2^i}\), with probability 1-1_/n_<sup>3</sup>, \(t_e^O=(1\pm\varepsilon)t_ep_i\). We then note that

\(\widehat{T}_\mathrm{H}=p_i^{-1}\left(\sum_{e:\mathrm{oracle}(e)=\mathrm{H}}t_{e,1}^O+t_{e,2}^O/2+t_{e,3}^O/3\right)\)

and the result follows. The coefficients of \(t_{e,i}^O\) compensate for overcounting - a triangle that has _i_ heavy edges attached to it is counted _i_ times.

**Lemma 4.5** (Termination with \(t^3\widehat{T}_\mathrm{L}+\widehat{T}_\mathrm{H}\))**.** Suppose that during round _i_ P-PASS terminates and outputs \(t^3\widehat{T}_\mathrm{H}+\widehat{T}_\mathrm{L}\). Then with probability at least \(1-\delta-1/\mathrm{poly}(n)\) it is a \((1\pm\varepsilon)\) approximation of _T_.

_Proof._ Since _T=T_<sub>H</sub>+_T_<sub>L</sub>, we only need to show that \(t^3\widehat{T}_\mathrm{L}\in(1\pm\varepsilon)T_\mathrm{L}\). The proof is similar in structure to the proof of 3.4, however since we look over the stream _S_<sup>L</sup> and not _S_, the specifics change slightly.

Let \(\tau_j\) be the guess when \(\mathcal{A}(S_j^\mathrm{L},(1-\varepsilon)\tau_jt^{-3})\) outputs an estimate, and recall that that estimate is denoted \(\widehat{T}_\mathrm{L}\). There are two cases to check: The termination happened when \(\tau_j\) was a lower bound on _T_<sub>L</sub>, or \(\tau_j\) was not a lower bound on _T_<sub>L</sub>, yet A returned an estimate.

Suppose \(T_\mathrm{L}\ge\tau_j\) when round _i_ terminates. Since every guess satisfies \(\tau_j\ge\tau^*\ge U_i\) by definition, we have \(T_\mathrm{L}\ge\tau^*\), so max(_T_<sub>L</sub>_,U<sub>i</sub>_)=_T_<sub>L</sub> and representativeness gives \(T_j^\mathrm{L}\ge(1-\varepsilon)t^{-3}T_\mathrm{L}\ge(1-\varepsilon)t^{-3}\tau_j\). That is, \((1-\varepsilon)t^{-3}\tau_j\) is a lower bound on \(T_j^\mathrm{L}\). By the guarantees of A,

\(\widehat{T}_\mathrm{L}\in(1\pm\varepsilon)T_j^\mathrm{L}\subseteq(1\pm\varepsilon)^2t^{-3}T_\mathrm{L},\text{hence}t^3\widehat{T}_\mathrm{L}\in(1\pm\varepsilon)^2T_\mathrm{L}\)

as claimed.

Alternatively, suppose \(T_\mathrm{L}<\tau_j\) yet \(\mathcal{A}(S_j^\mathrm{L},(1-\varepsilon)\tau_jt^{-3})\) returned an estimate _X_. We claim that _X_ is still an approximation of _T<sub>j</sub>_. We show that by demonstrating that \(\tau_j\) can’t be far from a lower bound on _T_<sub>L</sub>, and therefore not far from a lower bound on \(T_j^\mathrm{L}\): Suppose by way of contradiction that \(T_\mathrm{L}<\tau_j/2\). Since A(_S<sub>j</sub>_) produced an output _X_, by property (i) it must satisfy

\((1-\varepsilon)(1-\varepsilon)t^{-3}\tau_j\le X.\)

However,

\(X\le(1+\varepsilon)T_j^\mathrm{L}+\varepsilon(1-\varepsilon)\tau_jt^{-3}\text{By property (ii)}\)<br>
\(\le(1+\varepsilon)t^{-3}\left[T_\mathrm{L}+\varepsilon\mathrm{max}(T_\mathrm{L},U_i)\right]+\varepsilon t^{-3}\tau_j\text{By Lemma 4.1 over the graph induced by light edges}\)<br>
\(\le(1+\varepsilon)t^{-3}\left[\frac{\tau_j}{2}+\varepsilon\tau_j+\varepsilon\tau_j\right]\text{By}T_\mathrm{L}\le\tau_j/2\text{and}U_i\le\tau^*\le\tau_j\)<br>
\(\le(1+\varepsilon)\left(\frac{1}{2}+2\varepsilon\right)t^{-3}\tau_j\)<br>
\(\le\frac{3}{4}\left(1+\frac{1}{2}\varepsilon\right)t^{-3}\tau_j\)

where the last inequality holds when \(\varepsilon<1/10\). Therefore

\((1-\varepsilon)(1-\varepsilon)t^{-3}\tau_j\le X\le\frac{3}{4}\left(1+\frac{1}{2}\varepsilon\right)t^{-3}\tau_j\)

Contradiction when \(\varepsilon<1/10\). Therefore, \(\tau_j/2\le T_\mathrm{L}\le\tau_j\), and the output _X_ satisfies

\((1-\varepsilon)^2t^{-3}T_\mathrm{L}\le(1-\varepsilon)^2t^{-3}\tau_j\le X\le(1+\varepsilon)t^{-3}[T_\mathrm{L}+\varepsilon\mathrm{max}(T_\mathrm{L},U_i)]+2\varepsilon t^{-3}T_\mathrm{L}\le(1+\varepsilon)(1+4\varepsilon)t^{-3}T_\mathrm{L}.\)

Rescaling \(\varepsilon\) gets the desired result. The probability analysis is shown in 4.3.

