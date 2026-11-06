## 2.3. Implementations

We begin by discussing the computation of YT **v** for any given vector **v**. Since T is a sparse matrix, computing the matrix-vector product T **v** only requires linear complexity of O(_mn_). As the action of Y is a simple reordering of entries that poses virtually no work, computing YT **v** needs the same complexity. Alternatively, due to the fact that T itself is a block Toeplitz matrix, it is well-known that T **v** (and hence YT **v**) can be computed in O(_mn_log_n_) operations using fast Fourier transforms and the required storage is of O(_mn_).

Now, we discuss how to efficiently invert \(\mathcal{P}_\alpha\), based on similar arguments discussed in, for instance, \[28, Section 4\]. The invertibility of \(\mathcal{P}_\alpha\) is guaranteed for \(\alpha\in(0,1)\), which will be proven in the next section. In each iteration of MINRES, it is required to compute \(\mathcal{P}_\alpha^{-1}\mathbf{y}=\mathcal{C}_\alpha^{-1/2}(\mathcal{C}_\alpha^{-1/2})^T\mathbf{y}\) for any given vector **y**.

Note that \(\mathcal{C}_\alpha\) is composed of the \(\alpha\)-circulant matrices \(B_j^{(\alpha)}=D_\alpha^{-1}\mathbb{F}^*\Lambda_{\alpha,j}\mathbb{F}D_\alpha\), _j_=1,2, where \(\Lambda_{\alpha,j}=\mathrm{diag}(\lambda_{j,k}^{(\alpha)})_{k=1}^n\) with \(\lambda_{1,k}^{(\alpha)}=1+\alpha^\frac{2}{n}\theta_n^{2(k-1)}\) and \(\lambda_{2,k}^{(\alpha)}=-2\alpha^\frac{1}{n}\theta_n^{k-1}\). Also, \(D_\alpha=\mathrm{diag}(\alpha^\frac{i-1}{n})_{i=1}^n\) and \(\mathbb{F}=\frac{1}{\sqrt{n}}[\theta_n^{(i-1)(j-1)}]_{i,j=1}^n\) with \(\theta_n=\mathrm{exp}(\frac{2\pi\mathbf{i}}{n})\) and \(\mathbf{i}=\sqrt{-1}\). Considering (1.6) and the eigendecomposition of \(L=U\Lambda U^T\), we have

\((\mathcal{C}_\alpha^{-1/2})^T=\big(\big(B_1^{(\alpha)}\otimes L+B_2^{(\alpha)}\otimes(-2I_m)\big)^{-1/2}\big)^T\)<br>
\(=\big(\big(D_\alpha^{-1}\mathbb{F}^*\Lambda_{\alpha,1}\mathbb{F}D_\alpha\otimes U\Lambda U^T+D_\alpha^{-1}\mathbb{F}^*\Lambda_{\alpha,2}\mathbb{F}D_\alpha\otimes(-2I_m)\big)^{-1/2}\big)^T\)<br>
\(=(D_\alpha^{-1}\mathbb{F}^*\otimes U)^{-T}\big(\big(\Lambda_{\alpha,1}\otimes\Lambda+\Lambda_{\alpha,2}\otimes(-2I_m)\big)^{-1/2}\big)^T(\mathbb{F}D_\alpha\otimes U^T)^{-T}.\)

Thus, the product \((\mathcal{C}_\alpha^{-1/2})^T\mathbf{y}\) for a given vector **y** can be implemented via the following three steps:

\(\text{Step 1: Compute}\widetilde{\mathbf{y}}=(\mathbb{F}D_\alpha\otimes U^T)^{-T}\mathbf{y};\)<br>
\(\text{Step 2: Compute}\widetilde{\mathbf{z}}=\big(\big(\Lambda_{\alpha,1}\otimes\Lambda+\Lambda_{\alpha,2}\otimes(-2I_m)\big)^{-1/2}\big)^T\widetilde{\mathbf{y}};\)<br>
\(\text{Step 3: Compute}\mathbf{z}=(D_\alpha^{-1}\mathbb{F}^*\otimes U)^{-T}\widetilde{\mathbf{z}}.\)

When the spatial grid is uniformly partitioned, the orthogonal matrix _U_ becomes a (multi- dimension) discrete sine transform matrix S. In this case, both Steps 1 & 3 can be computed efficiently via fast Fourier transforms and fast sine transforms in O(_mn_log_n_) operations. As for Step 2, the required computations take O(_nm_) operations since the matrix involved is a simple diagonal matrix.

In effect, the overall product \(\mathcal{P}_\alpha^{-1}\mathbf{y}=\mathcal{C}_\alpha^{-1/2}(\mathcal{C}_\alpha^{-1/2})^T\mathbf{y}\) can be computed by repeating the above three-step procedure two times.

In the case where the underlying differential equation involves variable coefficients, the implementation of our proposed preconditioner can be carried out in a similar way as in the constant-coefficient case. A related discussion will be given in Section 3.

