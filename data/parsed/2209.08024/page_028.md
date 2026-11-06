## Appendix

## A Projection of a search tree

**Theorem 2.1.** _Let T be a search tree on_ T _and_ H _a connected subgraph of_ T _. There is a unique search tree T_|<sub>H</sub> _on_ H _such that for every_ \(v\in V(\mathcal{H})\),<tbc>

\(\mathtt{Path}_{T|_\mathcal{H}}(v)=\mathtt{Path}_T(v)\cap V(\mathcal{H}).\)

<tbc>_Proof._ We denote by _u\<<sub>T</sub>v_ that _v_ is an ancestor of _u_ in _T_. We need to show that there is a unique search tree _T_|<sub>H</sub> on H such that for all \(u,v\in V(\mathcal{H})\),

\(u<_{T|_\mathcal{H}}v\Longleftrightarrow u<_Tv.\) (7)

_T_|<sub>H</sub> is constructed recursively as follows. Denote \(s=\mathtt{LCA}_T(\mathcal{H})\in V(\mathcal{H})\). Set _s_ as the root of _T_|<sub>H</sub>. The subtrees of _T_|<sub>H</sub> rooted at the children of _s_ will be all the trees _T|<sub>C</sub>_, where \(C\in\mathbb{C}(\mathcal{H}-s)\).

That _T_|<sub>H</sub> is a search tree on H is easily shown by induction on |_V_(H)|. Observing that (7) implies root(_T_|<sub>H</sub>)=`LCA`_<sub>T</sub>_(H), uniqueness also follows easily by induction. We show here by induction that (7) holds. Let \(u,v\in V(\mathcal{H})\) and let _r_=root(_T_|<sub>H</sub>). If _u_ and _v_ are in the same connected component \(C\in\mathbb{C}(\mathcal{H}-r)\), then by induction

\(u<_{T|_\mathcal{H}}v\Longleftrightarrow u<_{T|_C}v\Longleftrightarrow u<_Tv,\)

as required. If _u_ and _v_ are in two different connected components of H-_r_, then by construction, \(u\unknown\le_{T|_\mathcal{H}}v\). In that case since _r_=`LCA`_<sub>T</sub>_(H), we have _u\<<sub>T</sub>r_ and _v\<<sub>T</sub>r_, therefore also \(u\unknown\le_Tv\), as required. If _v=r_ then both _u\<<sub>T|<sub>H</sub></sub>v_ and _u\<<sub>T</sub>v_ hold. Finally, if _u=r_ then both \(u\unknown\le_{T|_\mathcal{H}}v\) and \(u\unknown\le_Tv\) hold.

We repeat here the definition of projection of a search tree given by Cardinal et al. \[CLP18\]. To avoid confusion, we denote by \(\tilde{T}|_\mathcal{H}\) the projection of _T_ to H as defined in \[CLP18\], and by _T_|<sub>H</sub> the projection as defined in Definition 2.1. We than show that in fact, \(\tilde{T}|_\mathcal{H}=T|_\mathcal{H}\).

As a preliminary step, Cardinal et al. show how to construct the projection of _T_ to T-_x_, where _x_ is a leaf of T . They distinguish between three cases:

1. _x_ has a parent and no child in _T_,<tbc>

2. _x_ has a parent and a single child in _T_,<tbc>

3. _x_=`root`(_T_).

In the first case, _x_ is simply removed from _T_. In the second case, _x_ is removed from _T_ and an edge is added between its parent and its child. In the third case, _x_ is removed and its only child is selected as the new root. This operation is referred to as _pruning x_ from _T_. The projection \(\tilde{T}|_\mathcal{H}\) is then defined as the tree obtained by iteratively pruning leaves that are not in H.

It is straightforward to verify that the pruning operation respects the equivalence (7). More precisely, if \(T'\) is obtained from _T_ by pruning _x_, then \(u\le_{T^\prime} v\Longleftrightarrow u\le_Tv\) whenever \(u,v\neq x\). By induction on the number of pruned vertices, it follows that

\(u\le_{\tilde{T}|_\mathcal{H}}v\Longleftrightarrow u\le_Tv\)

for all \(u,v\in V(\mathcal{H})\). That \(\tilde{T}|_\mathcal{H}=T|_\mathcal{H}\) follows from the uniqueness in Definition 2.1.

