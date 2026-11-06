### E. Analytical Depth Bounds for Specific Ansätze

Combining the stabilization depths D<sub>g</sub> derived for the DLA families in the preceding subsections with the general depth bounds given in (42) and (51), we establish explicit upper bounds on the circuit depths required for local unitary synthesis and state preparation. Specifically, these bounds guarantee the local generation of unitaries within a neighborhood of the identity in the dynamical Lie group _G_, as well as the preparation of states within a sufficiently small neighborhood of the ray orbit of the initial state \(|\psi\rangle\). The analytical results for Lie algebra dimensions, orbit dimension bounds, stabilization depths, and the corresponding sufficient circuit depths T<sub>g</sub> and \(\mathcal{T}_{\mathfrak{g},\psi}\) across these models are summarized in  IV.

TABLE IV. Sufficient numbers of original-control exponentials for local dynamical Lie group element synthesis (T<sub>g</sub>) and projective state orbit preparation (\(\mathcal{T}_{\mathfrak{g},\psi}\)) across various QAOA ansätze. Here, FMC and FMIS denote free (multi- angle) MaxCut and Maximum Independent Set QAOA variants, respectively, and GM-QAOA denotes Grover-Mixer QAOA. The parameters _n_ and _m_ represent the number of vertices and independence number of the underlying graph. The given values represent upper bounds derived from stabilization depths D<sub>g</sub>, dynamical Lie algebra dimensions dim(g), and projective orbit dimensions \(\mathrm{dim}(\mathcal{O}_{[\psi]})\), and are not necessarily optimal circuit depths.

## VIII. GLOBAL SYNTHESIS ON FULL UNITARY INVARIANT SECTORS

In this section, we pass from local synthesis near the identity and the initial-state ray to uniform global synthesis on g-invariant subspaces \(V\subseteq W\). We assume throughout that the image of the dynamical Lie algebra on _V_ is

\(\mathfrak{g}|_V=\mathfrak{u}(V)\mathrm{or}\mathfrak{g}|_V=\mathfrak{su}(V).\) (78)

Thus, _full_ in this section refers specifically to full unitary or special-unitary controllability on _V_ , rather than to pure-state controllability in its more general sense.

In this regime, global depth bounds can be obtained by reducing the decomposition problem to a two-level unitary synthesis procedure.

### A. Two-Stage Approach to Global Unitary Synthesis

Let _D_:=dim(_V_) and fix an orthonormal basis \(\{|1\rangle,\dots,|D\rangle\}\) for _V_ . For \(1\le r<s\le D\), the standard Hermitian generators for the two-level su(2) sub-blocks are defined by

\(X_{rs}:=E_{rs}+E_{sr},Y_{rs}:=-i(E_{rs}-E_{sr}),Z_{rs}:=E_{rr}-E_{ss},\) (79)

where \(E_{rs}:=|r\rangle\langle s|\) denotes the elementary matrix unit. The global synthesis procedure operates via the following two-stage paradigm.

**Step 1. Synthesis of elementary generator flows.** Starting from the dynamical Lie algebra generators, we first construct exact implementations of the single-parameter flows

\(e^{itY_{rs}}(\mathrm{or}e^{itX_{rs}})\mathrm{and}e^{itZ_{rs}},\) (80)

\begin{tabular}{ccccccc}
Circuit family & DLA, g & dim(g) & \(\mathrm{dim}(\mathcal{O}_{[\psi]})\) & D<sub>g</sub> & Sufficient T<sub>g</sub> & Sufficient \(\mathcal{T}_{\mathfrak{g},\psi}\) \\
FMC, P_<sub>n</sub>_ & so(2_n_) & _n_(2_n_-1) & \(\le n(2n-1)\) & \(\le 2n-1\) & _n_(4_n_-3)(2_n_-1) & _n_(4_n_-3)(2_n_-1) \\
FMC, C_<sub>n</sub>_ & \(\mathfrak{so}(2n)^{\oplus 2}\) & \(2n(2n-1)\) & \(\le 2n(2n-1)\) & \(\le 2n-1\) & 2_n_(4_n_-3)(2_n_-1) & 2_n_(4_n_-3)(2_n_-1) \\
FMC, _K<sub>n</sub>_ & \(\mathfrak{su}(2^{n-1})^{\oplus 2}\) & \(2^{2n-1}-2\) & \(\le 2^{n+1}-3\) & \(\le 2n-1\) & (4_n_-3)(2<sup>2_n_-1</sup>-2) & (4_n_-3)(2<sup>_n_+1</sup>-3) \\
Red. FMC, _K<sub>n</sub>_ & su(2<sup>_n_-1</sup>) & 2<sup>2_n_-2</sup>-1 & 2<sup>_n_</sup>-2 & \(\le 2n-1\) & (4_n_-3)(2<sup>2_n_-2</sup>-1) & (4_n_-3)(2<sup>_n_</sup>-2) \\
FMIS, \(n\ge 3\) & u(|_F_|) & |F|<sup>2</sup> & 2|F|-2 & \(\le 8n+4m-2\) & (16_n_+8_m_-5)|F|<sup>2</sup> & (16_n_+8_m_-5)(2|F|-2) \\
GM-QAOA & u(_d_) & _d_<sup>2</sup> & 2_d_-2 & \(\le d^2\) & (2_d_<sup>2</sup>-1)_d_<sup>2</sup> & (2_d_<sup>2</sup>-1)(2_d_-2) \\
\end{tabular}

