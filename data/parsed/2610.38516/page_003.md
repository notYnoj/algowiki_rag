<tbc>on the edges in decreasing weight, with a _q_-energy minimisation restricted to each plateau of equal weight \[14,27\]. Allène et al. \[2,3\] showed that the min cut of the powered weights becomes a maximum spanning forest cut as _p_ grows, and Cousty et al. \[15\] that this cut is the watershed cut of the graph. Grady’s prior-augmented RW \[20\] adds unary terms, which we use throughout.

#### Learning through segmentation algorithms.

Unrolling an iterative algorithm into a network \[23,26\] and differentiating an optimisation layer implicitly \[4,6\] are well-known techniques; CRF-as-RNN \[33\] unrolls mean-field inference as a last layer. Closest to us, Cerrone et al. \[9\] learn the edge weights of a seeded RW end to end from given seeds; we add unaries, the temperature path to the PW with its exact limit, and instances as labels. Wolf et al. \[32\] learn inside a seeded watershed by structured learning, and spanning structures can also be made differentiable by perturbation \[7\] or stochastic softmax relaxations \[31\]; ours is the deterministic relaxation that the PW framework already contains. In the morphology literature, Challa et al. \[11\] train features with a triplet loss so that a watershed on them classifies hyperspectral pixels, and Chierchia and Perret \[12\] fit ultrametrics, the hierarchical form of the watershed, by gradient descent on a relaxed objective; in both the watershed is differentiated through a surrogate. The deep watershed transform \[5\] and HoVer-Net \[22\] predict maps on which a non-differentiable watershed is run afterwards. Our relaxation is not a surrogate but a member of the same family: the Random Walker is the Power Watershed at finite p, and its limit is the watershed itself.

### 3 The watershed layer

#### 3.1 Energy, temperature and limit

Let \(c_e\ge 0\) be the cost of edge _e_ and, for each pixel _i_, \(c_i^1,c_i^0\ge 0\) the costs of attaching it to the foreground and background labels. With everything raised to the inverse temperature _p_,

\(E_p(x)=\sum_{e=\{u,v\}}w_e\left(x_u-x_v\right)^2+\sum_ia_i^1\left(x_i-1\right)^2+\sum_ia_i^0x_i^2,w_e=e^{-pc_e},a_i^1=e^{-pc_i^1},a_i^0=e^{-pc_i^0}.\text{(2)}\)

Stationarity yields the symmetric positive definite system

\(\left(L(w)+\mathrm{diag}(a^0+a^1)\right)x=a^1,\) (3)

where _L(w_) is the weighted graph Laplacian. The unaries are edges to two virtual label nodes of an augmented graph, so (2) is the seeded (_p,_2) energy on that graph with the two virtual nodes as seeds. Hence _x<sup>p</sup>_ is the probability that a random 2-forest at inverse temperature _p_ connects pixel _i_ to the foreground node (Appendix B.1), and \(x^\infty=\mathrm{lim}_{p\rightarrow\infty} x^p\) is the PW of the augmented graph:

