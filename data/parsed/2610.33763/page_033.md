are (_d_-1)-level _r_-block Toeplitz matrices. In this recursive design, the blocks in the first block row and first block column of the matrix tell you everything you need to know about it, just like in the case of a single-level matrix. From the computational perspective, this makes the storage requirement for Toeplitz matrices drop to only _O(N_(**_n_**)_r_<sup>2</sup>), compared to \(O\big(\big(\)(_N_(**_n_**)_r_)<sup>2</sup>\(\big)\) for a generic dense matrix.<br>
A compact expression for a multi-level block Toeplitz matrix can be formulated by defining, for \(n\in\mathbb{N}\) and \(k\in\mathbb{Z}\), define the matrix \(J_n^{(k)}\in\mathbb{R}^{n\times n}\) by<tbc>

\([J_n^{(k)}]_{i,j}:=\delta_{i-j,k}=\left\{\begin{array}{ c c }
1, & i-j=k, \\
0, & \text{otherwise},
\end{array}\right.i,j=1,\dots,n,\)

<tbc>where \(\delta_{p,q}\) is the Kronecker delta, i.e.<tbc>

\(\delta_{p,q}=\left\{\begin{array}{ c c }
1, & p=q, \\
0, & p\neq q.
\end{array}\right.\)

<tbc>Equivalently, \(J_n^{(k)}\) is a matrix with all ones on the _k_-th diagonal and zeros elsewhere. The main diagonal is numbered as 0, diagonals above as -1,-2_,...,-n_+1, and those below as 1,2_,...,n_-1. For the multi-level case, where \(\mathbf{n}\in\mathbb{N}^d\) and \(\mathbf{k}\in\mathbb{Z}^d\), are both _d_-dimensional vectors (for example, **_n_**=(_n_<sub>1</sub>_,...,n<sub>d</sub>_) and **_k_**=(_k_<sub>1</sub>_,...,k<sub>d</sub>_)), we define its multi-level version:<tbc>

\(J_\mathbf{n}^{(\mathbf{k})}=J_{n_1}^{(k_1)}\otimes J_{n_2}^{(k_2)}\otimes\cdots\otimes J_{n_d}^{(k_d)}.\)

<tbc>Then, _T_**_n_** admits the following representation:<tbc>

\(T_\mathbf{n}=[A_{\mathbf{i}-\mathbf{j}}]_{\mathbf{i},\mathbf{j}=\mathbf{1}}^\mathbf{n}=\sum_{\mathbf{k}=\mathbf{1}-\mathbf{n}}^{\mathbf{n}-\mathbf{1}}J_\mathbf{n}^{(\mathbf{k})}\otimes A_\mathbf{k}.\) (3.1)

<tbc>It can be proven componentwise by explicitly computing the (**_i_**_,**j**_)-th block on the right-hand side of the equation and applying the properties of the Kronecker product.<br>
Given a matrix-valued function \(f:[-\pi,\pi]^d\rightarrow\mathbb{C}^{r\times r}\) belonging to the space of integrable functions \(L^1([-\pi,\pi]^d)\), that is, such that all its entries are in \(L^1([-\pi,\pi]^d)\), it is possible to construct a class of multi-level block Toeplitz matrices associated with _f_. Let \(\hat{f}_\mathbf{k}\) denote the **_k_**-th Fourier coefficient of _f_, defined for any \(\mathbf{k}\in\mathbb{Z}^d\) as<tbc>

\(\hat{f}_\mathbf{k}:=\frac{1}{(2\pi)^d}\int_{[-\pi,\pi]^d}f(\theta)e^{-i\mathbf{k}\cdot\theta} d\theta\in\mathbb{C}^{r\times r},\)

<tbc>where _i_<sup>2</sup>=-1 and \(\mathbf{k}\cdot\theta=k_1\theta_1+\cdots+k_d\theta_d\), the integral being computed entrywise. For any \(\mathbf{n}\in\mathbb{N}^d\), the **_n_**-th Toeplitz matrix associated with _f_ is the _d_-level _r_-block Toeplitz matrix, denoted by _T_**_n_**(_f_), whose blocks are the Fourier coefficients of _f_, arranged along the block diagonals according to the following definition:<tbc>

\(T_\mathbf{n}(f):=[\hat{f}_{\mathbf{i}-\mathbf{j}}]_{\mathbf{i},\mathbf{j}=\mathbf{1}}^\mathbf{n}\in\mathbb{C}^{N(\mathbf{n})r\times N(\mathbf{n})r}.\)

<tbc>The family \(\{T_\mathbf{n}(f)\}_{\mathbf{n}\in\mathbb{N}^d}\) is called the family of (multi-level block) Toeplitz matrices associated with _f_, which is referred to as the _generating function_. Using Equation (3.1), _T_**_n_**(_f_) can also be represented as<tbc>

\(T_\mathbf{n}(f)=\sum_{\mathbf{k}=\mathbf{1}-\mathbf{n}}^{\mathbf{n}-\mathbf{1}}J_\mathbf{n}^{(\mathbf{k})}\otimes\hat{f}_\mathbf{k}=\sum_{k_1=1-n_1}^{n_1-1}\cdots\sum_{k_d=1-n_d}^{n_d-1}\big(J_{n_1}^{(k_1)}\otimes\cdots\otimes J_{n_d}^{(k_d)}\big)\otimes\hat{f}_{(k_1,\dots,k_d)}.\)

