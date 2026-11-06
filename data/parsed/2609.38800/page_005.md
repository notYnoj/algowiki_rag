## 3.1 The 1-Sided Estimator and Center-Point Caching

For a given parameter point \(\theta\in\mathbb{R}^p\) and a random perturbation vector \(\Delta\in\{-1,+1\}^p\) drawn uniformly (i.e., each component is an independent Rademacher random variable) and \(\nu>0\), we define the _1-sided (forward) simultaneous perturbation gradient estimator_:

\(g(\theta,\Delta):=\frac{f(\theta+\nu\Delta)-f(\theta)}{\nu}\Delta.\) (4)

Historically, the quantum computing community has favored the 2-sided symmetric estimator, \(\frac{f(\theta+\nu\Delta)-f(\theta-\nu\Delta)}{2\nu}\Delta\), to eliminate first-order bias. However, the symmetric estimator shifts in both directions, leaving the actual center point \(\theta\) unmeasured.

The 1-sided estimator requires exactly two circuit evaluations (one at \(\theta+\epsilon\Delta\) and one at \(\theta\)), but it possesses a critical structural advantage: the center-point evaluation \(f(\theta)\) appears explicitly. This explicitness enables our core mechanism, as the center-point can be evaluated once, stored in classical memory, and reused. How this caching manifests depends on the chosen variance-reduction routing path:

• **Anchor Caching (Non-Recursive CRVG):** The tracking signal relies on a fixed epoch anchor. We evaluate the anchor’s center-point \(f(\theta_0)\) exactly once at the start of the epoch and cache it for the entirety of the inner loop.<tbc>

• **Trajectory Caching (Recursive CRVG):** The tracking signal relies on the immediate previous step. We dynamically cache the current center-point \(f(\theta_t)\) at step _t_ so that it serves as the required previous center-point \(f(\theta_{t-1})\) for step _t_+1.

By intentionally extracting and caching these exact measurements in classical memory, we entirely eliminate the need to re-evaluate them on the quantum hardware during the inner loop.

### The 25% Efficiency Guarantee.

In a standard zeroth-order variance-reduction framework, computing the tracking signal requires two finite-difference gradient estimates along a shared random direction \(\Delta\): one at the current point \(\theta_t\), and a reference estimate at either the previous point \(\theta_{t-1}\) (Recursive) or the static anchor point \(\theta_0\) (Non-Recursive). A naive 1-sided implementation requires 4 distinct circuit executions per step: \(f(\theta_t)\), \(f(\theta_t+\nu\Delta)\), \(f(\theta_\mathrm{ref})\), and \(f(\theta_\mathrm{ref}+\nu\Delta)\), where \(\theta_\mathrm{ref}\in\{\theta_{t-1},\theta_0\}\).

With Temporal State Caching, we recognize that the reference expectation value \(f(\theta_\mathrm{ref})\) was already physically evaluated either dynamically in the previous iteration or statically at the epoch start. By recalling this "center-point" directly from classical memory, we only need to execute the two newly perturbed circuits plus the new center-point \(f(\theta_t)\) (which is then cached for the subsequent step). This mathematical recycling drops the inner-loop circuit cost from 4 to exactly 3, yielding a strict 25% reduction in quantum hardware utilization.

Consequently, when utilizing a stochastic mini-batch of size _B_ for the anchor gradient over an outer loop of _S_ epochs with an inner loop length of _m_, the total number of distinct circuit configurations is evaluated as:

• **Anchor evaluation:** _S(B_+1) circuits (evaluating one shared anchor center point and _B_ independent stochastic perturbations at the start of each epoch).<tbc>

• **Inner loop:** 3_Sm_ circuits (exactly 3 per inner step via center-point caching).<tbc>

• **Total structural cost:** _S(B_+1+3_m_) distinct circuit configurations.

## 3.2 Variant 1: 3-Circuit Non-Recursive CRVG

The Non-Recursive CRVG variant utilizes an SVRG-type update rule \[Johnson and Zhang, 2013\]. It anchors the variance reduction to a fixed snapshot parameter, \(\theta_0^{(s)}\), which is evaluated once at the beginning of the epoch. The non-recursive tracking estimator is defined as:

\(v_t=g(\theta_t,\Delta_t)-g(\theta_0^{(s)},\Delta_t)+v_0^{(s)}.\) (5)

By caching the anchor evaluation \(f(\theta_0^{(s)})\) for the entire duration of the epoch, we repeatedly recycle this baseline measurement against the shifting inner-loop parameters, significantly compounding our hardware savings.

