<tbc>_(b) Margin from a Gaussian order statistic._ The threshold _d<sub>k</sub>_ is, by construction, the _k_-th order statistic among processed squared distances. Intuitively, after processing \(i\gg k\) candidates, _d<sub>k</sub>_ tracks the lower tail of the distance distribution: if distances cluster around mean \(\mu\), then _d<sub>k</sub>_ sits a (slowly growing) number of standard deviations _below_ \(\mu\) and stays below \(\mu\). A typical non-nearest candidate has true squared distance close to \(\mu\), so its margin \(\Delta=\|\mathbf{q}-\mathbf{x}\|^2-d_k\) is typically positive. Formally, under the Gaussian distance approximation, the Dvoretzky-Kiefer-Wolfowitz (DKW) inequality \[39\] on the empirical distance CDF bounds the threshold by \(d_k\le\mu+\sigma\Phi^{-1}(k/(i+1)+\epsilon_i)\) with high probability, where \(\epsilon_i=\mathcal{O}\left(\sqrt{ln(1/\delta)/i}\right)\) and \(\Phi\) is the standard normal CDF. For \(k\checkmark i\) and \(k/(i+1)+\epsilon_i<1/2\), the quantile is negative, so the margin satisfies \(\Delta\unknown-\sigma\Phi^{-1}(k/(i+1)+\epsilon_i)>0\) with high probability. The exact union bound is in the technical report.

_(c) Aggregation._ Summing the pruning depth \(\rho\) over all _N_ candidates and substituting the margin estimate, we get:

\(\mathbb{E}[\text{Cost}]\le c\cdot\frac{Nd}{\alpha},\)

where the constant \(c=c(R,\sigma,k,N)\) is the averaged, capped log- margin term from steps (a) and (b). It is bounded and data-dependent.  3 confirms that the measured scanned fraction tracks \(1/\alpha\) within a small constant on our data; empirically the effective constant is order-one and close to 1, so the dominant scaling is \(\mathbb{E}[\text{Cost}]\lesssim Nd/\alpha\). □

_Empirical Validation._ Panorama beats the brute-force cost _Nd_ whenever \(\alpha\) exceeds the effective margin constant, with speedup scaling as \(\alpha/c\). The cost model is checked on two axes. First, Proposition 5.1 predicts that the fraction of dimensions evaluated will scale as \(1/\alpha\).  3 reports the measured fraction alongside the theoretical \(1/\alpha\) on each dataset: the prediction tracks measurement within a small factor across all six benchmarks, so the leading \(1/\alpha\) term governs the speedup. Second, if Panorama evaluates a fraction _p_ of the dimensions, ideal scaling predicts a wall-clock speedup of 1_/p_. Figure 13 plots this semi-empirical prediction against measured QPS. On IVFFlat the points sit on the diagonal; on IVFPQ they exceed it, since the sub-quantizer-major layout of §6.2 unlocks cache benefits beyond what the cost model captures. The algorithmic pruning we predict translates faithfully into measured throughput.

## 5.3 Out-of-Distribution Robustness

When a query is drawn from a different distribution than the indexed data--adversarial inputs, cross-domain transfer, modality shifts--its tail energy decays at a rate \(\alpha_q\) distinct from the database rate \(\alpha_x\). The Cauchy-Schwarz remainder depends on the geometric mean \(\sqrt{e^{-\alpha_qm/d}\cdot e^{-\alpha_xm/d}}\), so the effective decay rate becomes the _arithmetic mean_

\(\alpha_\text{eff}=\frac{\alpha_q+\alpha_x}{2}.\)

Substituting this effective rate into Proposition 5.1 gives the corresponding robustness bound.

Proposition 5.2 (Out-of-distribution cost). _If query and database tail energies decay at rates_ \(\alpha_q\) _and_ \(\alpha_x\)_, respectively, and the OOD candidate stream has margin constant c_<sub>ood</sub>_, then the expected_<tbc>

<tbc>_coordinate-evaluation cost satisfies_<tbc>

