<tbc>In Fig. 14, we show the three different GMMs used in our experiments, which were sampled randomly with fixed seeds. We observe that GMM #1 has relatively large variances, allowing for less numerical difficulty, while GMM #2 and (to an even larger extent) GMM #3 have some almost-degenerate covariances, leading to increased numerical instability. Note that GMM #2 appears to be the best separated, which can yield better EM convergence.

## A.4 Discussion on Gradient Ground Truths

As discussed in Section 2.3, the most natural baseline for the computation of a gradient of EM is the full automatic differentiation method (AD). Unfortunately, this strategy is only theoretically sound under strong assumptions \[Gil92; Bec94; MO20\], and may be prone to the propagation of numerical errors across iterations. Due to this latter issue in particular, one may not claim that the AD gradient is exact. In order to discuss its use as a baseline (in particular in Section 4.5), we compare it to the gradient computed using the finite differences approximation (FD) with a step size \(\varepsilon_\mathrm{FD}\), implemented using `torch.autograd.gradcheck.\_get\_numerical\_jacobian` in Pytorch \[Pas+19\]. The experimental setting is as in Section 4.5: in Fig. 15, we observe the relative MSEs \(\|J_\mathrm{FD}-J_\mathrm{AD}\|_2^2/\|J_\mathrm{AD}\|_2^2\) varying the FD step size \(\varepsilon_\mathrm{FD}\in\{10^{-5},10^{-6},10^{-7}\}\) on three different GMMs, taking each time 60 samples for the data _X_ with _n_=300, _d_=3 and running EM with _K_=3 and<tbc>

low
medium
high
GMM μ
GMM v

GMM #1
GMM #2
GMM #3

Figure 13: Two fixed GMMs \(\mu\) (top) and \(\nu\) (bottom) used in Section 3.2. Columns correspond to low (\(\sigma=10\)), medium (\(\sigma=0.5\)), and high (\(\sigma=0.1\)) separation.

Figure 14: 3D representation of the three GMMs used in Section 4.5 to compare EM gradient methods.

