# Faster Algorithms for Induced Patterns

3<tbc>

<tbc>_tomorphism avoiding conditions_ for many pattern graphs on 5 to 7 vertices and derive the following results:

- There are at least five 5-vertex connected graphs _G_ (out of 21) that can be detected in \(\widetilde{O}(nm)\)-time.<tbc>

- There are at least sixty-five 6-vertex connected graphs _G_ (out of 112) that can be detected in \(\widetilde{O}(m^2)\)-time.<tbc>

**-** The graphs _P_<sub>7</sub> and _C_<sub>7</sub> can be detected in \(\widetilde{O}(nm^2)\)-time.

We derive _O(nm_), _O(m_<sup>2</sup>), and _O(nm_<sup>2</sup>) algorithms for detecting induced _P_<sub>5</sub>, _P_<sub>6</sub>, and _P_<sub>7</sub> respectively. To the best of our knowledge, the previous best algorithmic upper bounds which are given by Hoàng, Kaminski, Sawada, and Sritharan \[6\] for detecting induced _P_<sub>5</sub>, _P_<sub>6</sub>, and _P_<sub>7</sub> are _O(m_<sup>2</sup>), _O(nm_<sup>2</sup>), and _O(m_<sup>3</sup>) respectively when considering both number of vertices and edges of the host graph. Therefore, the above results improve existing bounds for lengths 5, 6, and 7 for the cases where \(m=\Theta(n^{1+\epsilon})\), \(0\le\epsilon<1\).

We give a \(\widetilde{O}(nm)\)-time algorithm for _C_<sub>5</sub> which is optimal. This algorithm is an improvement on the _O(n_<sup>3</sup>)-time algorithm given by Komarath, Kumar, Mishra, and Setthia \[7\] when _m=o(n_<sup>2</sup>). We stress that simply having a (1,1)-width tree decomposition for a pattern is not sufficient to derive a faster algorithm for finding induced copies. For example, the complete bipartite graph _K_<sub>2,3</sub> has a (1,1)-width tree decomposition. But, we could not derive \(\widetilde{O}(nm)\)-time algorithms for finding it as those tree decompositions do not have automorphism avoiding conditions. Our techniques for finding induced subgraphs are illustrated using an example in Section A.

One drawback of our method (and many existing methods such as the ones in \[1,5,10\] used to derive faster algorithms for finding induced patterns) is that the analysis of specific subgraphs do not scale to larger patterns. For example, our algorithm for _C_<sub>7</sub> requires constructing specific tree decompositions for over 100 graphs. Therefore, we do not believe it will be possible to extend our analysis, or similar approaches, to derive algorithms for _C<sub>k</sub>_ for arbitrary _k_. However, we show that by imposing natural restrictions on the host graph, for example, restricting them to bipartite graphs, the required analysis may become simple enough for infinite size pattern families. We show:

- An \(\widetilde{O}(m^{k-1})\)-time algorithm for detecting induced _P_<sub>2_k_</sub> in bipartite graphs.<tbc>

**-** An \(\widetilde{O}(nm^{k-1})\)-time algorithm for detecting induced _C_<sub>2_k_</sub> in bipartite graphs.

To the best of our knowledge, for general host graphs, the fastest algorithms to find induced _P_<sub>2_k_</sub> runs in time _O(n_<sup>2_k_-2</sup>) \[1\]. Note that our algorithm is never worse than this and is significantly faster when _m=o(n_<sup>2</sup>), with the catch that ours only work when the host graph is bipartite. Similarly, our algorithm for _C_<sub>2_k_</sub> improves upon the trivial _O(m<sup>k</sup>_)-time algorithm when \(m=\omega(n)\).

Observe that an \(\widetilde{O}(m^k)\)-time algorithm is trivial for even vertex paths and cycles in general graphs. By assuming that the host is bipartite, we slighly improve on this running-time, and only for \(m=\Theta(n^{1+\epsilon})\), \(0\le\epsilon<1\) for cycles. We

