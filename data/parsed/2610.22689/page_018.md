<tbc>connected graph that is neither bipartite nor a cycle), the free DLA is isomorphic to the direct sum of two special unitary Lie algebras:

\(\mathfrak{g}_{\Gamma,\mathrm{free}}\cong\mathfrak{su}(W_{\Gamma,\mathrm{even}})\oplus\mathfrak{su}(W_{\Gamma,\mathrm{odd}})\cong\mathfrak{su}(2^{n-1})\oplus\mathfrak{su}(2^{n-1}),\) (57)

where _n_=|_V_| is the order of \(\Gamma\), and \(W_{\Gamma,\mathrm{even}}\) (resp. \(W_{\Gamma,\mathrm{odd}}\)) denotes the subspace spanned by Hadamard basis states containing an even (resp. odd) number of \(|-\rangle\) factors.

To highlight the structural differences between standard and free DLAs as well as their respective stabilization depths, we present numerical results for all non-isomorphic asymmetric graphs of order _n_=6 (see  I).

TABLE I. Comparison of dimensions and stabilization depths for free \((\mathfrak{g}_{\Gamma,\mathrm{free}})\) and standard \((\mathfrak{g}_{\Gamma,\mathrm{std}})\) dynamical Lie algebras across all eight non-isomorphic asymmetric graphs of order _n_=6.

Complementing these empirical findings, the following theorem establishes analytical upper bounds on the stabilization depth of free DLAs across several canonical graph families.

**Theorem VII.3.** Let \(\Gamma\) be a graph belonging to one of the following families:

• a path graph _P<sub>n</sub>_ (with \(\mathfrak{g}_{P_n,\mathrm{free}}\cong\mathfrak{so}(2n)\)),<tbc>

• a cycle graph _C<sub>n</sub>_ (with \(\mathfrak{g}_{C_n,\mathrm{free}}\cong\mathfrak{so}(2n)\oplus\mathfrak{so}(2n)\)),<tbc>

• a complete graph _K<sub>n</sub>_ (with \(\mathfrak{g}_{K_n,\mathrm{free}}\cong\mathfrak{su}(2^{n-1})\oplus\mathfrak{su}(2^{n-1})\)).

The stabilization depth of the corresponding free dynamical Lie algebras satisfy

\(\mathcal{D}_{\mathfrak{g}_{P_n,\mathrm{free}}}\le 2n-1(n\ge 2),\mathcal{D}_{\mathfrak{g}_{C_n,\mathrm{free}}}\le 2n-1(n\ge 3),\mathcal{D}_{\mathfrak{g}_{K_n,\mathrm{free}}}\le 2n-1(n\ge 2).\) (58)

## B. Reduced DLAs for the MaxCut Problem

The MaxCut cost function exhibits a global Z<sub>2</sub> (bit-flip) symmetry that permits fixing the classical state of an arbitrary reference vertex \(v\in V\) (e.g., _x<sub>v</sub>_=0) without altering the maximum cut value, as the full solution set remains reconstructible via bitwise inversion. A comprehensive exposition of the corresponding symmetry-reduced QAOA formulations, including their dynamical Lie algebras, circuit properties, and algebraic structures, is provided in \[29\]; here, we briefly review the relevant setup.

Quantum mechanically, imposing _x<sub>v</sub>_=0 breaks this two-fold degeneracy and projects the _n_-qubit Hilbert space \((\mathbb{C}^2)^{\otimes n}\) onto an (_n_-1)-qubit subspace:

\(W_v=\mathbb{C}^2\otimes\cdots\otimes\mathbb{C}^2\otimes\underbrace{\mathbb{C}|x_v=0\rangle}_{v\text{-th position}}\otimes\mathbb{C}^2\otimes\cdots\otimes\mathbb{C}^2\simeq(\mathbb{C}^2)^{\otimes(n-1)}.\) (59)

Under this reduction, Pauli _Z_-operator on vertex _v_ is replaced by its respective scalar eigenvalue \((Z_v\mapsto 1)\). Consequently, edge interactions incident to _v_ simplify to single-qubit _Z_ operators. The reduced mixer and problem Hamiltonians acting on _V_\\{_v_} become

\(H_M^v=\sum_{w\in V\backslash\{v\}}X_w,H_P^v=\sum_{(w,w^\prime)\in Epw,w^\prime\neq v}Z_wZ_{w^\prime}+\sum_{(v,w)\in E}Z_w.\) (60)

\begin{tabular}{ccccccccc}
\(\Gamma\) & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\(\mathrm{dim}(\mathfrak{g}_{\Gamma,\mathrm{free}})\) & 2046 & 2046 & 2046 & 2046 & 2046 & 2046 & 2046 & 2046 \\
\(\mathcal{D}_{\mathfrak{g}_{\Gamma,\mathrm{free}}}\) & 17 & 21 & 29 & 17 & 21 & 17 & 19 & 13 \\
\(\mathrm{dim}(\mathfrak{g}_{\Gamma,\mathrm{std}})\) & 1984 & 1970 & 1983 & 1984 & 1984 & 1984 & 1984 & 1984 \\
\(\mathcal{D}_{\mathfrak{g}_{\Gamma,\mathrm{std}}}\) & 19 & 21 & 29 & 19 & 21 & 17 & 19 & 17 \\
\end{tabular}

