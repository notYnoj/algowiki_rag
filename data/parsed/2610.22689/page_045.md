<tbc>such that the pair signs satisfy<tbc>

\(\varepsilon_a\varepsilon_b=+1,\text{and}\varepsilon_r\varepsilon_s=-1\text{for every}\{r,s\}\in M_v\backslash\{\{a,b\}\}.\) (D17)

<tbc>Since _S=S_<sup>†</sup>=_S_<sup>-1</sup>, conjugating _X<sub>rs</sub>_ by _S_ yields \(SX_{rs}S^{-1}=\varepsilon_r\varepsilon_sX_{rs}\). Applied to \(\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\), this sign assignment flips the direction of every matching term except the target _X<sub>ab</sub>_:<tbc>

\(S\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}S^{-1}=Q_v+X_{ab}-\sum_{\{r,s\}\in M_v\backslash\{\{a,b\}\}}X_{rs}.\) (D18)

<tbc>Averaging \(\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\) with its conjugated counterpart yields<tbc>

\(\frac{1}{2}\left(\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}+S\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}S^{-1}\right)=Q_v+X_{ab}.\) (D19)

<tbc>Crucially, the operators \(\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\) and \(S\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}S^{-1}\) commute. Indeed, both are block-diagonal with respect to the orthogonal decomposition<tbc>

\(W_\mathcal{F}=\oplus_{w\in\mathrm{Fix}(\tau_v)}\mathrm{span}_\mathbb{C}\{|w\rangle\}\oplus\oplus_{\{r,s\}\in M_v}\mathrm{span}_\mathbb{C}\{|r\rangle,|s\rangle\}.\) (D20)

<tbc>On each two-dimensional matching subspace \(\mathrm{span}_\mathbb{C}\{|r\rangle,|s\rangle\}\), \(\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\) restricts to the Pauli-_X_ matrix, while \(S\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}S^{-1}\) restricts to either +_X_ (on {_a,b_}) or -_X_ (on _M<sub>v</sub>_\\{{_a,b_}}). Because _X_ commutes with \(\pm X\), the sum-of-generators exponentiates to a product of commuting unitaries:<tbc>

\(e^{-i\frac{t}{2}\widehat{H}_{CX,v}}\big|_{W_\mathcal{F}}e^{-i\frac{t}{2}S\widehat{H}_{CX,v}}\big|_{W_\mathcal{F}}S^{-1}=e^{-it(Q_v+X_{ab})}.\) (D21)

<tbc>As the diagonal projector _Q<sub>v</sub>_ and the off-diagonal generator _X<sub>ab</sub>_ have disjoint support on _W_<sub>F</sub>, they commute (\[_Q<sub>v</sub>,X<sub>ab</sub>_\]=0). We can therefore isolate the target two-level flow _e_<sup>-_itX<sub>ab</sub>_</sup> as

\(e^{-itX_{ab}}=e^{itQ_v}e^{-i\frac{t}{2}\widehat{H}_{CX,v}}\big|_{W_\mathcal{F}}Se^{-i\frac{t}{2}\widehat{H}_{CX,v}}\big|_{W_\mathcal{F}}S^{-1},\) (D22)

where we used the identity \(e^{-i\frac{t}{2}S\widehat{H}_{CX,v}}\big|_{W_\mathcal{F}}S^{-1}=Se^{-i\frac{t}{2}\widehat{H}_{CX,v}}\big|_{W_\mathcal{F}}S^{-1}\).

**Proposition D.2.** Let \(\Gamma=(V,E)\) be a connected graph with \(D=|\mathcal{F}|\ge 4\). For any vertex \(v\in V\) and every toggle edge \(\{a,b\}\in M_v\), the two-level flow \(e^{-itX_{ab}}(t\in\mathbb{R})\) can be synthesized exactly using at most

\(K_X^{(v)}\le 3K_\mathrm{diag}+2\le 6\Delta_\Gamma D+3D-6\Delta_\Gamma+2\) (D23)

native pulses.

Consequently, for any pair of distinct feasible configurations \(r,s\in\mathcal{F}\), the corresponding two-level flow _e_<sup>-_itX<sub>rs</sub>_</sup> can be synthesized exactly using at most

\(K_X\le K_X^{(v)}+2\Delta_\Gamma\le 3K_\mathrm{diag}+2+2\Delta_\Gamma\le 6\Delta_\Gamma D+3D-4\Delta_\Gamma+2\) (D24)

native pulses.

_Proof._ Fix \(v\in V\) and a toggle edge \(\{a,b\}\in M_v\). We employ the realization of _e_<sup>-_itX<sub>ab</sub>_</sup> from (D22). The diagonal unitary _e<sup>itQ<sub>v</sub>_</sup> requires at most _K_<sub>diag</sub> native pulses. Each of the two evolutions under \(\widehat{H}_{CX,v}\) requires one native mixer pulse, while _S_ and _S_<sup>-1</sup> each require at most _K_<sub>diag</sub> pulses. Therefore,

\(K_X^{(v)}\le K_\mathrm{diag}+1+K_\mathrm{diag}+1+K_\mathrm{diag}=3K_\mathrm{diag}+2.\)

Substituting the upper bound for _K_<sub>diag</sub> from (D14) yields the bound in (D23).

Now let \(r,s\in\mathcal{F}\) be distinct feasible bitstrings. By (D10), the toggle group contains the alternating group:

\(\mathcal{A}_\mathcal{F}\subseteq\mathcal{T}(\Gamma).\)

