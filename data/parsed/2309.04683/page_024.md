It is natural to consider the case where we are allowed to have multiple locations to put the boxes, which motivates our multiple nested boxes problem.

**Definition 5.5** (Multiple Nested Boxes)**.** _Given n boxes in d dimension of size_ (_b_<sub>1</sub>_,...,b<sub>d</sub>_) _and k piles, find the maximum number of boxes we can use such that each in each pile, each box fits into the next (without rotation). We say that box a of size_ (_a_<sub>1</sub>_,...,a<sub>d</sub>_) _fits into box b of size_ (_b_<sub>1</sub>_,...,b<sub>d</sub>_) _if_ \(a_i\le b_i\) _for all_ \(1\le i\le d\).

**Theorem 5.6.** _Multiple nested boxes with k dimension can be solved in time_ \(O(n^{k+1-\varepsilon})\) _for some_ \(\varepsilon>0\).

_Proof._ We first sort all the boxes by their volume in increasing order _B_<sub>1</sub>_,...,B<sub>n</sub>_, and let

\(w_\ell[i_1,\dots,i_k,j]=\left\{\begin{array}{ c c }
-1 & \text{if}B_j\text{fits into}B_{i_\ell} \\
0 & \text{otherwise.}
\end{array}\right.\)

To see that this indeed solves multiple nested boxes, we claim that -_T_\[_i_<sub>1</sub>_,...,i<sub>k</sub>_\] is the maximum number of boxes over all assignments such that the rank of the outer box in _t_-th pile is at most _i<sub>t</sub>_. This will solve the multiple nested boxes when _i_<sub>1</sub>=_...=i<sub>k</sub>=n_+1.

We proceed by induction. When _i_<sub>1</sub>=_...=i<sub>k</sub>_=1, we have _T_\[_i_<sub>1</sub>_,...,i<sub>k</sub>_\]=0. There is no box with rank 0 so we cannot put any boxes. Now for general (_i_<sub>1</sub>_,...,i<sub>k</sub>_), by recurrence we have

\(T\big[i_1,\dots,i_k\big]=min_{1\le\ell\le k}\big\{min_{1\le j_\ell<i_\ell}\big\{T\big[i_1,\dots,i_{\ell-1},j_\ell,i_{\ell+1},i_k\big]+w_\ell\big[i_1,\dots,i_k,j_\ell\big]\big\}\big\}.\)

For any assignment (_u_<sub>1</sub>_,...,u<sub>k</sub>_) to the piles such that the _t_-th pile outer box has rank \(u_t\le i_t\), it can be achieved from adding \(B_{u_\ell}\) to the assignment \((u_1,\dots,u_{\ell-1},u'_\ell,u_{\ell+1},\dots,u_k)\) with the guarantee that \(B_{u_\ell^\prime}\) fits inside \(B_{u_\ell}\). This case is covered by the right-hand-side of the equation because by induction hypothesis,

\(-T\big[u_1,\dots,u_{\ell-1},u'_\ell,u_{\ell+1},\dots,u_k\big]-w_\ell\big[u_1,\dots,u_k,u'_\ell\big]\)

is the maximum over the assignments under this procedure.

Therefore, right-hand-side of the equation is exactly all possible ways to achieve the assignment (_u_<sub>1</sub>_,...,u<sub>k</sub>_) such that \(u_t\le i_t\) for all _t_, so our kD LWS instance indeed solves the multiple nested boxes with _k_ dimension. In addition, notice that \(w_\ell\) only depends on its \(\ell\)-th and last coordinate, so it can be expressed as a matrix. The same reasoning in Theorem 3.6 shows that it can be reduced to \[Static\](k-1)D LWS with rank 1, which implies that it can be solved in time \(O(n^{k+1-\varepsilon})\) for some \(\varepsilon>0\).

## 6 Applications of 2D LWS<sup>PT</sup>

In section 4, we showed we can solve polygon triangulation and 2D LWS<sup>PT</sup> with different tensors. In this section, we discuss more applications of 2D LWS<sup>PT</sup>.

### 6.1 Matrix-Chain Multiplication

The matrix-chain multiplication problem was introduced in \[God73\] and is defined as follows:

**Definition 6.1** (Matrix-Chain Multiplication)**.** _Given a chain of n matrices A_<sub>1</sub>_,...,A<sub>n</sub> where matrix A<sub>i</sub> has dimension_ \(d_{i-1}\times d_i\)_, find the order of matrix multiplications which minimizes the number of scalar multiplications using the straightforward matrix multiplication algorithm._

Recall that multiplying an \(n\times m\) matrix by an \(m\times p\) matrix using the straightforward algorithm uses \(n\cdot m\cdot p\) scalar multiplications. Moreover, the order in which you multiply a chain of matrices determines the number of scalar multiplications performed. For instance, consider three matrices _A_<sub>1</sub>_,A_<sub>2</sub>_,A_<sub>3</sub> with dimensions (10,20), (20,30), and (30,40) respectively. Multiplying (_A_<sub>1</sub>_,A_<sub>2</sub>)_A_<sub>3</sub> takes \((10\cdot 20\cdot 30)+(10\cdot 30\cdot 40)=\)<tbc>

