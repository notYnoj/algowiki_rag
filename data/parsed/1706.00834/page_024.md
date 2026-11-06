<tbc>item \(p_i\in[0,1]\). The gain is defined as the sum of the profits of the items picked in the packing predicted by the algorithm in that trial. The goal is to predict with a sequence of packings minimizing regret which is the difference between the total gain of the algorithm and the total gain of the single best packing chosen in hindsight.

Note that this online learning problem only deals with exponentially many solutions when there are exponentially many feasible packings. If the number of packings is polynomial, then it is practical to simply run the Hedge algorithm with one weight per packing. Here we consider a setting of the problem where maintaining one weight per packing is impractical. We assume _C_ and _h<sub>i</sub>_’s are in such way that the number of feasible packings is exponential in _n_.

## The Dynamic Programming Representation.

Finding the optimal packing can be solved via dynamic programming (Kleinberg and Tardos, 2006). Each subproblem is denoted by a pair (_i,c_) for \(0\le i\le n\) and \(0\le c\le C\), indicating the knapsack problem given items 1_,...,i_ and capacity _c_. The base subproblems are (0_,c_) for \(0\le c\le C\) and the complete subproblem is (_n,C_). The dynamic programming for the knapsack problem uses the following max-sum recurrence:

\(\text{OPT}(i,c)=\left\{\begin{array}{ c c }
0 & i=0 \\
\text{OPT}(i-1,c) & c<h_i \\
\text{max}\{\text{OPT}(i-1,c),p_i+\text{OPT}(i-1,c-h_i)\} & \text{else.}
\end{array}\right.\)

This recurrence always recurses on 1 subproblem. Thus the multipaths are regular paths and the problem is essentially the online longest-path problem with several sink nodes. The associated DAG has the subproblems/vertices \(V=\{(i,c)|0\le i\le n,0\le c\le C\}\), source _s_=(_n,C_) and sinks \(\mathcal{T}=\{(0,c)|0\le c\le C\}\). Also at node (_i,c_), the set \(M_{(i,c)}^{(\text{out})}\) consists of two edges going from the node (_i,c_) to the nodes (_i_-1_,c_) and (_i_-1_,c-h<sub>i</sub>_). Figure 6 illustrates an example of the DAG and a sample path associated with a packing.

Since the above recurrence relation correctly solves the offline optimization problem, every path in the DAG represents a packing, and every possible packing can be represented<tbc>

