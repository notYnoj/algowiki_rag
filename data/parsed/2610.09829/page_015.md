(_ii)_ _for every two endpoints x and y of distinct root edges, the distance between x and y is at least L_-2_m_+1,<tbc>

(_iii)_ _g(F_)=_L, and for each_ \(i\in[m]\), \(C_i,C'_i,S_i,S'_i\) _are shortest cycles,_<tbc>

_(iv)_ _F contains at most four edge-disjoint shortest cycles, and_ \(\{C_i,C'_i,S_i,S'_i\}\) _for_ \(i\in[m]\) _are the only packings of four edge-disjoint shortest cycles,_<tbc>

_(v)_ _for each_ \(i\in[m]\)_, there is a packing of four edge-disjoint shortest cycles such that any root edge except e<sub>i</sub> and_ \(e'_i\) _is not contained in the cycles of the packing, and for any packing of four edge-disjoint shortest cycles, there is a unique_ \(i\in[m]\) _such that the opposite roots_ \(e_i,e'_i\) _are in the cycles of the packing and all other roots are not included in the cycles._

_Proof._ Property (i) immediately follows from the construction of _F_. We have (ii) because the root edges are the middle edges of paths \(P_i,P'_i\) for \(i\in[m]\). Since these paths are of length _L_-2_m_+1 and the endpoints of distinct paths are distinct, the distance between _x_ and _y_ is at least _L_-2_m_+1 for any two endpoints _x_ and _y_ of distinct root edges.

To see (iii), note that for all \(i\in[m]\), the length of the cycles \(C_i,C'_i,S_i,S'_i\) is _L_ by the definition of the cycles. To show that _g(F_)=_L_, observe that the length of _C_ is _p=L_+4_m_+2_\>L_. Therefore, for any shortest cycle _R_, there is \(i\in[m]\) such that _R_ contains an edge of one of the paths \(P_i,P'_i,Q_i,Q'_i\). Suppose that _R_ contains an edge of _P<sub>i</sub>_. Notice that the distance between the endpoints of _P<sub>i</sub>_ is 2_m_-1 by the construction of _F_. Moreover, the shortest path between the endpoints of _P<sub>i</sub>_ is unique, and it is the shortest path between these vertices in _C_. Thus, _R=C<sub>i</sub>_. Similarly, if _R_ contains an edge of _Q<sub>i</sub>_ then _R=S<sub>i</sub>_. The cases when _R_ contains an edge of \(P'_i\) or \(Q'_i\) are symmetric. This proves that _g(F_)=_L_. Moreover, we proved that \(\bigcup_{i=1}^m\{C_i,C'_i,S_i,S'_i\}\) is the set of all shortest cycles in _F_.

To prove (iv), observe that for each \(i\in[m]\), \(\{C_i,C'_i,S_i,S'_i\}\) is a packing of four edge-disjoint cycles. Notice that the cycles _C<sub>i</sub>_ and _C<sub>j</sub>_ for \(i,j\in[m]\) have common edges by the construction of _F_, and the same holds for \(C'_i\) and \(C'_j\), _S<sub>i</sub>_ and _S<sub>j</sub>_, and \(S'_i\) and \(S'_j\). Thus, every packing of four edge-disjoint shortest cycles is \(\{C_{i_1},C'_{i_2},S_{i_3},S'_{i_4}\}\) for some \(i_1,i_2,i_3,i_4\in[m]\), and _F_ has no packing of size five. If _i_<sub>1</sub>_\>i_<sub>3</sub>, then _C_<sub>_i_<sub>1</sub></sub> and _S_<sub>_i_<sub>3</sub></sub> share an edge by the construction of _F_. Therefore, \(i_1\le i_3\). Similarly, we have that \(i_3\le i_2\) and \(i_2\le i_4\), that is, \(i_1\le i_3\le i_2\le i_4\). If _i_<sub>4</sub>_\>i_<sub>1</sub>, then _C_<sub>_i_<sub>1</sub></sub> and \(S'_{i_4}\) have a common edge. We conclude that _i_<sub>1</sub>=_i_<sub>2</sub>=_i_<sub>3</sub>=_i_<sub>4</sub>. This proves that \(\{C_i,C'_i,S_i,S'_i\}\) for \(i\in[m]\) are the only packings of four edge-disjoint shortest cycles.

Property (iv) immediately implies (v) and this concludes the proof.

**Vertex selection gadget.** Next we construct the vertex selection gadget _H_ (see Figure 7). Its construction follows the ideas of the hardness proof in \[4, Theorem 1.2\].

(i) Construct a cycle _C=u_<sub>0</sub>_...u_<sub>_q_-1</sub>_u_<sub>0</sub> of length _q_=(_hm_+1)(2_m_+1)+_L_; we assume that for \(i\ge q\), _u<sub>i</sub>=u_<sub>_imod q_</sub>,<tbc>

(ii) set _r_=(_hm_+1)(2_m_+1), and for each \(i\in[n]\),<tbc>

- construct a \((u_{ri-1},u_{ri-1+\ell})\)-path _P<sub>i</sub>_ of length \(\ell\),<tbc>

**-** construct a \((u_{ri+\ell},u_{ri+L})\)-path \(P'_i\) of length \(\ell\).<tbc>

