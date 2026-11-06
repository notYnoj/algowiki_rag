- If \(i\equiv 0mod2\), then path \(P_{d_1,d_2}^s\) takes an edge of the form<tbc>

<tbc>\((i,x,y,z)\rightarrow(i+1,x+1,y,z+f_{d_1}(i/2)).\)<tbc>

**-** If \(i\equiv 1mod2\), then path \(P_{d_1,d_2}^s\) takes an edge of the form<tbc>

<tbc>\((i,x,y,z)\rightarrow(i+1,x,y+1,z+f_{d_2}((i-1)/2).\)<tbc>

<tbc>We have established that path \(P_{d_1,d_2}^s\) starts at node \(s\in L_0\), and we have established which type of edge \(P_{d_1,d_2}^s\) takes between layers _L<sub>i</sub>_ and _L_<sub>_i_+1</sub> where \(i\in[0,2r-1]\), so we have uniquely specified path _P_. We define P to be the collection of paths \(\{P_{d_1,d_2}^s\}_{s,d_1,d_2}\) defined over all choices of \(s\in S\) and \(d_1,d_2\in[1,r]\).

We state without proof several properties of this graph construction.

**Lemma C.1** (cf. Proposition 5.1 of \[VXX24\])**.** _Graph G and paths_ P _have the following properties:_

1. \(|V(G)|=\Theta(r^5)\), \(|E(G)|=\Theta(r^5)\)_, and_ \(|\mathcal{P}|=\Theta(r^6)\).<tbc>

_2._ _(Uniqueness.) Every critical path in_ P _is the unique path between its endpoints in G._<tbc>

_3._ _(Low Overlap.) Any path_ \(\sigma\) _in G of length at most_ \(s\le 2r\) _is contained in at most O_((_r/s_)<sup>2</sup>) _distinct critical paths in_ P.

This graph construction of \[VXX24\] implies a polynomial lower bound on the diameter of _O(m_)-size shortcuts. We summarize this property of _G,_P in the following theorem.

**Theorem C.2** (cf. Theorem 1.3 of \[VXX24\])**.** _Fix a constant c\>_0_. Let_ \(H\subseteq TC(G)\) _be a shortcut set of G of size_ \(|H|\le c\cdot|E(G)|\)_. If construction parameter r of G,_P _is chosen to be sufficiently large, then there must exist an_ \(s\rightsquigarrow t\) _path_ \(P\in\mathcal{P}\) _such that_ \(\mathrm{dist}_{G\cup H}(s,t)=\Omega(r)=\Omega(|V(G)|^{1/5})\)_. Consequently, for any O(m)-size shortcut set_ \(H\subseteq TC(G)\)_, graph_ \(G\cup H\) _has diameter_ \(\Omega(n^{1/5})\).

The proof of Theorem C.2 uses a potential function argument which shows that every shortcut edge in _H_ can only decrease the lengths of paths in P by a small amount; intuitively, this follows from the low overlap property of paths in P stated in Lemma C.1.

## C.2 Steiner Shortcut to \[VXX24\]

We will now give a Steiner shortcut for the lower bound construction of \[VXX24\]. This Steiner shortcut rules out the possibility of extending Theorem C.2 to Steiner reachability shortcut sets via the argument used in \[VXX24\]. Formally, we will prove the following theorem about the graph _G_ and set of paths P corresponding to the lower bound construction of \[VXX24\].

**Theorem C.3** (Steiner Shortcut for \[VXX24\] Construction)**.** _Graph G and set of paths_ P _admit a Steiner reachability shortcut set H such that_

1. _H has O(r_<sup>4</sup>)=_O_(|_V(G_)|_/r_) _Steiner nodes and O(r_<sup>5</sup>)=_O_(|_E(G_)|) _edges, and_<tbc>

_2._ _For every_ \(s\rightsquigarrow t\) _path_ \(P\in\mathcal{P}\)_, there exists an_ \(s\rightsquigarrow t\) _path of length two in_ \(G\cup H\).<tbc>

