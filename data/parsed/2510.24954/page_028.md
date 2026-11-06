**Lemma A.2** (cf. Theorem 13 of \[AB24\])**.** _For every sufficiently small_ \(\epsilon>0\)_, there exists an infinite family of n-node directed graphs G, each with an associated collection of directed paths_ P _in G with the following properties:_

1. \(|\mathcal{P}|\ge n^{2-4\epsilon^{1/2}}\),<tbc>

_2._ _each path_ \(P\in\mathcal{P}\) _has_ \(|P|=n^\epsilon\) _edges,_<tbc>

_3._ _paths in_ P _are pairwise edge-disjoint, and_<tbc>

_4._ _each path_ \(P\in\mathcal{P}\) _is the unique directed path between its endpoints in graph G._

Using Lemma A.2, we can directly prove Theorem A.1.

_Proof of Theorem A.1._ Let \(\epsilon>0\) be a sufficiently small constant and let _m_ be some function of _n_ such that \(m\in\left[n,n^{2-4\epsilon^{1/2}+\epsilon}\right]\). By Lemma A.2, there exists an infinite family of _n_-node directed graphs _G_, each with an associated collection of directed paths P in _G_ satisfying the properties in Lemma A.2. Since paths in P are pairwise edge-disjoint and each has length at least \(n^\epsilon\), we observe that

\(|E(G)|\ge|\mathcal{P}|n^\epsilon\ge n^{2-4\epsilon^{1/2}+\epsilon}.\)

We can ensure that \(|E(G)|=\Theta(m)\) by repeatedly removing paths in P from graph _G_ until we achieve the desired graph density. After performing this procedure, |_E(G_)|=_m_ and \(|\mathcal{P}|=mn^{-\epsilon}\ge m^{1-\epsilon}\), by Property 2 of Lemma A.2.

We will achieve our Steiner shortcut lower bound via an information theoretic argument. More specifically, we use graph _G_ to construct a graph family G of size |G|=2<sup>|P|</sup>. For each subset \(S\subseteq\mathcal{P}\), we define graph _G<sup>S</sup>_ as follows:

1. Initially, let _G<sup>S</sup>_:=_G_.<tbc>

2. For each path \(P\in\mathcal{P}-S\), remove every edge in _P_ from graph _G<sub>S</sub>_, so that \(G^S\leftarrow G^S-E(P)\).

Since paths in P are pairwise edge-disjoint in _G_ by Lemma A.2, a path \(P\in\mathcal{P}\) is contained in graph _G<sup>S</sup>_ if and only if \(P\in S\).

For each graph _G<sup>S</sup>_=(_V<sup>S</sup>,E<sup>S</sup>_) where \(S\subseteq\mathcal{P}\), let \(G_+^S=(V^S\cup V_+^S,E^S\cup E_+^S)\) be a Steiner shortcut graph of _G<sup>S</sup>_ with diameter at most \(n^\epsilon/2\) that minimizes \(|V_+^S|+|E_+^S|\). (Recall that the size of a Steiner shortcut graph is precisely \(|V_+^S|+|E_+^S|\).) We claim that one of these graphs \(G_+^S\) has size at least \(|V_+^S|+|E_+^S|\ge\tilde{\Omega}(m^{1-\epsilon})\).

For each \(S\subseteq\mathcal{P}\), let \(H_+^S=G_+^S-E^S\). This graph contains exactly the Steiner edges \(E_+^S\) in graph \(G_+^S\). We define the graph family G to be \(\mathcal{G}=\{H_+^S\}_{S\subseteq\mathcal{P}}\). Let \(x=max_{S\subseteq\mathcal{P}}|V_+^S|+|E_+^S|\). We observe that each graph \(H_+^S\in\mathcal{G}\) has at most _x+n_ vertices and at most _x_ edges. Now note that without loss of generality, we can interpret each directed graph \(H_+^S\in\mathcal{G}\) as a subgraph of a vertex-labeled, complete, directed graph with _x_ vertices. We denote this universal graph as \(\hat{G}\). Under this interpretation, \(H_+^S\subseteq\hat{G}\) for each \(H_+^S\in\mathcal{G}\).

Now we claim that for distinct sets of paths \(S,S'\subseteq\mathcal{P}\), we have that \(H_+^S\neq H_+^{S^\prime}\) (we say that \(H_+^S=H_+^{S^\prime}\) if both graphs correspond to the same subgraph of \(\hat{G}\), and we say that \(H_+^S\neq H_+^{S^\prime}\) otherwise). Since \(S\neq S'\), we may assume without loss of generality that there exists a path \(P\in S-S'\). Since \(G_+^S\) is a Steiner shortcut graph of _G<sup>S</sup>_ with diameter \(\le n^\epsilon/2\), and path _P_ has length \(|P|=n^\epsilon\), and path _P_ is a unique path in _G<sup>S</sup>_ by Property 4 of Lemma A.2, we conclude that there must exist a path in graph \(H_+^S=G_+^S-E^S\) between a pair of vertices (_s,t_) in the transitive closure of path _P_. On the other hand, no edge in path _P_ is contained in graph \(G^{S^\prime}\), i.e., \(E(P)\cap E^{S^\prime}=\emptyset\), so by Property 4 of Lemma A.2, there does not exist a path in graph \(G_+^{S^\prime}\) between<tbc>

