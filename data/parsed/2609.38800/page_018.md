## Appendix

## A Derivation of Baseline Sample Complexity

We start with the following lemma.

**Lemma 4** (Total Finite-Shot Variance of the PSR Estimator)**.** Let \(\hat{g}\) be the stochastic gradient vector estimated via the exact Parameter-Shift Rule, where each shifted circuit is evaluated using a finite number of measurement shots _N_. The total variance of the PSR gradient vector strictly scales as O(_p/N_). Consequently, for a constant shot allocation _N_=O(1), the total spatial variance is \(\sigma_{PSR}^2=\mathcal{O}(p)\).

_Proof._ By definition, the total variance of the stochastic gradient vector \(\hat{g}\in\mathbb{R}^p\) is the trace of its covariance matrix, which corresponds to the expected squared Euclidean distance from the true analytical gradient \(\nabla f(\theta)\):<tbc>

\(\sigma_{PSR}^2=\mathbb{E}\left[\|\hat{g}-\nabla f(\theta)\|^2\right]=\sum_{j=1}^p\text{Var}(\hat{g}_j)\) (24)

<tbc>For each coordinate \(j\in\{1,\dots,p\}\), the PSR estimator computes the partial derivative as:

\(\hat{g}_j=\frac{1}{2}\left(\hat{f}\left(\theta+\frac{\pi}{2}e_j\right)-\hat{f}\left(\theta-\frac{\pi}{2}e_j\right)\right)\) (25)

where \(\hat{f}(\cdot)\) is the empirical expectation value obtained from _N_ independent measurement shots. The variance of any finite-shot quantum expectation value is bounded by \(\frac{\|H\|^2}{N}\) . Because the hardware measurements for the positive and negative shifts are statistically independent, the variance of a single estimated coordinate is:

\(\text{Var}(\hat{g}_j)=\frac{1}{4}\left[\text{Var}\left(\hat{f}\left(\theta+\frac{\pi}{2}e_j\right)\right)+\text{Var}\left(\hat{f}\left(\theta-\frac{\pi}{2}e_j\right)\right)\right]\le\frac{1}{4}\left[\frac{\|H\|^2}{N}+\frac{\|H\|^2}{N}\right]=\frac{\|H\|^2}{2N}\) (26)

Because the Hamiltonian norm \(\|H\|\) is a physical constant bounded by the spectral properties of the target observable, the variance of each individual coordinate scales strictly as O(1_/N_).

Substituting this coordinate-wise bound back into the total vector variance equation yields:

\(\sigma_{PSR}^2=\sum_{j=1}^p\text{Var}(\hat{g}_j)\le\sum_{j=1}^p\frac{\|H\|^2}{2N}=\frac{p\|H\|^2}{2N}\) (27)

Therefore, if the optimization trajectory utilizes a constant, hardware-efficient shot allocation _N_=O(1) for each circuit execution, the total variance of the PSR vector scales linearly with the dimension of the parameter space, \(\sigma_{PSR}^2=\mathcal{O}(p)\).

To establish the baseline sample complexities for the Parameter-Shift Rule (PSR) and Simultaneous Perturbation Stochastic Approximation (SPSA) presented in  1, we rely on the standard convergence results for non-convex Stochastic Gradient Descent (SGD) \[Ghadimi and Lan, 2013\] and the formal variance properties of quantum gradient estimators \[Sweke et al., 2020\].

For a generic non-convex objective function, standard SGD requires \(T=\mathcal{O}(\sigma^2/\epsilon^4)\) iterations to converge to an \(\epsilon^2\)-stationary point (where \(\mathbb{E}[\|\nabla f(\theta)\|^2]\le\epsilon^2\)), with \(\sigma^2\) representing the total variance of the gradient estimator. The total sample complexity C is strictly the product of the number of iterations _T_ and the inner-loop circuit evaluation cost per step.

### A.1 Parameter-Shift Rule (PSR)

The PSR estimator computes the analytic gradient coordinate-by-coordinate. When evaluated under finite-shot noise using O(1) measurements per circuit, the independent shot noise accumulates across the parameter vector. As established in Lemma 3, the total variance of the PSR estimator scales linearly with the dimension: \(\sigma_{PSR}^2=\mathcal{O}(p)\).

• **Iteration Complexity:** Given the total variance \(\sigma^2=\mathcal{O}(p)\), the number of SGD iterations required to converge is \(T_{PSR}=\mathcal{O}(p/\epsilon^4)\).<tbc>

• **Inner-Loop Cost:** PSR requires exactly 2_p_ distinct circuit evaluations per gradient step.<tbc>

• **Total Sample Complexity:**<tbc>

\(\mathcal{C}_{PSR}=T_{PSR}\times 2p=\mathcal{O}\left(\frac{p}{\epsilon^4}\right)\times\mathcal{O}(p)=\mathcal{O}\left(\frac{p^2}{\epsilon^4}\right).\) \(\text{(28)}\)

