## 1 Introduction

Every graph of maximum degree \(\Delta\) can be properly colored with at most \(\Delta+1\) colors (with a simple greedy algorithm). The famous _Brooks’ theorem_ \[7\] states that \(\Delta\) colors are enough for almost all graphs, except for two cases, complete graphs and odd cycles, where \(\Delta+1\) colors are needed. This means that - except for those two cases - every vertex _v_ is colored from the palette \(\{1,\dots,\Delta\}\) in such a way that each of its deg(_v_) neighbors receives different colors than _v_.

### 1.1 Partial Coloring

A natural generalization of proper coloring is _partial coloring_ \[2,6,18,22\]. Given two integers \(k\ge 0\) and \(c\ge 1\), a _k-partial c-coloring_ of a graph assigns to each vertex a color from {1_,...,c_} such that every vertex _v_ has at least min{_k,_deg(_v_)} neighbors with a color different from its own.

This notion generalizes several well-known coloring paradigms:

• For \(k=\Delta\), where \(\Delta\) is the maximum degree of the graph, _k_-partial (_k_+1)-coloring corresponds to proper \((\Delta+1)\)-coloring and _k_-partial _k_-coloring corresponds to proper \(\Delta\)-coloring.<tbc>

• For _k_=1, the condition captures the classical notion of _weak coloring_ \[22\].

The problems of proper \((\Delta+1)\)-coloring \[1,3,11,13,14,16,21,24,26\], proper \(\Delta\)-coloring \[4,10, 15,16,23\] and _weak_ coloring \[2,6,18,22\] have been studied extensively in the distributed computing paradigm. The notion of partial coloring brings all these problems in the same framework.

For every integer _k_ and every graph _G_, a _k_-partial (_k_+1)-coloring always exists. As outlined in \[9\] and implicitly in \[2\], a simple greedy algorithm achieves this: initialize all vertices with color 1, and process the vertices sequentially. For each vertex _v_, let _C(v_) denote the set of colors in its neighborhood. If |_C(v_)|=_k_+1, the vertex retains its color. Otherwise, we color it with any color from {1_,...,k_+1}\\_C(v_). This construction guarantees that each vertex has enough differently colored neighbors at the end of the process. Moreover, once two adjacent vertices are assigned different colors during any stage of the algorithm, they permanently maintain this property.

From a distributed perspective, Das, Fraigniaud, and Rosén \[9\] studied the complexity of computing such a coloring in the LOCAL model. They designed an \(O(logn\cdot log^2k)\)-round algorithm for _k_-partial (_k_+1)-coloring using the rounding framework from \[16\] which matches their round complexity of \(O(logn\cdot log^2\Delta)\) for proper \((\Delta+1)\)-coloring. The result suggested that "relaxing" the constraints of proper coloring to partial coloring made the problem "easier", as demonstrated by the improvement of the round complexity. They also posed an open problem; what is the distributed complexity of _k_-partial _k_-coloring? The problem of proper \(\Delta\)-coloring admits polylogarithmic round complexity ( \[4,16\]) in the deterministic LOCAL model. This question can also be viewed as whether this relaxation extends computation advantage to proper \(\Delta\)-coloring as well.

While proper \(\Delta\)-coloring is well understood in the classical (centralized) setting - with known characterizations and complexity classifications -- the same is not true for _k_-partially _k_-colorable graphs. To the best of our knowledge, no characterization or complexity classification is known for the decision problem: given a graph _G_ and integer _k_, is _Gk_-partially _k_-colorable? The problem is far from being trivial. For example, our quest for characterization of _k_-partial _k_-colorability quickly yielded non-trivial obstructions (which, for instance, do not even have (_k_+1)-clique as a subgraph, see Figure 1 for such an example).

In this work, we initiate a systematic study of this problem. We first investigate the classical complexity of recognizing _k_-partially _k_-colorable graphs. Then, leveraging structural insights, we<tbc>

