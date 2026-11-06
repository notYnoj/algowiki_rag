## 1.1. Problem Setting

We use D to denote a set of vectors in _d_ dimensional space _R<sup>d</sup>_. Given a query point _q_, a nearest neighbor query returns a point \(o^*\in\mathcal{D}\) such that its Euclidean distance to q is the minimum among D. Compared with exact NNS, the ANNS trades a little accuracy for efficiency. The ANNS problem can be defined as follows:

**Definition 1.** (\(\epsilon\)_-Nearest Neighbor Search). Given a query point q and an approximation ratio_ \(\epsilon\)_,a_ \(\epsilon\)_-NNS query returns a point_ \(o\in\mathcal{D}\) _such that_ \(\delta(o,q)\le(1+\epsilon)\delta(o^*,q)\) _where_ \(o^*\in\mathcal{D}\) _is the exact nearest neighbor of q._

It is easy to generalize \(\epsilon\)-NNS to \(\epsilon\)-KNNS when we require the query return a sequence of _K_ points _\<o_<sub>1</sub>_,o_<sub>2</sub>_,...,o<sub>k</sub>\>_ such that for each \(o_i(i\in[1,K])\), we have \(\delta(o_i,q)\le(1+\epsilon)\delta(o_i^*,q)\) where _o<sub>i</sub>_<sup>∗</sup> is i-th nearest neighbor of _q_. When we adopt proximity graphs to solve ANNS, it is difficult for us to model and evaluate results according to \(\epsilon\). Instead, precision is used to evaluate the accuracy of searched results. Precision is defined as follows:

\(precision=\frac{|R\cap G|}{|G|}\)

where _R_ is result returned by algorithm and _G_ is groundtruth. A higher precision indicates a smaller value of \(\epsilon\), which means that the result is more accurate.

## 1.2. Non-Graph-based Algorithm

Research on non-graph-based algorithms is much earlier than that of graph- based algorithms. Many excellent algorithms are born among them, which can be roughly divided into three categories: hashing-based, tree-based and quantization-based methods. The hashing-based methods include LSH\[7\], SH\[9\], KLSH\[21\], USPLH\[22\], AGH\[23\], DSH\[24\], etc. They propose new hash functions to improve the probability of collisions between similar vectors and avoid collisions between non-similar vectors. The tree-based indexes include Kdtree\[25\], R-tree\[26\], Cover Tree\[27\]\[28\], Ball-tree\[19\], etc. There are two main<tbc>

