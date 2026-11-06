the independence of the computations at the different quadrature nodes makes these methods well suited to parallel implementation.

Existing research into quadrature-based algorithms \[5, 4, 6\] typically focuses on the quadrature discretization error, with the assumption that the integrand can be computed exactly. However, when using an iterative method such as the shifted conjugate gradient (Shifted CG) method \[7\] for computing \((t^{1/\alpha} I+A)^{-1}b\), the integrand is not computed exactly. The resulting error must therefore be considered. An unanswered question is how the stopping criterion in iterative methods should be set at each quadrature node.

In this paper, we analyze the integrand evaluation error for the case where _A_ is Hermitian positive definite. We propose a stopping criterion for an iterative method for solving linear systems in the integrand at each quadrature node. First, we derive an upper bound on the integrand evaluation error using the residuals of approximate solutions to the linear systems \((t_k^{1/\alpha} I+A)^{-1}b\). This allows the integral evaluation error to be estimated both theoretically and numerically. We hence propose the stopping criterion for an iterative method for each linear system to compute \(A^\alpha b\) with the prescribed accuracy.

The remainder of this paper is organized as follows. Section 2 analyzes the error arising from the inexact evaluation of the integrand. A practical stopping criterion for the iterative solver is devised such that the overall approximation meets a prescribed tolerance condition. Section 3 reports numerical experiments that illustrate the effectiveness of the proposed error-control technique. Finally, Section 4 finishes with concluding remarks.

## 2. Error Analysis and Control

In this section, we analyze the integrand evaluation error and propose a stopping criterion of an iterative method for solving \((t_k^{1/\alpha} I+A)^{-1}b\) that guarantees a prescribed overall error condition.

Two sources of error arise when computing \(A^\alpha b\) via Equation (2): the discretization error due to numerical quadrature and the error in evaluating the integrand at each quadrature node. Taking the exact value of the integrand contribution at the _k_th node as<tbc>

\(g_k:=\frac{sin(\alpha\pi)}{\alpha\pi}w_kA\left(t_k^{1/\alpha} I+A\right)^{-1}b,\)

<tbc>and its computed approximation denoted \(\tilde{g}_k\), the total error can be decomposed as

\(\left\|A^\alpha b-\sum_{k=1}^m\tilde{g}_k\right\|_2\le\underbrace{\left\|A^\alpha b-\sum_{k=1}^mg_k\right\|_2}_\text{quadrature error}+\underbrace{\left\|\sum_{k=1}^mg_k-\sum_{k=1}^m\tilde{g}_k\right\|_2}_\text{intrand evaluation error}\) (3)

where \(\|\cdot\|_2\) denotes the vector 2-norm (Euclidean norm).

To bound the total error by a tolerance level \(\epsilon\), we control the first term (quadrature error) and the second term (intrand evaluation error) on the right-hand side of Equation (3) so that neither of these quantities exceeds \(\epsilon/2\). The quadrature error was previously analyzed using the GJ quadrature \[5, 4\] and the DE formula \[6, 8\]. Therefore, we focus on controlling the integrand evaluation error so that it is bounded by \(\epsilon/2\).

### 2.1. Estimating the integrand evaluation error

To ensure that the total integrand evaluation error is no greater than \(\epsilon/2\), it suffices, by the triangle inequality, to bound the error at each quadrature node by \(\epsilon/(2m)\):<tbc>

\(\left\|\sum_{k=1}^mg_k-\sum_{k=1}^m\tilde{g}_k\right\|_2\le\sum_{k=1}^m\|g_k-\tilde{g}_k\|_2\le\frac{\epsilon}{2}.\)

<tbc>It therefore suffices to enforce, for each _k_=1_,...,m_, the condition

\(\|g_k-\tilde{g}_k\|_2\le\frac{\epsilon}{2m}.\) (4)

We present the following proposition to estimate the error at each quadrature node. The error in computing \(A(\sigma I+A)^{-1}b\) is estimated using an approximate solution \(\tilde{x}\) of the shifted linear system \((\sigma I+A)x=b\) expanded in terms of the residual norm \(\|b-(\sigma I+A)\tilde{x}\|_2\).

