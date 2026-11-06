<tbc>**Lemma 5.6.** _If_ |_U_|=_s and V(G_)\\_U is a clique, then_ \(\chi(G)\) _can be computed in time_ 2<sup>_O(s_log(_s_+2))</sup>(_n_+1)<sup>_O_(1)</sup>.

_Proof._ Enumerate the partitions \(\pi\) of _U_ into independent sets. In any proper coloring inducing \(\pi\), a vertex of _W_ either has a color not used on _U_, or shares a color with one part of \(\pi\). No two vertices of _W_ can share a color. Thus the possible sharing is described by a matching in the bipartite graph whose sides are \(\pi\) and _W_, with a part adjacent to \(v\in W\) when _v_ has no neighbor in that part. If a maximum matching has size \(a(\pi)\), the fewest colors for this partition are

\(|\pi|+|W|-a(\pi).\)

Taking the minimum over \(\pi\) gives \(\chi(G)\). There are at most _s<sup>s</sup>_ partitions for \(s\ge 1\), and each matching is computed in polynomial time. The empty partition handles _s_=0. □

We shall use the following elementary fact to handle the many singleton color classes. It does not depend on the structure of _G_.

**Lemma 5.7.** _Let_ \(\mathbf{m},\mathbf{m}'\) _be positive profiles on_ \[_k_\] _of the same total size, and suppose that G admits a proper coloring of profile_ \(\mathbf{m}'\)_. Let_ \(J\subseteq[k]\) _contain every color having multiplicity at least two in either profile. Replace each color outside J by a common label_ ∗_. For a fixed word w of profile_ **m**_, the minimum Hamming distance to a proper coloring of profile_ \(\mathbf{m}'\) _equals the minimum Hamming distance between the resulting label maps._

_Proof._ Different labels imply different colors, so passing to labels can only decrease a distance. To prove the reverse inequality, take any proper coloring _y_ of profile \(\mathbf{m}'\) and let _R<sub>w</sub>,R<sub>y</sub>_ be the positions with label ∗ in the two maps. Both restrictions to the star positions are bijections onto the same color set _S_=\[_k_\]\\_J_, since every color in _S_ has multiplicity one in both profiles.

Keep the colors of _y_ outside _R<sub>y</sub>_. On \(R_w\cap R_y\), assign the colors of _w_. Fill _R<sub>y</sub>_\\_R<sub>w</sub>_ bijectively with the unused colors in _S_. This preserves the target profile and properness: all changed color classes are singletons. It also makes the two colorings agree at every position at which their label maps agree. Consequently its Hamming distance from _w_ is exactly the label distance of the original pair. Minimizing proves the assertion. □

We can now combine the type description with Theorem 5.7: only the colors occurring more than once need individual names. The resulting count is controlled by the size of the cover and by the difference between the order and chromatic number.

**Proposition 5.8.** _Suppose that_ \(|U|\le s\), _V(G_)\\_U is a clique, and_ \(n-\chi(G)\le e\)_. Then both B(G_) _and B_<sub>w</sub>(_G_) _can be computed in time f(s,e_)(_n_+1)<sup>_O_(1)</sup>_, for a computable function f. One may take_<tbc>

\(f(s,e)=2^{O(se+(s+e)log(s+e+2))}.\)

<tbc>_Proof._ Compute \(k=\chi(G)\) by Theorem 5.6, and put \(d=n-k\le e\). For every positive profile **m** on \[_k_\],<tbc>

\(\sum_i(m_i-1)=d.\)

<tbc>Consequently its set _N_ of nonsingular colors has size at most _d_, and

\(\sum_{i\in N}m_i=d+|N|\le 2e.\)

Up to a permutation of color names, there are only a bounded number of such profiles: their nonsingular excesses _m<sub>i</sub>_-1 form a partition of _d_. A _profile shape_ is a profile considered up to a permutation of color names. We enumerate these shapes, choose a labeled representative of each, and discard it if it is not the profile of a proper coloring. The properness test is included in the description enumeration below. A simultaneous permutation of color names preserves repair distances, so these representatives suffice for the outer maximum in both parameters.

First consider _B(G_) and fix one such profile **m**. Use labels \(N\cup\{*\}\), with ∗ replacing singleton colors. The nonsingular labels occupy at most 2_e_ vertices. For a label map to come<tbc>

