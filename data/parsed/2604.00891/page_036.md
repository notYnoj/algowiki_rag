consecutive pair (_v<sub>x<sub>i</sub></sub>,v_<sub>_x<sub>i</sub>_+1</sub>) lies within the same connected component of _G<sub>X</sub>_ or of \(G'_Y\), that is, there are paths in _G<sub>X</sub>_ or \(G'_Y\) connecting _x<sub>i</sub>_ and _x_<sub>_i_+1</sub>. Moreover, these paths are pairwise edge- disjoint as \(E_X\cap(E_Y\backslash E_\mathcal{M})=\emptyset\) and two paths in the same graph are edge disjoint as they belong to different connected components (we may assume that each node _u<sub>p<sub>j</sub></sub>_ appears at most once in the cycle). Hence, we can concatenate all paths to get a closed walk in _H_ that does not repeat any edges, contradicting the fact that _H_ is acyclic.

In the other direction, assume that \((P_X,P'_Y)\) is acyclic. We will show that _H_ is acyclic and that it has connected components for _B_ as described by \(P_X\sqcup P_Y\). Note that the latter is shown by Lemma 12. Hence, assume towards a contradiction that _H_ contains a cycle _C_. Since _G<sub>X</sub>_ and _G<sub>Y</sub>_ are each acyclic, _C_ must contain edges from both _G<sub>X</sub>_ and _G<sub>Y</sub>_. Let _C<sub>X</sub>_ and \(C'_Y\) denote the subset of edges in _E<sub>X</sub>_ and _E<sub>Y</sub>_\\_E_<sub>M</sub> and let \(w_1,w_2,\dots,w_\ell\) be the vertices at the end of maximal subpaths of _C_ in _C<sub>X</sub>_ and/or \(C'_Y\). Note that \(w_i\in\mathcal{M}\) for each \(i\in[\ell]\) as _Z_ is a separator and _G<sub>X</sub>_ and _G<sub>Y</sub>_ only contain the vertices in M in _Z_. By definition, _w<sub>i</sub>_ and _w_<sub>_i_+1</sub> (where \(w_{\ell+1}=w_1\)) are contained in the same block _p<sub>i</sub>_ in _P<sub>X</sub>_ or \(P'_Y\), respectively. Note that \((w_1,p_1,w_2,\dots,w_\ell,p_\ell)\) forms a cycle in \(F_{P_X,P'_Y}\), a contradiction to \((P_X,P'_Y)\) being acyclic. Thus, _H_ is acyclic. This concludes the proof.

As a last step before showing how to solve Maximum-Weight Induced Forest in subexponential parameterized time, we analyze the number of possible partitions for a given pebble set.

**Lemma 14.** _Let_ (_B,x_) _be a pair that is almost measured with respect to two integers d and_ \(\alpha\)_, where_ \(\alpha\) _is a constant. Let_ M _be a pebble set for_ \((B,d,\alpha,x)\)_. Then, the number of possible partitions of_ M _is in_ O(2<sup>66000\(\sqrt{d}\mathrm{log}^{10(d)}\)) _and all partitions can be enumerated in the same time._

_Proof._ Since (_B,x_) is almost measured with respect to _d_ and \(\alpha\), it holds that \(x\le 200\mathrm{log}^7(d)\). Moreover, \(\mathcal{M}\subseteq(B_\mathrm{he}\cup B_\mathrm{li})\), \(|B_\mathrm{he}|\le 40x\alpha\sqrt{d}\) and \(|\mathcal{M}\cap B_\mathrm{li}|\le 20x\alpha\sqrt{d}\mathrm{log}(d)\) because M is a pebble set for \((B,d,\alpha,x)\). Thus, \(|\mathcal{M}|\le 60(200\mathrm{log}^7(d))\alpha\sqrt{d}\mathrm{log}(d)=12000\alpha\sqrt{d}\mathrm{log}^8(d)\).

The number of partitions for a set of size _n_ is known as the _n_<sup>th</sup> Bell’s number and is known to be at most _n<sup>n</sup>_. There are even slightly better upper bounds \[BT10\], but this simple bound will be sufficient for our purpose.

If \(d<256\cdot 2^\alpha\), then the number of partitions is constant, that is, in O(1). So assume that \(d\ge 256\cdot 2^\alpha\). Then, the number of possible partitions of M is upper-bounded by

\(|\mathcal{M}||^{|\mathcal{M}|}\le(12000\alpha\sqrt{d}\mathrm{log}^8(d))^{12000\alpha\sqrt{d}\mathrm{log}^8(d)}\)<br>
\(\le(d^2\sqrt{d}d^3)^{12000\alpha\sqrt{d}\mathrm{log}^8(d)}\)<br>
\(=2^{12000\alpha\sqrt{d}\mathrm{log}^8(d)\mathrm{log}(d^{5.5})}\)<br>
\(\le 2^{66000\sqrt{d}\mathrm{log}^{10(d)}}.\)

Here, the second inequality is due to the fact that \((256\alpha)^2>12000\alpha\) and \(\mathrm{log}^8(d)\le d^3\) for all \(d\ge 256\). The last inequality is due to the fact that \(\alpha\le\mathrm{log}(d)\).

Note that we can enumerate all partitions of M efficiently, that is, with constant delay on average by iteratively deciding for each vertex \(v\in\mathcal{M}\) to which already existing block it is added or whether a new block consisting only of _v_ is added. This concludes the proof.

With the above three lemma at hand, we can now show how to apply Theorem 3 to Maximum- Weight Induced Forest. A request will consist of a pebble set, a partition of this pebble set, and an integer \(\ell\). The output describes the maximum weight of a forest with at most \(\ell\) vertices containing exactly the pebble set in the portal set and having connected components for the pebbles<tbc>

