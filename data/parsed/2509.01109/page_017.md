<tbc>("Refine.") to progressively obtain coarse- and fine-grained spatial adaptations. We conduct ablation studies on GPSToken-M128 to validate the contribution of each component.

6 presents the quantitative results. The baseline refers to the method that uses Gaussian- parameterized tokens without incorporating any spatially-adaptive components. The term "baseline+" denotes the method that additionally includes the "Refine." component. In contrast, GPSToken integrates both the "Init." and "Refine." components. As shown in the table, "baseline+" yields improvements over the baseline across both sample-level and distribution-level metrics, with a decrease of 0.01 in LPIPS and a decrease of 0.21 in "rec. FID". These enhancements indicate the general improvement achieved by adjusting Gaussians to match local textures. Compared to "baseline+", GPSToken significantly improves distribution-level metrics, achieving reductions of 0.19 in FID and 0.35 in sFID, while showing slight improvements in sample-level metrics (an increase of 0.06 in PSNR and 0.003 in SSIM). This demonstrates the effectiveness of "Init." component, which reallocates more Gaussians from simple regions to complex ones, thereby capturing finer semantic details in texture-rich regions without compromising reconstruction performance.

As shown in Fig. 9, without the "Init." component, the Gaussian maps from "baseline+" still roughly align in a 2D grid, even after refinement. This limits their ability to fit complex textures, only capturing edges in simple regions. In contrast, with the "Init." component, GPSToken aggregates more Gaussians in texture-rich areas, making it better suited to fit complex structures. This highlights the importance of "Init." component in achieving spatially adaptive representation of fine-grained visual contents.

**Ablation Studies on Params.** We further conduct experiments on the selection of parameters \(\lambda\), _s_, and _s_<sub>min</sub>. The results are shown in  7.

• **Entropy Threshold** \(\lambda\): As stated in Eq. 4 of the main paper, \(\lambda\) balances region size and complexity. A larger \(\lambda=5\) encourages Gaussians to concentrate on complex regions, leading to only minor performance degradation. In contrast, setting \(\lambda=0\) allocates Gaussians solely based on region size, resulting in a uniform spatial distribution. This causes a significant drop in performance:<tbc>

\begin{tabular}{cccccccccc}
\multirow{2}{*}{**Method**} & \multicolumn{2}{c}{**Components**} & \multicolumn{3}{c}{**sample-level**} & \multicolumn{4}{c}{**distribution-level**} \\
 & Init. & Refine. & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) & rec. FID \(\downarrow\) & rec. sFID \(\downarrow\) & FID \(\downarrow\) & sFID \(\downarrow\) \\
**baseline** & & & 23.52 & 0.638 & 0.110 & 1.02 & 4.07 & 2.59 & 4.34 \\
**baseline+** & & \(\unknown\) & 24.00 & 0.654 & 0.100 & 0.81 & 3.59 & 2.37 & 4.31 \\
**GPSToken** & \(\unknown\) & \(\unknown\) & 24.06 & 0.657 & 0.080 & 0.65 & 3.28 & 2.18 & 3.96 \\
\end{tabular}



6: Ablation studies of our spatial adaptivity designs on the \(256\times 256\) reconstruction task. \(\unknown\) indicates that the component is used. "Init." and "Refine." denote the spatially-adaptive token initialization and spatially-adaptive token refinement, respectively.

input **_g_** of baseline+ baseline+ **_g_** of GPSToken GPSToken

Figure 9: **Illustration of "baseline+" and GPSToken.** Left to right: the input image, visualization of Gaussians of "baseline+", the reconstruction of "baseline+", visualization of Gaussians of GPSToken, the reconstruction of GSPToken.

