Last but not least, many computations involving block circulant matrices can be significantly accelerated by using the FFT. The computational cost of the matrix-vector product _C_<sub>**_n_**_,r_</sub>**_x_**, where \(\mathbf{x}\in\mathbb{C}^{N(\mathbf{n})r}\), is reduced from the conventional \(O\big((N(\mathbf{n})r)^2\big)\) operations necessary for dense matrices to only \(O\big(rN(\mathbf{n})logN(\mathbf{n})+r^2N(\mathbf{n})\big)\) operations, by using the following approach:

1. Compute \(\mathbf{y}=F_{\mathbf{n},r}^*\mathbf{x}\) via the FFT applied to each of the _r_ components, in _O(rN_(**_n_**)log_N_(**_n_**)) flops;<tbc>

2. Compute \(\mathbf{z}=\Lambda_{\mathbf{n},r}\mathbf{y}\), that is, _N_(**_n_**) products of size _r_, in _O(r_<sup>2</sup>_N_(**_n_**)) flops;<tbc>

3. Compute _F_<sub>**_n_**_,r_</sub>**_z_** via the FFT, in _O(rN_(**_n_**)log_N_(**_n_**)) flops.

In the same way, \(C_{\mathbf{n},r}^{-1}\mathbf{x}\) can be computed as \(F_{\mathbf{n},r}\Lambda_{\mathbf{n},r}^{-1}F_{\mathbf{n},r}^*\mathbf{x}\), where the inversion of \(\Lambda_{\mathbf{n},r}\) amounts to solving _N_(**_n_**) independent linear systems of size _r_. Similar techniques apply to the most relevant matrix operations, such as matrix-matrix products, matrix inversion, the solution of linear systems, and the computation of the spectrum, which makes block circulant matrices exceptionally efficient and powerful in practical applications. For a fixed _r_, all the above costs reduce to _O(N_(**_n_**)log_N_(**_n_**)), with a hidden constant depending on _r_.

**Remark 3.1** _This algorithm can be adapted to accommodate general multi-level block Toeplitz matrices through the use of an immersion (or embedding) technique. The central idea is to embed the original Toeplitz matrix into a larger block circulant matrix, and then perform the matrix-vector multiplication using the circulant structure as described above. The required result is then obtained by appropriately extracting the relevant portion from the output. By adopting this strategy, the computational complexity of the block Toeplitz matrix-vector product is also reduced to O(rN_(**_n_**)log_N_(**_n_**)+_r_<sup>2</sup>_N_(**_n_**)).

**Remark 3.2** _Finally, it is important to note that each step of the process is fully parallelizable. Therefore, in a parallel model of computation, the theoretical computational cost of all the aforementioned algorithms can be further reduced to O_(log_N_(**_n_**))_, for a fixed block size r._

## 3.3 \(\omega\)-circulant matrices

By introducing a parameter \(\omega\in\mathbb{C}\backslash\{0\}\), the class of uni-level circulant matrices can be extended to the so-called \(\omega\)_-circulant matrices_. In this thesis, we restrict our attention to the uni-level case and do not consider multi-level \(\omega\)-circulant matrices. These matrices have the following structure:

\([C_n^{\omega]}_{i,j}:=\left\{\begin{array}{ c c }
a_{(i-j)modn} & \text{if}i>j, \\
\omega a_{(i-j)modn} & \text{if}i\le j,
\end{array}\right.i,j=1,\dots,n.\)

where \(a_k\in\mathbb{C}\) for _k_=0_,...,n_-1. Here, the parameter \(\omega\) acts as a scaling factor for certain matrix entries, setting these matrices apart from the standard circulant case.

