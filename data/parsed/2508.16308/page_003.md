<tbc>develop distributed lower bounds for computing _k_-partial _k_-colorings in graphs that are guaranteed to admit such a coloring.

For distributed computing, we work in the standard LOCAL model of distributed computing \[20\]. In this model, the input graph represents a communication network where each node is a computational entity. The nodes communicate in synchronous rounds, exchanging unbounded-sized messages with their neighbors. Each node has a unique identifier (typically from a polynomial-size range) and knows only its own id and the size of the universe of the ids at the beginning of the computation. The complexity of a distributed algorithm is measured in the number of rounds until all nodes produce their output. In our context, each node must eventually decide its color based on the information available in its local neighborhood.

A more detailed discussion of the LOCAL model is provided in Section 4.

## 2 Related Work

### Proper \((\Delta+1)\)-Coloring.

For many years, the fastest known deterministic algorithms for proper \((\Delta+1)\)-coloring in graphs with maximum degree \(\Delta\) required essentially \(2^{O(\sqrt{logn})}\) rounds in _n_-node networks \[1,24\]. This long-standing upper bound was only recently surpassed when a polylogarithmic-round algorithm for \((\Delta+1)\)-coloring was introduced \[26\]. All prior algorithms relied on a particular type of graph decomposition, and the breakthrough in \[26\] demonstrated how to efficiently compute this decomposition within a polylogarithmic number of rounds.

A major advance followed in 2020, when it was shown that \((\Delta+1)\)-coloring can be achieved in \(O(logn\cdot log^2\Delta)\) rounds \[16\], this time without graph decomposition, by using rounding of a fractional solution. For large \(\Delta\), this algorithm still runs in _O_(log<sup>3</sup>_n_) rounds, which was subsequently improved to \(\tilde{O}(log^2n)\) \[13\] and more recently to \(\tilde{O}(log^{5/3}n)\) \[14\].

The problem of proper \((\Delta+1)\)-coloring has also been studied exclusively with respect to round complexity as a function of the parameter \(\Delta\). This line of work has yielded algorithms for \((\Delta+1)\)-coloring that run in \(\widetilde{O}(\sqrt{\Delta})+O(log^*n)\) rounds \[3,11,21\]. However, these are efficient only when \(\Delta\) is small -- specifically, their running times are polylogarithmic in _n_ only if \(\Delta\) itself grows polylogarithmically with _n_.

### Proper \(\Delta\)-Coloring.

The problem of proper \(\Delta\)-coloring has been extensively studied in the distributed setting. The work of \[23\] established the _distributed Brooks’ theorem_, showing that if all but one vertex of the graph are already \(\Delta\)-colored, the coloring can be extended by recoloring a path of length \(O(log_\Delta n)\) from that vertex, leading to a distributed \(\Delta\)-coloring algorithm with complexity \(O(\Delta\cdot polylogn)\) and a randomized version with complexity \(O(log^3n/log\Delta)\) rounds. Subsequent work has significantly improved these bounds. The work of \[15\] presented a randomized algorithm with round complexity \(O(log\Delta)+2^{O(\sqrt{loglogn})}\) for \(\Delta\ge 4\). Later, \[16\] gave the first deterministic polylogarithmic-time algorithm for all \(\Delta\ge 3\), with round complexity \(O(log^2\Delta log^2n)\). The work of \[10\] designed the first randomized polyloglog_n_-round LOCAL algorithm for the problem. Most recently, Bourreau et al. \[4\] obtained an \(O(log^4\Delta+log^2\Delta lognlog^*n)\) round deterministic LOCAL algorithm for \(\Delta\ge 3\), which remains the state of the art for the problem.

### Partial Coloring.

Under certain restrictions, efficient algorithms and lower bounds for partial coloring are known. For example, in (constant) \(\Delta\)-regular graphs, there exists a deterministic algorithm that computes a _k_-partial 3-coloring in _O_(log<sup>∗</sup>_n_) rounds whenever \(\Delta\ge 3k-4\) and \(k\ge 3\),<tbc>

