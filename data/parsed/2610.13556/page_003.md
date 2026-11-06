<tbc>The response description also yields a general repetition theorem for ordinary villainy. Theorem 4.11 gives a computable rational number \(\Lambda(G)\ge F_k(G)\) such that

\(B(mG)=m\Lambda(G)+O_G(1).\)

Here _O<sub>G</sub>_(1) denotes an error bounded by a constant depending only on _G_. The slope comes from an optimization that allows fractional proportions of copies to receive each source and target coloring, as defined in (4.15). Its maximum is attained by a distribution using at most _k_ source words. Moreover, \(B(mG)-m\Lambda(G)\) is eventually periodic, with a computable period and threshold. Thus Theorem 4.12 determines the possible growth of the difference between the repair rules: it is bounded precisely when \(\Lambda(G)=F_k(G)\), in which case it is eventually periodic; otherwise it grows linearly.

### 1.2. Fixed-parameter recognition.

Our algorithmic result computes both exact parameters using the potentially smaller weak villainy as parameter. Theorem 5.1 gives running time _h(B_<sub>w</sub>(_G_))(_n_+1)_<sup>c</sup>_, where _h_ is computable and _c_ is an absolute constant, without either value being supplied. Given an integer \(t\ge 0\), it also computes the two truncated values

\(min\{B(G),t+1\}\text{and}min\{B_\mathrm{w}(G),t+1\}\)

in time _f(t_)(_n_+1)_<sup>c</sup>_ for a computable function _f_. Thus both equality recognition, deciding whether a parameter equals _t_, and threshold recognition, deciding whether it is at most _t_, are fixed-parameter tractable in _t_: the polynomial exponent in the input size is independent of _t_. They are polynomial-time problems at every fixed value. In particular, unless P=NP, there is no fixed value at which villainy recognition is NP-complete.

The structural input is a matching bound. If \(B_\mathrm{w}(G)\le t\), then either _G_ has a vertex cover of size at most 2_t_, or \(\chi(G)\ge n-2t\) and the complement of _G_ has a vertex cover of size at most 4_t_. The same conclusion holds when \(B(G)\le t\). The proof groups vertices outside these covers by their neighborhoods and retains only source profiles realized by optimal proper colorings. In the small-cover case, a bounded-length formula with variables for the type sizes permits elimination of its quantified variables before the input multiplicities are substituted. In the complement-cover case, symmetries that fix the source coloring remove the need to enumerate singleton color names individually. The polynomial exponent is independent of _t_; the proof does not give a practical bound on the function _f_.

### 1.3. Related repair problems and organization.

Garnero et al. [9] study repair of an arbitrary given coloring and the fixing number used above. De Biasi and Lauri [5] consider a source promised to be a rearrangement of an optimal coloring. Their _r_-Fix-Promise problem is an individual weak-repair instance; their swap problem uses the number of color exchanges as cost. Our recognition problem quantifies over every admissible disturbance.

Count-aware component optimization also appears in the two-color repair algorithm of Fellows et al. [7]. It chooses orientations of bipartite components for one given source, subject to total color counts and a swap budget. For villainy, one must additionally retain jointly realizable responses before taking the worst-source maximum.

Finally, endpoint Hamming distance differs from proper-coloring reconfiguration [1, 8], where every intermediate coloring must be proper. Ordinary villainy constrains only the initial and final color multiplicities.

Section 2 fixes the notation and definitions. Section 3 gives the counterexamples to superadditivity. Section 4 develops the profile composition laws and the repeated-copy theorem. Section 5 proves fixed-parameter recognition, and Section 6 discusses further questions.

## 2. Color profiles and repair distances

All graphs are finite and simple. Unless otherwise stated, a graph _G_ is nonempty, has order _n_, and has chromatic number _k_. We use a fixed set C of _k_ labeled colors.

