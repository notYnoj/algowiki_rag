## A.5.1 Disjoint cycles

Let _P_ be the permutation matrix of the port involution, and let _J<sub>D</sub>_ be the all-ones matrix. The transition matrix for a nonbacktracking port word is _Q=J<sub>D</sub>-P_. Its eigenvalues are _D_-1, 1, and -1 with multiplicity _D_-2. Hence

\(\mathrm{tr}(Q^L)=(D-1)^L+1+(D-2)(-1)^L=(1+o(1))(D-1)^L.\) (189)

For two vertex-disjoint cycles the channel events are independent. There are (_n_)<sub>2_L_</sub>/(2_L_)<sup>2</sup> ordered pairs of labelled vertex cycles. Applying (171) to their union and (189) to each cycle bounds their contribution to E_Y_ <sup>2</sup> by

\((1+o(1))\frac{(n)_{2L}}{(2L)^2}n^{-2L}(D-1)^{2L}p_L^2=(1+o(1))\mu_L^2.\) (190)

## A.5.2 Overlapping cycles

Consider distinct length-_L_ cycles with _j_ common edges. Their intersection consists of paths and isolated vertices. If it has \(k\ge 1\) components, their union has

\(w=2L-j\text{edges},v=2L-j-k\text{vertices}.\) (191)

There are at most (_CL)<sup>Ck</sup>_ abstract intersection patterns: record the endpoints of the common paths on both cycles, pair the components, and record their orientations. Isolated vertices use coincident endpoints. This bound is independent of _j_.

For each pattern there are at most _n<sup>v</sup>_ embeddings and _D(D_-1)<sup>_w_-1</sup> connected port-labellings. By (171), its graph contribution, including B_<sub>n</sub>_, is at most

\((1+o(1))\frac{D}{D-1}n^{-k}(D-1)^{2L-j}.\) (192)

Let _J_ count unordered favorable pairs sharing a vertex, setting _J_=0 outside B_<sub>n</sub>_. Combining this bound with Eqs. (183) and (188) and summing over _j_ gives

\(\frac{\mathbb{E}J}{\mu_L^2}\le L^{C_1}\sum_{k=1}^L\left(\frac{CL^{C_1}}{n}\right)^k\mathrm{max}_{0\le j<L}\left((D-1)Z^2\right)^{-j}=o(1).\) (193)

Indeed, (_D_-1)_Z\>_1 implies ((_D_-1)_Z_<sup>2</sup>)<sup>-1</sup>_\<D_-1, so (172) bounds the maximum by \((D-1)^L\le n^\kappa\). The sum is therefore \(n^{\kappa-1+o(1)}=o(1)\).

## A.5.3 Disjoint favorable cycles and decoding failure

The diagonal contribution to E_Y_ <sup>2</sup> is \(\mathbb{E}Y=o(\mu_L^2)\). Together with Eqs. (188), (190) and (193), this gives

\(\frac{Y}{\mu_L}\rightarrow 1,\frac{J}{\mu_L^2}\rightarrow 0\text{in probability}.\) (194)

Join two favorable cycles when they share a vertex. An independent set in this intersection graph has size at least _Y_<sup>2</sup>/(_Y_+2_J_) when _Y\>_0. This bound follows by ordering its vertices uniformly at random and retaining each vertex that precedes all its neighbors: the expected number retained<tbc>

