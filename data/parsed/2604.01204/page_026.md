## 2 Feature interpolation

For a spatial coordinate **p** lying on the surface of our topology, or inside of its volume, we can compute the feature vector by barycentrically interpolating the feature vectors at the vertices of the shape. For example, for a 2D triangle with vertices **v**<sub>1</sub>,**v**<sub>2</sub>,**v**<sub>3</sub>, the feature vector _f_(**p**) is computed as

\(f(\mathbf{p})=\sum_{i=1}^n\alpha_if_i\) (2)

where _f<sub>i</sub>_ are the features at the triangle vertices, and \(\alpha_i\) are the barycentric coordinates at the evaluated point. In the case of 2D triangles, barycentric weights are computed as

\(\alpha_i=\frac{A_i}{A},A=\sum_{j=1}^nA_j\) (3)

\begin{tabular}{cccc}
References & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) \\
Downscaled PNGs & **29.022** & **0.8447** & **0.2026** \\
JPEG (original) & 28.738 & 0.8341 & 0.2164 \\
\(\Delta\) & -0.284 & -0.0106 & +0.0138 \\
\end{tabular}

bicycle
room
NHT (ours)
34
NHT (ours)
Spherical Betas
Spherical Betas
25
Spherical Voronoi
Spherical Voronoi
32
24
23
30
PSNR
PSNR
22
28
21
26
20
0
10000
20000
30000
40000
50000
60000
70000
0
10000
20000
30000
40000
50000
60000
70000
iteration
iteration

**Fig.2:** Eval-set PSNR during training on MipNeRF360 scenes _bicycle_ (outdoors, 194 images) and _room_ (indoors, 311 images). Overfitting can manifest when scenes are sparsely captured and trained for a higher number of epochs.

** 5:** Effect of reference image format on MipNeRF360 evaluation for NHT (Ours). _Downscaled PNGs_ uses _gsplat_’s default strategy, which downscales and converts the provided JPEG references to lossless PNGs before training and evaluation. _JPEG (original)_ trains and evaluates directly on the provided JPEG-compressed references without any preprocessing. JPEG compression artifacts in the ground truth lower the effective quality ceiling, slightly degrading all three metrics.

