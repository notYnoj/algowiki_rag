function of a \(3\times 3\) matrix is a quadratic polynomial in it (Eq. 13), so the evolution operator in constant-density matter is fixed once the three eigenvalues are known, and the Vandermonde system (Eq. 15) is nothing more than the bookkeeping that makes this concrete. From there the DMP rotation reads naturally as a resummation rather than an approximation: it eliminates the near-degenerate eigenvalue behind the \(\hat{A}\rightarrow 1\) divergence and replaces the unbounded \((1-\hat{A})^{-1}\) with the bounded \(\epsilon_0\le 0.015\) (Eq. 46). The same operator language carries the wave-packet analysis, which puts the matter- dressed coherence lengths in the 10<sup>4</sup>-10<sup>6</sup>km range and hence _L/L_<sub>coh</sub> at the 10<sup>-3</sup>-10<sup>-2</sup> level--decoherence is small, though by a more modest margin than is sometimes assumed. Finally, the closed-form Jacobians in the NuFIT 6.0 basis (Eqs. 51-56) make linearized uncertainty propagation a matter of one matrix product, with Feldman-Cousins held in reserve for the boundaries where the Gaussian picture breaks.

We are not proposing a replacement for NuFast-LBL. For the O(10<sup>6</sup>)-O(10<sup>7</sup>) evaluations a production fit demands, the Denton-Parke algorithm [44] is the right choice and we say so plainly. The analytic route earns its place elsewhere: where one wants continuity in every parameter, limits that can be read off by hand, and Jacobians that propagate correlated uncertainties in closed form. Those are the demands of interpretation and validation, not of likelihood minimization, and that is the work this framework is meant for.

The extensions to non-standard interactions and sterile-neutrino su(4) topologies follow the same algebraic logic, with the Cayley-Hamilton polynomial rising to cubic order for the \(4\times 4\) case. As DUNE, HK, and JUNO approach their design sensitivities, the interplay between matter effects, CP violation, and parameter degeneracies will require exactly the kind of algebraic transparency this framework is designed to provide.

## Acknowledgements

We thank the NuFIT collaboration for maintaining their publicly accessible global fit at `nu-fit.org`, and Peter Denton and Stephen Parke for making the NuFast-LBL code and the _Looking Glass_ comparison publicly available. The experimental work of the Super- Kamiokande, SNO, KamLAND, Daya Bay, T2K, and NOvA collaborations underpins every quantitative statement here. We express our deepest gratitude to Professor Takaaki Kajita for his invaluable guidance and thorough reviews, which significantly shaped and refined this manuscript into its final form.

### Funding.

This research received no specific funding from public, commercial, or not- for-profit agencies.

### Data Availability.

The NuFIT 6.0 parameters and covariance are available at `http:// www.nu-fit.org`. The NuFast-LBL code is available at `https://github.com/PeterDenton/ NuFast-LBL`.

### Conflicts of Interest.

The authors declare no competing interests.

## References

