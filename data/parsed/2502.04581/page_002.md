cannot be solved in time \(O(n^{k-\epsilon})\) for any \(\epsilon>0\). Most notably, reductions from _k_-OV, _k_- SUM and the weighted _k_-clique problem have been used to establish _n_<sup>_k-o_(1)</sup>-time conditional lower bounds, often matching known algorithms; see [50] for a detailed survey.

In this context, the 3-SUM hypothesis is arguably the first - and particularly central - hardness assumption for conditional lower bounds. Initially introduced to explain various quadratic-time barriers observed in computational geometry [35], it has since been used to show quadratic-time hardness for a wealth of problems from various fields [52, 46, 6, 40, 29, 3, 21]. Its generalization, the _k_-SUM<sup>1</sup> hypothesis, has led to further conditional lower bounds beyond the quadratic-time regime [31, 4, 1, 2, 41]. For a more comprehensive overview, we refer to [50].

The centrality of the 3-SUM hypothesis for understanding quadratic-time barriers begs an interesting question: Does 3-SUM fully capture quadratic-time solvability, in the sense that it is hard for the entire class DTIME(_n_<sup>2</sup>)? Alas, Bloch, Buss, and Goldsmith [10] give evidence that we are unlikely to prove this: If 3-SUM is hard for DTIME(_n_<sup>2</sup>) under quasilinear reductions, then \(\mathsf{P}\neq\mathsf{NP}\). Thus, to understand precisely the role of 3-SUM to understand quadratic-time computation, the more reasonable question to ask is:

_What is the largest class_ C _of problems such that_ 3_-SUM is_ C_-hard?_<sup>2</sup>

Finding a large class C for which 3-SUM is hard may be seen as giving evidence for the 3-SUM hypothesis. Furthermore, such a result may clarify the true expressive power of the 3-SUM hypothesis, much like the NP-completeness of 3-SAT highlights its central role for polynomial intractability.

### 1.1 Our approach

We approach our central question from a descriptive complexity perspective. This line of research has been initiated by Gao et al. [36], who establish the sparse OV problem as complete for the class of model checking first-order properties. One can interpret this result as showing that the OV problem expresses relational database queries in the sense that a truly subquadratic algorithm for OV would improve the fine-grained data complexity of such queries (see [36] for details). Related works further delineate the fine-grained hardness of model checking first-order properties and related problem classes [49, 14, 12, 7, 13, 32], see Section 1.3 for more discussion.

Towards continuing the line of research on fine-grained completeness theorems, we introduce a class of problems corresponding to deciding formulas in linear integer arithmetic over finite sets of integers. Specifically, consider the vectors

\(x_1=(x_1[1],\dots,x_1[d_1]),\dots,x_k=(x_k[1],\dots,x_k[d_k])\)

as quantified variables, and let _t_<sub>1</sub>_,...,t<sub>l</sub>_ be free variables. Moreover, let

\(X:=\{x_1[1],\dots,x_1[d_1],\dots x_k[1],\dots,x_k[d_k],t_1,\dots,t_l\},\)

<sup>1</sup> The _k_-SUM problem asks, given sets _A_<sub>1</sub>_,...,A<sub>k</sub>_ of _n_ numbers, whether there exist \(a_1\in A_1,\dots,a_k\in A_k\) such that \(\sum_{i=1}^ka_i=0\). The _k_-SUM hypothesis states that for no \(\epsilon>0\) there exists a \(O(n^{\lceil k/2\rceil-\epsilon})\) time algorithm that solves _k_-SUM. <sup>2</sup> Note that there are different reasonable notions of reductions to consider. Rather than the quasilinear reductions used by Bloch et al., we will consider the currently more commonly used notion of fine- grained reductions; see Section 1.2 for details on the notion of completeness that we will use.

