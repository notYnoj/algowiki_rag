To minimize the total execution cost with respect to the epoch length _m_, we balance the two terms, yielding \(m=\mathcal{O}\left(\frac{p}{\epsilon^2}\right)\). Substituting this back into the complexity equation produces the theoretical optimal cost:

\(\mathcal{C}_{rec}=\mathcal{O}\left(\frac{\sqrt{p/\epsilon^2}}{\epsilon^2}\right)=\mathcal{O}\left(\frac{\sqrt{p}}{\epsilon^3}\right)\) (23)

**Conclusion**. By replacing the computationally heavy analytical PSR anchor, which would require \(\mathcal{O}(p^2/\epsilon^2)\) circuit executions to suppress finite-shot noise, with a stochastic zeroth-order mini-batch, CRVG drops the anchor evaluation cost to strictly \(\mathcal{O}(p/\epsilon^2)\). Because the physical outer loop requires \(S\ge 1\), the algorithm must evaluate this anchor batch at least once, creating a fundamental execution floor of \(\mathcal{O}(p/\epsilon^2)\). Therefore, the rigorously bounded total sample complexities across all regimes of _p_ and \(\epsilon\) to reach an exact \(\epsilon^2\)-stationary point are:

• **Non-Recursive CRVG:** \(\mathcal{O}\left(max\left\{\frac{p}{\epsilon^2},\frac{p^{2/3}}{\epsilon^{10/3}}\right\}\right)\)<tbc>

• **Recursive CRVG:** \(\mathcal{O}\left(max\left\{\frac{p}{\epsilon^2},\frac{\sqrt{p}}{\epsilon^3}\right\}\right)\)

This formally proves the mathematical separation between the two variance-reduced routing paths. By successfully controlling the spatial variance without inflating the inner loop, the fully recursive variant achieves theoretical scaling for deep quantum circuits.

## 4.6 Complexity Comparison and Theoretical Advantages

To contextualize the theoretical contributions of the CRVG framework, we benchmark its oracle complexity against the standard gradient estimation techniques utilized in Variational Quantum Algorithms (VQAs).  1 summarizes the per-step inner-loop circuit cost, the estimator spatial variance, and the total sample complexity required to converge to an \(\epsilon^2\)-stationary point (where \(\mathbb{E}[\|\nabla f(\theta)\|^2]\le\epsilon^2\)).

**The Dimensionality Barrier in Standard Methods:**<br>
As shown in  1, existing NISQ optimization techniques fail to decouple the total sample complexity from the parameter dimension _p_. The Parameter-Shift Rule (PSR) evaluates an unbiased analytic gradient, but its structural requirement to evaluate 2_p_ distinct circuit configurations per step, combined with the O(_p_) accumulated shot variance across the vector, yields a massive total sample complexity of \(\mathcal{O}(p^2/\epsilon^4)\). Conversely, simultaneous perturbation methods like SPSA successfully reduce the per-step execution cost to an optimal O(1) constant. However, this per-step efficiency is immediately undermined by a severe spatial variance penalty that scales linearly with the circuit depth, O(_p_). Overcoming this injected variance necessitates significantly more optimization steps, ultimately yielding an asymptotic sample complexity of \(\mathcal{O}(p/\epsilon^4)\).

**The Theoretical Separation of CRVG Routing Paths:**<br>
Our proposed CRVG framework strictly dominates the existing baselines by utilizing a 1-sided estimator with Center- Point Caching, dropping the inner-loop circuit cost to exactly 3 while maintaining a tightly bounded spatial variance of O(1). Furthermore,  1 exposes a critical theoretical separation between our two variance-reduced routing paths:

• **Non-Recursive CRVG:** While strictly improving upon standard SPSA, the non-recursive variant is structurally bottlenecked by its restrictive learning rate limitations, mathematically capping its sample complexity at \(\mathcal{O}(max\{p/\epsilon^2,p^{2/3}/\epsilon^{10/3}\})\).<tbc>

• **Recursive CRVG:** The recursive variant strictly dominates the non-recursive baseline. By leveraging a history-dependent update, the recursive framework permits a more aggressive learning rate, accelerating convergence with respect to dimensionality and improving it to a complexity of \(\mathcal{O}(max\{p/\epsilon^2,\sqrt{p}/\epsilon^3\})\).<tbc>

\begin{tabular}{cccc}
**Optimization Algorithm** & **Inner Cost** & **Spatial Variance** & **Total Sample Complexity** \\
Parameter-Shift Rule (PSR) & 2_p_ & O(_p_) & \(\mathcal{O}\left(\frac{p^2}{\epsilon^4}\right)\) \\
Standard SPSA & O(1) & O(_p_) & \(\mathcal{O}\left(\frac{p}{\epsilon^4}\right)\) \\
**Non-Recursive CRVG (Ours)** & 3 & O(1) & \(\mathcal{O}\left(max\left\{\frac{p}{\epsilon^2},\frac{p^{2/3}}{\epsilon^{10/3}}\right\}\right)\) \\
**Recursive CRVG (Ours)** & 3 & O(1) & \(\mathcal{O}\left(max\left\{\frac{p}{\epsilon^2},\frac{\sqrt{p}}{\epsilon^3}\right\}\right)\) \\
\end{tabular}

1: Comparison of sample complexities to achieve an \(\epsilon^2\)-stationary point. Here, _p_ denotes the number of parameterized gates, and the target accuracy bounds the expected squared norm of the gradient.

