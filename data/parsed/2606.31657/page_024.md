**Lemma 5.6.** _Assume_ S _covers at least_ \((1-\varepsilon)|U^+|\) _elements and, by Lemma 5.4, contains exactly one set per block. Then the decoded assignment x=D_(S) _satisfies at least_ \((1-2\varepsilon)m\) _clauses. In particular, this conclusion holds whenever_ \(M\le m/k\)_, because then_ \(|U^+|=m+Mk\le 2m\) _and all guards are covered._

_Proof._ All _Mk_ guards are covered. Hence the number of covered clause elements is at least \((1-\varepsilon)|U^+|-Mk=(1-\varepsilon)(m+Mk)-Mk=(1-\varepsilon)m-\varepsilon Mk\ge(1-2\varepsilon)m\) whenever \(Mk\le m\). By Lemma 5.2, this equals the number of satisfied clauses.

## 5.3 Sensitivity Transfer

We now relate algorithms for the maximum _k_-coverage problem to algorithms for Max E3SAT.

**Theorem 5.7** (Restatement of Theorem 1.5)**.** _There exists_ \(\varepsilon_0>0\) _such that, for every_ \(\varepsilon\in(0,\varepsilon_0)\) _and every_ \(k<1/(2\varepsilon)\)_, any randomized_ \((1-\varepsilon)\)_-approximation algorithm_ B _for the maximum k- coverage problem (in expectation) has an instance I_<sup>+</sup> _with_ OPT(_I_<sup>+</sup>)=|_U_<sup>+</sup>| _on which_

\(\text{Sens}(\mathcal{B},I^+)=\Omega(k),\)

_with an implicit constant that is universal._

_Proof._ Let \(\varepsilon_0\in(0,1)\) and _c\>_0 be the constants supplied by Corollary 5.1. Fix \(\varepsilon\in(0,\varepsilon_0)\), \(k<1/(2\varepsilon)\), and a randomized \((1-\varepsilon)\)-approximation algorithm B.

_Step 1: Build an E3SAT algorithm from_ B. Define \(\mathcal{A}_\text{sat}:=D\circ\mathcal{B}\circ R_k^+\) and set _M_:=_m/k_ in the reduction \(R_k^+\).

_Step 2:_ A<sub>sat</sub> _is_ \((1-\varepsilon_0)\)_-accurate on satisfiable inputs._ When \(\Phi\) is satisfiable, choosing the set whose block restriction matches a satisfying assignment yields perfect coverage of \(R_k^+(\Phi)\). Because _M=m/k_ and \(k<1/(2\varepsilon)\), we have \(M>\varepsilon|U^+|\) (indeed \(|U^+|=m+Mk\le 2m\) and \(M\ge m/k>2\varepsilon m\)). Therefore Lemma 5.4 ensures that \(\mathcal{B}(R_k^+(\Phi))\) selects exactly one set per block, and Lemma 5.6 gives that \(D\circ\mathcal{B}(R_k^+(\Phi))\) satisfies at least \((1-2\varepsilon)m\ge(1-\varepsilon_0)m\) clauses in expectation.

_Step 3: Invoke the Max E3SAT sensitivity bound._ We choose \(\varepsilon_0\) to be small enough. Then by (6), there exist a satisfiable \(\Phi\) and a clause \(C'_t\) on the same variable triple as some \(C_t\in\mathcal{C}\) such that the instance \(\Phi':=\Phi-C_t+C'_t\) satisfies

\(\mathsf{EMD}_{d_\text{H}}(\mathcal{A}_\text{sat}(\Phi),\mathcal{A}_\text{sat}(\Phi'))\ge cn,\)

where _n_=|_V_|. Let \(I^+=R_k^+(\Phi)\) and \(I^{+\prime}=R_k^+(\Phi')\). By Lemma 5.3, \(I^{+\prime}\) is obtained from _I_<sup>+</sup> by reprogramming the single clause element _e<sub>t</sub>_, so it is a valid neighbor in the maximum _k_-coverage problem.

_Step 4: EMD contraction through the decoder._ Let F<sup>(_k_)</sup> denote the set of _k_-subfamilies of F. Conditioning on the event that B selects exactly one set per block (which holds for both _I_<sup>+</sup> and \(I^{+\prime}\) by the guard argument above), Lemma 5.5 shows that the decoder _D_ is _n/_(2_k_)-Lipschitz from (F<sup>(_k_)</sup>_,d_H) to ({0,1}_<sup>V</sup>,d_H). Let \(D_*\mu\) denote the pushforward of a distribution \(\mu\) under _D_. The Lipschitz contraction property for earthmover distance therefore implies

\(\mathsf{EMD}_{d_\text{H}}(D_*\mathcal{B}(I^+),D_*\mathcal{B}(I^{+\prime}))\le\frac{n}{2k}\cdot\mathsf{EMD}_{d_\text{H}}(\mathcal{B}(I^+),\mathcal{B}(I^{+\prime})).\)

Combining with Step 3 and rearranging gives \(\mathsf{EMD}_{d_\text{H}}(\mathcal{B}(I^+),\mathcal{B}(I^{+\prime}))\ge\Omega(k)\), which is precisely \(\text{Sens}(\mathcal{B},I^+)=\Omega(k)\). Because \(R_k^+(\Phi)\) is perfectly coverable, this concludes the promised instance.

