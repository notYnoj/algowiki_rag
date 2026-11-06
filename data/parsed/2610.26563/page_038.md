apply this to all three factors. The leading coefficients \(\sigma_0\) are as in Definition 25:

where \(\sigma(\Xi(\lambda))=\sigma_0\lambda^{-h}(1+O(\lambda))\). The constructions are due to \[7, 30, 34\]. In particular, the leading Smirnov factor norms are \(\sqrt{6+\sqrt{5}}\lambda^{-2}\), \(\sqrt{5}\lambda^{-2}\), and \(\sqrt{12}\lambda^{-2}\), while its first residual coefficient is nonzero.

Spectral norms multiply under tensor products. Consequently, _k_ direct levels have norm product \(\sigma(\Xi(\lambda))^k\) and limiting fraction 1/(1+_kh_). The cyclic product of three Bini rectangular steps gives _b_=12, _r<sub>b</sub>_=1000, _h_=3, and \(\theta=1/4\). One Schönhage square step gives \(\theta=1/3\). An exact algorithm for the remaining subproblems contributes a \(\lambda\)-independent norm product, preserving these limiting fractions. With its count modeled by LITA’s exponent \(\omega_L=\mathrm{log}_{32}14197\), one approximate square step has comparison curve

\(\xi(1,q,r_b(q/b)^{\omega_L})=\frac{b^3}{r_b}(q/b)^{3-\omega_L},q\ge b.\) (172)

Its ratio to the LITA curve is \(b^{\omega_L}/r_b\). Changes of basis can alter the norm products at fixed rank \[4, 21, 19\].

## C Further bounds for square-product constructions

This appendix collects the weighted comparison, accuracy coefficients, integer-dimension comparisons, and a shared-variable square-product construction.

### C.1 Weighted and centered comparison counts

For a complete fixed-shape family S, apply (96) to the scaled blocks. By (87), only the desired products and B(S) remain, giving

\(\Phi_\mathcal{S}^\mathrm{wt}(\lambda)=\phi_\mathcal{S}+\sum_{(i,j,k)\in\mathcal{B}(\mathcal{S})}\lambda^{a_i+b_j+c_k}\phi_{ijk},R(\Phi_\mathcal{S}^\mathrm{wt}(\lambda))\le(n+2)^d.\) (173)

For a conflict-free family this is exact. Otherwise the positive powers give a degeneration. Since the weighted embedding is independent of \(\lambda\), normalized exponents of height _h_ give approximation error of order \(\lambda\) and \(\sigma(\Xi(\lambda))\) of Definition 24 of order \(\lambda^{-h}\). For balanced parts, its exact ratio \(\sigma(\Xi(\lambda))/\sigma_c\) is the upper-bound expression in (141) times \(\lambda^{-h}\). They retain limiting fraction at least 1/(1+_h_) by the balance in Section 7. Thus weighting and explicit correction can be compared on the same support with the same exponents.

The budget comparison follows from (97). The normalized saving is given by (165). Since weighting removes every replicated term, its remaining mixed products form a subset of those constrained by the corresponding corrected construction. With the same grading it therefore has no smaller degree gap and no worse limiting retained fraction. The capacity comparison optimizes over all saved weighted supports at each requested fraction.

### C.2 Norm coefficients for the approximation families

5 evaluates the leading coefficients in (148). Definition 23 gives \(\beta'(0)\) by grouping the remaining mixed products of degree one. The spectral coefficient uses the blocks with the smallest exponent in (131). Exact families satisfy the common comparison (136).

\begin{tabular}{ccccc}
formula & _r_ & _h_ & \(\sigma_0\) & \(\theta\) \\
Bini \(\langle 3,2,2\rangle\) & 10 & 1 & \(6+2\sqrt{2}\) & 1/2 \\
Schönhage \(\langle 3,3,3\rangle\) & 21 & 2 & \(5\sqrt{7}\) & 1/3 \\
Smirnov \(\langle 3,3,3\rangle\) & 20 & 6 & \(2\sqrt{15(6+\sqrt{5})}\) & 1/7 \\
\end{tabular}

