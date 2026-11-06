Straightforward DP solves the LWS problem in _O(n_<sup>2</sup>) time. Since the input matrix _w_ has \(\Omega(n^2)\) entries, it requires quadratic time to read the input, so a faster algorithm isn’t possible in general. However, if the _w_ matrix is given in a smaller, compressed form, then one may hope for subquadratic-time algorithms.<sup>1</sup>

One example that \[KPS17\] focuses on is the case when _w_ is a low-rank matrix. If _w_ has rank _r\<n_<sup>_o_(1)</sup>, then one can be given as input matrices \(A,B\in\mathbb{R}^{n\times r}\) such that \(w=A\times B^T\), so the input size to the problem is only _n_<sup>1+_o_(1)</sup>.

Interestingly, Künnemann showed via fine-grained reductions that this problem is subquadratic-time _equivalent_ to the well-studied Min-IP problem for vectors of dimension _r_: Given as input \(x_1,\dots,x_n,y_1,\dots,y_n\in\mathbb{R}^r\), find the _x<sub>i</sub>,y<sub>j</sub>_ minimizing the inner product \(\langle x_i,y_j\rangle\). This problem can be solved in time _O(n_<sup>2-1_/r_</sup>) using geometric techniques \[Yao82, Mat91, AESW90\], and thus has a truly-subquadratic time algorithm whenever _r_ is a constant. On the other hand, it is known that assuming the Strong Exponential Time Hypothesis (SETH), the Min-IP problem requires time _n_<sup>2-_o_(1)</sup> even when _r_ is slightly super-constant _r_=2log<sup>∗</sup>_n_ \[Che20\], and thus the DP algorithm is essentially optimal. (Here log<sup>∗</sup> denotes the very slowly-growing iterated logarithm function.)

In this paper, we investigate the optimality of higher-dimensional DP formulations. We focus especially on generalizing LWS with low-rank matrices. As we will see, the known one-dimensional reductions do not generalize in a straightforward way, leading to a variety of generalizations and an intricate landscape of results. We will find that many classical higher-dimensional DP problems like the polygon triangulation problem are captured by our generalizations.

There are two choices to be made when generalizing LWS with low-rank matrices to higher dimensions: what is the higher-dimensional generalization of matrix rank (section 1.2) and what is the higher-dimensional generalization of the LWS recurrence (section 1.3).

## 1.2 Generalizations of matrix rank

The rank of a matrix has many equivalent definitions. However, when these definitions are generalized to higher-dimensional tensors, they lead to different notions. Prominent examples with applications in algebra, combinatorics, algorithm design, and complexity theory include the rank, subrank, border rank, slice rank, flattening rank, analytic rank, and geometric rank (see, e.g., \[OR20, KMZZ0\]). It is thus not clear, in general, which notion to use when generalizing results involving low-rank matrices.

We focus here on the two notions which arise naturally in known DP problems: tensor rank and slice rank.

### Tensor Rank

A _d_-dimensional (order-_d_) tensor \(w\in\mathbb{R}^{n_1\times n_2\times\cdots\times n_d}\) has rank 1 if there are vectors \(x_1\in\mathbb{R}^{n_1},\dots,x_d\in\mathbb{R}^{n_d}\) such that, for all \(i_1\in[n_1],\dots,i_d\in[n_d]\) we have \(w[i_1,\dots,i_d]=x_1[i_1]\cdot x_2[i_2]\cdots x_d[i_d]\). More generally, the rank of tensor _w_ is the minimum non-negative integer _k_ such that there are rank 1 tensors _w_<sub>1</sub>_,...,w<sub>k</sub>_ for which \(w=w_1+\cdots+w_k\). This notion is sometimes also called canonical polyadic decomposition (CPD) rank.

For instance, in the polygon triangulation discussed earlier, the tensor _w_ whose entry _w_\[_i,j,k_\] gives the weight of triangle (_i,j,k_) has rank 1 because the weight of the triangle (_i,j,k_) is \(w[i,j,k]=x_i\cdot x_j\cdot x_k\).

For another example, consider the airplane refueling problem: an airplane is traveling on a grid with dimension _k_ such that each point in the grid is a refueling airport. The airplane starts at location (1_,...,_1) and wants to arrive at location (_n,...,n_). The cost of flying from \((i_1,\dots,i_{\ell-1},j_\ell,i_{\ell+1},\dots,i_k)\) to (_i_<sub>1</sub>_,...,i<sub>k</sub>_) is \(w[i_1,\dots,i_k,j_\ell]\) (the airplane can only flies on the grid). The problem asks to minimize the cost of traveling.

<sup>1</sup>There has also been prior work on algorithms which assume _w_ has some additional structure which does not mean _w_ is compressible, but which lets one solve the problem without looking at most entries of _w_. For instance, \[HL87\] and \[Wil88\] give _O(n_log_n_) and _O(n_) time algorithms, respectively, for solving LWS with concave weights, i.e., when the entries of the matrix _w_ are promised to satisfy a quadrangle inequality. See also \[GG89, KK90, MM88\].

