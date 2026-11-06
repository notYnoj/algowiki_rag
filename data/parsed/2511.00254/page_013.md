<tbc>and could be very small (again, see Section A.2 for more details). We defer the details to the full version, but one can show how to efficiently compute an almost-uncrossed flow that is _approximately_ feasible - that is, for any \(\epsilon>0\), in polynomial time we can find an almost-uncrossed flow that is feasible for \((G,H,(1+\epsilon)u,d)\). The details are similar to the uncrossing algorithm in \[19\]. Essentially, by rounding the flow on each path down slightly and removing support paths with very little flow, we can ensure that the remaining flow values are all common multiples of a small but sufficiently large fraction, which ensures the uncrossing steps make enough progress to terminate in polynomial time. We summarize the final result below.

**Theorem 3.9.** _Let_ (_G,H_) _be pairwise-planar and let_ (_G,H,u,d_) _be a congestion instance. Let_ \(\epsilon>0\) _be any constant. If the instance is feasible, then there exists a strongly uncrossed flow_ \(f'\) _such that_ \(f'\) _is feasible for_ \((G,H,(1+\epsilon)u,d)\)_. The flow_ \(f'\) _can be computed in polynomial time._

Note that \(f'/(1+\epsilon)\) is feasible for \((G,H,u,d/(1+\epsilon))\), so this approximate guarantee is useful for maximization as well as congestion. Combining this theorem with our rounding results Theorem 1.2 and Theorem 1.3, we obtain Theorem 1.4.

### 3.2 Integral Flow-Multicut Gap

In this subsection we prove Theorem 1.5. Here we are concerned with maximization instances (_G,H,u_). A _multicut_ is a set of supply edges \(R\subseteq E(G)\) such that _G-R_ does not contain any _st_-path for any \((s,t)\in E(H)\). The minimum capacity of a multicut is at least the maximum value of a (fractional) multiflow. The ratio of these quantities is the _(fractional) flow-multicut gap_<sup>11</sup> The _integral flow-multicut gap_ is the ratio of the minimum capacity of a multicut to the maximum value of an integral multiflow.

An immediate corollary of Theorem 3.8 and Theorem 1.2 is that for pairwise planar (_G,H_), the integral flow-multicut gap is bounded by _O_(1) times the (fractional) flow-multicut gap. We combine this with the following result by Tardos and Vazrani \[33\] to conclude Theorem 1.5.

**Theorem 3.10** (Tardos and Vazrani \[33\])**.** _For any maximization instance_ (_G,H,u_) _where G is planar, the (fractional) flow-multicut gap is bounded by O_(1).

## 4 Maximization Setting: Rounding and Hardness

In this section, we prove Theorem 1.2 and Theorem 1.6, which cover our rounding and inapproximability results for maximum uncrossed multiflow.

### 4.1 Uncrossed String Graphs and Approximate Integer Decomposition

First we prove Theorem 1.2. Our approach is to establish a so-called approximate integer decomposition property \[3, 5\] for uncrossed multiflows. The outline of the strategy is as follows. Suppose we are given an uncrossed multiflow _f_, which achieves a value of \(\beta\). Imagine scaling _f_ by a positive integer _k_ such that _kf_ is integral. Of course, _kf_ may not be feasible. However suppose we are able to show that _kf_ can be decomposed as the sum of a small number _b_ of feasible integral flows. That is \(kf=\sum_{i=1}^bf^i\) where each _f<sup>i</sup>_ is integral and feasible. At least one of the _f<sup>i</sup>_ flows achieves a 1_/b_ fraction of the value of _kf_, and hence a _k/b_ fraction of the value of _f_.

How can we achieve such a decomposition? Suppose (for simplicity) that _kf_ sends 1 unit of flow along paths \(\mathcal{P}=\{P_1,\dots,P_\ell\}\). Furthermore suppose that each edge of _G_ has unit capacity and hence each appears on at most _k_ paths. Our goal then is to partition the paths into classes such that every edge appears at most once in each class; the classes then define the flows _f<sup>i</sup>_. Equivalently, we seek to partition the paths so that paths in the same class do not share an edge. Phrased this way, we can recognize this as a graph colouring problem on the edge-intersection graph of P.

<sup>11</sup>Note: this is different from the similarly named _flow-cut gap_, which is defined for congestion instances and relates the minimum congestion value to the sparsity of cuts (not necessarily multicuts). See \[7\] for instance.

