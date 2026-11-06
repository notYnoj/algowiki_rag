**Corollary 5.1.** _There exist constants_ \(\varepsilon_0\in(0,1)\) _and c\>_0 _such that for every randomized Max E3SAT algorithm_ A _that, on every satisfiable instance_ \(\Phi=(V,\{0,1\},\mathcal{C}=\{C_1,\dots,C_m\})\)_, outputs in expectation a_ \((1-\varepsilon_0)\)_-approximate assignment, there is a satisfiable_ \(\Phi\) _with_

\(\mathrm{max}_{i\in[m]}\mathrm{max}_{C^\prime\in\mathcal{L}_i}\mathsf{EMD}_{d_\mathrm{H}}\big(\mathcal{A}(\Phi),\mathcal{A}(\Phi-C_i+C')\big)\ge c|V|.\) (6)

_Here_ L_<sub>i</sub> denotes the set of clauses on the three variables that appear in C<sub>i</sub>, and_ \(\Phi-C_i+C'\) _is the instance obtained from_ \(\Phi\) _by replacing C<sub>i</sub> with_ \(C'\).

## 5.2 Block Gadget Reduction

Fix integers _n_=|_V_| and \(k\le n\). Without loss of generality, we assume that _n_ is divisible by _k_. Partition _V_ into _k_ disjoint blocks \(V=V_1\sqcup\cdots\sqcup V_k\) with |_V<sub>i</sub>_|=_n/k_. For each \(i\in[k]\) and \(\alpha\in\{0,1\}^{V_i}\) create a set \(S_{i,\alpha}\). For every clause \(C_j\in C\) create an element _e<sub>j</sub>_, and include \(e_j\in S_{i,\alpha}\) whenever the restriction \(\alpha\) satisfies a literal of _C<sub>j</sub>_ whose variable lies in _V<sub>i</sub>_. Let \(\mathcal{F}=\big\{S_{i,\alpha}|i\in[k],\alpha\in\{0,1\}^{V_i}\big\}\).

Let _m_=|_C_|. Without loss of generality, we assume that _m_ is divisible by _k_. We choose _M=m/k_. For each block _i_, add a multiset _G<sub>i</sub>_ of _M_ new guard elements. Every set \(S_{i,\alpha}\) contains the guards _G<sub>i</sub>_, while no set \(S_{i^\prime,\alpha^\prime}\) with \(i'\neq i\) contains them. Write _U_<sub>cl</sub>={_e_<sub>1</sub>_,...,e<sub>m</sub>_}, \(U_\mathrm{gd}=\sqcup_{i=1}^kG_i\), and define \(U^+=U_\mathrm{cl}\cup U_\mathrm{gd}\). The resulting maximum _k_-coverage problem instance is denoted by \(R_k^+(\Phi)=(U^+,\mathcal{F})\).

**Lemma 5.2.** _For any choice of exactly one set per block, say_ \(\{S_{i,\alpha_i}\}_{i=1}^k\)_, let_ \(x\in\{0,1\}^V\) _be the concatenation of the block assignments_ \(\alpha_1,\dots,\alpha_k\)_. Then_

\(\big|\left(\bigcup_{i=1}^kS_{i,\alpha_i}\right)\cap U_\mathrm{cl}\big|=|\{C_j\in C|x\text{\textit{satisfies}}C_j\}|.\)

**Lemma 5.3** (Neighbor preservation)**.** _If_ \(\Phi'\) _is obtained from_ \(\Phi\) _by modifying one clause C<sub>t</sub>, then_ \(R_k^+(\Phi')\) _is obtained from_ \(R_k^+(\Phi)\) _by reprogramming the single element e<sub>t</sub> while leaving all guards untouched._

**Lemma 5.4** (Near-perfect coverage forces one choice per block)**.** _Let_ \(I^+=R_k^+(\Phi)\) _and_ \(\varepsilon\in(0,1)\)_. Suppose a k-subfamily_ S _covers at least_ \((1-\varepsilon)|U^+|\) _elements. If_ \(M>\varepsilon|U^+|\)_, then_ S _contains at least one set from each block. As_ |S|=_k, it in fact contains exactly one from every block and therefore covers all guards U_<sub>gd</sub>.

_Proof._ If block _i_ contributes no set, all _M_ guards in _G<sub>i</sub>_ remain uncovered, contradicting \(\big|\bigcup_{S\in\mathcal{S}}S\big|\ge(1-\varepsilon)|U^+|\) when \(M>\varepsilon|U^+|\). With _k_ blocks and budget _k_, covering each block at least once is equivalent to selecting exactly one per block.

### A canonical decoder.

Whenever S contains exactly one set from each block we write it as \(\mathcal{S}=\{S_{i,\alpha_i}\}_{i=1}^k\) and define \(D(\mathcal{S})\in\{0,1\}^V\) to be the concatenation of the block assignments.

**Lemma 5.5** (Decoder Lipschitzness)**.** _Let_ \(\mathcal{S},\mathcal{S}'\) _be k-subfamilies that each contain exactly one set per block. Then_

\(d_\mathrm{H}\big(D(\mathcal{S}),D(\mathcal{S}')\big)\le\frac{n}{2k}\cdot d_\mathrm{H}(\unknown_\mathcal{S},\unknown_{\mathcal{S}^\prime}).\)

_Proof._ Changing the choice within one block removes one set and adds another, increasing the symmetric difference by two. Each affected block modifies at most _n/k_ assignment bits, so the claimed Lipschitz bound follows.

