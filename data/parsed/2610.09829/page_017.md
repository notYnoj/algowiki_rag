(_iv)_ _H contains at most two edge-disjoint shortest cycles, and_ \(\{C_i,C'_i\}\) _for_ \(i\in[n]\) _are the only packings of two edge-disjoint shortest cycles,_<tbc>

(_v)_ _for every_ \(i\in[n]\)_, there is a packing of two shortest cycles in H such that the slot edges in S<sub>i</sub> are free, and for each packing of two shortest cycles in H, there is a unique_ \(i\in[n]\) _such that S<sub>i</sub> contains free slots._

_Proof._ Properties (i) and (ii) follow immediately from the construction of _H_.

To show (iii), observe that for each \(i\in[n]\), the length of _C<sub>i</sub>_ and \(C'_i\) is _L_. Consider an arbitrary shortest cycle _R_ in _H_. Since the length of _C_ is _q_=(_hm_+1)(2_m_+1)+_L\>L_, _R_ contains an edge _e_ outside _C_. Then there is \(i\in[n]\) such that either \(e\in E(P_i)\) or \(e\in E(P'_i)\). Suppose that \(e\in E(P_i)\) (the case \(e\in E(P'_i)\) is symmetric). Then _R_ contains _P<sub>i</sub>_. Notice that the shortest path between the endpoints of _P<sub>i</sub>_ in _C_ is the unique shortest path between these vertices in _H_. Thus, _R=C<sub>i</sub>_. By symmetry, \(R=C'_i\) if \(e\in E(P'_i)\). This proves (iii). Also, we obtain that \(\bigcup_{i=1}^n\{C_i,C'_i\}\) is the set of shortest cycles of _H_.

To prove (iv), notice that _C<sub>i</sub>_ and \(C'_i\) are edge-disjoint shortest cycles for \(i\in[n]\). Then each \(\{C_i,C'_i\}\) is a packing of two edge-disjoint shortest cycles. To show that we have no other packings of size at least two, observe that for distinct \(i,j\in[n]\), _C<sub>i</sub>_ and _C<sub>j</sub>_ have common edges by the construction of _H_, and the same holds for \(C'_i\) and \(C'_j\). Then any packing of edge-disjoint shortest cycles is of the form \(\{C_i,C'_j\}\) for some \(i,j\in[n]\). However, if \(i\neq j\), _C<sub>i</sub>_ and \(C'_j\) have common edges by the construction of _H_. This proves (iv).

Finally, (iv) together with the construction of _H_ immediately imply (v). This concludes the proof.

Now we are ready to construct \(G'\) and complete the proof of Theorem 1.1.

