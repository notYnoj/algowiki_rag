block case. For \(n,r\in\mathbb{N}\), we define an _r_-block \(\omega\)-circulant matrix \(C_{n,r}^\omega\in\mathbb{C}^{nr\times nr}\) as follows:<tbc>

\(\left[C_{n,r}^\omega\right]_{i,j}:=\left\{\begin{array}{ c c }
A_{(i-j)\mathrm{mod}n} & \text{if}i>j, \\
\omega A_{(i-j)\mathrm{mod}n} & \text{if}i\le j,
\end{array}\right.i,j=1,\dots,n,\)

<tbc>where \(A_k\in\mathbb{C}^{r\times r}\) for _k_=0_,...,n_-1 are _n_ general (not necessarily structured) matrices. Explicitly:<tbc>

\(C_{n,r}^\omega=\left[\begin{array}{ c c c c c c c c }
A_0 & \omega A_{n-1} & \omega A_{n-2} & \cdots & \cdots & \omega A_1 \\
A_1 & A_0 & \omega A_{n-1} & \omega A_{n-2} & & \vdots \\
A_2 & A_1 & \ddots & \ddots & \ddots & \vdots \\
\vdots & A_2 & \ddots & \ddots & \ddots & \omega A_{n-2} \\
\vdots & & \ddots & \ddots & \ddots & \omega A_{n-1} \\
A_{n-1} & \cdots & \cdots & A_2 & A_1 & A_0
\end{array}\right].\)

<tbc>A compact representation for \(C_{n,r}^\omega\) is given by<tbc>

\(C_{n,r}^\omega=\sum_{j=0}^{n-1}(Z_n^\omega)^j\otimes A_j.\)

<tbc>Moreover, \(C_{n,r}^\omega\) can be block-diagonalized as<tbc>

\(C_{n,r}^\omega=F_{n,r}^\omega\Lambda_{n,r}^\omega(F_{n,r}^\omega)^{-1},\)

<tbc>where<tbc>

\(F_{n,r}^\omega:=F_n^\omega\otimes I_r,\)

<tbc>and<tbc>

\(\Lambda_{n,r}^\omega:=\mathrm{diag}_{j=0,\dots,n-1}\left(p\left(\frac{2\pi j}{n}\right)\right)\)

<tbc>with

\(p(\theta):=\sum_{k=0}^{n-1}\omega^\frac{k}{n}A_ke^{ik\theta}\in\mathbb{C}^{r\times r}.\)

Note that \(C_{n,r}^\omega\) is not a two-level \(\omega\)-circulant matrix, since the matrices _A<sub>k</sub>_ do not necessarily possess a specific structure and the function \(p(\theta)\) is an \(r\times r\) matrix rather than a scalar. Nevertheless, when _r_ is a fixed integer, the matrix-vector product can still be computed in O(_n_log_n_) floating-point operations in a sequential setting, or in O(log_n_) steps in a parallel computational model, where the hidden constant in the O-notation depends on _r_. If _r_ varies and tends to infinity and each inner matrix _A<sub>k</sub>_ admits a diagonalization with cost O(_r_log_r_), then the overall computational cost becomes O(_nr_log(_nr_)) flops in the sequential case, or O(log(_nr_)) parallel steps. For a review on recent applications concerning _r_-block \(\omega\)-circulant structures, refer to \[31\] and references therein.

