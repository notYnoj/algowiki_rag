<tbc>Similarly to the setting of BSTs, a natural goal is to find an STT in which the expected depth of a vertex is as small as possible; we refer to such a tree as an _optimal tree_, noting that it is not necessarily unique. This optimization task can be studied both for the uniform probability distribution over the vertices, and for the more general case of an arbitrary distribution given as input. We refer to the first as the _unweighted_ and the second as the _weighted_ problem.

For BSTs, both the unweighted and the weighted problems are well-understood. In the unweighted case, a simple balanced binary tree achieves the optimum. In the weighted case, an optimal tree on _n_ vertices can be found in time O(_n_<sup>2</sup>) by Knuth’s algorithm \[Knu71\], a textbook example of dynamic programming. No faster algorithm is known in general, although Larmore’s algorithm \[Lar87\] achieves better bounds under certain regularity assumptions on the weights; for example, if the probability assigned to each vertex is \(\Omega(1/n)\), then the optimum can be found in time O(_n_<sup>1.591</sup>).

By contrast, the complexity of computing an optimal STT is far less understood. Even in the unweighted case, no polynomial-time algorithm is known, and the problem is not known to be NP-hard even with arbitrary weights. Recently, a PTAS was given for the weighted problem \[BK22\], but its running time for obtaining a \((1+\varepsilon)\)-approximation of the optimal STT is \(\mathcal{O}(n^{1+2/\varepsilon})\), which is prohibitive for reasonably small values of \(\varepsilon\). Note that the apparently easier problem of minimizing the _maximum depth_ of a vertex, i.e., computing the _treedepth_ of a tree, can be solved in linear time by Schäffer’s algorithm \[Sch89\], and treedepth itself has many algorithmic applications, e.g., see \[NdM12, §6,7\].

## Centroid trees.

Given the relatively high cost of computing optimal binary search trees, research has turned already half a century ago to efficient approximations. Mehlhorn has shown \[Meh75, Meh77\] that a simple BST that can be computed in O(_n_) time closely approximates the optimum. More precisely, both the optimum cost and the cost of the obtained tree are in \[_H/_log(3)_,H_+1\], where _H_ is the binary entropy of the input distribution.<sup>1</sup> Alternatively, the cost can be upper bounded by `OPT`+log(`OPT`)+log_e_, where `OPT` is the cost of the optimal tree. Observe that this means that the approximation ratio gets arbitrarily close to 1 as `OPT` goes to infinity. <sup>2</sup>

The BST that achieves the above guarantees is built by recursively picking roots such as to make the weights of the left and right subtrees "as equal as possible". This is a special case of a _centroid tree_, defined as follows. Given a tree T , a _centroid_ of T is a vertex whose removal from T results in components with<tbc>

<sup>1</sup>All logarithms in this paper are base 2. <sup>2</sup>Results for BSTs are sometimes presented in a more general form, where the input distribution also accounts for _unsuccessful searches_, i.e., it may assign non-zero probabilities to the _gaps_ between neighboring vertices and outside the two extremes. Extending such a model to STTs is straightforward, but perhaps less natural in the case of general trees, we therefore omit it for the sake of simplicity, and consider only successful searches.

a
b
o
c
g
o
b
o
a
c
e
f
d
h
i
d
g
j
b
e
f
j
k
e
g
i
f
i
h
k
a
c
d
j
k
h

Figure 1: (_Left._) Tree T . (_Middle._) Centroid tree of T . (_Right._) A different STT on T . Colors indicate weights (probabilities), _w(e_)=_w(h_)=_w(i_)=0.15, _w(d_)=_w(j_)=_w(k_)=0.10, and all other vertices have weight 0.05. Observe that the centroid tree is (in this example) unique.

