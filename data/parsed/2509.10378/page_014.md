<tbc>Figure 6a shows the model similarity between the \(\mathcal{N}_{L16}^\mathrm{FNO}\) and \(\mathcal{N}_{L8}^\mathrm{FNO}\), and \(\mathcal{N}_{L32}^\mathrm{FNO}\) models. Using \(\mathcal{N}_{L16}^\mathrm{FNO}\) as the reference, the weights of \(\mathcal{N}_{L32}^\mathrm{FNO}\) are more closely aligned along the diagonal compared to \(\mathcal{N}_{L8}^\mathrm{FNO}\), suggesting that for FNO models, the learned mapping for _L_=8 differs from those for _L_=16 and _L_=32. This observation aligns with the lower performance of directly applying \(\mathcal{N}_{L16}^\mathrm{FNO}\) to the _L_=8 case. Meanwhile, the FCN models trained on different action parameters show high similarity among the model weights (Figure 6b), indicating these models have learned similar mappings. Indeed, as described in the previous section, directly applying \(\mathcal{N}_{L16}^\mathrm{FCN}\) to the _L_=8 and _L_=32 cases achieves comparable performance to models specifically trained on those cases. These results imply the target mapping may dominantly depend on the local features of the gauge field. While the FNO models may have overfitted the global structure of the gauge field, which could vary for different problem sizes, the FCN models, thanks to the architecture restriction, learn the local dependency that appears to generalize across action parameters.

With the model output \(\tilde{U}_\mu(x)\) generating effective preconditioning operators, we further investigate the relationship between \(U_\mu(x)\) and \(\tilde{U}_\mu(x)\). Specifically, we compute and visualize the characteristics of \(\tilde{U}_\mu(x)\) through the changes in phase angles and magnitudes of the corresponding entries relative to \(U_\mu(x)\). For _all_ models, we observe that the average phase difference remains very close to \(\pi\), matching up to the fourth digit, while the magnitudes of \(\tilde{U}_\mu(x)\) is close to \(\frac{1}{2}|U_\mu(x)|\), where \(|U_\mu(x)|=1\). For additional details, Figure 7 shows such differences from applying \(\mathcal{N}_{L16}^\mathrm{FNO}\) to an instance of the _L_=64 case, showing similar average differences in magnitudes and phase angles. When taking the signed phase difference, the heat maps and histograms show almost every entry in \(\tilde{U}_\mu(x)\) gets rotated by \(\pi\) from \(U_\mu(x)\).

These results demonstrate that the learned mappings from various models share close characteristics, supporting that our proposed framework learns a general mapping of the form in (5), which may be simple as reducing the modulus of \(U_\mu(x)\) by half and rotating the phases by \(\pi\). To test this simple relationship, we then construct the preconditioner generating configurations explicitly, following \(\tilde{U}_\mu^\mathrm{simple}(x)=-\frac{1}{2}U_\mu(x)\), and use the resulting preconditioning operators to apply to the CG solve. Given the hopping representation of the Wilson Dirac operator, \(D^\dagger D[U_\mu(x)]=|1-2\kappa H|^2\), where \(H=H[U_\mu(x)]\) is the hopping matrix which depends linearly on \(U_\mu(x)\) \[61\], one can argue that \(D^\dagger D[-0.5U_\mu(x)]=|1+\kappa H|^2\simeq_{\kappa\rightarrow 0}|1+2\kappa H|\simeq|1-2\kappa H|^{-1}\simeq(D^\dagger D[U_\mu(x)])^{-1}\). Therefore, one might expect \(D^\dagger D[\tilde{U}_\mu^\mathrm{simple}(x)]\) to be an effective preconditioner at small \(\kappa\). It is nevertheless<tbc>

(a)
(b)
NL=8
1.0
NL=8
0.6
NL=32
0.8
NL=32
0.4
0.6
0.2
Other model weights
0.4
Other model weights
0.0
0.2
0.0
-0.2
-0.4
-0.2
-0.6
-0.4
-0.50
-0.25
0.00
0.25
0.50
-0.25
0.00
0.25
0.50
0.75
1.00
Weights of NL = 16
Weights of NL = 16

Fig. 6. Scatter plots of model weights learned from different lattice gauge fields. (a) FNO-based; (b) FCN-based.

