<tbc>Finally, after establishing sufficient exploration, we connect learning on \(\mathbf{1}^\perp\) to the terminal opportunity cost.

LEMMA D.8. _For every_ \(\mathbf{x}\in\mathbb{R}^I\),<tbc>

\(S_k^*(\mathbf{x})=S_k^*(\mathbf{Px}),\sum_{i\in S_k^*(\mathbf{x})}x_i=\sum_{i\in S_k^*(\mathbf{Px})}(\mathbf{Px})_i+k\overline{x},\overline{x}:=\frac{1}{I}\mathbf{1}^\top\mathbf{x}.\)

<tbc>_Consequently, if_

\(\mathbb{E}\|P\unknown_T-P\unknown\|_\infty\rightarrow 0,\)

_then_ \(\mathbb{E}[\mathrm{OC}_T]\rightarrow 0\).

_Proof._ Since _x<sub>i</sub>_=(_Px)<sub>i</sub>+<o>x</o>_ for every _i_, any size-_k_ subset _A_ satisfies<tbc>

\(\sum_{i\in A}x_i=\sum_{i\in A}(\mathbf{Px})_i+k\overline{x}.\)

<tbc>The term _k<o>x</o>_ does not depend on _A_, so \(S_k^*(\mathbf{x})=S_k^*(\mathbf{Px})\). Evaluating the sum at \(A=S_k^*(\mathbf{x})\) gives<tbc>

\(\sum_{i\in S_k^*(\mathbf{x})}x_i=\sum_{i\in S_k^*(\mathbf{Px})}(\mathbf{Px})_i+k\overline{x}.\)

<tbc>For the opportunity-cost bound, note that \(S_k^*(\unknown_T)=S_k^*(P\unknown_T)\) by the identity just proved. Next, note that the sum of the _k_ largest elements is _k_-Lipschitz in the L-infinity norm: for any \(\mathbf{x},\mathbf{y}\in\mathbb{R}^I\),<tbc>

\(\sum_{i\in S_k^*(\mathbf{x})}x_i-\sum_{i\in S_k^*(\mathbf{y})}y_i\le\sum_{i\in S_k^*(\mathbf{x})}(x_i-y_i)\le k\|\mathbf{x}-\mathbf{y}\|_\infty.\)

<tbc>Interchanging **_x_** and **_y_** gives<tbc>

\(\left|\sum_{i\in S_k^*(\mathbf{x})}x_i-\sum_{i\in S_k^*(\mathbf{y})}y_i\right|\le k\|\mathbf{x}-\mathbf{y}\|_\infty.\)

<tbc>Thus,

\(0\le\mathrm{OC}_T=\sum_{i\in S_k^*(P\unknown)}(P\unknown)_i-\sum_{i\in S_k^*(P\unknown_T)}(P\unknown_T)_i+\sum_{i\in S_k^*(P\unknown_T)}\left((P\unknown_T)_i-(P\unknown)_i\right)\le 2k\|P\unknown_T-P\unknown\|_\infty.\)

Taking expectations gives the result. \(\square\)

## D.4. Proof of Theorem 2

We now have the tools to prove Theorem 2.

_Proof._ Define the set of directions sampled infinitely often, \(E_\infty:=\{L\in\mathcal{D}:L\text{is sampled infinitely often}\}\). For each \(\mathcal{E}\subseteq\mathcal{D}\), let \(\unknown_\mathcal{E}:=\{E_\infty=\mathcal{E}\}\). Fix \(\mathcal{E}\subseteq\mathcal{D}\) and work on \(\unknown_\mathcal{E}\). Let

\(M:=\mathrm{span}(\mathcal{E}),R_M:=\text{orthogonal projector onto}M,Q:=\mathrm{Id}_I-R_M.\)

We claim that on \(\unknown_\mathcal{E}\), \(\mathbf{1}^\perp\subseteq M\). Assume for contradiction that \(\mathbf{1}^\perp\unknown\in M\). Because directions outside E are sampled only finitely often and D\\E is finite, there exists an almost-surely finite round _T_<sup>∗</sup> such that after round _T_<sup>∗</sup> no direction outside E is ever sampled again.

