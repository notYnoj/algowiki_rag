<tbc>Lemma 4.13. _The lookup table_ T _answers each subset sampling query for each configuration_ \(\vec{c}\) _for the 4S problem in_ \(O(1+\mu(\vec{c}))\) _expected time, where_ \(\mu(\vec{c})\) _is the expected size of the subset sample._

Proof. Since each \(\vec{c}\) can be encoded in _O_(1) words, locating the row \(A(\vec{c})\) in the lookup table T can be performed in _O_(1) time. By our assumption at the beginning of this section, generating an index of \(A(\vec{c})\) uniformly at random can be achieved in _O_(1) expected time. Retrieving the subset sampling result from the _K_-bit string _r_ can be performed in _O_(1+|_r_|) time in the Word RAM model, where |_r_| is the number of items in the sampling result. Therefore, the overall query time is bounded by \(O(1+\mu(\vec{c}))\) in expectation. □

Lemma 4.14. _The lookup table_ T _can be constructed in O(n_<sub>0</sub>) _time and the space consumption of_ T _is bounded by O(n_<sub>0</sub>).

Proof. For an input configuration \(\vec{c}\), there are 2_<sup>K</sup>_ possible subset sampling results _r_. The probability of each _r_ can be computed in _O(K_) time. Furthermore, \(A(\vec{c})\) contains _m_<sup>2_K_</sup> cells and each cell stores _K_ bits. The total running time for constructing \(A(\vec{c})\) is thus bounded by \(O(K\cdot 2^K+K\cdot m^{2K})=O(K\cdot m^{2K})\) time. Summing over all (_m_+1)_<sup>K</sup>_ rows, the overall construction time of T is bounded by \(O((m+1)^K\cdot K\cdot m^{2K})\) time. As \(K\in O(loglogn_0)\) and \(m\in O(loglogn_0)\), this construction time is thus bounded by _O(n_<sub>0</sub>). In terms of space consumption, T contains in total \((m+1)^K\cdot K\cdot m^{2K}\) bits, which is bounded by _O(n_<sub>0</sub>) words. □

## 4.4 Bridging the Hierarchy and the Lookup  via Adapters

It remains to show how to convert a final-level PSS query instance into an input configuration for the 4S problem in _O_(1) time on the fly during query time. Once this is accomplished, then Lemma 4.11 implies that the PSS query \((\alpha,\beta)\) on _S_ can be answered optimally.

For this purpose, we introduce an _adapter_ for each final-level PSS query instance. And the space consumption of each such adapter is bounded by _O_(1) words. As there are at most _O(n_<sub>0</sub>) final-level<tbc>

(m2) K cells
= (0,0, 0)
= (1,0, 0)
(m + 1)K rows
= (c1, c2, CK)
ro
ro
= (m, m, m)
ro
ro
ro
ro
ro
r1
r1
r1
r2
6
3
Pr(r0) = (m2)K
Pr(r1) = (m2)K

Fig. 2. Visualization of a lookup table. It contains (_m_+1)_<sup>K</sup>_ rows, each row corresponds to a configuration, and each row contains (_m_<sup>2</sup>)_<sup>K</sup>_ cells. Each cell holds a _K_-bit string, e.g. _r_<sub>0</sub>_,r_<sub>1</sub>_,..._. As shown in the figure, for a given configuration \(\vec{c}=\{c_1,c_2,\dots,c_K\}\), if \(Pr(r_0)=\frac{6}{(m^2)^K}\), then there are 6 cells storing _r_<sub>0</sub> in the corresponding row.

