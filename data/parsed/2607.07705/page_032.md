Recall that, at a high level, our FPT-algorithm consisted of two parts: (i) finding a small family of tree edge sets that are candidates for removal, and (ii) for a fixed such set, reducing the problem to Weighted Directed Feedback Arc Set. In this scheme, allowed edges posed no major issue: we simply retained all of them in the reduced instance and let the black-box algorithm for WDFAS deal with them.

Although the second part of the scheme above can be easily modified to work with rational weights, the first part’s building blocks (Lemma 3 and Lemma 4) rely heavily on the integrality of profits. Since we could not come up with any analogues of these lemmas for rational weights, we had to abandon the entire scheme and deal with allowed edges by other means.

On the positive side, we note that by Lemma 2, the total weight of allowed edges is still bounded by 3_k_.

## 5.2.1 Inv-respecting subgraphs

As a starting point, we aim to mimic the setting without allowed edges. Although subgraphs of the form \(T-S+\mathrm{Inv}(S)+A'\) with \(A'\subseteq A\) are not necessarily acyclic, it remains tempting to search for solutions of this kind, because their weight equals \(\mathbf{w}(T)+\mathbf{p}(S)+\mathbf{w}(A')\). This would enable us to reuse the ideas tied to edge profits. We call such subgraphs Inv_-respecting_, and extend this terminology to instances that admit a solution of this structure.

Fortunately, we can always seek a solution that is almost Inv-respecting, in the sense that the total weight of the inverse edges it discards is at most **w**(_A_).

**Claim 13.** _claimAlmostInvResp If_ I=(_G,_**w**_,k_) _is a yes-instance of_ \(MAS/\mathrm{Max}ST(\mathbb{Q}_{\ge 1})\)_, there exists a solution_ \(X\subseteq G\) _to_ I _with S=E(T_)\\_E(X_) _such that_ \(\mathbf{w}(\mathrm{Inv}(S)\backslash E(X))\le\mathbf{w}(A)\).

_Proof of Claim 13._ Consider an arbitrary solution \(X'\), and let \(S':=E(T)\backslash E(X')\). Define \(B'\) as \(\mathrm{Inv}(S')\backslash E(X')\). If \(\mathbf{w}(B')\le\mathbf{w}(A)\), we are done. Otherwise, consider the subgraph \(X:=X'+B'-A\). Note that _X_ contains the same set of tree edges as \(X'\). Moreover, since \(X'\) is acyclic, Observation 2 guarantees that \(X'\subseteq T-S'+\mathrm{Inv}(S')+A\). Consequently, \(X\subseteq T-S'+\mathrm{Inv}(S')\). From the definition of \(B'\) it follows that \(\mathrm{Inv}(S')\subseteq X\). Therefore, \(X=T-S'+\mathrm{Inv}(S')\).

Since \(B'\cap E(X')=\emptyset\), we have \(\mathbf{w}(X)\ge\mathbf{w}(X')+\mathbf{w}(B')-\mathbf{w}(A)\). Moreover, as we know that \(X=T-S'+\mathrm{Inv}(S')\), by Lemma 1 it is acyclic. Therefore, _X_ is also a feasible solution of I.

Additionally, _X_ satisfies the needed property. Indeed, let _S_:=_E(T_)\\_E(X_). As shown above, we have \(S=S'\). Thus from \(\mathrm{Inv}(S')\subseteq X\) it follows that \(\mathbf{w}(\mathrm{Inv}(S)\backslash E(X))=0\le\mathbf{w}(A)\). \(\lrcorner\)

This allows us to reduce an arbitrary instance to an Inv-respecting one in time _m_<sup>**w**(_A_)</sup>: we simply guess which inverse edges are discarded by a solution and remove them from the graph. If the guess is correct, the resulting instance admits an Inv-respecting solution.

## 5.2.2 Compressed representation of acyclic subgraphs

Note that an Inv-respecting solution is defined by two edge sets: _S_ and \(A'\). Moreover, due to Lemma 2, the number of allowed edges is at most 3_k_. Therefore, we can enumerate all \(A'\subseteq A\), and for each choice, search for a suitable set _S_. To ensure that \(T-S+\mathrm{Inv}(S)+A'\) is acyclic for a fixed \(A'\), we rely on the following alternative characterization.

Let \(V'\) be the set of vertices incident to \(A'\). Since _X=T-S_+Inv(_S_) is acyclic, any cycle in \(X+A'\) must intersect \(V'\). Furthermore, such a cycle can be decomposed into directed paths in<tbc>

