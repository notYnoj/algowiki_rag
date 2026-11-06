we have:

\(\left(\frac{d\phi}{dx}\right)_{j-\frac{1}{2}}=\frac{1}{h}\sum_{s=1}^mc_s^{(1)}\left(\phi_{j+s-1}-\phi_{j-s}\right)+O(h^{2m}),\phi_{j-\frac{1}{2}}=\sum_{s=1}^mc_s^{(0)}\left(\phi_{j+s-1}+\phi_{j-s}\right)+O(h^{2m}).\) (2.34)

By eliminating lower-order terms via Taylor expansion, the coefficients \(c_s^{(1)}\) and \(c_s^{(0)}\) can be determined by solving the following linear system:

\(\left(\left(\frac{2t-1}{2}\right)^{2s+k-2}\right)_{1\le s,t\le m}\left(c_s^{(k)}\right)_{1\le s\le m}=\left(\frac{1}{2}0\cdots 0\right)^\top.\) (2.35)

The coefficients for 1D finite difference stencils of orders 2, 4, 6, 8, and 10, derived from (2.35), are summarized in  1.

Previous conclusions can be naturally extended to high-order cases: by using the results of Lemma 2.1 and Proposition 2.8, high-order discrete operators can be constructed within a matrix-free framework. Moreover, such an improvement in accuracy is achieved without causing additional time or memory expenses: In numerical implementations, we first solve coefficients \(c_s^{(0)}\) and \(c_s^{(1)}\) based on the desired order 2_m_, then compute the diagonal matrices \(\Lambda_0\), \(\Lambda_1\) by Lemma 2.1 and construct diagonal blocks K_<sub>i</sub>_ (_i_=1,2,3) by Proposition 2.8. The diagonal blocks K_<sub>i</sub>_ are stored in a complex array of length 3_N_<sup>3</sup>, diagonal elements and upper diagonal elements of K_<sub>B</sub>_, \(\mathcal{K}_\mathcal{P}^{-1}\) are stored by two complex arrays and two real (float) arrays (of length 3_N_<sup>3</sup>). The total memory usage of storing K<sub>A</sub>,K<sub>B</sub> and \(\mathcal{K}_\mathcal{P}^{-1}\) sums up to 192_N_<sup>3</sup> bytes with double precision.

**Remark 2.10.** _The result for null space_ H _of the kernel compensation and the penalty coefficient_ \(\gamma\)_, as is discussed in Proposition 2.5, holds for high-order discretization. The proof lies in analyzing the spectrum of_ BB<sup>†</sup> _with high-order stencil, which involves computing the eigenvalues of_ \(\mathbf{K}_i^\dagger\mathbf{K}_i\) _by Lemma 2.1. The derivation follows the same process as the second-order case._

**Remark 2.11.** _We give a brief summary of Section 2: Yee’s scheme approximates the model problems_ (1.4) _and_ (2.9)_, arriving at a preliminary result_ (2.12)_. Kernel compensation formulation_ (2.13) _eliminates the null space. Finally_ (2.32) _provides a preconditioned formulation that allows matrix-free operations for implementing_ A,B<sup>†</sup>B _and preconditioning. tion_ (2.32) _is adopted for numerical experiments in Section 4._

## 3. Treatment of Permittivity \(\varepsilon\)

To ensure the correctness and robustness of kernel compensation formulation (2.13), \(\mathcal{M}_\varepsilon\) is strictly required to be HPD. This section details how we construct the map \(E_h\mapsto\mathcal{M}_\varepsilon E_h\). Subsection 3.1 discusses the simplest case for a diagonal \(\varepsilon_1\). When \(\varepsilon_1\) has nonzero off-diagonal entries, we encounter the critical issue of DoF misalignment.

