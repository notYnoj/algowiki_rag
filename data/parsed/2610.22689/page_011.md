<tbc>**Remark V.1.** Physically, _H<sub>M</sub>_ corresponds to the isotropic limit (\(\gamma=0\)) of the 1D _XY_ spin chain with free boundary conditions introduced by Lieb, Schultz, and Mattis \[20\]. The problem Hamiltonian _H<sub>P</sub>=N_<sub>1</sub> acts as a localized boundary potential (or single-site occupation pin). Particle-number-preserving _XY_ mixers of this form serve as a standard mechanism for hard-constrained optimization in the Quantum Alternating Operator Ansatz \[16\].

The mixer _H<sub>M</sub>_ in (23) generates nearest-neighbor excitation-hopping transitions, thereby commuting with the total particle-number operator \(\sum_{j=1}^nN_j\) and preserving each fixed-particle subspace _W<sub>k</sub>_ defined in (22). When restricted to _W<sub>k</sub>_, the operator _H<sub>M</sub>_|<sub>_W<sub>k</sub>_</sub> is irreducible with entrywise non-positive off-diagonal matrix elements in the computational basis. Consequently, by the Perron-Frobenius theorem, _H<sub>M</sub>_|<sub>_W<sub>k</sub>_</sub> possesses a unique ground state \(|\xi_k\rangle\), whose computational basis expansion coefficients are strictly positive. Furthermore, the optimal configurations for the problem Hamiltonian _H<sub>P</sub>=N_<sub>1</sub> within _W<sub>k</sub>_ are precisely those computational basis states \(|S\rangle\) for which site 1 is unoccupied (\(1\notin S\)):

\(W_{P,\mathrm{min}}=\mathrm{ker}\big(N_1\big|_{W_k}\big)=\mathrm{span}\{|S\rangle|S\subseteq\{1,\dots,n\},|S|=k,1\notin S\}\) (24)

and has real dimension

\(\mathrm{dim}_\mathbb{R}(W_{P,\mathrm{min}})=2\genfrac(){pt}{2}{n-1}{k}.\) (25)

The following proposition establishes that the initial state \(|\xi_k\rangle\) generates a low-dimensional orbit that nonetheless spans the entire subspace _W<sub>k</sub>_ and contains exponentially many exact optima.

**Proposition V.2.** Let \(W_k\subset(\mathbb{C}^2)^{\otimes n}\) be the _k_-Hamming weight subspace defined in (22), let

\(\mathfrak{g}_{n,k}=\left\langle iH_M\big|_{W_k},iH_P\big|_{W_k}\right\rangle_\mathrm{Lie}\)

be the associated dynamical Lie algebra, and let \(G_{n,k}\subseteq\mathrm{U}(W_k)\) be its connected dynamical Lie group. Then, for an initial reference state \(|\xi_k\rangle\) corresponding to a single Slater determinant formed by _k_ occupied single-particle orbitals, the DLA g_<sub>n,k</sub>_, the projective orbit \(\mathcal{O}_{[\xi_k]}=G_{n,k}\cdot[\xi_k]\), and the cyclic subrepresentation \(W_{\mathfrak{g}_{n,k},|\xi_k\rangle}\) satisfy:

\(\mathfrak{g}_{n,k}\cong\mathfrak{u}(n),\mathrm{dim}_\mathbb{R}(\mathfrak{g}_{n,k})=n^2,\) (26)

\(\mathrm{dim}_\mathbb{R}\mathcal{O}_{[\xi_k]}=2k(n-k),\) (27)

\(W_{\mathfrak{g}_{n,k},|\xi_k\rangle}=W_k,\mathrm{dim}_\mathbb{R}(W_{\mathfrak{g}_{n,k},|\xi_k\rangle})=2\genfrac(){pt}{2}{n}{k}.\) (28)

All \(\genfrac(){pt}{2}{n-1}{k}\) optimal computational basis states are exactly reachable, up to a global phase, by finite alternating circuits as in (15).

**Remark V.3.** At half-filling \(k=\lfloor(n-1)/2\rfloor\), both the cyclic space dimension and the number of mutually orthogonal reachable optimal states grow exponentially as \(n\rightarrow\infty\):

\(\genfrac(){pt}{2}{n}{k}=\Theta\left(\frac{2^n}{\sqrt{n}}\right)\mathrm{and}\genfrac(){pt}{2}{n-1}{k}=\Theta\left(\frac{2^n}{\sqrt{n}}\right),\) (29)

whereas the dynamical Lie algebra orbit dimension scales only quadratically as O(_n_<sup>2</sup>).

A complete, rigorous proof of Proposition V.2, together with its representation-theoretic details and geometric interpretations, is provided in Appendix B; a schematic overview of this geometric phenomenon is illustrated in Figure 3.

