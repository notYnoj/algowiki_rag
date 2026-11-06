**Lemma 8.18.** _Let_ \(k\ge 3\)_. There is an algorithm that given a k-regular graph G, a parity_ \(p\in\{\text{odd},\text{even}\}\)_, and a labeled graph H checks whether_ CFI(_G,p_) _and H are isomorphic. Further the algorithm runs in time O_(|_V(G_)|<sup>_f(k_)</sup>) _for some computable function f._

_Proof._ By construction the graph CFI(_G,p_) has a maximum degree of 2<sup>_k_-2</sup>+1. By \[GNS23\], isomorphism testing on unlabeled graphs with maximum degree 2<sup>_k_-2</sup>+1 can be done in time \(O(n^{log(2^{k-2}+1)^c})\subseteq O(n^{k^c})\) for a fixed constant _c_ that is independent of _k_. By \[BC79\], the problem of finding isomorphism in unlabeled graphs is polynomially time equivalent to the problem of finding isomorphism in labeled graphs. Thus, there is an algorithm that runs in time _O_(|_V(G_)|<sup>_f(k_)</sup>), for some computable function _f_, and checks if a labeled graph _H_ is isomorphic to CFI(_G,p_).

Write G for the set if of all graphs.

**Lemma 8.19.** _There is a function_ \(\text{CFI}:\mathcal{G}\rightarrow\{0,1\}\) _with the following properties:_

• _The function_ CFI _is computable in polynomial time: Given a colored graph G or order n, we can compute_ CFI(_G_) _in time O(n<sup>c</sup>_) _for some fixed constant c._<tbc>

• _For all isomorphic graphs G and H we obtain_ CFI(_G_)=CFI(_H)._<tbc>

