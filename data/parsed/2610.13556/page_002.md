<tbc>the cost of repairing one source at each target profile (Theorem 4.8). For graphs of small weak villainy, a structural bound reduces all relevant colorings to boundedly many vertex types, grouping vertices with the same neighbors in a specified vertex set (Section 5.2).

## 1.1. Disjoint unions and profile composition.

The requirement that the global source profile be feasible couples the components. Although a disturbance preserves the total number of occurrences of each color, its restriction to a component need not have the profile of any proper coloring of that component. Similarly, an ordinary repair may transfer color multiplicities between components while preserving their global totals. When the chromatic numbers differ, one component also gains access to a larger palette. These features distinguish villainy from the unrestricted Hamming covering radius, the greatest distance of any word to a prescribed set of words. That radius is additive on Cartesian products of codes [3, Section II.C].

Our first results answer both unrestricted superadditivity questions negatively. For every real _C\>_0, there exists a connected graph _G_ such that<tbc>

\(B_\mathrm{w}(G\sqcup K_3)<B_\mathrm{w}(G)+B_\mathrm{w}(K_3)-C.\)

<tbc>Thus one summand in the weak counterexample can be a fixed triangle. For ordinary villainy, equal chromatic numbers do not suffice: for every real _C\>_0, there exists a connected graph _G_ with \(\chi(G)=3\) such that

\(B(G\sqcup G)<2B(G)-C.\)

Theorems 3.1 and 3.2 give explicit constructions.

To describe what replaces additivity, we keep track of source and target profiles. For weak repair, the relevant local information is the largest repair distance among words of each prescribed source profile, with the palette fixed in advance. Theorem 4.3 expresses the value on a union through these local radii. The formula separates the effect of changing the palette from that of transferring color counts between components. It gives an exact equality criterion in local profile data, including when the chromatic numbers differ.

Repeated copies admit a particularly simple weak-repair theorem. Let _mG_ denote the disjoint union of _m_ copies of _G_, put \(k=\chi(G)\), and let _F<sub>k</sub>(G_) be the _k_-fixing number of Garnero et al. [9]: the maximum distance to a proper _k_-coloring over _all_ source words on that palette. If _m=qk+r_ with \(0\le r<k\), Theorem 4.5 proves<tbc>

\(0\le mF_k(G)-B_\mathrm{w}(mG)\le r\big(F_k(G)-B_\mathrm{w}(G)\big).\)

<tbc>In particular, _B_<sub>w</sub>(_mG_)=_mF<sub>k</sub>(G_) whenever _k_ divides _m_, and _B_<sub>w</sub>(_mG)/m_ converges to _F<sub>k</sub>(G_). Moreover, weak villainy is additive over every repetition if and only if _B_<sub>w</sub>(_G_)=_F<sub>k</sub>(G_); it suffices to test the union of _k_ copies. The proof balances the color counts of a worst unrestricted source by cyclically relabeling its colors on _k_ copies. Theorem 4.6 makes the eventual behavior effective. For _n_=|_V(G_)| and \(k\ge 2\), put<tbc>

\(M=\big(2(k-1)n+1\big)^{k-1},N=(k-1)M.\)

<tbc>For every \(m\ge N\), the defect _mF<sub>k</sub>(G_)-_B_<sub>w</sub>(_mG_) is periodic. Its least period is

\(h=\mathrm{gcd}\{\ell\ge 1:B_\mathrm{w}(\ell G)=\ell F_k(G)\},h|k,\)

and the gcd can be computed using only \(\ell\le M\). Beyond _N_, the fixing-number bound is attained exactly when _h|m_. These weak-repair results hold on any fixed palette of size at least \(\chi(G)\).

Ordinary repair requires more information. A single disturbed coloring has a repair cost for each possible target profile, and these costs must be retained together. Maximizing each coordinate separately can combine costs that no single disturbance realizes. We therefore use the full response functions and discard only those bounded above at every target profile by another realizable response. To combine two responses, we minimize the sum of their costs over all splits of the target profile. This operation, called min-plus convolution in Theorem 4.8, gives Theorem 4.9. The resulting equality tests are finite criteria in component data; they do not constitute a structural classification of all equality pairs.

