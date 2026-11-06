<tbc>from a proper coloring, the vertices assigned each nonstar label must form an independent set. This can be checked from the description: its vertices in _U_ must be independent, the label may occur at most once in the clique _W_, and any such vertex must have a type disjoint from that label’s vertex set in _U_. The star positions impose no constraint, because they receive distinct singleton colors. We retain only descriptions having total count _m<sub>i</sub>_ for every \(i\in N\) and total star count _k_-|_N_|, for both sources and targets.

By Theorem 5.7, the distance to a best repair of the same profile is exactly the distance to a best proper label map. By Theorem 5.4, this minimum, and then the maximum over disturbed words, can be evaluated using descriptions alone. The number of descriptions is bounded by a function of _s,e_. For example, after choosing the at most (_e_+1)_<sup>s</sup>_ labels on _U_, the at most 2_e_ nonstar occurrences outside _U_ are distributed among at most _e_2_<sup>s</sup>_ label-type pairs. An overcount is

\((e+1)^s(e2^s+1)^{2e}.\)

Star counts are then determined by the type sizes. Testing all descriptions and comparing all pairs proves the first running-time bound.

For weak villainy, the target may have a different profile. Here the choice of target nonsingleton colors must be made after the disturbed word has been fixed. We describe this order explicitly. For each source description using labels \(N\cup\{*\}\), choose one full-color representative _w_, assigning the source singleton colors bijectively to its star positions. All words represented by this reduced description have the same weak repair distance. Indeed, two such words are related by an automorphism in \(\Gamma\) followed by a permutation of singleton color names that fixes _N_. Both transformations preserve Hamming distances and the set of proper _k_-colorings.

With _w_ fixed, let \(N'\) be the nonsingleton colors of a target. Colors in \(N'\backslash N\) are singleton in the source; call them _promoted colors_. Each is identified by its unique position in _w_. Enumerating their names separately would introduce a factor depending on _n_ with exponent _e_. We avoid this by using symmetries that fix the full source word.

Let \(\gamma\in\Gamma\) permute only source-star positions within each outside type, fixing all other vertices. Define a color permutation \(\pi_\gamma\) by \(\pi_\gamma(w(v))=w(\gamma(v))\) on source singleton colors, and fix every color in _N_. For any target coloring _y_, put

\((T_\gamma y)(v)=\pi_\gamma\big(y(\gamma^{-1}(v))\big).\)

Then \(T_\gamma w=w\). Moreover, \(T_\gamma\) preserves properness and Hamming distance, because \(\gamma\) is a graph automorphism and \(\pi_\gamma\) is a permutation of colors. In particular, \(d_\mathrm{H}(w,T_\gamma y)=d_\mathrm{H}(w,y)\).

These transformations act transitively on choices of promoted colors that occupy the same source singleton positions in _U_ and have the same number of source positions in each outside type. Consequently, we need only choose a subset of the source singleton positions in _U_, and integers \(h_\tau\ge 0\) with \(\sum_\tau h_\tau\le e\), not exceeding the available number of source-star positions of type \(\tau\). For each choice, fix one set of \(h_\tau\) singleton names from that type. There are at most 2_<sup>s</sup>_(2_<sup>s</sup>_+1)_<sup>e</sup>_ such choices: the count vectors are overcounted by sequences of _e_ type names or unused slots. Choose also the subset \(N'\cap N\), and retain only sets with \(|N'|\le d\). For each resulting \(N'\), enumerate every assignment

\(m'_i\ge 2(i\in N'),m'_i=1(i\notin N'),\sum_{i\in N^\prime}(m'_i-1)=d.\)

Every target is equivalent, under a transformation fixing _w_, to one of these choices. Its excesses are carried along by the color permutation and occur in the enumeration. For each choice, use the label set \(J\cup\{*\}\) with \(J=N\cup N'\). The star label now represents exactly the colors that are singleton in both profiles. Theorem 5.7 applies to this fixed source and target profile, and Theorem 5.4 computes the minimum over proper target descriptions. Colors in \(N'\backslash N\) have one source occurrence, and colors in \(N\backslash N'\) have one target occurrence; these occurrences retain their individual labels. Thus no potential agreement is lost by the reduction. Each target description must have total count \(m'_i\) for \(i\in J\) and exactly _k_-|_J_| star positions; target profiles with no proper description are discarded.

