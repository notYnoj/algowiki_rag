running the algorithm, we can create three different stacks for the three different types of components by exploring the instance in linear time. Now, we do have a nested for-loop for the case that deals with paths involving an odd number of agents and for the case that deals with cycles involving an odd number of agents. Asymptotically, each execution of the inner loop requires at most linear time in the length of the path or cycle, i.e., linear in the number of agents. Furthermore, we have at most a linear number of components in the number of agents. The quadratic upper bound follows as required.

This positive result implies a tight tractability frontier: Deviator-Max-sri and Deviator- BA-Max-sri can both be solved very efficiently when preference lists are of length at most 2. However, the problems are NP-hard even in the bipartite case and when preference lists are of length at most 3, as previously established in Corollaries 3.2 and 5.2, respectively.

## 7 Resolving Further Open Cases

When aggregating an overview of known and newly established complexity results in  1 (to follow in Section 8), we identified two further cases that, to the best of our knowledge, have not yet been detailed explicitly in existing literature. Both concern the minimisation of blocking agents in sri across the whole instance, i.e., the MinBA-AlmostStable-sri problem, which is also the special case of Deviator-BA-sri where _D=A_. It is known that MinBA- AlmostStable-sri is NP-hard when preference lists are of length 5 \[11\].

The first result shows that when preference lists are very short, then MinBA-AlmostStable- sri is solvable in polynomial time. This follows immediately from our algorithm in Section 6.

**Theorem 7.1.** MinBA-AlmostStable-sri _can be solved in O(n_) _time when preference lists are of length at most 2 (where n is the number of agents)._

_Proof._ We already noted above that MinBA-AlmostStable-sri is the special case of the problem Deviator-BA-sri where all agents are part of the deviator set. Therefore, due to Theorem 6.1, Algorithm 2 solves MinBA-AlmostStable-sri to optimality in, asymptotically, at most linear time in the number of agents.

The second result shows that MinBA-AlmostStable-sri remains intractable even when preference lists are complete.

**Theorem 7.2.** MinBA-AlmostStable-sri _is_ NP-hard _even when all preference lists are complete._

_Proof._ Suppose we could minimise the number of blocking agents in polynomial time. Then we could decide in polynomial time whether, for a given sri instance _I_ with complete preference lists (which would be more appropriately denoted by src) and a non-negative integer _k_, _I_ admits a matching with at most _k_ blocking agents. Note that this problem is NP-complete when preference lists are permitted to be incomplete, as Chen et al. \[11\] showed. We will denote the general problem (not requiring complete preference lists) by _k_-AlmostStable- sri and the restricted problem requiring complete preference lists by _k_-AlmostStable-src. Below, we give a simple reduction from the former problem to the latter.

Let \((I=(A,\succ),k)\) be an instance of _k_-AlmostStable-sri with _n_ agents. We construct an instance \((I'=(A',\succ'),k)\) of _k_-AlmostStable-src as follows. Start with \(I'=I\), i.e., every agent in _A_ is also in \(A'\) and the preferences \(\succ'\) are initially the same as in \(\succ\). Then, for every agent \(a_i\in A\), create _k_ additional dummy agents \(a_i^1,a_i^2,\dots,a_i^k\) in \(A'\). Furthermore, append these agents in increasing order of superscript to the end of \(\succ'_{a_i}\), and let \(\succ'_{a_i^s}\) (for all \(1\le s\le k\)) rank just _a<sub>i</sub>_ to start with. After all dummy agents have been introduced and the modifications to \(\succ'\) have been made, complete all preference lists of \(\succ'\) by appending all previously unranked agents<tbc>

