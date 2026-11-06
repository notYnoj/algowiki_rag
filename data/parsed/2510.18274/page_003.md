## 1 Introduction

The _minimum s-t cut_ problem is a cornerstone of combinatorial optimization and graph algorithms. Formally, given an undirected, unweighted graph _G_=(_V,E_) on _n_ vertices, along with two distinguished terminals \(s,t\in V\) , the goal is to compute an _s-t_ cut of the vertex set--that is, a partition (_S,T_) with \(s\in S\) and \(t\in T\)--that minimizes the number of edges crossing the cut, i.e., the quantity \(|E(S,T)|:=|E\cap(S\times T)|\). In this work, we study the complexity of computing a minimum _s-t_ cut in two computational models that restrict access to the input graph.

### Cut-query.

In this setting, we may query an oracle with a partition (_S,T_) of _V_ (i.e. _a cut_) to obtain the cut value |_E(S,T_)|. Our goal is to compute a minimum _s-t_ cut of _G_ while minimizing the total number of queries made to the oracle. This problem was first introduced by the work of Rubinstein, Schramm, and Weinberg \[RSW18\] in an effort to study submodular function minimization problem.<sup>2</sup> While the "trivial" _O(n_<sup>2</sup>) queries suffices to _learn_ the whole undirected graph, the work of \[RSW18\] were the first to break this quadratic barrier via an \(\widetilde{O}(n^{5/3})\)-query algorithm utilizing the randomized construction of a cut sparsifier. More recently, Anand, Saranurak, and Wang \[ASW25\] developed a new deterministic algorithm, matching the same \(\widetilde{O}(n^{5/3})\) query complexity. Notably, their approach is purely combinatorial via an implementation of Dinitz’s blocking flow algorithm \[Din70\], thereby is vastly different from the techniques deployed in \[RSW18\]. Nevertheless, both algorithms circumvent the necessity to learn the whole graph which information-theoretically require \(\widetilde{\Omega}(n^2)\) queries to the oracle when the graph is dense.

The works of Rubinstein, Schramm, and Weinberg \[RSW18\] and Anand, Saranurak, and Wang \[ASW25\] approach the _s-t_ minimum cut problem from two completely orthogonal perspectives; yet both arrive at algorithms with the same query complexity of \(\widetilde{O}(n^{5/3})\). This convergence naturally raises the question: _Do the current_ \(\widetilde{O}(n^{5/3})\)_-query upper bounds represent a latent barrier for computing a minimum s-t cut?_ In this work, we show that we can indeed go below this bound.

**Theorem 1.1** (Main result #1)**.** _There is a randomized algorithm that computes a minimum s-t cut of an undirected unweighted graph G. The algorithm always makes_ \(\widetilde{O}(n^{8/5})\) _cut queries to G and succeeds with high probability._

In addition, our algorithm can be extended to enumerate _all_ minimum _s-t_ cuts within the same query complexity, although we do not make this extension explicit in our later analysis. We also highlight that our algorithms are simple, purely combinatorial, and can be naturally interpreted as a recursive greedy procedure.

### Two-player communication.

In this setting, input graph _G_=(_V,E_) is edge-partitioned across two players, namely Alice has _G<sub>A</sub>_=(_V,E<sub>A</sub>_), and Bob has _G<sub>B</sub>_=(_V,E<sub>B</sub>_), with \(E=E_A\cup E_B\). The players are allowed to exchange a sequence of messages (via a _protocol_) with the goal of computing a minimum _s-t_ cut of _G_ while minimizing the total amount of communication between the players.

In fact, any upper bound in the cut-query model translates to an upper bound in the communication setting, with an additional _O_(log_n_) factor. To see this, observe that any cut query can be simulated with _O_(log_n_) bits of communication: Alice locally computes |_E<sub>A</sub>(S,T_)| and sends the result to Bob, who then computes |_E<sub>B</sub>(S,T_)| and sends it back to Alice. The players can thus recover the cut value by computing |_E(S,T_)|=|_E<sub>A</sub>(S,T_)|+|_E<sub>B</sub>(S,T_)|. Since both |_E<sub>A</sub>(S,T_)| and<tbc>

<sup>2</sup>The problem was in fact studied earlier by Cunningham \[Cun85\] who observed that the problem can be solved in \(\widetilde{O}(n^2)\) queries even on weighted directed graphs. Note, however, that the \(\widetilde{O}(n^2)\) query complexity is trivial for undirected graphs.

