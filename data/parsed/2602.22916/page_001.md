# A Simple Distributed Deterministic Planar Separator

Yaseen Abd-Elhaleem<sup>∗</sup> <br>
yaseenuniacc@gmail.com

Michal Dory<sup>†</sup> <br>
mdory@ds.haifa.ac.il

Oren Weimann<sup>‡</sup> <br>
oren@cs.haifa.ac.il

**Abstract**

A balanced separator of a graph _G_ is a set of vertices whose removal disconnects the graph into connected components that are a constant factor smaller than _G_. Lipton and Tarjan [FOCS’77] famously proved that every planar graph admits a balanced separator of size \(O(\sqrt{n})\), as well as a balanced separator of size _O(D_) that is a simple path (where _D_ is the graph’s diameter). In the centralized setting, these separators can both be found in linear _O(n_) time. In the distributed setting, since the diameter _D_ is a trivial universal lower bound for the number of rounds required to solve many optimization problems, separators of size _O(D_) are preferable over those of size \(O(\sqrt{n})\).

It was not until [Ghaffari, Parter DISC’17] that an algorithm was devised to compute such an _O(D_)-size separator distributively in \(\widetilde{O}(D)\) rounds<sup>1</sup>, by adapting the Lipton-Tarjan algorithm to the distributed model. Since then, this algorithm was used in several distributed algorithms for planar graphs, e.g., [Ghaffari, Parter DISC’17], [Li, Parter S’19], [Abd-Elhaleem, Dory, Parter and Weimann PODC’25]. However, the algorithm is randomized, deeming the algorithms that use it to be randomized as well. Obtaining a deterministic algorithm remained an interesting open question until very recently, when a (complex) deterministic separator algorithm was given by [Jauregui, Montealegre and Rapaport PODC’25].

In this paper, we present a much simpler deterministic separator algorithm with the same (near- optimal) \(\widetilde{O}(D)\)-round complexity. While previous works devised either complicated or randomized ways of transferring weights from vertices of _G_ to faces of _G_, we show that a straightforward way also works: Each vertex simply transfers its weight to one arbitrary face it belongs to. That’s it!

We note that a deterministic separator algorithm directly derandomizes the state-of-the-art distributed algorithms for classical problems on planar graphs such as single-source shortest-paths, maximum-flow, directed global min-cut, and reachability.

<sup>∗</sup>_Department of Computer Science, University of Haifa. Supported in part by the Israel Science Foundation grant No. 810/21 and No. 2829/25._ <sup>†</sup>_Department of Computer Science, University of Haifa. Supported in part by the Israel Science Foundation grant No. 2829/25._ <sup>‡</sup>_Department of Computer Science, University of Haifa. Supported in part by the Israel Science Foundation grant No. 810/21._ <sup>1</sup>The \(\widetilde{O}(\cdot)\) notation is used to omit poly log _n_ factors.

