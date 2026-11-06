achieves a lower MAE. For Student-_t_ and exponential distributions, our method reaches a lower asymptotic error floor due to its smaller true deterministic bias at the same clipping/truncation level. Under this calibration, the bias term is practically significant and our estimator has lower MAE and clipping bias. The signed-estimate standard deviations are also smaller ( 2); these empirical differences do not imply a rate separation.

### 5.2 1-bit best-arm identification

We evaluate the empirical performance of our proposed 1-bit best-arm identification algorithms across three distinct experimental setups. To analyze the sample complexity and safety of each approach, the confidence parameter \(\delta\) is varied from 0.01 to 0.5. We compare three variations of our 1-bit algorithm--FIXEDCLIP, RESTARTPHASE, REUSEPHASE--against the full real-valued-feedback UGAPE baseline of Gabillon et al. [7]. Appendix F.3 gives the full setup, query cap, and exploration tuning. The tuned implementations are assessed empirically.

Figure 2 illustrates the stopping round as a function of \(\delta\) across the three experimental settings. The performance gap between the 1-bit algorithms and the unquantized baseline is most significant in the Bernoulli environment and relatively smaller in the Normal and Student-t settings. When gaps are uniform, as in the Bernoulli test where \(\Delta_k\) is identical for all suboptimal arms, the three 1-bit algorithms perform similarly because no arms can be eliminated early at coarser resolutions. However, in the Normal and Student-t settings where \(\Delta_k\) varies, the phased adaptive-clipping algorithms demonstrate a clear advantage by eliminating arms with larger gaps much earlier than the fixed-clipping approach.

## 6 Conclusion

We introduced a fixed-confidence best-arm identification framework for finite-variance, 1-bit feedback environments. Using a novel randomized-threshold mean estimator, we developed a baseline fixed- clipping algorithm alongside a gap-adaptive phased alternative which achieves worst-case optimality up to loglog factors. Addressing current limitations offers clear avenues for future work. First, our algorithms rely on an localization assumption; developing methods that weaken or remove this requirement is an important next step. Second, our analysis currently relies on a K-arm worst-case lower bound, leaving the exact instance-dependent complexity of 1-bit BAI open. Finally, extending our time-uniform 1-bit primitive to broader pure-exploration tasks presents an exciting direction for communication-constrained learning.

## Acknowledgments

We thank Prof. Jonathan Scarlett for his helpful comments and suggestions.

