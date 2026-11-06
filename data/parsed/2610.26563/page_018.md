For \((i,j,k)\in\mathcal{B}(\mathcal{S})\), the remaining term is \(\phi_{ijk}\) of Definition 15. When the three selected part sizes sum to _d_, every local multiplicity in a choice in B(S) equals one and \(\phi_{ijk}\) is itself a matrix multiplication trilinear form. If the selected part sizes sum to less than _d_, coordinates with \(\eta_r=0\) remain and \(\phi_{ijk}\) is a centered trilinear form rather than a matrix multiplication tensor.

For each replicated intersection, inclusion-exclusion subtracts the aggregate with one coordinate deleted, adds those with two coordinates deleted, and continues over its subsets. This preserves the desired products and cancels every mixed product with a replicated coordinate. The following identity gives both the remaining terms and the cost of these corrections.

**Lemma 6** (Centered correction identity)**.** _Define_<tbc>

\(\Phi_\mathcal{S}=\sum_{P\in\{\emptyset\}\cup\mathcal{P}(\mathcal{S})}(-1)^{|P|}(n+1)^{|P|}\mathcal{A}_\mathcal{S}(P).\) (92)

<tbc>_For the target form_ \(\phi_\mathcal{S}\) _defined in_ (80),<tbc>

\(\Phi_\mathcal{S}=\phi_\mathcal{S}+\sum_{(i,j,k)\in\mathcal{B}(\mathcal{S})}\phi_{ijk},R(\Phi_\mathcal{S})\le\rho_\mathcal{S}(n).\) (93)

<tbc>_Proof._ Apply (87) with Q=P(S). For a diagonal choice, \(\mathcal{R}_{ttt}=\emptyset\) and _Q<sup>T</sup>Q=I<sub>n</sub>_ recovers the desired product. If some \(\eta_r=2\), then \(\phi_{ijk}=0\) by centering. For every remaining choice with \(\mathcal{R}_{ijk}\neq\emptyset\), all its nonempty subsets belong to P(S), so

\(c_{\mathcal{P}(\mathcal{S})}(\mathcal{R}_{ijk})=\sum_{P\subseteq\mathcal{R}_{ijk}}(-1)^{|P|}=0.\) (94)

The other non-diagonal choices are exactly B(S). Summing (83) over the evaluated aggregates gives the rank bound.

For a fixed-shape family \(\mathcal{S}\subseteq B_{s,t,v}\), every mixed choice has

\(\sum_{r\in F}\eta_r(i,j,k)=|U_i|+|V_j|+|W_k|=t+s+v=d.\) (95)

Hence a choice with \(\eta_r\le 1\) for all _r_ must have \(\eta_r=1\) for every _r_. In this case B(S) consists exactly of the non-diagonal compatible combinations of Definition 7.

If this fixed-shape family is conflict-free, no mixed products remain, so the identity is already an exact algorithm.

Splitting the weighted aggregate of Algorithm 1 by the coordinates _P_ at the padded index _n_+1 gives

\(\Phi_\mathcal{S}^\mathrm{wt}=\sum_{P\subseteq F}(-1)^{|P|}(n+1)^{|P|}\mathcal{A}_\mathcal{S}(P).\) (96)

Padding leaves only blocks that omit _P_, and their three weight factors multiply to (-1)<sup>|_P_|</sup>(_n_+1)<sup>|_P_|</sup>. Thus the weighted algorithm evaluates all subsets, while the corrected algorithm retains only those needed.

Since P(S) consists of nonempty subsets of _F_,

\(\rho_\mathcal{S}(n)\le\sum_{P\subseteq F}(n+1)^{d-|P|}=(n+2)^d.\) (97)

Thus the corrected algorithm uses at most the rank budget of the weighted embedding, with lower counts when fewer subsets require correction.

