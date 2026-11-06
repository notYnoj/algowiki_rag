<tbc>submanifold of that unit sphere of oftentimes significantly lower dimension. Moreover, mere membership in the orbit’s closure does not automatically guarantee attainability via a finite sequence of gate applications without explicit circuit-depth bounds. Finally, knowledge of the generated Lie algebra alone does not specify the required resource overhead, as different generator sets can yield identical algebras at drastically different synthesis costs. This paper’s main goal is to bridge the algebraic, geometric, and circuit-level descriptions.

Let _H_<sub>1</sub>_,...,H<sub>s</sub>_ be a collection of Hamiltonians on a finite-dimensional Hilbert space _W_ and \(|\xi\rangle\) the initial state. We write<tbc>

\(G:=\left\langle e^{-itH_j}|t\in\mathbb{R},1\le j\le s\right\rangle\subseteq U(W)\) (1)

<tbc>for the group of finite native-control products. It is a connected subgroup with dynamical Lie algebra

\(\mathfrak{g}=\langle iH_1,\dots,iH_k\rangle_\mathrm{Lie}\) (2)

and need not be closed in _U(W_).

The elements of _G_ are the unitary transformations that can be implemented exactly by finite sequences of native-control evolutions. In particular, the corresponding variational quantum ansatz generates unitaries of the form

\(U_L(\theta)=e^{-i\theta_LH_{j_L}}\cdots e^{-i\theta_1H_{j_1}},j_\ell\in\{1,\dots,k\}.\) (3)

Here, the sequence **_j_**=(_j_<sub>1</sub>_,...,j<sub>L</sub>_) determines the Hamiltonians applied across successive layers, while \(\theta=(\theta_1,\dots,\theta_L)\in\mathbb{R}^L\) provides the corresponding continuous variational parameters, with _L_ denoting the circuit depth.

Consider an initial state \(|\xi\rangle\). Its projective orbit \(G\cdot[\xi]\) consists of the states attainable (up to a global phase) from \(|\xi\rangle\) by finite circuits as in (3), whereas the closure of this orbit describes asymptotic reachability.

We first establish general criteria for converting asymptotic state preparation into exact, finite-depth realization using parameterized circuits of the form (3) (Section IV). We prove that this exactness property is guaranteed whenever the projective dynamical group, defined as the image of _G_ under the quotient map \(U(W)\rightarrow PU(W)\), is closed, as well as when the initial state is a nondegenerate eigenstate of a generator, even when the group itself is not closed (Theorem IV.4). A related result shows that if an observable _H<sub>P</sub>_ satisfies \(iH_P\in\mathfrak{g}\), its energy infimum over a reachable state orbit is attained by a finite circuit (Theorem IV.8). These statements apply to finite-dimensional Hamiltonian variational ansätze generally; neither full unitary controllability nor a specific layer structure is required.

For QAOA, the exact-reachability criterion yields a broad consequence. If the problem Hamiltonian is diagonal and the mixer is irreducible and stoquastic in the computational basis, the mixer possesses a unique Perron–Frobenius ground state. Prior work demonstrates that QAOA initialized in this state approaches the optimal problem Hamiltonian eigenspace (ground space) asymptotically as the depth increases \[5\]. Our criterion upgrades this conclusion: some _finite_ alternating circuit, utilizing only the original mixer and problem Hamiltonian, prepares an exact ground state (Theorem IV.9). This is a statement regarding attainability; it does not bound the minimum circuit depth nor provide an efficient method for computing the optimal angles.

Exact reachability leaves open the quantitative question of the circuit depth required to attain it. Building on conjugation-based iterative DLA basis construction proposed in \[9\], we derive exact local synthesis depth bounds from the commutator order filtration of the DLA (Theorem VI.4). Importantly, the filtration is constructed directly from the set of generators **a** rather than the DLA g itself. If _c<sub>q</sub>_ new linearly independent Lie algebra directions emerge at filtration level _q_, and D**<sub>a</sub>** is the stabilization depth of the filtration, defined as the minimal index at which the filtration stabilizes (see Definition VI.2), any element within a sufficiently small open neighborhood of the identity in the dynamical Lie group can be synthesized using at most

\(\mathcal{T}_\mathrm{loc}\le\sum_{j=1}^{\mathcal{D}_\mathbf{a}}(2j-1)c_j\le(2\mathcal{D}_\mathbf{a}-1)\mathrm{dim}(\mathfrak{g})\) (4)

parametrized exponentials of the basic control Hamiltonians. The corresponding infinitesimal state orbit preparation uses the directions tangent to the orbit, which can be far fewer than the dimension of the group because the state may possess a large _stabilizer_ (i.e., the subgroup of unitaries leaving the state invariant up to a global phase). Thus, the filtration measures how rapidly the physical controls acquire new directions,

