## 2 Problem Setup and Background

### 2.1 Optimization Problem

We consider the unconstrained non-convex optimization problem<tbc>

\(min_{\theta\in\mathbb{R}^p}f(\theta),\) (2)

<tbc>where \(f:\mathbb{R}^p\rightarrow\mathbb{R}\) is the VQA objective (1) representing the expectation value of a Hamiltonian _H_ with respect to a parameterized quantum state: \(f(\theta)=\langle 0|U^\dagger(\theta)HU(\theta)|0\rangle\). Here \(U(\theta)\) is a unitary operator parameterized by \(\theta\). The parameterized unitary takes the standard layered form

\(U(\theta)=\prod_{j=1}^PW_je^{-i\theta_jP_j/2},\) (3)

where _W<sub>j</sub>_ are fixed entangling unitaries and \(P_j\in\{I,X,Y,Z\}^{\otimes n}\) are Pauli-string generators satisfying \(P_j^2=I\) and \(\|P_j\|=1\). The function _f_ is treated as a black-box oracle, that is, we can query \(f(\theta)\) for any \(\theta\) via circuit execution and measurement, but we do _not_ have access to \(\nabla f(\theta)\).

### 2.2 The Gradient Estimation Challenge

The fundamental challenge in quantum optimization is that the gradient \(\nabla f(\theta)\) cannot be computed via backpropagation. Instead, one must rely on:

• **Parameter-Shift Rule (PSR)** \[Mitarai et al., 2018, Schuld et al., 2019\]: Computes \(\partial f/\partial\theta_j=\frac{1}{2}[f(\theta+\frac{\pi}{2}\mathbf{e}_j)-f(\theta-\frac{\pi}{2}\mathbf{e}_j)]\), requiring 2_p_ circuit evaluations per gradient, scaling as O(_p_).<tbc>

• **Simultaneous Perturbation Stochastic Approximation (SPSA)** \[Spall, 2002\]: Computes \(\hat{\mathbf{g}}=\frac{f(\theta+\nu\Delta)-f(\theta-\nu\Delta)}{2\nu}\Delta\) with \(\Delta\in\{-1,+1\}^p\) drawn uniformly and \(\nu>0\), requiring only O(1) circuit evaluations but introduces O(_p_) spatial variance \[Sweke et al., 2020, Gacon et al., 2021\].

### 2.3 The Bias-Throughput Trade-off

The current paradigm in Variational Quantum Algorithms is dominated by a pursuit of "unbiased" gradient estimators. This is standard in classical optimization, but in the noisy of NISQ devices, this pursuit has become a performance bottleneck. Classical variance reduction (e.g., SVRG \[Johnson and Zhang, 2013\] and SARAH \[Nguyen et al., 2017\]) suppresses estimator variance via periodic "snapshot" gradients and recursive tracking. However, the snapshot requires an exact full gradient, costing O(_p_) circuits. When the inner-loop estimator is two-sided symmetric, every recursive update requires four circuit evaluations, two for the current-step estimate and two for the other estimate, and no evaluation can be reused.

We propose a paradigm shift: by transitioning to a one-sided estimator, the circuit evaluation at the current parameter point \(f(\theta_t)\) appears explicitly in the estimator and can be cached and recycled across consecutive recursive steps. This center-point caching mechanism reduces the inner-loop cost from 4 to 3 circuits per step, a saving that compounds over the entire optimization trajectory.

## 3 The CRVG Algorithm

The Cached Recycled Variance-Reduced Gradient (CRVG) algorithm resolves a fundamental impasse in quantum optimization: how to achieve the tight variance control of classical variance-reduction methods without sacrificing the highly efficient O(1) circuit complexity of simultaneous perturbation.

We achieve this through a simple but powerful hardware-aware design principle called Temporal State Caching. By abandoning the traditional two-sided symmetric estimator in favor of a one-sided approach, CRVG exposes the unperturbed quantum state, allowing us to mathematically recycle expensive quantum measurements across optimization steps. Below, we formalize this mechanism and introduce two distinct routing paths: the Non-Recursive CRVG and the Recursive CRVG.

