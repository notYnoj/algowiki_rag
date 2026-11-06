# A Near-Optimal Offline Algorithm for Dynamic All-Pairs Shortest Paths in Planar Digraphs

Debarati Das<sup>∗</sup> Maximilian Probst Gutenberg<sup>†</sup> Christian Wulff-Nilsen<sup>‡</sup>

**Abstract**

In the planar, dynamic All-Pairs Shortest Paths (APSP) problem, a planar, weighted digraph _G_ undergoes a sequence of edge weight updates and the goal is to maintain a data structure on _G_, that can quickly answer distance queries between any two vertices \(x,y\in V(G)\).

The currently best algorithms [FOCS’01, SODA’05] for this problem require \(\tilde{O}(n^{2/3})\) worst- case update and query time, while conditional lower bounds [FOCS’16] show that either update or query time \(\tilde{\Omega}(\sqrt{n})\) is needed<sup>1</sup>.

In this article, we present the first algorithm with near-optimal \(\tilde{O}(\sqrt{n})\) worst-case update and query time for the offline setting, where the update sequence is given initially. This result is obtained by giving the first offline dynamic algorithm for maintaining dense distance graphs (DDGs) faster than recomputing from scratch after each update.

Further, we also present an _online_ algorithm for the incremental APSP problem with \(\tilde{O}(\sqrt{n})\) worst-case update/ query time. This allows us to reduce the online dynamic APSP problem to the online decremental APSP problem, which constitutes partial progress even for the online version of this notorious problem.

<sup>∗</sup>University of Copenhagen, Denmark, das@di.ku.dk. <sup>†</sup>ETH Zurich, Switzerland, maximilian.probst@outlook.com. Supported by Rasmus Kyng’s Start-up Grant at ETH. Work done while at BARC, supported by Thorup’s Investigator Grant No. 16582. <sup>‡</sup>University of Copenhagen, Denmark, koolooz@di.ku.dk. The author is supported by the Starting Grant 7027- 00050B from the Independent Research Fund Denmark under the Sapere Aude research career programme. <sup>1</sup>We use \(\tilde{O}\) and \(\tilde{\Omega}\)-notations to hide poly-logarithmic factors in _n_.

