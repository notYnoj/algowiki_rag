**5. Conclusion.** We analyzed sequences of SPD linear systems in which spectral information from a reference matrix _A_ with simple eigenvalues is reused for a perturbed matrix _A(t_)=_A+tE_. Our comparison considered deflated CG and PCG equipped with a scaled spectral preconditioner constructed from the same selected eigenvectors of _A_.

An energy-norm characterization of deflated CG, combined with first-order perturbation analysis, yields an asymptotic comparison of the two methods. After one additional PCG iteration, the squared PCG error is bounded, up to higher-order perturbation terms, by an explicit multiple of the squared deflated CG error. The analysis also motivates the scaling parameter \(\theta_m\). Numerical experiments show that the scaled spectral preconditioner closely reproduces the convergence of deflated CG while avoiding the construction of the deflation projector and its associated products with the perturbed matrix. PCG with this preconditioner is therefore a promising alternative to deflation for sequences of closely related large-scale systems.

An important direction for future work is to extend the perturbation analysis to SPD matrices with multiple eigenvalues. We also fix the perturbation direction _E_ and vary only its magnitude _t_; allowing _E_ to vary and deriving bounds over a class of symmetric perturbations would yield a more general analysis.

## REFERENCES

