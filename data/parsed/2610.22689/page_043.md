<tbc>Similarly, utilizing the decomposition of a CNOT gate into Pauli string exponentials up to a global phase,<tbc>

\([\mathrm{CX}_{c\rightarrow t}]=\left[e^{-i\pi(I_c\otimes X_t)/4}e^{-i\pi(Z_c\otimes I_t)/4}e^{i\pi(Z_c\otimes X_t)/4}\right],\) (D3)

<tbc>each of the three constituent two-qubit Pauli string flows can likewise be conjugated into native generators with depth at most 2D**<sub>a</sub>**-1, giving

\(K_\mathrm{CX}\le 3(2\mathcal{D}_\mathbf{a}-1)=6\mathcal{D}_\mathbf{a}-3.\) (D4)

Substituting _K_<sub>1q</sub> and _K_<sub>CX</sub> into the general circuit-level bounds of Theorem VIII.4 directly yields the total depth bounds.

We next establish the proof of Theorem VIII.8 by breaking down the construction into three core technical phases: exact synthesis of diagonal operators, toggle-controlled extraction of single matrix units, and obtaining the resulting global and state-to-state depth bounds.

### a. Exact Synthesis of Diagonal Operators

We now establish an explicit depth bound for synthesizing arbitrary diagonal unitaries on the feasible subspace _W_<sub>F</sub>. Let \(D:=|\mathcal{F}|\ge 4\), and assume the underlying graph \(\Gamma=(V,E)\) is connected.

For any vertex \(v\in V\) , consider the local Pauli-_Z_ operator restricted to _W_<sub>F</sub>, denoted by _Z<sub>v</sub>|_<sub>_W_<sub>F</sub></sub>. Partition the feasible set into bitstrings where the bit at position indexed by _v_ is empty vs. occupied:<tbc>

\(\mathcal{F}_v^0:=\{x\in\mathcal{F}|x_v=0\},\mathcal{F}_v^1:=\{x\in\mathcal{F}|x_v=1\}.\) (D5)

<tbc>The matrix trace of _Z<sub>v</sub>|_<sub>_W_<sub>F</sub></sub> counts the difference in subset sizes:

\(\mathrm{Tr}_{W_\mathcal{F}}(Z_v)=|\mathcal{F}_v^0|-|\mathcal{F}_v^1|>0.\) (D6)

Indeed, flipping the _v_th bit gives a one-to-one map from \(\mathcal{F}_v^1\) into \(\mathcal{F}_v^0\). However, this map fails to be surjective whenever _v_ has a neighbor \(w\in\mathcal{N}_v\), as the single-vertex independent set \(\{w\}\in\mathcal{F}_v^0\) cannot lie in its image.

Let \(\mu_v:=\frac{1}{D}\mathrm{Tr}_{W_\mathcal{F}}(Z_v)>0\) denote the normalized trace, and define the traceless centered operator<tbc>

\(Z_{v,0}:=Z_v|_{W_\mathcal{F}}-\mu_vI_{W_\mathcal{F}},\mathrm{Tr}_{W_\mathcal{F}}(Z_{v,0})=0.\) (D7)

<tbc>For any permutation \(P\in\mathcal{T}(\Gamma)\), denote its unitary matrix representation on _W_<sub>F</sub> by \(\widehat{P}\in\mathrm{U}(W_\mathcal{F})\). We form the traceless diagonal difference operator<tbc>

\(B_P:=Z_v|_{W_\mathcal{F}}-\widehat{P}Z_v|_{W_\mathcal{F}}\widehat{P}^\dagger=Z_{v,0}-\widehat{P}Z_{v,0}\widehat{P}^\dagger,\) (D8)

<tbc>and define the real linear span

\(\mathcal{E}_v:=\mathrm{span}_\mathbb{R}\{B_P|P\in\mathcal{T}(\Gamma)\}\subseteq\mathfrak{d}_0(W_\mathcal{F}),\) (D9)

where \(\mathfrak{d}_0(W_\mathcal{F})\cong\mathbb{R}^{D-1}\) denotes the space of all traceless diagonal Hermitian operators on _W_<sub>F</sub>.

By a result of Striker \[28, Corollary 3.24\], for every connected graph \(\Gamma\), the toggle group satisfies

\(A_\mathcal{F}\subseteq\mathcal{T}(\Gamma)\subseteq\mathrm{Sym}(\mathcal{F}),\) (D10)

where _A_<sub>F</sub> and Sym(F) denote the alternating and symmetric groups on F, respectively.

For every \(Q\in\mathcal{T}(\Gamma)\), one has

\(\widehat{Q}B_P\widehat{Q}^\dagger=B_{QP}-B_Q\in E_v,\)

which proves that _E<sub>v</sub>_ is a \(\mathcal{T}(\Gamma)\)-invariant subspace (subrepresentation) of d<sub>0</sub>(_W_<sub>F</sub>).

To show that _E<sub>v</sub>_=d<sub>0</sub>(_W_<sub>F</sub>), first note that \(E_v\neq\{0\}\): the diagonal operator _Z_<sub>_v,_0</sub> is nonconstant because the feasible configurations \(\varnothing\) and {_v_} have opposite _Z<sub>v</sub>_-eigenvalues, and the transitive action of \(\mathcal{T}(\Gamma)\) cannot fix a nonconstant diagonal vector. Since the subspace d<sub>0</sub>(_W_<sub>F</sub>) is isomorphic to the standard real representation

