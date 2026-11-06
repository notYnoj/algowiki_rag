Recall that the Catalan numbers _C_<sub>0</sub>_,C_<sub>1</sub>_,C_<sub>2</sub>_,..._ can be defined recursively by _C_<sub>0</sub>=1 and

\(C_n=\sum_{k=1}^nC_{k-1}\cdot C_{n-k}.\) (2)

_C<sub>n</sub>_ counts many different combinatorial objects, such as the number of triangulations of a convex polygon with _n_+2 vertices, and the number of binary trees with _n_+1 leaves. (See, e.g., \[Sta15\].) The variable _k_ being summed over in Equation (2) typically corresponds to ways to partition the combinatorial object into two smaller parts. This leads to our new definition, in which we want to instead _minimize_ over all ways to partition the object:

**Definition 1.3** (2D LWS<sup>PT</sup>)**.** _Given as input an_ \(n\times n\times n\) _tensor w, the_ 2D LWS<sup>PT</sup> _problem asks to compute the value of T_\[_n,n_\] _given the dynamic programming recurrence relation:_

\(T[i,j]=\left\{\begin{array}{ c c }
0 & \text{if}j-i\le 1 \\
min_{i<k<j}\left\{T[i,k]+T[k,j]+w[i,j,k]\right\} & \text{otherwise.}
\end{array}\right.\)

For instance, this captures the polygon triangulation problem defined above when \(w[i,j,k]=w_i\cdot w_j\cdot w_k\), which is unsurprising as polygon triangulations are counted by the Catalan numbers; this inspires the name 2D LWS<sup>PT</sup>. We show in Section 6 below that this recurrence also captures other natural problems such as optimal binary search tree construction (optimizing over binary trees, which are counted by Catalan numbers) and matrix chain multiplication (optimizing over sequences of properly matched parentheses, again counted by Catalan numbers). Furthermore, in each of these examples, the rank (for polygon triangulation) or slice rank (for the other two examples) of _w_ is 1.

## 1.5 Main Results and Proof Structure Overview

### Reduction notation

Before stating our results, we introduce one piece of notation for denoting the results of fine-grained reductions between problems with different running times. For computational problems _P,Q_, we say that _P_ "reduces" to _Q_, denoted by \(P\rightarrow Q\) if a polynomial speedup for _Q_ yields a polynomial speedup for _P_. More precisely, suppose _P,Q_ are solved in time _T<sub>p</sub>,T<sub>q</sub>_, respectively, via the straightforward algorithms. We say that _P_ "reduces" to _Q_, denoted by \(P\rightarrow Q\) if for every \(\varepsilon>0\) there exists a \(\delta>0\) such that, given a \(O(T_q^{1-\varepsilon})\) time algorithm for _Q_, one gets a \(O(T_p^{1-\delta})\) time algorithm for _P_.

For example, \(\mathsf{SAT}\rightarrow\mathsf{Min}\mathsf{IP}_{n,clogn}\) means that if there is an algorithm for Min-IP<sub>_n,_clogn</sub> with running time \(O(n^{2-\varepsilon})\) for some \(\varepsilon>0\), then there is an algorithm for SAT with running time \(O(2^{(1-\delta)n})\) for some \(\delta>0\). \(\mathsf{3Min}\mathsf{IP}\rightarrow\mathsf{Min}\mathsf{IP}\) means that if there is an algorithm for Min-IP with running time \(O(n^{2-\varepsilon})\) for some \(\varepsilon>0\), then there is an algorithm for 3Min-IP with running time \(O(n^{3-\delta})\) for some \(\delta>0\). When it may be unclear, the formal statements of our results are stated in the theorems below.

### 1.5.1 kD LWS Hierarchy and Hardness.

We establish a hierarchy of kD LWS problems and describe their connections to kMin-IP, summarized by the following diagram.

