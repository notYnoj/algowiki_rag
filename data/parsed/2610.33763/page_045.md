This construction can be extended to the multi-level setting by defining the multi- level generators for \(\mathbf{n}\in\mathbb{N}^d\) as

\(W_\mathbf{n}^{(1)}=W_{n_1}\otimes\left(\otimes_{l=2}^dI_{n_l}\right),W_\mathbf{n}^{(2)}=I_{n_1}\otimes W_{n_2}\otimes\left(\otimes_{l=3}^dI_{n_l}\right),\vdots W_\mathbf{n}^{(d)}=\left(\otimes_{l=1}^{d-1}I_{n_l}\right)\otimes W_{n_d}.\text{(3.5)}\)

Accordingly, a multi-level _r_-block \(\tau\) matrix admits the representation

\(S_{\mathbf{n},r}=\sum_{\mathbf{k}=\mathbf{0}}^{\mathbf{n}-\mathbf{1}}\left(W_{n_1}^{k_1}\otimes\cdots\otimes W_{n_d}^{k_d}\right)\otimes A_\mathbf{k},A_\mathbf{k}\in\mathbb{R}^{r\times r}.\)

Matrices _S_<sub>**_n_**_,r_</sub> that belong to the multi-level _r_-block \(\tau\) algebra are referred to as multi-level block \(\tau\) matrices.

## 3.4.1 Spectral properties and the discrete sine transform

In close analogy with the diagonalization theory for circulant matrices, \(\tau\) matrices can also be diagonalized by means of a related fast transform. More precisely, the Discrete Sine Transform (DST) is the linear mapping that associates with each vector \(\mathbf{x}\in\mathbb{C}^n\) the vector _Q<sub>n</sub>**x**_, where the matrix _Q<sub>n</sub>_, known as the sine transform matrix, is defined as

\(Q_n:=\sqrt{\frac{2}{n+1}}\left[sin\left(\frac{rs\pi}{n+1}\right)\right]_{r,s=1}^n.\)

It is closely connected to the Fast Sine Transform, which enables the DST to be computed in O(_n_log_n_) real arithmetic operations, requiring roughly half the computational cost of the well-known FFT \[138\]. The matrix _Q<sub>n</sub>_ is real, symmetric, and orthogonal. Its multilevel extension, for \(\mathbf{n}\in\mathbb{N}^d\), is defined as

\(Q_\mathbf{n}:=Q_{n_1}\otimes\cdots\otimes Q_{n_d},\)

and the _d_-level DST is given by the matrix-vector product _Q_**_<sub>n</sub>x_**, with \(\mathbf{x}\in\mathbb{C}^{N(\mathbf{n})}\). By exploiting the properties of the Kronecker product, it follows that _Q_**_<sub>n</sub>_** is a real, symmetric, and orthogonal matrix, and therefore \(Q_\mathbf{n}=Q_\mathbf{n}^T=Q_\mathbf{n}^{-1}\). Its _r_-block counterpart is defined as

\(Q_{\mathbf{n},r}:=Q_\mathbf{n}\otimes I_r,\)

which inherits the same properties, so that \(Q_{\mathbf{n},r}=Q_{\mathbf{n},r}^T=Q_{\mathbf{n},r}^{-1}\). As a consequence, we obtain the following spectral decomposition for multi-level block \(\tau\) matrices.

