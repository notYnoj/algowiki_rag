### Algorithms and Exploration Parameter Tuning

We evaluate three variations of our 1-bit algorithm--FIXEDCLIP, RESTARTPHASE, and REUSEPHASE--against the full-feedback UGAPE baseline.

In practice, theoretically derived confidence intervals can be overly conservative. For the empirical comparison, we introduce a constant exploration multiplier to the leading confidence radius term. For the 1-bit algorithms, this is implemented as an `exploration` parameter that directly scales the logarithmic \(x_n(\gamma)\) term within the tail-integral confidence bounds.

The exploration parameters were tuned as follows:

• **FIXEDCLIP**: The exploration parameter was tuned to 0.04 for the Bernoulli environment and 0.05 for the Normal and Student-t environments.<tbc>

• **RESTARTPHASE & REUSEPHASE**: The exploration parameter was consistently set to 0.03 across all three environments.<tbc>

• **UGAPE Baseline**: The exploration constant _c_ scaling the empirical Bernstein/Hoeffding radius was tuned per environment to 0.06 for Bernoulli, 0.0002 for Normal, and 0.0005 for Student-t.

### UGAPE Modifications for Unbounded Support

For bounded-support environments (e.g., Bernoulli), the UGAPE baseline uses the raw full-feedback rewards. However, for unbounded- support environments (such as the Normal and Student-t settings), the UGAPE baseline is modified to include finite-variance clipping. In these unbounded settings, it still receives full continuous feedback, but it clips every observed reward around the arm’s anchor using the same fixed clipping scale _L_ as the FIXEDCLIP algorithm. The corresponding finite-variance clipping bias is then explicitly added to the algorithm’s confidence radius.

The reported empirical error frequencies remain at or below the target \(\delta\) in the tested configurations. Reducing the exploration multipliers below their theorem values and imposing the experimental query cap do not preserve the proved PAC guarantee automatically. These results are empirical assessments of the tuned implementations; Theorems 8 and 10 concern the stated, untuned confidence radii and stopping rules.

### F.4 Compute resources

All numerical simulations were executed on a dedicated Linux workstation equipped with an Intel(R) Core(TM) Ultra 9 285K processor (24 cores, up to 5.1 GHz) and 128 GB of RAM.

In terms of computational cost, the standalone 1-bit mean estimation experiments required approximately 40 minutes of total execution time. The best-arm identification (BAI) experiments are more computationally intensive due to the adaptive sampling and large number of Monte Carlo iterations (5000 runs per configuration); each BAI experiment (Bernoulli, Normal, and Student-t) required approximately 10 hours to complete.

