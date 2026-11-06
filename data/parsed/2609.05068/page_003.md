<tbc>average delay function _d<sub>a</sub>_=1/<sub>(_c<sub>a</sub>-y<sub>a</sub>_)</sub> following from the classical M/M/1 queuing model [20], where _y<sub>a</sub>_ denotes the flow (or load) of _a_. Consequently, for any path \(p\in P^k\) carrying positive flow (i.e., if \(x_p^k>0\)), the total delay through _p_ should be less than or equal to _d<sup>k</sup>_. The Delay-Constrained Maximum Concurrent Flow problem (denoted DCMCF) can then be expressed as follows:

\(\text{DCMCF:}max\gamma\)<br>
\(\sum_{p\in P^k}x_p^k=\gamma\forall k\in K\) (1)

\(y_a\ge\sum_{k\in K,p\in P^k|_{a\in p}}x_p^kb^k\forall a\in A\) (2)

\(\sum_{a\in p}\frac{1}{c_a-y_a}\le d^k\text{if}x_p^k>0\forall k\in K,p\in P^k\) (3)

\(y_a\le c_a\forall a\in A\) (4)

\(x_p^k\ge 0\forall k\in K,p\in P^k.\) (5)

Observe that \(\gamma\) represents the throughput factor, or maximum proportion of each commodity that can be carried through the network. Constraints (1) establish the connection between \(\gamma\) and the \(x_p^k\) proportions ; the equality sign used in this formulation could be equivalently replaced by an inequality without changing the optimal solution of this problem. Constraints (2) relate the flow on an arc \(a\in A\) to the sum of flows on paths containing _a_. The delay constraints are stated in (3). Observe that each Constraint (3) is active if and only if the corresponding path is used (i.e., if \(x_p^k>0\)). Constraints (4) introduce capacity limitations; note that, because of the delay constraint, the load of each arc is always strictly lower than its capacity. Observe that the delay along a path \(p\in P^k\) is at least \(\sum_{a\in p}\frac{1}{c_a}\). We may therefore assume that \(\sum_{a\in p}\frac{1}{c_a}<d^k\) for each path \(p\in P^k\), since any path violating this condition can be discarded.<br>
After multiplication by \(x_p^k\), (3) can be reformulated as:

\(\sum_{a\in p}\frac{x_p^k}{c_a-y_a}\le x_p^kd^k\forall k\in K,p\in P^k.\) (6)

It is worth highlighting that, while this reformulation of the delay constraint incorporates the path-usage condition into a differentiable analytical<tbc>

