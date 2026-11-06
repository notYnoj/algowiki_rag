## C.1 Pre-processing _H_

As an initial step, we apply a pre-processing procedure to _H_ as follows:

1. Alice computes a spanning forest F_<sub>A</sub>_ of her full input graph _G<sub>A</sub>_=(_V,E<sub>A</sub>_). She then sends F_<sub>A</sub>_ to Bob and adds it to _H_.<tbc>

2. Bob computes a spanning forest F_<sub>B</sub>_ of his full input graph _G<sub>B</sub>_=(_V,E<sub>B</sub>_). He then sends F_<sub>B</sub>_ to Alice and adds it to _H_.<tbc>

3. The players then combine \(\mathcal{F}_A\cup\mathcal{F}_B\) and compute a set of vertices \(V'\subseteq V\) , consisting of vertices in _V_ that are reachable from _s_ via \(\mathcal{F}_A\cup\mathcal{F}_B\).<tbc>

4. Alice and Bob remove all vertices in \(V\backslash V'\) from their respective private graphs and from the public graph _H_.

This pre-processing procedure is relatively cheap in communication: it requires only 2 rounds of communication and incurs a cost of \(\widetilde{O}(n)\) bits. A key observation is that the graph \(\mathcal{F}_A\cup\mathcal{F}_B\) preserves pairwise connectivity of vertices in _G_. That is, a pair of vertices _u_ and _v_ is connected in _G_ if and only if they are connected in \(\mathcal{F}_A\cup\mathcal{F}_B\). Therefore, the vertex set \(V'\) obtained in Step 3 represents all the vertices in _V_ that are reachable from _s_ in _G_.

The consequences of this pre-processing are as follows. Steps 1 and 2 only add edges to _H_, ensuring that \(\nu(H)\) never decreases. The deletions in Step 4 do not affect the max-flow value of either _G_ or _H_, because any vertex not reachable from _s_ cannot participate in any _s-t_ flow. Thus, the pre-conditions of Claim C.1 remain valid after the pre-processing.

Moreover, after the pre-processing, the vertex set of _H_ becomes \(V'\), and _H_ contains \(\mathcal{F}_A\cup\mathcal{F}_B\) as a subgraph. Consequently, every vertex in _H_ is reachable from _s_, enabling us to assert the following assumption.

**Assumption C.3.** _In the public graph H, every vertex_ \(v\in V(H)\) _is reachable from s._

## C.2 Residual Witness

We now formally define the revised notion of witness in which we call a _residual witness_.

**Definition C.4** (Residual Witness)**.** _Let_ G=(_V,E_) _be an unweighted undirected graph with two designated terminals s and t, and G contains F as a flow subgraph. A tuple_ W=(_S,T,Y_) _is called a_ residual witness _of_ G _w.r.t F (or just residual witness for short) if the following conditions hold:_

1. (_S,T_) _is an s-t cut of_ G_<sub>F</sub> with value_ \(w_{\mathcal{G}_F}(S,T)\le k-k'-1\).<tbc>

_2._ \(Y=E_{\mathcal{G}_F}(S,T)\cup X\)_, where_ \(X\subseteq(S\times T)\backslash E_{\mathcal{G}_F}(S,T)\) _is of size at most_ \(k-k'-1-w_{\mathcal{G}_F}(S,T)\).

Intuitively, each \((a,b)\in X\) represents a _currently non-existent_ unit-capacity undirected edge that cross the cut (_S,T_). The set _X_ then represents a _pre-allocated_ set of edges that could potentially be added to G in the future, ensuring that the cut value of (_S,T_) remains at most \(k-k'-1\). Note unlike the previous definition of witness, it is possible to have \(X=\emptyset\).

**Invariant C.5** (Residual Witness Invariant)**.** _For any_ G _containing F as a flow subgraph, we have_ \(\nu(\mathcal{G})\ge f-k'\) _if and only if_ \(\mathcal{W}_F(\mathcal{G})=\emptyset\).

