More explicitly,<tbc>

\(Z_n^2=\left[\begin{array}{ c c c c c c c }
0 &  &  &  & 1 & 0 &  \\
0 & \ddots &  &  &  &  & 1 \\
1 & \ddots & \ddots &  &  &  &  \\
 & \ddots & \ddots & \ddots &  &  &  \\
 &  & \ddots & \ddots & \ddots &  &  \\
 &  &  & 1 & 0 & 0
\end{array}\right],Z_n^3=\left[\begin{array}{ c c c c c c c }
0 &  &  &  & 1 & 0 & 0 \\
0 & \ddots &  &  &  & 1 & 0 \\
0 & \ddots & \ddots &  &  &  & 1 \\
1 & \ddots & \ddots & \ddots &  &  &  \\
 & \ddots & \ddots & \ddots & \ddots &  \\
 &  &  & 1 & 0 & 0 & 0
\end{array}\right],\cdots\)

<tbc>Hence, any uni-level _r_-block circulant matrix can be expressed as a linear combination of Kronecker products of these powers with the blocks _A<sub>k</sub>_:<tbc>

\(C_{n,r}=\sum_{k=0}^{n-1}Z_n^k\otimes A_k.\) (3.2)

<tbc>Conversely, since \(Z_n^n=I_n\) and, more generally, \(Z_n^k=Z_n^k\mathrm{mod}n\) for any \(k\in\mathbb{Z}\), any finite sum of the form

\(\sum_{k\in K}Z_n^k\otimes A_k,A_k\in\mathbb{C}^{r\times r},K\subset\mathbb{Z},\)

is an _r_-block circulant matrix. For this reason, _Z<sub>n</sub>_ is commonly referred to as the generator of circulant matrices of order _n_.<br>
The multi-level generalization of circulant matrices is straightforward. For \(\mathbf{n}\in\mathbb{N}^d\) and \(\mathbf{k}\in\mathbb{Z}^d\), we define<tbc>

\(Z_\mathbf{n}^\mathbf{k}:=Z_{n_1}^{k_1}\otimes Z_{n_2}^{k_2}\otimes\cdots\otimes Z_{n_d}^{k_d}.\)

<tbc>Using this definition, any multi-level block circulant matrix can be written as

\(C_{\mathbf{n},r}=\sum_{\mathbf{k}=\mathbf{0}}^{\mathbf{n}-\mathbf{1}}Z_\mathbf{n}^\mathbf{k}\otimes A_\mathbf{k}.\)

This formula is directly analogous to the uni-level case and demonstrates that, just as for classic circulant matrices, the structure of multi-level block circulant matrices is fully captured by these shift matrices and the set of blocks _A<sub>k</sub>_.

## 3.2.1 Spectral structure and fast solvers for circulant matrices

Circulant matrices are widely used in numerical analysis due to their deep connection with the Discrete Fourier Transform (DFT) and, consequently, with the Fast Fourier Transform (FFT). Recall that the DFT is the linear mapping that associates to a vector \(\mathbf{x}\in\mathbb{C}^n\) its product with the Fourier matrix _F<sub>n</sub>_, namely _F<sub>n</sub>**x**_. The FFT is an efficient algorithm for computing the DFT in O(_n_log_n_) operations, in contrast to the O(_n_<sup>2</sup>) operations required by a standard matrix–vector multiplication \[138\]. The fact that block circulant matrices are uniformly block-diagonalizable by the Fourier matrix makes them particularly attractive for practical applications.<br>
We start by introducing the Fourier matrix of order \(n\in\mathbb{N}\):

\(F_n:=\frac{1}{\sqrt{n}}\left[e^{-2\pi i\frac{rs}{n}}\right]_{r,s=0}^{n-1}\in\mathbb{C}^{n\times n},i=\sqrt{-1}.\) (3.3)

