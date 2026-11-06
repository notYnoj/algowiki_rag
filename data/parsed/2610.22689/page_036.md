<tbc>The image \(\iota_\mathcal{P}(\mathrm{Gr}(k,n))\) consists precisely of the rays of _decomposable k_-tensors, physically corresponding to single Slater determinants of _k_ occupied single-particle orbitals. As the mixer restriction \(H_M\big|_{W_k}=-d\Gamma_k(A_{P_n})\) is nondegenerate, its unique _k_-particle ground state is given by the wedge product of the _k_ lowest-energy single-particle orbitals. In particular, the projective ground state \([\xi_k]\) lies within the Plücker image of the Grassmannian Gr(_k,n_). Furthermore, since the natural action of U(_n_) on Gr(_k,n_) is transitive, the dynamical Lie group _G<sub>n,k</sub>_ orbit of any state \([\psi]\in\iota_\mathcal{P}(\mathrm{Gr}(k,n))\) coincides with the full Grassmannian image:

\(\mathcal{O}_{[\psi]}:=G_{n,k}\cdot[\psi]=\iota_\mathcal{P}(\mathrm{Gr}(k,n)).\) (B11)

Since the dynamical Lie group acts transitively on Gr(_k,n_) with stabilizer isomorphic to the maximal block-diagonal subgroup \(\mathrm{U}(k)\times\mathrm{U}(n-k)\), the orbit can be identified with the homogeneous space \(\mathrm{U}(n)/(\mathrm{U}(k)\times\mathrm{U}(n-k))\). Its real manifold dimension is given by the difference of Lie group dimensions:

\(\mathrm{dim}_\mathbb{R}(\mathcal{O}_{[\psi]})=\mathrm{dim}_\mathbb{R}(\mathrm{U}(n))-\mathrm{dim}_\mathbb{R}(\mathrm{U}(k))-\mathrm{dim}_\mathbb{R}(\mathrm{U}(n-k))=n^2-k^2-(n-k)^2=2k(n-k),\) (B12)

which scales at most quadratically in \(n(\mathrm{dim}_\mathbb{R}(\mathcal{O}_{[\psi]})\le n^2/2)\). On the other hand, the dimension of the Hilbert space _W<sub>k</sub>_ is \(\genfrac(){pt}{2}{n}{k}\), and the ground space _W_<sub>_P,_min</sub> of the problem Hamiltonian in (25) has exponential dimension \(\genfrac(){pt}{2}{n-1}{k}\) when \(k\propto n\).

## Appendix C: Derivation of Stabilization Depths for QAOA Architectures

This section provides the rigorous analytical derivation of the stabilization depth bounds for dynamical Lie algebras arising from the QAOA architectures defined in Section VII, formally verifying the assertions made therein.

_Proof of Theorem VII.3._ **Path and Cycle Graphs.** According to  V of \[17\], the bases of the corresponding free DLAs with respective generating sets

\(\mathbf{a}_{P_n,\mathrm{free}}=\{iX_s,iZ_jZ_{j+1}|s\in\{1,\dots,n\},j\in\{1,\dots,n-1\}\}\mathbf{a}_{C_n,\mathrm{free}}=\{iX_s,iZ_jZ_{j+1},iZ_1Z_n|s\in\{1,\dots,n\},j\in\{1,\dots,n-1\}\},\)

consist of the single-site generators _iX<sub>s</sub>_ (for \(s\in\{1,\dots,n\}\)) alongside multi-qubit Pauli strings comprising a contiguous block of _X_ operators on the interior sites {_b_+1_,...,b+k_-1}, bounded at the endpoints _b_ and _b+k_ by pairs of operators from {_Z,Y_}, with identity operators implicitly understood to be assigned to the remaining positions. These composite basis elements are indexed by their starting position _b_ and length parameter _k_:

\(P_{ZZ}^{b,k}=Z_bX_{b+1}\dots X_{b+k-1}Z_{b+k},P_{ZY}^{b,k}=Z_bX_{b+1}\dots X_{b+k-1}Y_{b+k},P_{YZ}^{b,k}=Y_bX_{b+1}\dots X_{b+k-1}Z_{b+k},P_{YY}^{b,k}=Y_bX_{b+1}\dots X_{b+k-1}Y_{b+k},\text{(C1)}\)

where \(1\le b<b+k\le n\) for the path graph, and \(1\le b<b+k\le 2n\) for the cycle graph (with indices evaluated modulo _n_).

Any such string can be generated iteratively from the core two-local generators. For instance, \(P_{ZZ}^{b,k}\) is constructed via the following sequence of commutators:

\([X_{b+1},Z_bZ_{b+1}]\propto Z_bY_{b+1},[Z_{b+1}Z_{b+2},Z_bY_{b+1}]\propto Z_bX_{b+1}Z_{b+2},[X_{b+2},Z_bX_{b+1}Z_{b+2}]\propto Z_bX_{b+1}Y_{b+2},[Z_{b+2}Z_{b+3},Z_bX_{b+1}Y_{b+2}]\propto Z_bX_{b+1}X_{b+2}Z_{b+3},\text{(C2)}\)

