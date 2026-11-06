### Regret Bound.

As mentioned earlier, the number of binary trees with _n_ nodes is the _n_th Catalan number. Therefore \(\mathcal{N}=\frac{(2n)!}{n!(n+1)!}\in(2^n,4^n)\). Also note that each multipath representing a BST consists of exactly _D=n_ multiedges. Thus using Theorem 10, EH achieves a regret bound of \(\mathcal{O}(n\sqrt{L^*})\). Moreover, since |_M_|=_O(n_<sup>3</sup>), using Theorem 14, CH achieves a regret bound of \(\mathcal{O}(n^\frac{1}{2}(\mathrm{log}n)^\frac{1}{2}\sqrt{L^*})\).

## 5.2 Matrix-Chain Multiplication

Given a sequence _A_<sub>1</sub>_,A_<sub>2</sub>_,...,A<sub>n</sub>_ of _n_ matrices, our goal is to compute the product \(A_1\times A_2\times\dots\times A_n\) in the most efficient way. Using the standard algorithm for multiplying pairs of matrices as a subroutine, this product can be found by a specifying the order which the matrices are multiplied together. This order is determined by a _full parenthesization_: A product of matrices is fully parenthesized if it is either a single matrix or the multiplication of two fully parenthesized matrix products surrounded by parentheses. For instance, there are five full parenthesizations of the product _A_<sub>1</sub>_A_<sub>2</sub>_A_<sub>3</sub>_A_<sub>4</sub>:

\((A_1(A_2(A_3A_4)))\)<br>
\((A_1((A_2A_3)A_4))\)<br>
\(((A_1A_2)(A_3A_4))\)<br>
\((((A_1A_2)A_3)A_4)\)<br>
\(((A_1(A_2A_3))A_4).\)

We consider the online version of _matrix-chain multiplication_ problem (Cormen et al., 2009). In each trial, the algorithm predicts with a full parenthesization of the product \(A_1\times A_2\times\dots\times A_n\) without knowing the dimensions of these matrices. Then the adversary reveals the dimensions of each _A<sub>i</sub>_ at the end of the trial denoted by \(d_{i-1}\times d_i\) for all \(i\in\{1..n\}\). The loss of the algorithm is defined as the number of scalar multiplications in the matrix-chain product in that trial. The goal is to predict with a sequence of full parenthesizations minimizing regret which is the difference between the total loss of the algorithm and the total loss of the single best full parenthesization chosen in hindsight. Observe that the number of scalar multiplications in the matrix-chain product cannot be expressed as a linear loss over the dimensions of the matrices _d<sub>i</sub>_’s.

### The Dynamic Programming Representation.

Finding the best full parenthesization can be solved via dynamic programming (Cormen et al., 2009). Each subproblem is denoted by a pair (_i,j_) for \(1\le i\le j\le n\), indicating the problem of finding a full parenthesization of the partial matrix product _A<sub>i</sub>...A<sub>j</sub>_. The base subproblems are (_i,i_) for \(1\le i\le n\) and the complete subproblem is (1_,n_). The dynamic programming for matrix chain multiplication uses the following min-sum recurrence:

\(\mathrm{OPT}(i,j)=\left\{\begin{array}{ c c }
0 & i=j \\
\mathrm{min}_{i\le k<j}\{\mathrm{OPT}(i,k)+\mathrm{OPT}(k+1,j)+d_{i-1}d_kd_j\} & i<j.
\end{array}\right.\)

This recurrence always recurses on 2 subproblems, thus for all multiedges \(m=(v,U)\in M\) we have |_U_|=2. The associated multi-DAG has the subproblems/vertices \(V=\{(i,j)|1\le i\le j\le n\}\), source _s_=(1_,n_) and sinks \(\mathcal{T}=\{(i,i)|1\le i\le n\}\). Also at node (_i,j_), the<tbc>

