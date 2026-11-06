\(|(S,\bar{S})|=|E\backslash(E[S]\cup E[\bar{S}])|.\)

Throughout this paper, we use the terms cut size and cut cardinality interchangeably. By Menger’s theorem \[3\], the local edge-connectivity \(\lambda(u,v;G)\) is equivalent to the size of the minimum cut separating _u_ and _v_.

We use \(G\cup\{e\}\) and _G_\\{_e_} to represent the graph resulting from the insertion or deletion of edge _e_, respectively. In the context of our edge-connectivity maintenance algorithms, _e<sub>new</sub>_ refers to a newly inserted edge, while _e<sub>old</sub>_ refers to an existing edge identified for removal during Redundancy Elimination. Similarly, _e<sub>del</sub>_ denotes an edge targeted for deletion by Connectivity Restoration, and _E<sub>aug</sub>_ represents the set of augmenting edges computed by the framework to restore edge-connectivity.

To address problems defined in Section 1 efficiently, we rely on a fundamental graph- theoretic property regarding the locality of connectivity changes. The following lemma characterizes the structural impact of removing an edge from a _k_-edge-connected graph,

**Lemma 1.** _Let G_=(_V,E_) _be an undirected and k-edge-connected graph and e_={_u,v_} _be an edge in E. Let_ \(G'=G\backslash\{e\}\)_. If_ \(\lambda(G')<k\)_, then_ \(\lambda(u,v;G)=k-1\)_. Furthermore, any cut in_ \(G'\) _which cardinality is less than k must separate u and v._

_Proof._ Consider any cut \((S,\bar{S})\) in \(G'\) with cardinality strictly less than _k_. Since the original graph _G_ is _k_-edge-connected, the cardinality of this cut in _G_ must have been at least _k_. The removal of the single edge _e_={_u,v_} can reduce size of a cut by at most one, and this occurs if and only if _e_ crosses the cut (i.e., \(u\in S\) and \(v\in\bar{S}\) or vice versa). Therefore, for the cut’s capacity to drop below _k_ in \(G'\), its original capacity must have been exactly _k_, and it must separate _u_ and _v_, resulting in a final cardinality of exactly _k_-1.

We use this lemma directly in the restoration algorithm of Section 5.

## 4 Restoration after Edge Addition

### 4.1 Sparse certificate maintenance

To identify and eliminate redundant edges, we use a sparse certificate as introduced by Nagamochi and Ibaraki \[12\]. The edge set of a graph _G_ can be decomposed into a sequence of edge-disjoint spanning forests _F_<sub>1</sub>_,F_<sub>2</sub>_,...,F<sub>m</sub>_. For maintaining _k_-edge-connectivity, it suffices to maintain only the first _k_ forests, which form the sparse certificate \(G_{cert}=\bigcup_{i=1}^kF_i\). The following lemma establishes that this subgraph preserves the relevant edge-connectivity properties:

**Lemma 2** (From \[12\])**.** _For a simple graph G_=(_V,E), let F<sub>i</sub>_=(_V,E<sub>i</sub>_) _be a maximal spanning forest in_ \(G-E_1\cup E_2\cup\cdots\cup E_{i-1}\) _for i_=1,2_,...,|E|, where possibly_ \(E_i=E_{i+1}=\cdots=E_{|E|}=\emptyset\) _for some i. Then each spanning subgraph_ \(G_i=(V,E_1\cup E_2\cup\cdots\cup E_i)\) _satisfies_

\(\lambda(x,y;G_i)\ge min\{\lambda(x,y;G),i\}\text{\textit{for all}}x,y\in V,\) (1)

_where_ \(\lambda(x,y;H)\) _denotes the local edge-connectivity between x and y in graph H._

In particular, if \(k\le\lambda(G)\), the subgraph \(G_k=\left(V,\bigcup_{i=1}^kE_i\right)\) is itself _k_-edge-connected.

The sparse certificate is constructed using the linear-time sparsification method of Nagamochi and Ibaraki \[12\], presented in Algorithm 1. The procedure partitions _E_ into a sequence of edge-disjoint forests _E_<sub>1</sub>_,E_<sub>2</sub>_,...,E_<sub>|_E_|</sub> in a single pass over the graph. Each vertex _v_ maintains a rank _r(v_), initially set to zero, that tracks the number of forests containing an edge incident to _v_. At each step, the algorithm selects an unscanned vertex _x_ with maximum rank and assigns each unscanned edge _e_={_x,y_} to forest _E_<sub>_r(y_)+1</sub>. Since _y_ has no edge in _E_<sub>_r(y_)+1</sub> at the time of processing, this assignment preserves acyclicity. Ranks are then updated: _r(x_) (if _r(x_)=_r(y_)) and _r(y_) are incremented. Each edge is thus placed into the lowest-index forest that can accept it in _O_(1) time, yielding an overall running time of _O(m_). We use this procedure as a preprocessing step to construct the sparse certificate before handling dynamic edge additions.

