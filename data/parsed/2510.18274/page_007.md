## Cut and Minimum Cut.

Let _G_=(_V,E_) be a (possibly directed weighted) graph with a designated terminals _s_ and _t_. A _cut_ of _G_ is defined as a partition (_S,T_) of the vertex set _V_ . If \(s\in S\) and \(t\in T\), we say such cut is an _s-t cut_. An undirected/directed edge \((a,b)\in E\) is said to _cross_ the cut if \(a\in S\) and \(b\in T\). The set of edges crossing the cut (_S,T_) is denoted by _E<sub>G</sub>(S,T_). The _size_ of a cut (_S,T_) is defined as the cardinality of _E<sub>G</sub>(S,T_), given by |_E<sub>G</sub>(S,T_)|. The _value_ of a cut is the total weight of the edges crossing the cut, quantified as \(w_G(S,T)=\sum_{e\in E_G(S,T)}w_G(e)\). When _G_ is undirected and unweighted, we may write the cut value by _w<sub>G</sub>(S,T_) or |_E<sub>G</sub>(S,T_)|. For clarity, we reserve the notation of cut value |_E<sub>G</sub>(S,T_)| solely for the case that _G_ is undirected and unweighted. For the remaining cases, we write the cut value as _w<sub>G</sub>(S,T_).

The _minimum s-t cut value_ of _G_, denoted by MinCut(_G_), is the minimum value among all possible _s-t_ cuts. An _s-t_ cut that attain the minimum cut value is called a _minimum s-t cut_. A cut (not necessarily an _s-t_ cut) of smallest value is called a _global minimum cut_. The following theorem, established in \[FF56\], formalizes the duality between maximum flow and minimum cuts.

**Theorem 2.4** (Max-Flow Min-Cut Theorem)**.** _For any graph G with a source s and sink t, the maximum value of an s-t flow equals the minimum value of an s-t cut, formally:_<tbc>

\(MaxFlow(G)=MinCut(G).\)

<tbc>Throughout this paper, we use \(\nu(G)\) to denote the value of the maximum _s-t_ flow and, equivalently, the value of the minimum _s-t_ cut in the graph _G_:

\(\nu(G):=MaxFlow(G)=MinCut(G).\)

More precisely, we define \(\nu_{s,t}(G)\) as the value of the minimum _s-t_ cut. Since we always fix a specific pair of terminals (_s,t_), we omit the subscripts and simply write \(\nu(G)\).

### _k_-Connected Component.

Let _G_=(_V,E_) be an undirected graph that can possibly be weighted. We say \(U\subseteq V\) is _k-connected component_ iff _G_\[_U_\] has _global_ min-cut of value at least _k_. The following lemma is known. For its proof, we refer readers to Lemma 3.8 of \[RSW18\].

**Lemma 2.5.** _Let G be an n-vertex undirected weighted graph with no k-connected components. Then, we have_ \(w(G)\le k(n-1)\).

## Cut Sparsifier.

Let _G_ be an undirected graph that may be weighted, and let \(\varepsilon\in(0,1)\). We say an undirected weighted graph _H_ is an \(\varepsilon\)_-cut sparsifier_ of _G_ iff \(E(H)\subseteq E(G)\) and we have \((1-\varepsilon)\cdot w_G(S,T)\le w_H(S,T)\le(1+\varepsilon)\cdot w_G(S,T)\) for any cut (_S,T_).

2
2
2
2
S
t
S
t
2
2
2

Figure 1: Shown on the left is a graph _G_ with a flow graph _F_ of size 2 indicated by the union of red and blue edges. Shown on the right is _G<sub>F</sub>_ which is the residual graph of _G_ induced by _F_.

