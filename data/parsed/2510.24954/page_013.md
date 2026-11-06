**Definition 3.5** (Efficiency)**.** Fix \(G,G'=(V\cup V',E\cup E')\), and \(E'_{i,j}\) as above, and fix the set of critical shortest paths.

• The _efficiency of_ \(E'_{i,j}\) is the ratio of the number of \(E'_{i,j}\)-respecting critical shortest paths to \(|E'_{i,j}|\).<tbc>

• The _efficiency of a Steiner vertex u_ incident to \(E'_{i,j}\) is the ratio between the number of \(E'_{i,j}\)-respecting critical shortest paths passing through _u_ to \(\mathrm{deg}_{E'_{i,j}}(u)\).

Lemma 3.6 is a simple observation that follows from the definition of efficiency.

**Lemma 3.6.** _Let_ \(G\in\mathcal{G}_k\) _and_ \(G'=(V\cup V',E\cup E')\) _be a Steiner shortcut, and_ \(E'_{i,j}\subset E'\) _be a normalized Steiner shortcut set from L<sub>i</sub> to L<sub>j</sub>. Suppose u is a Steiner vertex incident to_ \(E'_{i,j}\)_, whose efficiency is at most the efficiency of_ \(E'_{i,j}\)_. Obtain_ \(E''_{i,j}\) _by deleting u and its incident edges, and rerouting critical shortest paths that used u. Then the efficiency of_ \(E''_{i,j}\) _is at least that of_ \(E'_{i,j}\).

_Proof._ Suppose there are \(\alpha\) many \(E'_{i,j}\)-respecting critical shortest paths passing through _u_ and \(\mathrm{deg}_{E_{i,j}^\prime}(u)=\beta\). Suppose there are \(\alpha'\) total \(E'_{i,j}\)-respecting critical shortest paths and \(|E'_{i,j}|=\beta'\). By Definition 3.5, \(E'_{i,j}\) has efficiency \(\alpha'/\beta'\), and, after deleting _u_, \(E''_{i,j}\) has an efficiency of at least \((\alpha'-\alpha)/(\beta'-\beta)\ge\alpha'/\beta'\), since \(\alpha/\beta\le\alpha'/\beta'\).

The following lemma is crucial for our analysis.

**Lemma 3.7.** _Recall from Definition 2.6 that_ \(\Delta=\Theta(r^\frac{d-1}{d+1})\) _is the number of critical subdirections. Given a graph_ \(G\in\mathcal{G}_k\) _and a Steiner shortcut_ \(G'=(V\cup V',E\cup E')\) _for G, the number of critical shortest paths passing through any Steiner vertex_ \(u\in V'\) _is at most_ \(\Delta^k\).

_Proof._ By the pigeonhole principle, if there are more than \(\Delta^k\) critical shortest paths passing through _u_ then two are associated with the same critical direction, say \((\vec{v}_0,\dots,\vec{v}_{k-1})\). Let the two critical pairs be \((a,a'),(b,b')\in P\), where

\(a=((0,0),(a_0,\dots,a_{k-1}))\)<br>
\(b=((0,0),(b_0,\dots,b_{k-1}))\)<br>
\(a'=((\ell,0),(a_0+\ell\vec{v}_0,\dots,a_{k-1}+\ell\vec{v}_{k-1}))\)<br>
\(b'=((\ell,0),(b_0+\ell\vec{v}_0,\dots,b_{k-1}+\ell\vec{v}_{k-1}))\)

Since \((a,a')\neq(b,b')\), there must exist an index _i<sup>⋆</sup>_ such that \(a_{i^\star}\neq b_{i^\star}\). Since the two critical shortest paths go through _u_ and the Steiner shortcut does not change the transitive closure on _V_ , it follows that \((a,b'),(b,a')\) are also in the transitive closure _E_<sup>∗</sup> of _G_. For _a_ to reach \(b'\) there must exist \(\ell\) critical subdirections \(\vec{u}_0,\vec{u}_1,\dots,\vec{u}_{\ell-1}\) such that<tbc>

\(a_{i^\star}+\sum_{j\in[0,\ell)}\vec{u}_j=b'_{i^\star}.\)

<tbc>Similarly, for _b_ to reach \(a'\), there must exist \(\ell\) critical subdirections \(\vec{u}'_0,\vec{u}'_1,\dots,\vec{u}'_{\ell-1}\) such that<tbc>

\(b_{i^\star}+\sum_{j\in[0,\ell)}\vec{u}'_j=a'_{i^\star}.\)

<tbc>Recall that \(a'_{i^\star}-a_{i^\star}=b'_{i^\star}-b_{i^\star}=\ell\vec{v}_{i^\star}\). Combining the equalities above, we get that<tbc>

\(\sum_{j\in[0,\ell)}(\vec{u}_j+\vec{u}'_j)=2\ell\vec{v}_{i^\star}.\)

