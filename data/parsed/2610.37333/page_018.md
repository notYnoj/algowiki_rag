<tbc>seed [67]. Unrolled, the loop is a chain of accepted steps, and each step is an implicit function of the parameters and of the _k_ stored history states, because the corrector equation _G<sub>n</sub>(y_<sub>_n_+1</sub>)=0 inherits the stored states through the multistep formula and the parameters through the right-hand side. Rather than naively differentiating through the Newton algorithm, we apply the implicit function theorem at the converged root [49, 85], which turns the constant mass matrix step dependence into the tangent recurrence

\(W_n\dot{y}_{n+1}=\frac{\partial f}{\partial\theta}\dot{\theta}-\frac{1}{\gamma_n}M\sum_{j=1}^k\alpha_j\dot{y}_{n+1-j},\) (12)

where _W<sub>n</sub>_ is the exact pencil of Eq. (4) evaluated at the root, the first term carries the direct parameter dependence, and the sum carries the stored history tangents into the new step. To ensure the correctness of the derivative, a fresh pencil matrix _W<sub>n</sub>_ and factorization must be used at an extra computational cost rather than the potentially stale factor used by the forward program. We employ the frozen-controller approximation, such that we apply gradient truncation to the adaptive order and step size control flow. Instead, tangents differentiate the realized control schedule as a fixed discretization [49]. Because forward mode AD carries one tangent per seed, the cost retains the \(O(n_\theta T(n))\) scaling of FSA. To reduce practical cost, we leverage the shared pencil factorization to efficiently batch the tangent computation at each step.

For systems with many parameters, such as training modern deep neural networks, the \(O(n_\theta T(n))\) scaling of the forward methods renders differentiation practically infeasible. Fortunately, reverse-mode and adjoint methods compute the gradient of a scalar cost directly, at a cost that no longer multiplies in \(n_\theta\). In the continuous setting, adjoint sensitivity analysis introduces the costate \(\lambda(t)\in\mathbb{R}^n\) and, for a constant mass matrix and a cost of integral form \(\mathcal{L}=\int_{t_0}^{t_f}g(y,\theta,t)dt\), integrates the adjoint system backward from _t<sub>f</sub>_,<tbc>

\(M^T\lambda'=-\frac{\partial f}{\partial y}^T\lambda-\frac{\partial g}{\partial y}^T,\lambda(t_f)=0,\) (13)

<tbc>after which the gradient follows from the quadrature

\(\frac{d\mathcal{L}}{d\theta}=\int_{t_0}^{t_f}\big(\frac{\partial g}{\partial\theta}+\lambda^T\frac{\partial f}{\partial\theta}\big)dt+\lambda(t_0)^TM\frac{\partial y_0}{\partial\theta},\) (14)

