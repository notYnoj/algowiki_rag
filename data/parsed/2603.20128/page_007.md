<tbc>Since results on the LLFF dataset are not provided, we only compare against SuperGaussian on Blender (Tab. 1). For S2Gaussian \[32\], since the authors do not provide publicly available code, we directly report the results as presented in the original paper. And 3DSR \[5\] on LLFF dataset. 4) _Generalizable NeRFs_: MVSGaussian \[21\], GeFU \[22\], and GDB-NeRF \[8\], evaluated on DTU with input images resized to 512\(\times\)512.

**Quantitative and Qualitative Analysis.** s 1, 2, and 3 summarize quantitative results, and Figures 6,3 and 4, and provide visual comparisons. Backbone-only NVS methods degrade severely at extreme low-resolution inputs (100\(\times\)100 and 200\(\times\)200), in many cases performing worse than bicubic upsampling. This is due to the reduced number of rays and the strong ambiguity of LR observations, which prevent accurate high-frequency reconstruction. In contrast, when combined with our NGP-SR, NeRF and 3DGS backbones achieve significant improvements across all metrics, demonstrating the effectiveness of our framework as a modular SR component. On Blender, our method outperforms both NeRF-SR and FastSR-NeRF at extremely low resolutions (100\(\times\)100, despite their reliance on HR references, while also surpassing SuperGaussian and in most cases. On LLFF, NGP-SR achieves especially strong performance, which can be attributed to training on all images per scene--similar to NeRF-SR, and the tendency of our NGP-based interpolation to overfit more effectively to observed views. This property allows NGP-SR to reconstruct high-fidelity details when test views share similar content with the training set. On DTU, NGP-SR generalizes well to unseen test scenes, producing sharper details and more consistent reconstructions from LR inputs and camera poses.

## 5 . Ablation Study

We conduct comprehensive ablation studies to analyze the contributions of key components in our framework. To systematically assess the effectiveness of these modules, we create subnetworks by individually removing each component and report both qualitative and quantitative outcomes on the Lego scene from the Blender dataset, using a resolution scale factor of \(\times\)2 and input resolution of \(100\times 100\).

<tbc>Results are summarized in  4 and qualitatively illustrated in Figure 5.

**Camera-Aware Mapping Network (**G<sub>**cam**</sub>**)** This module integrates view-dependent feature vectors with camera pose embeddings via an MLP, enabling robust viewpoint adaptation. For ablation, we replace G<sub>cam</sub> with a simpler two- layer MLP without camera pose conditioning. The resulting model suffers a notable performance drop (PSNR: -3.27 dB, SSIM: -0.053, LPIPS: +0.02), confirming the critical role of explicit camera pose embedding.

**Global Feature Extractor (**G<sub>**CNN**</sub>**)** This component captures structural and textural context from low-resolution inputs. Ablating this module significantly degrades reconstruction quality (PSNR: -16.58 dB, SSIM: -0.407, LPIPS: +0.409), demonstrating its importance in providing global context. Qualitative results in Figure 5 highlight clear fail<tbc>

\begin{tabular}{cccc}
\multirow{2}{*}{Methods} & \multicolumn{3}{c}{DTU} \\
 & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS\(\downarrow\) \\
MVSGaussian & 21.95 & 0.863 & 0.112 \\
GeFU & 23.15 & 0.880 & **0.100** \\
GDB-NeRF & 22.42 & 0.867 & 0.111 \\
Ours (\(\times\)4) & **31.38** & **0.884** & 0.122 \\
\end{tabular}

\begin{tabular}{cccc}
\multirow{2}{*}{Methods} & \multicolumn{3}{c}{Lego\(\times\)2 (100\times 100)} \\
 & PSNR \(\uparrow\) & SSIM \(\uparrow\) & LPIPS \(\downarrow\) \\
Ours w/o G<sub>cam</sub> & 26.69 & 0.892 & 0.082 \\
Ours w/o G<sub>CNN</sub> & 13.38 & 0.538 & 0.471 \\
Ours w/o G<sub>fuse</sub> & 13.69 & 0.585 & 0.436 \\
Ours & **30.60** & **0.952** & **0.075** \\
\end{tabular}

Ours w/o Gcam
Ours w/o GCNN
Ours w/o GFuse
Ours

