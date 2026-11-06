## D. Global Synthesis for Free Flip-or-Stay MIS QAOA

In this subsection, we apply the orbit-generation bounds from Theorem VIII.2 to the free DLA for MIS QAOA on a connected graph \(\Gamma=(V,E)\), obtaining concrete global bounds on circuit synthesis.

We retain the notation established in Section VIIC. However, rather than working directly with the restricted free DLA \(\mathfrak{g}_{\Gamma,\mathrm{free},\mathcal{F}}\) from (70), we analyze the closely related algebra

\(\widehat{\mathfrak{g}}_{\Gamma,\mathrm{free},\mathcal{F}}:=\left\langle\left\{i\widehat{H}_{CX,v}\right|_{W_\mathcal{F}},iZ_v\right|_{W_\mathcal{F}}\right\}_{v\in V}\right\rangle_\mathrm{Lie},\) (96)

where \(\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\) denotes the restriction of the local controlled-X mixer operator to the feasible subspace _W_<sub>F</sub>. The action of \(\widehat{H}_{CX,v}\) on a computational basis state \(|x\rangle\) (for \(x\in\{0,1\}^n\)) is given by

\(\widehat{H}_{CX,v}|x\rangle:=H_{CX,v}|x\rangle+(I-\mathcal{P}_v)|x\rangle=\left\{\begin{array}{ c c }
|x^{(v)}\rangle, & \text{if}x_w=0\text{for all}w\in\mathcal{N}_v, \\
|x\rangle, & \text{if}x_w=1\text{for some}w\in\mathcal{N}_v,
\end{array}\right.\) (97)

where _x_<sup>(_v_)</sup> denotes the bitstring _x_ with the _v_-th bit flipped (cf. (68) and (69)). As shown in \[30, Theorem IV.2\], this modification still results in the generation of the full unitary algebra:

\(\widehat{\mathfrak{g}}_{\Gamma,\mathrm{free},\mathcal{F}}\cong\mathfrak{u}(W_\mathcal{F}).\) (98)

Throughout this subsection, _native pulse_ refers to the Flip-or-Stay control family

\(\widehat{\mathfrak{a}}_\mathrm{MIS}:=\left\{i\widehat{H}_{CX,v}\big|_{W_\mathcal{F}},iZ_v\big|_{W_\mathcal{F}}\big|v\in V\right\}.\)

Thus the bounds below are stated in the hatted Flip-or-Stay pulse alphabet.

We next observe that each local mixer stabilizes the set F of feasible bitstrings, thereby inducing a well- defined combinatorial action directly on F. Specifically, for each vertex \(v\in V\) , the local mixer defines a set-theoretic toggle map \(\tau_v:\mathcal{F}\rightarrow\mathcal{F}\) given by

\(\tau_v(x):=\left\{\begin{array}{ c c }
x^{(v)}, & \text{if}x_w=0\text{for all}w\in\mathcal{N}_v, \\
x, & \text{if}x_w=1\text{for some}w\in\mathcal{N}_v.
\end{array}\right.\) (99)

As \(\tau_v\) either leaves a bitstring \(x\in\mathcal{F}\) invariant or swaps an isolated pair \(x\leftrightarrow x^{(v)}\), each \(\tau_v\) acts as an involution on the feasible set F:

\(\tau_v^2=\mathrm{id}_\mathcal{F}\text{for all}v\in V.\) (100)

The collection of these local toggles generates a permutation subgroup of the symmetric group Sym(F), known as the _independent-set toggle group_:

\(\mathcal{T}(\Gamma):=\langle\tau_v\rangle_{v\in V}\subseteq\mathrm{Sym}(\mathcal{F}).\) (101)

Importantly, the involutory nature of \(\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\) (see (100)) implies that exponentiating the local mixer flow at parameter \(t=\pi/2\) yields

\(e^{i\frac{\pi}{2}\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}}=\mathrm{cos}\left(\frac{\pi}{2}\right)I_{W_\mathcal{F}}+i\mathrm{sin}\left(\frac{\pi}{2}\right)\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}=i\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}.\) (102)

Thus, up to an overall global phase factor _i_, executing the action of a single discrete toggle permutation \(\tau_v\) on _W_<sub>F</sub> requires exactly one native continuous pulse evolution under the Hamiltonian \(\widehat{H}_{CX,v}\big|_{W_\mathcal{F}}\).

To quantify the pulse complexity of synthesizing arbitrary permutations within the toggle group \(\mathcal{T}(\Gamma):=\langle\tau_v\rangle_{v\in V}\subseteq\mathrm{Sym}(\mathcal{F})\), we define the toggle group diameter \(\Delta_\Gamma\) as the diameter of its Cayley graph with respect to the generating set in (101):

\(\Delta_\Gamma:=\mathrm{diamCay}\big(\mathcal{T}(\Gamma),\{\tau_v|v\in V\}\big).\) (103)

