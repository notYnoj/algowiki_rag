<tbc>for a fixed target GMM \(\nu\), an initialisation \(\theta_0\) and a number of EM steps _T_. We use a variant of EM presented in Algorithm 2 that **fixes the mixture weights** in this experiment. We will compare three gradient computation methods to compute (or approximate) the gradient of \(F_X^T(\theta_0)\) with respect to _X_, within the gradient descent of E_<sub>T</sub>_, performed using automatic differentiation. The setup is as follows: the initial dataset \(X\in\mathbb{R}^{200\times 2}\) corresponds to samples of a GMM \(\mu_0\) with 3 components, and we want to displace this point cloud to match a target GMM \(\nu\) with 3 components. We represent the setup in Fig. 3a and the flow for AD method in Fig. 3b.

The results for the AI method are both visually and quantitatively very close to AD. We observe satisfactory convergence of the flow of E_<sub>T</sub>_ towards the target GMM \(\nu\). In many applications involving fixed EM weights (Algorithm 2), we observe that particles follow rectilinear trajectories, which is a similar behaviour to Wasserstein flows of \(\mathrm{W}_2^2\) (see \[CNR25, Section 5.3\]). We interpret this phenomenon as a consequence of the fixed weights, which translate to a Lagrangian viewpoint on the GMMs. In simple cases, the \(\mathrm{MW}_2^2\)-optimal plans between the GMMs may not change during the flow, and thus the particles are moved along the induced (rectilinear) trajectories between each GMM component (see \[DD20, Proposition 4\]). In Fig. 3c, we show the flow with the OS method, which yields almost identical results to AD. We also experimented with the Warm-Start flow from Algorithm 3, which is a different minimisation method to minimise E_<sub>T</sub>_, yet yielded almost identical final losses to the AD. In Appendix A.5, we investigate in further detail the impact of warm-starting the AD method, concluding that the results are comparable and become equal when _T_≈10.

## 4.3 Flow of \(\mathrm{EM}-\mathrm{MW}_2^2\) in 2D: Discussion on Uniform Weights

We now consider a similar setting to Section 4.2, but without fixing the weights in the EM algorithm, i.e. using standard EM Algorithm 1. We compare two settings: the first with non-uniform weights \(w_0:=(\frac{1}{5},\frac{1}{5},\frac{3}{5})\) for the initial GMM, and weights \(w_1:=(\frac{1}{2},\frac{3}{10},\frac{1}{5})\) for the target GMM; and the second with uniform weights for both. In Fig. 4, we show the flow of E_<sub>T</sub>_ with the AD method. We observe in Fig. 4a that the flow for non-uniform weights converges to an unsatisfactory local minimum, with a final GMM weight of \[0.38990256, 0.2000008, 0.41009664\] instead of the target \[0.5, 0.3, 0.2\], as shown on the simplex in Fig. 4b. In contrast, the flow for uniform weights presented in Fig. 4c converges to the target GMM and achieves a substantially lower energy, as reported in Fig. 4d. The weights stay close to uniform, with a final GMM weight of \[0.33700094, 0.31099346, 0.35200560\].

The optimisation failure in the non-uniform case is consistent with the essential stationary point problem illustrated in Section 3.3: intuitively, to change the weights of the current GMM, the particles need to change components, but this is difficult if the components are too distant. While our<tbc>

source GMM
target GMM
data
data GMM
(a) E_T_ flow setup.
(b) AD method.
(c) OS method.
Figure 3: Comparison of experimental setup and flows of E_T using different methods. The dark shades of purple correspond to earlier iterations, and the yellow shades to later iterations. (Warm- Start and AI are almost identical to AD)

