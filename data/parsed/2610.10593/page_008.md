\(\tau_0=2.37116\), the augmented-Lagrangian objective minimized during the final continuation is

\(\mathcal{L}(x;\lambda,\rho)=C-E_2(x)-\sum_{t\in\{0,4,3\}}\overline{R_t}(x)-\tau_0M(x)+\langle\lambda,h(x)\rangle+\frac{\rho}{2}\|h(x)\|_2^2.\) (17)

The average-role expression is a search surrogate. It agrees with the retained exponent only when _h_=0; otherwise it can overestimate the retained exponent. No conclusion about \(\omega\) is drawn from this surrogate alone, and equality of the roles is not a hypothesis of the certified construction.

After each outer pass, the multipliers are updated by \(\lambda\leftarrow\lambda+\rho h\). The penalty starts at \(\rho=20\) and is doubled after every fourth pass if \(\|h\|_\infty>2\cdot 10^{-7}\). The final continuation starts from a previously obtained point with minimum-based objective approximately 2.371161129895562, taking multipliers from the preceding continuation and resetting the penalty to 20. It consists of 20 outer passes, each with an inner iteration limit of 500, and records 10087 objective-and-gradient evaluations. The numerical computations use double precision, automatic differentiation in JAX, and SciPy’s L-BFGS-B implementation [5], without explicit bounds on the transformed coordinates.

## 3.2 Mass-dependent conditioning of quasi-Newton steps

The occurrence masses and local probabilities vary substantially in magnitude. The source of the scale mismatch can already be seen in a local term _mg(p_) with softmax probabilities _p_, holding its incoming mass _m_ fixed: its logit gradient is<tbc>

\(\frac{\partial(mg(p))}{\partial z_i}=mp_i\left(\frac{\partial g}{\partial p_i}-\sum_jp_j\frac{\partial g}{\partial p_j}\right).\)

<tbc>Small masses, and often small probabilities, suppress these coordinate gradients. This motivates a diagonal rescaling using mass and probability weights, also suggested by the corresponding Fisher- information scales. At the beginning of an outer pass, let _x_<sup>(0)</sup> be the current parameter vector. Optimize in coordinates _y_ defined by

\(x=x^{(0)}+Sy,S_{ii}=clip_{[0.03,10^6]}\left(max\{w_i,10^{-14}\}^{-1/2}\right).\) (18)

The weight _w<sub>i</sub>_ is the current occurrence mass times the appropriate local probability: orbit mass for a free complete split distribution, region weight for region logits, and region weight times split probability for split logits. Root logits use their root probabilities. For a dual marginal coordinate of marginal probability _p_, the weight is the occurrence and region mass times _p_(1-_p_). A leaf-\(\mu\) logit uses its occurrence mass. This is a diagonal conditioning rule, not an exact natural-gradient method. The scale is held fixed throughout each inner solve and recomputed between outer passes.

Each inner solve uses L-BFGS history length 40, function tolerance 10<sup>-15</sup>, gradient tolerance 10<sup>-9</sup>, and a line-search limit of 35. Relative to the preceding continuation, the scale cap is increased from 10<sup>5</sup> to 10<sup>6</sup>, the mass floor is decreased from 10<sup>-12</sup> to 10<sup>-14</sup>, and the history length is increased from 30 to 40. These changes concern numerical conditioning only; they do not alter the admissible tensor family.

## 3.3 Balancing extraction bottlenecks with six controls

The bottleneck gap in (16) motivates a correction that acts directly on the six role differences, even though the full parameter vector has 212820 coordinates. After every second outer pass, this<tbc>

