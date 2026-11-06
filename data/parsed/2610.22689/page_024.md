1. Any unitary operator _U_ on _V_ (or \(U\in\mathrm{SU}(V)\) when \(\mathfrak{g}\big|_V=\mathfrak{su}(D)\)) can be synthesized with a global depth _L_<sub>glob</sub> bounded by<tbc>

\(L_\mathrm{glob}\le\frac{D(D-1)}{2}\cdot\big(K_X+K_\mathrm{diag}\big)+K_\mathrm{diag}.\) \(\text{(86)}\)

2. From any computational basis state \(|e_r\rangle\), an arbitrary normalized state \(|\phi\rangle\in V\) can be synthesized, up to a global phase, with a circuit depth \(L_{e_r\rightarrow\phi}\) bounded by<tbc>

\(L_{e_r\rightarrow\phi}\le(D-1)K_X+K_\mathrm{diag}.\) \(\text{(87)}\)

3. Any pair of normalized states \(|\psi\rangle,|\phi\rangle\in V\) can be connected, up to a global phase, with a circuit depth _L_<sub>state</sub> bounded by

\(L_\mathrm{state}\le 2(D-1)K_X+2K_\mathrm{diag}.\) \(\text{(88)}\)

**Remark VIII.3.** Relating the system dimension to the DLA dimension via \(D=\mathcal{O}(\sqrt{\mathrm{dim}(\mathfrak{g})})\), where dim(g)=_D_<sup>2</sup> for u(_D_) and _D_<sup>2</sup>-1 for su(_D_), and letting K<sub>max</sub>:=max(_K<sub>X</sub>,K_<sub>diag</sub>) denote the maximum primitive synthesis cost bound,  V summarizes the asymptotic upper bounds on circuit depths for local versus global synthesis of unitary operators and quantum states.

Both local and global unitary synthesis scale directly with dim(g), with their fundamental distinction lying in their operational depth parameters: local-vicinity unitary synthesis is governed by the generator stabilization depth D<sub>**a**</sub> (see (42)), whereas global unitary synthesis is governed by the primitive cost bound K<sub>max</sub>. Similarly, for quantum state generation, local-vicinity synthesis is governed by the state orbit specific stabilization depth and local orbit dimension (see (51)), whereas the global uniform bound scales as \(\mathcal{K}_\mathrm{max}\sqrt{\mathrm{dim}(\mathfrak{g})}\). As a concrete illustration, Theorem VIII.8 establishes explicit global synthesis bounds for

TABLE V. Asymptotic upper bounds on circuit depths for local versus global synthesis of unitary operators and quantum states via dynamical Lie algebra generator flows.

multi-angle MIS QAOA, where the primitive synthesis cost bound evaluates to \(\mathcal{K}_\mathrm{max}=\mathcal{O}(D\Delta_\Gamma)\) with \(\Delta_\Gamma\) denoting the toggle group diameter and _D_=|F| representing the feasible independent-set subspace dimension.

## B. Circuit-Level Synthesis via Standard Gate Decompositions

In certain regimes, the foregoing global synthesis approach can be further refined by leveraging standard circuit compilation architectures. Specifically, the universal unitary synthesis results of Shende et al. \[26\] establish that an arbitrary operator in SU(2_<sup>n</sup>_), up to an overall phase, can be implemented using O(4_<sup>n</sup>_) CNOT gates and O(4_<sup>n</sup>_) single-qubit rotations, while its state-preparation construction uses only O(2_<sup>n</sup>_) such gates.

Translating this gate-level decomposition into our framework allows us to bound global unitary and state- to-state transition depths directly in terms of the primitive native implementation costs for single-qubit gates (_K_<sub>1q</sub>) and CNOT gates (_K_<sub>CX</sub>).

**Theorem VIII.4.** Let \(V\cong(\mathbb{C}^2)^{\otimes q}\) be a _D_=2_<sup>q</sup>_-dimensional Hilbert space equipped with an orthonormal basis \(\{|e_1\rangle,\dots,|e_D\rangle\}\) corresponding to an _n_-qubit system (_D_=2_<sup>n</sup>_). Suppose the restricted dynamical Lie algebra satisfies \(\mathfrak{g}\big|_V=\mathfrak{u}(V)\) or su(_V_), and assume that every primitive single-qubit gate is synthesized by a native circuit of length at most _K_<sub>1q</sub> and every CNOT gate by one of length at most _K_<sub>CX</sub>.

Then, every projective unitary \([U]\in\mathrm{PU}(V)\) can be synthesized with a circuit of depth

\(L_\mathrm{glob}^\mathrm{proj}\le\big(4^q-3\cdot 2^{q-1}\big)K_{1\mathrm{q}}+\big(\frac{3}{4}4^q-\frac{3}{2}2^q\big)K_\mathrm{CX}.\) (89)

\begin{tabular}{ccc}
**Regime** & **Unitary Synthesis** & **State-to-State** \\
**Local** & O(D<sub>**a**</sub>dim(g)) & \(\mathcal{O}(\mathcal{D}_{\mathbf{a},\psi} m_\psi)\) \\
**Global** & O(K<sub>max</sub>dim(g)) & \(\mathcal{O}(\mathcal{K}_\mathrm{max}\sqrt{\mathrm{dim}(\mathfrak{g})})\) \\
\end{tabular}

