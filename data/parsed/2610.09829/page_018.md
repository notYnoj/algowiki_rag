**Construction of** \(G'\)**.** Consider the instance (_G,V_<sub>1</sub>_,...,V<sub>h</sub>_) of Multicolored Clique. Let \(V_i=\{x_1^i,\dots,x_n^i\}\). For \(i,j\in[h]\) such that _i\<j_, let \(f_1^{(i,j)},\dots,f_m^{(i,j)}\) be the edges with their endpoints in _V<sub>i</sub>_ and _V<sub>j</sub>_. We construct \(G'\) as follows.

(i) For each \(i\in[h]\), construct a copy _H<sub>i</sub>_ of the vertex selection gadget _H_. Denote by \(S_1^i,\dots,S_n^i\) the sets of slot edges in _H<sub>i</sub>_.<tbc>

(ii) For each pair of indices \(i,j\in[h]\) such that _i\<j_, construct a copy _F<sub>i,j</sub>_ of the edge selection gadget _F_.<tbc>

(iii) For each pair of indices \(i,j\in[h]\) such that _i\<j_ and each \(t\in[m]\), consider \(f_t^{(i,j)}\) and assume that \(f_t^{(i,j)}=x_a^ix_b^j\) for some \(a,b\in[n]\). Then we identify the root edge _e<sub>t</sub>_ of _F<sub>i,j</sub>_ and an arbitrary slot edge in \(S_a^i\) that was not identified with any root edge in the previous steps, and identify the opposite root edge \(e'_t\) of _F<sub>i,j</sub>_ and an arbitrary slot edge in \(S_b^j\) that was not identified with any root edge before.

The construction of \(G'\) is shown in Figure 8 Notice that because \(\Delta(G)\le hm\) and \(|S_a^i|=|S_b^j|=hm\), we always can find unused slot edges in Step (iii) to perform the identifications.

We summarize the properties of \(G'\) in the next lemma.

**Lemma 4.3.** _The constructed graph_ \(G'\) _has the following properties:_

(_i)_ \(\Delta(G')\le 3\),<tbc>

_(ii)_ \(g(G')=L\)_, and for each shortest cycle R, there is either_ \(i\in[h]\) _such that R is a shortest cycle in H<sub>i</sub> or there are_ \(i,j\in[h]\) _with i\<j such that R is a shortest cycle in F<sub>i,j</sub>._

_Proof._ Property (i) immediately follows from Claims (i) of Lemma 4.1 and Lemma 4.2. To show (ii), note that \(G'\) has cycles of length _L_ that are cycles of the vertex and edge selection gadgets. Moreover, by Claims (iii) of Lemma 4.1 and Lemma 4.2, these cycles are shortest cycles in the gadgets. Consider a cycle _R_ of \(G'\) that is a shortest chordless cycle for which there is no vertex of edge selection gadget containing _R_. We claim that the length of _R_ is at least _L_+1.

Suppose that _R_ contains vertices of at least two copies of the vertex selection gadget. Then, by the construction of \(G'\), _R_ contains at least two edge-disjoint paths in some edge selection gadgets _F<sub>i,j</sub>_ and \(F_{i,j^\prime}\) whose endpoints are endpoints of distinct root edges of the gadgets. By Claim (ii) of Lemma 4.1, the length of each of these paths is at least _L_-2_m_+1. Then the length of _R_ is at least 2(_L_-2_m_+1)_\>L_ by the choice of _L_. Assume that _R_ contains vertices of one vertex selection gadget _H<sub>i</sub>_ for some \(i\in[h]\). Then _R_ contains vertices of one edge selection gadget _F<sub>i,j</sub>_ for some \(j\in[h]\). As \(E(R)\backslash E(H_i)\neq\emptyset\) and \(E(R)\backslash E(F_{i,j})\neq\emptyset\), _R_ is the union of edge-disjoint paths in _H<sub>i</sub>_ and _F<sub>i,j</sub>_, and the endpoints of these paths in _F<sub>i,j</sub>_ are the endpoints of the root edges identified with slot edges of _H<sub>i</sub>_. Since _R_ is a chordless cycle, _R_ does not contain a path in _F<sub>i,j</sub>_ whose endpoints are the endpoints of the same root edge. If _R_ has two edge-disjoint paths whose endpoints are endpoints of distinct root edges of _F<sub>i,j</sub>_, the length of _R_ is at least 2(_L_-2_m_+1)_\>L_ by Claim (ii) of Lemma 4.1. Suppose that _R_ contains one path in _F<sub>i,j</sub>_ whose endpoints are endpoints of distinct root edges. Then _R_ is the union of this paths and a path _H<sub>i</sub>_ with the same endpoints. By Claims (ii) of Lemma 4.1 and Lemma 4.2, the length of _R_ is at least (_L_-2_m_+1)+2_m\>L_. This finishes the case analysis and proves that the length of _R_ is at least _L_+1.

Since any shortest cycle in \(G'\) has no chord, we obtain that \(g(G')=L\), and each shortest cycle is a shortest cycle of either a vertex or an edge selection gadget. This concludes the proof.

