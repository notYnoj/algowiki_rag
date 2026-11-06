<tbc>**Theorem 4.9.** _For every_ \(k\ge max\{\chi(G),\chi(H)\}\) _and every source profile_ **a** _on_ \(G\sqcup H\),

\(\mathcal{R}_k(G\sqcup H,\mathbf{a})=Max\bigcup_{\alpha+\beta=\mathbf{a}}\big(\mathcal{R}_k(G,\alpha)\star\mathcal{R}_k(H,\beta)\big),\) (4.12)

_where the union ranges over_ \(\alpha\in\mathcal{A}_k(G)\) _and_ \(\beta\in\mathcal{A}_k(H)\)_. This composition is associative and commutative._

_Proof._ A source word on the union restricts to words _w,z_ on the two summands. At a fixed target profile **p**, any proper repair has local target profiles **u**,**v** with **u**+**v**=**p**. Once these profiles are fixed, the two repairs are independent and their distances add. The union response is therefore exactly _f<sub>w</sub>⋆f<sub>z</sub>_. Conversely, any pair of local response functions can be realized simultaneously by choosing its two source words independently.

This proves (4.12) before dominated responses are removed. Convolution is monotone in each argument: if \(f\le f'\) and \(g\le g'\), then \(f\star g\le f'\star g'\). Replacing a discarded local response by a maximal one can consequently only increase the resulting response. Pruning the local lists thus leaves the union’s maximal responses unchanged. Associativity and commutativity follow from those of min-plus convolution, and the same monotonicity permits pruning at every intermediate composition. □

This theorem is a reduction to finite local data; it does not assert that the response antichains are always small. When \(k=\chi(J)\), ordinary villainy is recovered from their diagonal entries:

\(B(J)=max_{\mathbf{a}\in\mathcal{M}_k(J)}max_{f\in\mathcal{R}_k(J,\mathbf{a})}f(\mathbf{a}).\) (4.13)

The antichain is a singleton whenever one source attains every coordinatewise maximum simultaneously. The common extremizer in \[13, Theorem 3.15\] gives

\(\mathcal{R}_3(C_{2r+1},\mathbf{a})=\{f_\mathbf{a}\},\)<br>
\(f_\mathbf{a}(\mathbf{p})=2r+1-\sum_{X\in[3]}min\{p_X,\lceil a_X/2\rceil\}(\mathbf{p}\in\mathcal{M}_3(C_{2r+1}))\)

for every source profile **a**, including infeasible ones: the same cyclic word, with all occurrences of each color consecutive, attains the displayed value at every target profile. Thus these directed radii supply the complete local response data needed for composition.

In general, however, it is essential to retain the antichain, rather than merely the largest value in each coordinate. For example, on _P_<sub>3</sub>=_K_<sub>1,2</sub> with two colors, order the target profiles by their _A_-counts 1,2. Sources with one _A_ have responses (0,3) and (2,1), according as _A_ occupies the center or a leaf. Sources with two _A_’s have responses (3,0) and (1,2). For two copies and the source split 1+2, the greatest convolution value at total _A_-count three is two. Taking coordinatewise maxima first instead gives

\(min\{2+2,3+3\}=4.\)

Indeed, the actual radius of profile (3,3) on 2_P_<sub>3</sub> is two: its two proper targets are complementary, their distances from a same-profile source are even and sum to six, and a source constant on each copy attains two. Thus the outer maximum over disturbances cannot in general be interchanged with the minimum over target profiles.

The response functions also give an exact criterion for equality under disjoint union. For an integer _j_, put

\(\mathcal{L}_f(j)=\{\mathbf{p}:f(\mathbf{p})\le j\},\mathcal{K}_L(f,g)=\bigcup_{j=0}^L\big(\mathcal{L}_f(j)+\mathcal{L}_g(L-j)\big),\)

with \(\mathcal{L}_f(j)=\varnothing\) for _j\<_0 and \(\mathcal{K}_{-1}(f,g)=\varnothing\).

**Proposition 4.10.** _Set_ \(k=\chi(G\sqcup H)\) _and let_ \(L\ge 0\) _be an integer. Then_ \(B(G\sqcup H)\le L\) _if and only if_

\(\alpha+\beta\in\mathcal{K}_L(f,g)\) (4.14)

