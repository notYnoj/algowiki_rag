_Proof._ We prove this by induction on \(\ell\) increasing. In the base case of \(\ell=1\), we have that \(2^{k_\ell}=n/2\) and the congruent pairs are the ones that were just compared. Now assume that this holds after layer \(\ell-1\) and let \(m=n/2^{k_\ell-1}\). Fix any _r_ such that \(0\le r<2^{k_\ell}\). We will show that this holds for the wires whose indices are congruent to \(r\mathrm{mod}2^{k_\ell}\). Let _e<sub>j</sub>_ be the _j_’th wire whose index is congruent to \(r\mathrm{mod}2^{k_{\ell-1}}\) and _o<sub>j</sub>_ be the _j_’th wire whose index is congruent to \(r+2^{k_\ell}\mathrm{mod}2^{k_{\ell-1}}\). In other words _e<sub>j</sub>_ is the wire at index \(r+2j\cdot 2^{k_\ell}\) and _o<sub>j</sub>_ is the wire at index \(r+(2j+1)2^{k_\ell}\). Note that for all \(0\le j<m-1\), \((o_j,e_{j+1})\in G_\ell\). By the inductive hypothesis, we know that<tbc>

\(e_j(\ell-1)\le e_{j+1}(\ell-1)\text{and}o_j(\ell-1)\le o_{j+1}(\ell-1)\)

<tbc>for all _j_. We also know that \(e_j(0)\le o_j(0)\) since they are on the same half of the input after the recursive call in Batcher’s. Since the \(e_j(\ell-1)\) are a sorted version of the _e<sub>j</sub>_(0)’s and likewise the \(o_j(\ell-1)\) are a sorted version of the _o<sub>j</sub>_(0)’s due to Fact 5.6, this implies that<tbc>

\(e_j(\ell-1)\le o_j(\ell-1)\)

<tbc>for all _j_. By a similar argument we know when \(j\neq m/2-1\) it must be the case that \(o_j(0)\le e_{j+1}(0)\) by the recursive call in Batcher’s. This maximum of one violation comparing _o<sub>j</sub>_(0) to _e_<sub>_j_+1</sub>(0) gives us that in the sorted orders before applying layer \(\ell\),<tbc>

\(o_j(\ell-1)\le e_{j+2}(\ell-1)\)

<tbc>for all \(0\le j<m-2\). Putting this together we have that:

\(e_j(\ell)\le\mathrm{max}(o_{j-1}(\ell-1),e_j(\ell-1))\)<br>
\(\le\mathrm{min}(o_j(\ell-1),e_{j+1}(\ell-1))=o_j(\ell)\)<br>
\(\le\mathrm{max}(o_j(\ell-1),e_{j+1}(\ell-1))=e_{j+1}(\ell)\)<br>
\(\le\mathrm{min}(o_{j+1}(\ell-1),e_{j+2}(\ell-1))\le o_{j+1}(\ell)\)

for all \(1\le j<m-2\). We now have that \(e_1(\ell)\le o_1(\ell)\le\dots\le e_{m-2}(\ell)\le o_{m-2}(\ell)\). We know \(o_0(\ell)\le e_1(\ell)\) and \(o_{m-2}(\ell)\le e_{m-1}(\ell)\) since pairs \(o_0(\ell),e_1(\ell)\) and _o_<sub>_m_-2</sub>_,e_<sub>_m_-1</sub> are compared in layer \(\ell\). Also we know that \(e_0(\ell)\le o_0(\ell)\) and \(e_{m-1}(\ell)\le o_{m-1}(\ell)\) since \(e_0(\ell-1)=e_0(\ell)\) is smaller than both possible values of \(o_0(\ell)\) and \(o_{m-1}(\ell-1)=o_{m-1}(\ell)\) is larger than both possible values of \(e_{m-1}(\ell)\). Doing this analysis for all _r_ completes the proof.

**Lemma 5.8.** _Let g be the gate_ \((i,i+2^{k_\ell})\in G_\ell\) _for_ \(\ell\ge 2\) _and_ \(r\equiv i(\mathrm{mod}2^{k_\ell})\)_. If Batcher’s odd even mergesort receives some permutation of_ \[_n_\] _as its input, then the smaller input to g is in the set_ \(S_g\subseteq\{i+r-2^{k_\ell}+1,\dots,i+r\}\) _and the larger input to g is in the set_ \(L_g\subseteq\{i+r+1,\dots,i+r+2^{k_\ell}\}\).

_Proof._ We prove this by induction on \(\ell\) decreasing. When \(\ell=\mathrm{log}n\) we have that the smaller input to _g_ must be _i_ and the larger input to _g_ must be _i_+1 since the output after this layer is sorted. Now assume the claim holds for all gates in layer \(\ell+1\). Now we split into two cases.

When \(r<2^{k_\ell-1}\) then in layer \(\ell+1\) we know that wire _i_ is an input to the gate \(g_1=(i-2^{k_\ell-1},i)\) and wire \(i+2^{k_\ell}\) is an input to the gate \(g_2=(i+2^{k_\ell-1},i+2^{k_\ell})\). By our inductive hypothesis, this means that \(S_g\subseteq S_{g_1}\cup L_{g_1}=\{i+r-2^{k_\ell}+1,\dots,i+r\}\) and \(L_g\subseteq S_{g_2}\cup L_{g_2}=\{i+r+1,\dots,i+r+2^{k_\ell}\}\).

When \(2^{k_\ell-1}\le r<2^{k_\ell}\) then in layer \(\ell+1\) we know that wire _i_ is an input to the gate \(g_1=(i,i+2^{k_\ell-1})\) and wire \(i+2^{k_\ell}\) is an input to the gate \(g_2=(i+2^{k_\ell},i+2^{k_\ell}+2^{k_\ell-1})\). Again our inductive hypothesis gives us that \(S_g\subseteq S_{g_1}\cup L_{g_1}\subseteq\{i+r-2^{k_\ell}+1,\dots,i+r\}\) and \(L_g\subseteq S_{g_2}\cup L_{g_2}=\{i+r+1,\dots,i+r+2^{k_\ell}\}\).

