For the diagonal elements (_j=k_), the derivation yields \(|H_{jj}|\le\|H\|\) similarly.

Thus, the Hessian \(\nabla^2f(\theta)\) is a \(p\times p\) real symmetric matrix where every entry is bounded in absolute value by \(\|H\|\). By standard matrix norm inequalities, the spectral norm \(\|\nabla^2f(\theta)\|_2\) is bounded by the Frobenius norm \(\|\nabla^2f(\theta)\|_F\):

\(\|\nabla^2f(\theta)\|_2\le\|\nabla^2f(\theta)\|_F=\sqrt{\sum_{j=1}^p\sum_{k=1}^p|H_{jk}|^2}\le\sqrt{p^2\|H\|^2}=p\|H\|.\) (35)

This means \(f(\theta)\) is globally _L_-smooth, where \(L=p\|H\|\). This completes the proof.

## B.2 Proof of Theorem 1

_Proof._ We prove the theorem as follows.

**Step 1: The Taylor Expansion (Integral Form)**

To understand the function’s behavior when perturbed by \(\nu\Delta\), we begin with the exact Taylor expansion utilizing the integral remainder:

\(f(\theta+\nu\Delta)=f(\theta)+\nu\nabla f(\theta)^\top\Delta+\int_0^1(1-\tau)\nu^2\Delta^\top\nabla^2f(\theta+\tau\nu\Delta)\Delta d\tau\) (36)

**Step 2: Constructing the 1-Sided Estimator**

The standard 1-sided estimator is defined as:

\(g(\theta,\Delta)=\frac{f(\theta+\nu\Delta)-f(\theta)}{\nu}\Delta\) (37)

Subtracting \(f(\theta)\) from both sides of the Taylor expansion, dividing by \(\nu\), and multiplying by the perturbation vector \(\Delta\) yields the expanded form of our estimator:

\(g(\theta,\Delta)=(\nabla f(\theta)^\top\Delta)\Delta+\nu\int_0^1(1-\tau)(\Delta^\top\nabla^2f(\theta+\tau\nu\Delta)\Delta)\Delta d\tau\) (38)

**Step 3: Extracting the True Gradient (The First Term)**

To find the expected value of the estimator, \(\bar{g}(\theta)\), we take the expectation \(\mathbb{E}_\Delta\) over the random vector \(\Delta\). For a Rademacher vector \(\Delta\), the components are independent, yielding a covariance matrix \(\mathbb{E}[\Delta\Delta^\top]=I\). Thus, evaluating the first term:

\(\mathbb{E}_\Delta[(\nabla f(\theta)^\top\Delta)\Delta]=\mathbb{E}_\Delta[\Delta\Delta^\top\nabla f(\theta)]=I\nabla f(\theta)=\nabla f(\theta)\) (39)

This proves the first term perfectly recovers the true analytical gradient.

**Step 4: Bounding the Bias (The Second Term)**

Because the first term is exactly \(\nabla f(\theta)\), any difference between the expected estimator \(\bar{g}(\theta)\) and the true gradient \(\nabla f(\theta)\) stems entirely from the second term (the integral). This difference is the estimator’s bias:

\(\bar{g}(\theta)-\nabla f(\theta)=\mathbb{E}_\Delta\left[\nu\int_0^1(1-\tau)(\Delta^\top\nabla^2f(\theta+\tau\nu\Delta)\Delta)\Delta d\tau\right]\) (40)

To find the maximum possible bias, we bound the norm of this expectation using three critical properties:

1. _Smoothness Guarantee:_ By Lemma 1, the spectral norm of the Hessian \(\nabla^2f\) is globally bounded by \(p\|H\|\). Therefore, the quadratic form inside the integral is bounded: \(\Delta^\top\nabla^2f(x)\Delta\le p\|H\|\|\Delta\|^2\).<tbc>

2. _Rademacher Norm:_ Since \(\Delta\) has _p_ components and each component is either 1 or -1, the squared norm is exactly the dimension: \(\|\Delta\|^2=p\). This bounds the quadratic form by \(p^2\|H\|\).<tbc>

3. _Evaluating the Integral:_ The deterministic part of the integral evaluates directly as \(\int_0^1(1-\tau)d\tau=\left[\tau-\frac{\tau^2}{2}\right]_0^1=\frac{1}{2}\).<tbc>

<tbc>Combining these bounds isolates the magnitude of the bias:

\(\|\bar{g}(\theta)-\nabla f(\theta)\|\le\nu\cdot p\|H\|\cdot p\cdot\int_0^1(1-\tau)d\tau=\frac{\nu p^2\|H\|}{2}\) (41)

This establishes the strict analytical bias bound, completing the proof.

