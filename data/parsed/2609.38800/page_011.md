### 4.7 Intersection with the Barren Plateau Phenomenon

While the CRVG framework successfully breaks the dimensionality barrier in gradient estimation, it is critical to delineate its capabilities from the fundamental landscape challenges posed by Barren Plateaus (BPs). As comprehensively formalized by Larocca et al. Larocca et al. \[2025\], a barren plateau occurs when the true analytical gradient of the objective function vanishes exponentially with system size, rendering the optimization landscape featureless. This geometric flattening stems from architectural choices such as excessive circuit expressiveness, global measurements, or unmitigated hardware noise.

To properly contextualize CRVG within the broader quantum optimization stack, we highlight the following distinctions:

• **Estimator Variance vs. Landscape Geometry:** The CRVG algorithm is designed to actively suppress the statistical variance introduced by finite-shot measurement noise and simultaneous spatial perturbations. It ensures the optimizer can effectively "see" the gradient direction. Conversely, a barren plateau is an intrinsic geometric property of the landscape where the gradient itself is exponentially close to zero.<tbc>

• **The Impact of BPs on Sample Complexity:** If a Variational Quantum Algorithm (VQA) is initialized within a barren plateau, the true gradient magnitude \(\|\nabla f(\theta)\|\) shrinks exponentially. To capture this vanishing signal while maintaining the \(\mathcal{O}(1/\epsilon^3)\) convergence guarantee, the target accuracy \(\epsilon\) must also be scaled down exponentially. Because suppressing quantum shot noise inherently requires \(N=\mathcal{O}(1/\epsilon^2)\) measurements, a barren plateau forces the required shot count to explode, effectively neutralizing CRVG’s algorithmic efficiency.<tbc>

• **A Synergistic Application:** Consequently, CRVG is not a remedy for barren plateaus. Instead, it is an extraction engine designed to operate within trainable, BP-free regimes. Its theoretical guarantees implicitly rely on the prerequisite application of BP-mitigation strategies, such as bounding dynamical Lie algebras, employing shallow hardware-efficient ansatzes, or utilizing data-informed initialization.

Ultimately, once architectural safeguards secure a non-vanishing gradient landscape, the CRVG framework can be applied to suppress the remaining finite-shot noise and estimator variance. This ensures that the classical optimization routine does not re-introduce dimension-dependent O(_p_) bottlenecks into an otherwise trainable quantum system.

## 5 Numerical Experiments

We evaluate the methods through four questions: (i) how SPSA and the two CRVG variants behave on representative finite-shot MaxCut trajectories, (ii) whether the ranking persists across instances and circuit depths, (iii) whether reduced sampled-objective calls translate into comparable solution quality, and (iv) whether the same conclusions extend to maximum independent set (MIS). The aggregate evidence favors SPSA as the dependable default optimizer: it has the simplest evaluation pattern, remains competitive across ansatzes and depths, and avoids the pronounced depth- and variant-sensitivity observed for CRVG. CRVG nevertheless identifies useful operating regimes, which we report rather than treating any method as uniformly dominant. We use graph instances from the dataset provided by Daniel Eggar et al. \[Sack and Egger, 2024\].

### 5.1 Experimental setting and evidence base

The experiments compare SPSA with non-recursive (SVRG-style) and recursive (SARAH-style) CRVG. MaxCut studies use EfficientSU2 or QAOA circuits; the MIS depth study uses QAOA. The principal QAOA depth sweeps contain the same 36 graphs at depths one, three, five, and seven, with 256 shots per sampled-objective call and one optimizer seed per instance.  2 inventories the archived evidence. Statevector and matrix-product-state (MPS) simulations are computational evidence, not quantum-hardware execution.

A stored history point is not a circuit-evaluation count. SPSA evaluates the current point and two perturbations while its archived nominal counter advances by two; CRVG anchors and diagnostic evaluations have analogous accounting differences. We therefore reconstruct sampled-objective calls from optimizer control flow. Every reconstructed call in the depth studies invokes one 256-shot Aer sampler job. Wall time is specific to the archived simulator and host and is not used as a prediction of hardware latency.

3 summarizes the broad MaxCut comparisons. SPSA is competitive across both ansatzes: it wins 10 of 30 EfficientSU2 instances and 14 of 30 QAOA instances despite the table selecting the better of two CRVG variants against a single SPSA run. The near-zero QAOA median margin (-0.008) is especially important operationally because it indicates that the added CRVG machinery does not produce a broad quality separation in that setting. The clean and noisy rows contain different instances, so their medians are not paired estimates of a noise effect.

