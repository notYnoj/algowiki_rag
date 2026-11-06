For each \(i\in[n]\), denote by _Q<sub>i</sub>_ the shortest (_u_<sub>_r(i_-1)</sub>_,u_<sub>_ri_-1</sub>)-path in _C_. Each _Q<sub>i</sub>_ is of length _r_-1=(_hm_+1)(2_m_+1)-1. For every \(i\in[n]\), we denote by _S<sub>i</sub>_ the set of _hm_ edges of _Q<sub>i</sub>_ at distance 2_m_ from each other and the endpoints of _Q<sub>i</sub>_. We say that the edges of _S<sub>i</sub>_ are _slot_ edges. For each \(i\in[n]\), we denote by _C<sub>i</sub>_ (\(C'_i\), respectively) the cycle obtained from _P<sub>i</sub>_ (\(P'_i\), respectively) by connecting its endpoints by the shortest path between them in _C_. Given a packing of two edge-disjoint shortest cycles, we say that a slot edge _e_ is _free_ if it is not included in the cycles of the packing.

We summarize the properties of the vertex selection gadget in the next lemma.

**Lemma 4.2.** _The vertex selection gadget H has the following properties:_

(_i)_ \(\Delta(H)\le 3\) _and the endpoints of the slot edges are of degree two,_<tbc>

(_ii)_ _for every two endpoints x and y of distinct slot edges, the distance between x and y is at least_ 2_m,_<tbc>

_(iii)_ _g(H_)=_L, and for each_ \(i\in[n]\), \(C_i,C'_i\) _are shortest cycles,_<tbc>

Q1
P' 1
S1
P' 2
Q2
P1
S2
P' n
P2
Qn
Sn
Pn

Figure 7: Construction of the vertex selection gadget. The slot edges are shown in red. Notice that because \((hm+1)(2m+1)(n-1)<\ell\), _P<sub>n</sub>_ has one endpoint on the shortest path in _C_ between the endpoints of \(P'_1\).

