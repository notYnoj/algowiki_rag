# Dynamic framework for edge-connectivity maintenance of simple graphs

Blażej Wróbel <sup>∗</sup>

March 10, 2026

**Abstract**

We present a framework for dynamically maintaining _k_-edge-connectivity of an undirected simple graph _G_ under edge insertions and deletions, where _k_ is a fixed constant. After an edge insertion, the algorithm identifies and removes a distinct redundant edge to maintain sparsity, in _O(k_log_n_) amortized time. After an edge deletion that reduces \(\lambda(G)\) below _k_, the algorithm restores _k_-edge-connectivity by adding at most two new edges (excluding the deleted edge), in _O(k_<sup>3/2</sup>_n_<sup>3/2</sup>) time. The insertion procedure combines Nagamochi–Ibaraki sparse certificates with Link-Cut Trees; the deletion procedure uses a single maximum-flow computation on the sparsified graph. Throughout all updates, the graph is maintained with _O(kn_) edges.

### 1 Introduction

Edge-connectivity is one of the fundamental measures of network reliability and fault tolerance. A graph is _k_-edge-connected if the removal of fewer than _k_ edges cannot disconnect it. We study the problem of actively maintaining _k_-edge-connectivity: given a graph _G_ with \(\lambda(G)\ge k\), the goal is to preserve this invariant under edge insertions and deletions by modifying the graph itself - not merely reporting whether the invariant holds. An edge insertion may make an existing edge redundant for _k_-edge-connectivity, while an edge deletion may reduce \(\lambda(G)\) below _k_. We address both cases:

1. Redundancy Elimination (Post-Addition): after insertion of a new edge _e<sub>new</sub>_={_u,v_}, local edge-connectivity between its endpoints may be greater than _k_. To maintain structural sparsity - specifically ensuring |_E_|=_O(kn_) - we identify and remove an existing edge \(e_{old}=\{x,y\}(e_{old}\neq e_{new})\) for which the condition \(\lambda(x,y;(G\cup\{e_{new}\})\backslash\{e_{old}\})\ge k\) (see Section 3 for definition of \(\lambda(x,y;G)\)) is met. This ensures that the graph remains sparse and _k_-edge-connected.

2. Connectivity Restoration (Post-Removal): after removal of an existing edge _e<sub>del</sub>_, the global edge-connectivity may drop below the required threshold, i.e., \(\lambda(G\backslash\{e_{del}\})<k\). In such cases, the framework computes and inserts a minimal set of augmenting edges \(E_{aug}(e_{del}\notin E_{aug})\) such that the condition \(\lambda((G\backslash\{e_{del}\})\cup E_{aug})\ge k\) holds.

Beyond its theoretical interest, our framework is motivated by settings where a network’s link structure must be actively maintained under dynamic changes. A natural application of Connectivity Restoration arises in survivable telecommunications network design, where nodes represent routers and edges represent physical communication links. Such networks are designed to be sparse and _k_-edge-connected so that data transmission survives up to _k_-1 simultaneous link failures [8]. When a link is lost - due to hardware malfunction or fiber cut - the operator must provision new links to restore the required redundancy. Our framework models this directly: the failed link is an edge deletion, and the algorithm computes the minimal set of new links to restore invariant \(\lambda(G)\ge k\).

<sup>∗</sup>Wrocław University of Science and Technology, Poland

