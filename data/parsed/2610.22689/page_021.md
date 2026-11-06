<tbc>where P_<sub>v</sub>_ is a projector onto the subspace in which all neighbors of _v_ are in the state \(|0\rangle\). By construction, each _H<sub>CX,v</sub>_ preserves the feasible subspace _W_<sub>F</sub>. Furthermore, since the problem Hamiltonian is diagonal in the computational basis, it preserves _W_<sub>F</sub> as well.

Consequently, it is natural to define the restricted free dynamical Lie algebra associated with these generators on _W_<sub>F</sub> as

\(\mathfrak{g}_{\Gamma,\mathrm{free},\mathcal{F}}:=\left\langle\left\{iH_{CX,v}\right|_{W_\mathcal{F}},iZ_v\right|_{W_\mathcal{F}}\right\}_{v\in V}\right\rangle_\mathrm{Lie}.\) (70)

The following result establishes that this restricted algebra achieves full Lie-algebraic controllability on the feasible subspace, while providing an explicit upper bound on its stabilization depth that scales linearly with the number of vertices and the independence number.

**Theorem VII.6.** Let \(\Gamma\) be a connected graph with \(|V(\Gamma)|\ge 2\) vertices, and independence number \(\alpha(\Gamma)\). The restricted free dynamical Lie algebra \(\mathfrak{g}_{\Gamma,\mathrm{free},\mathcal{F}}\) and its stabilization depth satisfy

\(\mathfrak{g}_{\Gamma,\mathrm{free},\mathcal{F}}\cong\mathfrak{u}(W_\mathcal{F})\text{and}\mathcal{D}_{\mathfrak{g}_{\Gamma,\mathrm{free},\mathcal{F}}}\le 8|V(\Gamma)|+4\alpha(\Gamma)-2.\) (71)

## D. Dynamical Lie Algebras for the Grover-Mixer QAOA

The Grover-mixer QAOA (GM-QAOA), introduced in \[4\], replaces standard local mixers with a highly nonlocal mixer Hamiltonian. The algorithm typically starts in a uniform superposition over all feasible configurations F,

\(|\xi\rangle:=\frac{1}{\sqrt{|\mathcal{F}|}}\sum_{x\in\mathcal{F}}|x\rangle.\) (72)

The Grover mixer _G<sub>M</sub>_ is defined as the orthogonal projection (up to a negative sign) onto this initial state:

\(G_M:=-|\xi\rangle\left\langle\xi\right|.\) (73)

Let _d_ denote the number of distinct values attained by the objective function _F_ over F. For each \(j\in\{1,\dots,d\}\), let \(\mathcal{F}_j\subseteq\mathcal{F}\) be the _j_-th level set of _F_, and define the normalized level-set state

\(|\xi_j\rangle:=\frac{1}{\sqrt{|\mathcal{F}_j|}}\sum_{x\in\mathcal{F}_j}|x\rangle.\) (74)

As established in \[31, Section V\], the quantum evolution under GM-QAOA remains strictly confined to the _d_-dimensional invariant subspace \(W_0\subseteq W\) spanned by these level-set states:

\(W_0:=\mathrm{span}\big\{|\xi_1\rangle,\dots,|\xi_d\rangle\big\}.\) (75)

Restricting both the mixer _G<sub>M</sub>_ and the problem Hamiltonian _H<sub>P</sub>_ to _W_<sub>0</sub>, we obtain the associated dynamical Lie algebra

\(\mathfrak{g}_\xi:=\left\langle iG_M\right|_{W_0},iH_P\big|_{W_0}\right\rangle_\mathrm{Lie}.\) (76)

Theorem III.1 of \[31\] shows that \(\mathfrak{g}_\xi\) is the full unitary algebra on this subspace:

\(\mathfrak{g}_\xi\cong\mathfrak{u}(W_0)\cong\mathfrak{u}(d).\) (77)

Consequently, GM-QAOA is fully controllable on _W_<sub>0</sub>, whose dimension equals the number _d_ of distinct objective-function values on the feasible set.

