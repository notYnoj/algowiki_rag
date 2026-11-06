**Proposition 1.** _Let_ \(A\in\mathbb{C}^{n\times n}\) _be Hermitian positive definite, and let_ \(\lambda_{max}\) _denote its largest eigenvalue. Then, for any real_ \(\sigma\ge 0\) _and any_ \(\mathbf{x}\in\mathbb{C}^n\)_, the following bound holds:_

\(\left\|A\left(\sigma I+A\right)^{-1}\mathbf{b}-\mathbf{Ax}\right\|_2\le\frac{1}{1+\sigma/\lambda_{max}}\left\|\mathbf{b}-\left(\sigma I+A\right)\mathbf{x}\right\|_2.\) (5)

_Proof._ By the definition of the induced operator norm, we have

\(\left\|A\left(\sigma I+A\right)^{-1}\mathbf{b}-\mathbf{Ax}\right\|_2=\left\|A\left(\sigma I+A\right)^{-1}\left(\mathbf{b}-\left(\sigma I+A\right)\mathbf{x}\right)\right\|_2\)<br>
\(\le\left\|A\left(\sigma I+A\right)^{-1}\right\|_2\left\|\mathbf{b}-\left(\sigma I+A\right)\mathbf{x}\right\|_2.\) (6)

For \(\lambda>0\), the scalar function \(f(\lambda)=\lambda/(\lambda+\sigma)\) is positive and increasing monotonically. Since _A_ is Hermitian positive definite, it follows that

\(\left\|A\left(\sigma I+A\right)^{-1}\right\|_2=max_{\lambda\in\sigma(A)}\frac{\lambda}{\lambda+\sigma}=\frac{\lambda_{max}}{\lambda_{max}+\sigma}=\frac{1}{1+\sigma/\lambda_{max}},\) (7)

where \(\sigma(A)\) denotes the spectrum (the set of eigenvalues) of _A_. Combining Equation (6) and (7) gives Equation (5).

The bound in Proposition 1 implies that the factor \(1/(1+\sigma/\lambda_{max})\) decreases as the shift parameter \(\sigma\) increases, leading to a tighter estimate in terms of the residual norm. Conversely, for small \(\sigma\), this factor approaches 1; the residual norm essentially acts directly as an upper bound for the error. This behavior is illustrated in Figure 1 with a concrete example involving a matrix _A_ that is the two-dimensional Laplacian discretized by the five-point centered difference scheme. As shown, the error is tightly bounded according to the proposed upper bound.

## 2.2. Derivation of a stopping criterion

As a corollary, we use Proposition 1 to derive a stopping criterion for the iterative solution at each quadrature node.

**Corollary 1.** _Let_ \(\alpha\in(0,1)\)_. For the kth shifted linear system_ \(\left(t_k^{1/\alpha} I+A\right)\mathbf{x}_k=\mathbf{b}\)_, let_ \(\tilde{\mathbf{x}}_k\) _be an approximate solution and define its residual as_ \(\mathbf{r}_k:=\mathbf{b}-\left(t_k^{1/\alpha} I+A\right)\tilde{\mathbf{x}}_k\)_. If, for all k_=1_,...,m,_

\(\left\|\mathbf{r}_k\right\|_2\le\frac{\epsilon}{2m}\frac{\alpha\pi}{sin(\alpha\pi)}\frac{1+t_k^{1/\alpha}/\lambda_{max}}{w_k},\) (8)

_then, the integrand evaluation error is bounded by_ \(\epsilon/2\).

