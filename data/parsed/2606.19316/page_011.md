<tbc>ing. Besides, the filled texture exhibits a stronger golden lus<tbc>

<tbc>ter than NeuMesh since a view-independent and geometry- agnostic modification color **_c_**_<sup>m</sup>_ is well decomposed on each vertex. It is worth noting that even though the template texture only contains a small area of texture codes, we still observe view-dependent effects (e.g., golden metal naturally exhibits specular reflections at different views).

**Texture painting.** In Fig. 8 (c), we show 2 examples of texture painting and also conduct the same editing with NeuMesh. For NeuMesh, the process of texture painting is to fine-tune the affected texture code while freezing the de<tbc>

\begin{tabular}{ccccc}
Resolution & Num. Vertices & \(\text{\textbf{PSNR}}\uparrow\) & \(\text{\textbf{SSIM}}\uparrow\) & \(\text{\textbf{LPIPS}}\downarrow\)(**Vgg**) \\
100 & 128.3K & 30.352 & 0.936 & 0.080 \\
200 & 215.8K & 31.900 & 0.952 & 0.058 \\
300 & 307.5K & 32.324 & 0.955 & 0.053 \\
\end{tabular}

Swapped Area
Original Object
Our Rendered Edited Objects
NeuMesh Rendered Edited Objects
(from red to yellow)
(a) Comparison on Texture Swapping
Original Object
Source Texture
Our Rendered Edited Objects
NeuMesh Rendered Edited Objects
(b) Comparison on Texture Filling
Original Rendered Object
Our Editing on 2D image
Our Rendered Edited Objects
NeuMesh Rendered Edited Objects

Fig. 8: **Editing results comparison.** We show texture editing examples on the DTU dataset \[20\] and the NeRF \(360^\circ\) Synthetic dataset \[40\].

TABLE 4: **Ablation on mesh resolution.** We compare the rendering quality with different marching cube resolutions on NeRF \(360^\circ\) synthetic dataset \[40\].

