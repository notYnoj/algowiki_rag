the seminal work of Welzl [49], which implies that for a given _n_-vertex graph from such a class, one can order its vertices in polynomial time so that every neighborhood is a union of O(log_n_) many intervals. The runtime was improved to O((_m+n_)log_n_) in very recent work with O(log<sup>2</sup>_n_) intervals for each vertex [23] instead of O(log_n_). Prior works [19, 25] achieve O(log<sup>2</sup>_n_) intervals on average per vertex in the same running time. In turn, such a representation can be transformed into an sd-degeneracy sequence of width O(log<sup>2</sup>_n_) [12].

Furthermore, [11] introduced a representation of the edge set of the graph, called a _signed tree model_. A signed tree model of a graph _G_ is a binary tree with leaves labeled with _V(G_) and additional transversal edges which can be positive or negative, and which fully determine the adjacency in _G_ (see Section 2 for a precise definition). Subsequent work [12] transformed signed tree models into _interval biclique partitions_, first defined in [13]. An interval biclique partition into _b_ bicliques of a graph _G_ is a labeling of _V(G_) with {1,2_,...,n_} together with a partition of _E(G_) into _b_ bicliques whose sides are intervals of {1,2_,...,n_}. By pipelining the results of [12, 11], we can first turn an sd-degeneracy sequence of width _d_ into a signed tree model with O(_dn_) transversal pairs in O(_dn+m_) time, and then into an interval biclique partition with O(_dn_) bicliques in O(_dn_log_n+m_) time.

While sd-degeneracy sequences, sparse signed tree models, and interval biclique partitions are relatively simple and often efficiently computable, they bypass the need for involved decomposition notions in classes of bounded twin-width/merge-width/flip-width, when the problem at hand lends itself to their algorithmic uses.

## 1.1 Our results

Our first contributions are two time-optimal algorithms for computing sd-degeneracy sequences of bounded width in classes of linear neighborhood complexity.

H-minor-free bounded cliquewidth bounded twin-width graph with linear neighborhood complexity bounded expansion bounded mergewidth Theorem 1, Theorem 2 conjectured equivalent sd-degeneracy sequence of width O(1) focus on O(1) distances bounded flipwidth Lemma 17 of [12], Lemma 3.1 of [11] signed tree model with O(n) transversal pairs bounded weak 2-coloring linear neighborhood complexity Item 1 of Theorem 1 of [12] bounded degenerate bounded versatile symmetric difference interval biclique partition with O(n) bicliques focus on neighborhoods Theorem 5 Lemma 14 bounded sd-degeneracy SSP matrix multiplication sparse graph classes

Figure 1: Properties of hereditary graph classes and implications among them.

Figure 2: Diagram of the algorithmic pipeline.

