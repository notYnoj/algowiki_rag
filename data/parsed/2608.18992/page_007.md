## 13:6 Tight Energy Lower Bounds for Distributed Graph Algorithms

The _conditional entropy of X conditioned on Y_ is defined as

\(\mathbf{H}[X|Y]=\mathbf{E}_Y[\mathbf{H}[X|Y=y]].\) (2)

The _conditional mutual information of X and Y_ is defined as

\(\mathbf{I}[X:Y|Z]=\mathbf{E}_Z[\mathbf{I}[X:Y|Z=z]]=\mathbf{H}[X|Z]-\mathbf{H}[X|Y,Z].\) (3)

\(\blacktriangleright\) **Fact 2.1.** _It holds that:_ **1.** \(\mathbf{I}[X:Y|Z]\le\mathbf{H}[X|Z]\le\mathbf{H}[X]\), **2.** \(\mathbf{I}[X:Y|Z]\le\mathbf{I}[X,W:Y|Z]\).

\(\blacktriangleright\) **Fact 2.2** (Chain Rule of Mutual Information)**.** **I**[_X:Y,Z|W_]=**I**[_X:Y|W_]+**I**[_X:Z|W,Y_].

\(\blacktriangleright\) **Fact 2.3** (Chain Rule of Conditional Entropy)**.** **H**[_X,Y|W_]=**H**[_X|W_]+**H**[_Y|X,W_].

\(\blacktriangleright\) **Fact 2.4.** \(\mathbf{H}[X]\le log_2(|\text{supp}(X)|)\)_, where_ supp(_X_) _denotes the support of X. Equality holds if X is uniformly distributed._

\(\blacktriangleright\) **Fact 2.5.** \(\mathbf{I}[X:Y,Z|W]\le|X|\).

\(\blacktriangleright\) **Fact 2.6** (Data Processing Inequality, see Theorem 2.8.1 in [18])**.** _If random variables X, Y, and Z form the Markov chain_ \(X\rightarrow Y\rightarrow Z\)_, i.e., the conditional distribution of Z depends only on Y and is conditionally independent of X, then_ \(\mathbf{I}[X:Y]\ge\mathbf{I}[X:Z]\).

## 2.4 Additional Related Work

We mainly focus on related works on lower bounds on energy complexity, though as mentioned in Section 1, several recent works have designed energy-efficient distributed _algorithms_ in the sleeping model for various fundamental problems including MIS, approximate matching, maximal matching, coloring, and vertex cover, broadcast, spanning tree, breadth-first spanning tree, minimum spanning tree (MST), and single-source shortest paths [15, 13, 14, 17, 9, 28, 29, 35, 24, 3, 30, 20, 6, 21, 23]). While some of these works assume the SLEEPING-CONGEST model, some assume the SLEEPING-RADIO model (see e.g., [24] for works in this model), where the radio network model is assumed. In this model, nodes can only broadcast to their neighbors, and there are interference constraints. It is important to note that lower bounds for the SLEEPING-CONGEST also apply to SLEEPING-RADIO, and hence all the lower bounds in this paper also apply.

Few works have shown lower bounds on energy complexity. As mentioned earlier, there is a lack of general techniques for showing energy lower bounds, partly due to the reasons mentioned in Section 1. Still, a notable lower bound on energy complexity is the \(\Omega(logn)\) lower bound for broadcast, which also applies for leader election and minimum spanning tree [13, 3]. This bound applies even to randomized algorithms and to the LOCAL model (where there are no restrictions on message sizes, unlike in CONGEST). The work of [9] showed a _deterministic_ lower bound of \(\Omega(logn)\) _node-averaged_ energy complexity for leader election on rings. This lower bound exploits the fact that \(\Omega(nlogn)\) is a deterministic lower bound on the message complexity of leader election in rings, and as a result, on average, a node has to transmit \(\Omega(logn)\) messages and hence be awake for so many rounds. This basic idea of exploiting per-node congestion is also used to demonstrate an energy-round trade-off in [3]. We note that the approach of [3] for showing energy-round trade-off (which uses the lower approach of [22] in conjunction with per-node congestion) is different from the information-theoretic approach (cf. Lemma 1) used in the current paper.

