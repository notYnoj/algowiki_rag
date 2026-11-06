## Approximate Implicit Gradient (AI).

Our goal is to approximate the gradient \(\frac{\partial\theta^*}{\partial X}(X)\) at a fixed point \(\theta^*\) of \(F(\cdot,X)\). Thanks to the differentiability property of Proposition 2.1 and under Assumption 1, we can differentiate with respect to _X_ using the chain rule:

\(\frac{\partial\theta^*}{\partial X}(X)=\frac{\partial}{\partial X}[F(\theta^*,X)]=\frac{\partial F}{\partial\theta}(\theta^*,X)\frac{\partial\theta^*}{\partial X}(X)+\frac{\partial F}{\partial X}(\theta^*,X).\) (7)

We deduce the following equation on \(\frac{\partial\theta^*}{\partial X}(X)\):

\(\left(I-\frac{\partial F}{\partial\theta}(\theta^*,X)\right)\frac{\partial\theta^*}{\partial X}(X)=\frac{\partial F}{\partial X}(\theta^*,X),\) (8)

using Assumption 1 again, we can invert the matrix on the left hand-side, yielding

\(\frac{\partial\theta^*}{\partial X}(X)=\left(I-\frac{\partial F}{\partial\theta}(\theta^*,X)\right)^{-1}\frac{\partial F}{\partial X}(\theta^*,X).\) (9)

We define the approximate implicit gradient by approximating \(\theta^*\approx\theta_T\):

\(J_\text{AI}:=\left(I-\frac{\partial F}{\partial\theta}(\theta_T,X)\right)^{-1}\frac{\partial F}{\partial X}(\theta_T,X)\) (10)

The implicit approximation is theoretically exact (barring numerical imprecision in the inversion in particular) when \(\theta_T=\theta^*\), however it requires additional costly computations: first evaluate the differential \(\partial_\theta F(\theta_T,X)\), and then solve a large linear system to compute \((I-\partial_\theta F(\theta^*,X))^{-1}\partial_XF(\theta^*,X)\).

## One-Step Gradient Approximation (OS).

The One-Step method (OS) studied in \[BPV24\] (within a particular framework of bi-level optimisation), works under the following condition:

**Condition 1.** \(\left\|\frac{\partial F}{\partial\theta}(\theta,X)\right\|_\text{op}\le\rho\checkmark 1\) for any \(\theta,X\).

In the case of the EM algorithm, Condition 1 is not verified, since the eigenvalues of the partial differential \(\frac{\partial F}{\partial\theta}(\theta,X)\) are commonly larger than 1, even in the neighbourhood of a fixed point. Under Condition 1, the OS approximation further neglects the term \((I-\partial_\theta F(\theta^*,X))^{-1}\) in Eq. (10), yielding the following expression:

\(J_\text{OS}:=\frac{\partial F}{\partial X}(\theta_{T-1},X)\approx\frac{\partial F}{\partial X}(\theta^*,X)\approx\left(I-\frac{\partial F}{\partial\theta}(\theta^*,X)\right)^{-1}\frac{\partial F}{\partial X}(\theta^*,X)=\frac{\partial\theta^*}{\partial X}(X).\) (11)

In practice, the OS method corresponds to computing the gradient of the EM output \(\theta_T(X)=F_X^T(\theta_0)\) with respect to the data _X_ only through the last iteration \(\theta_T(X)=F_X(\theta_{T-1})\), neglecting the dependence of the penultimate iteration \(\theta_{T-1}\) on _X_. Using automatic differentiation (for example with PyTorch \[Pas+19\]), this is done conveniently by computing \(\theta_{T-1}=F_X^{T-1}(\theta_0)\) without gradient computation (e.g. `with torch.no\_grad()`), and performing the last step with gradient computation. Due to this computation method, the OS gradient is numerically inexpensive compared to the others, albeit at the expense of precision. See \[BPV24\] for a detailed presentation.

## Time complexity and memory footprint.

The complexities of the gradient computation approaches are summarised in  1. As a baseline, the time complexity of the `forward` pass (EM algorithm without gradients) is O\(\big(\)_T(nKd_<sup>2</sup>+_Kd_<sup>3</sup>)\(\big)\), while its memory footprint is O(_Kd_<sup>2</sup>+_nd_). The complexities are deduced from the differential expressions in Appendix A.6. The O(_Kd_<sup>3</sup>) factor corresponds to inverting the _K_ covariance matrices of size \(d\times d\) during each E-step. The O(_nKd_<sup>2</sup>) factor comes from the M-step parameter updates (weights, means, covariances) and the differentiation of these updates with respect to _X_ or \(\theta\).

