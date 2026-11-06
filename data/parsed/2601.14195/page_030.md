<tbc>are contained in more than one blocking pair at each iteration of the main while loop. While at least one such agent remains, we repeat this rematching procedure with this agent taking the role of _a<sub>i</sub>_ in the argument above.

Asymptotically, Irving’s algorithm requires at most linear time in the sum of the preference list lengths of _I_ \[34\], which, due to bounded preference list lengths, is linear in the number of agents of _I_. The maximum-cardinality matching algorithm we described simply walks over paths and cycles, so it requires _O(m_) time for a graph with _m_ edges. We execute this on the acceptability graph of _I_, which has _n_ vertices and, again due to bounded preference list lengths, _m=O(n_) edges. Hence, computing _M<sub>C</sub>_ requires _O(n_) time. The rematching procedure, if invoked, is executed at most _O(n_) times because the number of agents in more than one blocking pair strictly decreases with each iteration (as argued above), and each execution requires constant time. We can implement the while loop efficiently by building a stack of unmatched agents (every agent involved in two blocking pairs must clearly be unmatched) and, at every iteration of the loop, popping an agent from this stack and verifying whether this agent is indeed blocking with both agents on its preference list (this can clearly be performed in constant time). Because we do the computation of the initial _M<sub>C</sub>_ and the rematching sequentially, and assuming that matching size comparisons can be implemented in constant time, we arrive at an overall time complexity of _O(n_).

This result identifies a tractable frontier. Even though minimax almost-stability is generally intractable, instances with very short preference lists admit an efficient computation. Such instances can arise in practical scenarios where agents may only choose between very limited options.

## 5.2 Minimax Maximum Matchings in Bipartite Graphs with Max-Degree 2

We now show how the high-level technique of Algorithm 1 for low-degree acceptability graphs in sri carries over to Minimax-AlmostStable-Max-smi. Specifically, the procedure we give in Algorithm 2 solves Minimax-AlmostStable-Max-smi to optimality when preference lists are of length at most 2. It works as follows: compute a stable matching _M<sub>S</sub>_ using the Gale-Shapley algorithm \[20\] and a maximum-cardinality matching _M<sub>C</sub>_ using the same procedure as the one that we described for Algorithm 1 (as the acceptability graph still only consists of paths and cycles). If |_M<sub>S</sub>_|=|_M<sub>C</sub>_| then return _M<sub>S</sub>_, otherwise perform the same rematching procedure on _M<sub>C</sub>_ as in Algorithm 1 and return this modified matching.

**Algorithm 2** Exact algorithm for Minimax-AlmostStable-Max-smi with lists of length \(\le 2\)

**Input:** _I_ : an smi instance

**Output:** _M_ : a matching

1: \(M_S\leftarrow\text{GaleShapley}(I)\triangleright\) Compute a stable matching

2: \(M_C\leftarrow\text{MaxCard}(I)\triangleright\) Compute a maximum-cardinality matching

3: **if** |_M<sub>S</sub>_|=|_M<sub>C</sub>_| **then**

4: **return** _M<sub>S</sub>_

5: **end if**

6: **while** \(\exists a_i\) such that |_bp<sub>a<sub>i</sub></sub>(M<sub>C</sub>_)|=2 **do** \(\triangleright\) Rematching procedure

7: pick one agent _a<sub>r</sub>_ that is in a blocking pair with _a<sub>i</sub>_

8: \(a_k\leftarrow M_C(a_r)\)

9: \(M_C(a_i)\leftarrow a_r;M_C(a_r)\leftarrow a_i;M_C(a_k)\leftarrow a_k\)

10: **end while**

11: **return** _M<sub>C</sub>_

