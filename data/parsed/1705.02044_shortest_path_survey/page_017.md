### 7.2 Discrete-Time Algorithms

Nannicini et al. [104] propose a bidirectional _A_<sup>∗</sup> algorithm that restricts the _A_<sup>∗</sup> search to a set of vertices that are defined by a time-independent algorithm. The bidirectional _A_<sup>∗</sup> algorithm operates in two modes, where the first mode, namely the _forward search_ algorithm, is run on the graph weighted by a specific cost function while the second mode, namely the _backward search_, is run on the graph weighted by a lower-bound function.

Delling and Wagner [37] reanalyzes various time-dependent technique. The concluded that the most of the techniques that operate over time-dependent graphs guarantee correctness by augmenting the preprocessing and query phases subroutines.

Foschini et al. [54] study the computational complexity of the shortest-paths problem over time- dependent graphs. They conclude that linear edge-cost functions causes the shortest path to the destination changes \(n^{\theta(logn)}\) times. They study the complexity of the arrival time by mapping the problem to a parametric shortest-paths problem in order for it to be analyzed correctly.

Demiryurek et al. [40] propose a technique to speed-up the fastest-path computation over time- dependent spatial graphs. They propose a technique based on the _A_<sup>∗</sup> bidirectional time-dependent algorithm that operates in two main stages. The first stage is pre-computation, where it partitions the graph into a set of partitions that do not overlap. Next, they calculate a lower-bound distance label for vertices and borders. The second state is online, where it probes for the fastest path by utilizing a heuristic function based on the computed distance labels. The results indicate that the proposed technique decreases the computation time and reduces the storage complexity significantly.

## 8 Stochastic Shortest-Path Algorithms

A stochastic shortest-path attempts to capture the uncertainty associated with the edges by modeling them as random variables. Then, the objective becomes to compute the shortest-paths based on the minimum expected costs. The two notable lines of research in this problem are adaptive and non- adaptive algorithms. The adaptive algorithms determine what the next best next hop would be based on the current graph at a certain time instance. The non-adaptive algorithms focus on minimizing the length of the path.

### 8.1 Adaptive Algorithms

Miller-Hooks and Mahmassani [96] propose an algorithm to determine the apriori least-expected-time- paths from all source vertices to a single destination vertex. This computation is for done for each departure time during busy time of the graph. They also propose a lower-bound over these apriori least-expected-time-paths.

Nikolova et al. [107] propose an algorithm that maximizes the probability without exceeding a specific threshold for the shortest-paths length. They define a probabilistic model where edge weights are drawn from a known probability distribution. The optimal path is the one with the maximum probability indicating a path that does not pass a specific threshold.

### 8.2 Non-Adaptive Algorithms

Loui [93] proposes using a utility function with the length of the path, where the utility function is monotone and non-decreasing. When the utility function exhibits a linear or an exponential behavior, it

