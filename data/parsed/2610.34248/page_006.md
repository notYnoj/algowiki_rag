### 3.5 Implementation & Experiment Summary

We implement HNSecW in two MPC configurations: 2PC in ABY \[12\] and 3PC in MP-SPDZ \[25\]. We evaluate on 10 ANN benchmarks at _M_=128 (SIFT-1M, GIST-1M, DEEP-100M, BIGANN-1B, DEEP-1M, DEEP-image, MNIST-60K, Fashion-60K, SPACEEV-1B, SSNPP-1B) \[4, 23, 26, 37, 45\], spanning _N_ from 60_K_ to 1_B_ and \(d\in[96,960]\). Experiments are conducted under LAN (4000 Mbps, 1 ms RTT) and WAN (320 Mbps, 50 ms RTT). On accuracy, HNSecW delivers Recall@\(k\ge 0.9\) for at least 95% of queries across the full evaluated range of \(k\in\{10,20,50,100\}\). On performance, HNSecW outperforms existing work on WAN 2PC by up to 22\(\times\) in end-to-end latency and 46\(\times\) in communication.

## 4 SINGLE QUERY PROOL

As discussed in Section 2, we decompose HNSW search into three components: the search logic flow, the data structures, and the graph/vector access patterns. In this section, we briefly outline how to make each component oblivious. Section 4.1 makes the control flow data-independent by replacing the original data-dependent stopping conditions with a fixed iteration bound. Section 4.2 redesigns the visited, candidate, and result structures as fixed-size arrays with uniform update rules. Section 4.3 ensures oblivious graph and vector access by avoiding repeated retrievals through per-layer reshuffled tables. Finally, Section 4.4 assembles these building blocks into the complete oblivious single-query protocol.

### 4.1 Making Logic Flow Oblivious

We first make HNSW’s search logic flow oblivious. At each layer, original HNSW iteratively finds the nearest candidate node and explores all its neighbors. The logic flow is inherently data-dependent.

The first source of data dependence is varying node degrees: exposing this variation would leak information about the graph and query. Fortunately, this dependency is easy to remove. Since HNSW enforces an out-degree upper bound _M_ per node, we pad each node’s neighbor list with randomly selected nodes from the same layer to obtain a fixed length of _M_. This padding does not reduce search quality: all real neighbors remain available for selection.

The more subtle challenge lies in the termination condition. In HNSW, the search stops when no better candidate remains (line 7-8 in Algorithm 1), or when the candidate set becomes empty (line 4 in Algorithm 1). Both conditions are inherently data-dependent. At first glance, this seems similar to the bounded-degree case, since the original HNSW paper \[32\] suggests that each layer can be traversed in a constant number of hops. One may use that constant as a fixed upper bound and pad execution with dummy searches. However, unlike node degree, this constant is not a worst-case bound; it arises from an expected-case analysis in \[32\] that assumes each layer forms a perfect Delaunay graph \[13\]. Real HNSW layers only approximate such structures, so the constant-hop guarantee does not hold in general. In fact, the best-known asymptotic bound for HNSW on arbitrary data is still _O(N_). A practical, data-independent iteration bound must therefore be derived from the actual termination behavior.

The first termination condition (lines 7-8 in Algorithm 1) triggers when the closest candidate can no longer improve the current result set. This can only happen after _ef_ search steps. Since every<tbc>

<tbc>node inserted into _W_ is also inserted into _C_, every node in the final _W_ must have been popped from _C_ and explored (i.e., cannot remain in _C_); otherwise, it would stay in _C_ and lead to \(min(C)\le max(W)\), contradicting the stopping condition. Hence, letting _s_ denote the number of search steps performed by standard HNSW at a given layer, we always have \(s\ge ef\) and can write exact search steps as \(s=ef+\Delta\), where residual \(\Delta\) captures work beyond the _ef_ steps. Therefore, to make the termination condition oblivious, a natural approach is to fix the number of search steps at each layer. Specifically, for each layer \(\ell\), we set the number of search steps to \(T^{(\ell)}=ef^{(\ell)}+\overline{\Delta^{(\ell)}}\), where \(\overline{\Delta^{(\ell)}}\) is a public upper parameter to bound the residual term and depends only on public quantities such as _N_, _d_, and _M_. Below, we present our strategy for setting \(ef^{(\ell)}\) and \(\overline{\Delta^{(\ell)}}\), both bounded by logarithmic terms, and show the resulting procedure performs robustly in practice. _However, designing termination strategies for HNSW that balance accuracy and efficiency remains an active research topic even in the non-private setting \[8\], and is not the main interest of this paper. Future termination strategies can also be integrated into our framework. Moreover, we highlight that, as long as the number of search steps increases by at most a logarithmic factor, our final complexity guarantee remains unchanged._

We begin with the choice of \(ef^{(\ell)}\). Standard HNSW \[32\] sets \(ef^{(\ell)}=1\) in all upper (non-base) layers, while treating the base- layer value as an input parameter. We now discuss how to set _ef_<sup>(0)</sup> at the base layer. To this end, we run HNSW with five values of _k_ on 10 ANN datasets spanning 60K-1B points and dimensions 96-960, using 10<sup>3</sup> queries per dataset. For each test, let _ef_<sup>∗</sup> denote the smallest base-layer value of _ef_<sup>(0)</sup> that achieves recall at least 90%. Figure 3 reports the 95% quantile of _ef_<sup>∗</sup> over these 50K tests. For all \(k\ge 5\), the offset _ef_<sup>∗</sup>-_k_ is at most 10 in at least 95% of the tests. Therefore, we set _ef_<sup>(0)</sup>=_k_+10 throughout our experiments, except in the ablation study on _ef_.

After fixing \(ef^{(\ell)}\), we discuss how to set \(\overline{\Delta^{(\ell)}}\). One natural idea is to set \(\overline{\Delta^{(\ell)}}\) to one empirical constant across all layers. We validate this strategy in the same 50K experiments by counting the residual steps required by standard HNSW under the above strategy for \(ef^{(\ell)}\). Figure 4 shows the results.

The results show that the residual steps are well bounded by a constant in the upper layers, but are substantially larger at the base layer. We therefore use an enhanced strategy. For upper layers, we set \(\overline{\Delta^{(\ell)}}\) to a constant _C_. For the base layer, we use the observation from recent work on early termination in HNSW \[8, 9\] that, after the first _ef_ steps, the probability of not having terminated decays geometrically with the number of additional steps. We therefore<tbc>

SIFT-1M
MNIST-60K
DEEP-image-9.99M
Yandex-DEEP-1B
Turing-1B
GIST-1M
Fashion-60K
BIGANN-1B
SPACEV-1B
SSNPP-1B
14
12
10
8
6
4
2
0
5
10
25 top-k
50
100

**Figure 3: Base-layer** _ef_<sup>∗</sup> **on the** 10 **datasets (**_M_=128) with** 95% **recall** \(\ge 0.9\) **over** 10<sup>3</sup> **queries.**

