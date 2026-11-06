**Claim 3.4.** _If_ ONEPASS _terminates and outputs a numerical value, then with probability at least_ \(1-\delta-1/\mathrm{poly}(n)\) _it is a_ \((1\pm\varepsilon)^2\) _approximation of T._

**Remark 3.5.** _Note that when_ \(\varepsilon\) _is small enough,_ \((1\pm\varepsilon)^2\approx(1\pm 2\varepsilon)\)_, so rescaling_ \(\varepsilon\) _results in the desired approximation._

_Proof._ Since we assume ONEPASS terminated with a numerical value it must terminate when \(\mathcal{A}(S_j,(1-\varepsilon)\tau_jt^{-3})\) outputs some estimate of _T<sub>j</sub>_. Let that estimate be _X_. We need to show that \(X\in(1\pm\varepsilon)^2t^{-3}T\). There are two cases to check: The termination happened when \(\tau_j\) was a lower bound on _T_, or \(\tau_j\) was not a lower bound on _T_, yet A returned an estimate.

Suppose \(T\ge\tau_j\) when ONEPASS terminates. By minimality of _t_, \(\tau_j\ge\tau_t\ge\tau^*/2\), so \(T\ge\tau^*/2\) and \(\mathrm{max}(T,\tau^*)\le 2T\). Hence, if _S<sub>j</sub>_ is representative, \(T_j\ge(1-2\varepsilon)t^{-3}T\ge(1-2\varepsilon)t^{-3}\tau_j\). That is, \((1-2\varepsilon)t^{-3}\tau_j\) is a lower bound on _T<sub>j</sub>_. Hence the output _X_ satisfies

\(X\in(1\pm\varepsilon)T_j\subseteq(1\pm\varepsilon)(1\pm 2\varepsilon)t^{-3}T\)

as claimed.

Alternatively, suppose \(T<\tau_j\) and ONEPASS still terminated. Then A outputs some _X_, even though \((1-\varepsilon)\tau_jt^{-3}\) is not necessarily a lower bound on _T<sub>j</sub>_. We claim that _X_ is still an approximation of _T<sub>j</sub>_. We show that by demonstrating that \(\tau_j\) can’t be far from a lower bound on _T_, and therefore not far from a lower bound on _T<sub>j</sub>_: Suppose by way of contradiction that \(T<\tau_j/2\). Since A(_S<sub>j</sub>_) produced an output _X_, by property (i) it must satisfy

\((1-\varepsilon)(1-\varepsilon)t^{-3}\tau_j\le X.\)

However,

\(X\le(1+\varepsilon)T_j+\varepsilon(1-\varepsilon)\tau_jt^{-3}\text{By property (ii)}\)<br>
\(\le(1+\varepsilon)t^{-3}\left[T+\varepsilon\mathrm{max}(T,\tau^*)\right]+\varepsilon t^{-3}\tau_j\text{By Lemma 4.1}\)<br>
\(\le(1+\varepsilon)t^{-3}\left[\frac{\tau_j}{2}+\varepsilon\tau_j+\varepsilon\tau_j\right]\text{By}T\le\tau_j/2\text{and}\tau^*\le\tau_j\)<br>
\(\le(1+\varepsilon)\left(\frac{1}{2}+2\varepsilon\right)t^-3\tau_j\)

ONEPASS
Input: A random order stream S with |S|=m.
0. Preprocessing:
Let t be the smallest integer such that 2-tm 3/2 c c -2(n ln(n)t + ln3(n)t5) and set =
Sample (m1, , mt) - Mult (m; 1/t, , 1/t) .
Segment the length-m stream into S1 |S2 | |St where |Sj | mj for j [t].
1. One Pass: For each j [t], run (Sj, (1- -)t-3 -
where = 2-j m1.5. Output its estimate scaled by t3 if the output is not FAIL. Otherwise, continue to the next segment.
If none of the outputs were an estimate, return FAIL.

Figure 2: A one-pass parameter free triangle counting algorithm that either produces a \((1\pm\varepsilon)\) approximation of _T_, or guarantees that \(T=\widetilde{O}(n)\).