\(\mathbb{E}[\text{Cost}_\text{ood}]\lesssim\frac{2c_\text{ood}Nd}{\alpha_q+\alpha_x}.\)

<tbc>_Proof sketch._ The proof of Proposition 5.1 remains unchanged _except_ for the per-candidate pruning depth bound that uses the tail- decay assumption. We revise that step with separate decay rates. The Cauchy-Schwarz remainder depends on the geometric mean of the two tail energies, \(\sqrt{R_{T(\mathbf{q})}^{(m,d)}R_{T(\mathbf{x})}^{(m,d)}}\). With the exponential tail holding separately for query and database, this becomes:

\(\sqrt{R_{T(\mathbf{q})}^{(m,d)}R_{T(\mathbf{x})}^{(m,d)}}\approx\|\mathbf{q}\|\|\mathbf{x}\|\sqrt{e^{-\alpha_qm/d}e^{-\alpha_xm/d}}\)<br>
\(=\|\mathbf{q}\|\|\mathbf{x}\|e^{-(\alpha_q+\alpha_x)m/(2d)}.\)

In effect, the level-_m_ gap decays exponentially with rate \(\alpha_\text{eff}=(\alpha_q+\alpha_x)/2\). Substituting \(\alpha_\text{eff}\) into the depth formula of Proposition 5.1 gives

\(\rho_\text{ood}\approx min\big\{d,\frac{2d}{\alpha_q+\alpha_x}\big[ln\left(\frac{C_0}{\Delta}\right)\big]_+\big\}.\)

Aggregating across _N_ candidates and absorbing the averaged OOD margin constant _c_ood yields the claimed cost. When the shift changes only tail compaction, _c_ood=_c_; if it also changes the distance distribution, _c_ood reflects the changed margin terms. □

_Interpretation._ As the OOD bound follows the _arithmetic mean_ of the two rates, in the worst case a query halves \(\alpha_\text{eff}\). A fully out-of- distribution query, \(\alpha_q\rightarrow 0\), leaves the leading term at \(2c_\text{ood}Nd/\alpha_x\), with a two-fold slowdown over Proposition 5.1 when the margin constant is unchanged. Panorama robustly benefits from a well-compacted database regardless of the query, as we confirm empirically with Hephaestus OOD workloads (Figure 12): Panorama remains competitive at all relative-contrast levels, while its speedup degrades gracefully as queries harden. Concretely, speedup degrades monotonically from \(25.1\times\) on the easiest workload to \(12.1\times\) on the hardest--a regime where probabilistic baselines either lose recall or cease to scale.

## 5.4 The \(\varepsilon\)-Relaxation

Equation (4) defines the relaxed score used by Panorama: it scales the Cauchy-Schwarz correction by a scalar \(\varepsilon\in(0,1]\), replacing 2_C<sup>m</sup>_ with \(2\varepsilon C^m\), where \(C^m=\sqrt{R_{T(\mathbf{q})}^{(m,d)}R_{T(\mathbf{x})}^{(m,d)}}\) is the worst-case residual coupling. Setting \(\varepsilon=1\) corresponds to the adversarial geometry in which Cauchy-Schwarz is tight; in high dimensions, however, this geometry is atypical--the residual coordinates of non-near- neighbors are nearly isotropic on the sphere, and their inner products are far smaller than the worst case.

Let \(\rho_m:=\pi_m/C^m\in[-1,1]\) denote the normalized residual inner product, where \(\pi_m=\sum_{j>m}T(\mathbf{q})_jT(\mathbf{x})_j\) is the true residual contribution. The worst case \(\rho_m=-1\) recovers the 4_C<sup>m</sup>_ gap underlying Proposition 5.1; under residual isotropy--realized on non-near-neighbor pairs by the intra-block rotation of §4.2--the typical case is \(\rho_m\approx 0\), giving a sharper \(2\varepsilon C^m\) gap. Re-deriving the per-candidate depth with this sharper gap produces an additive shift of \((d/\alpha)ln\varepsilon\).

