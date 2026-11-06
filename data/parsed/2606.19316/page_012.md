<tbc>coder. This leads to the inevitable fact that the model reaches a sub-optimal result when the color of the painting is beyond the color spectrum that the texture decoder learned, e.g., the unsaturated green color in Lego and the uncolored letter in the teddy bear in Fig. 8 (c). Conversely, the proposed per-vertex modification colors are easily modified since they do not rely on the appearance interpretation of a neural decoder. Our method offers a reasonable editing result and a user-friendly editing pipeline by directly painting on 2D images and then transferring the painting into the 3D radiance field. Please refer to our supplementary video for a vivid animation of these editing results.

## 4.5 Efficiency Comparisons

We evaluate the efficiency of Neuralangelo \[32\], BakedSDF\* \[88, 90\], NeuMesh \[83\] and our method on a single RTX 3090 GPU. We take NeRF Synthetic 360\(^\circ\) \[40\] as the test dataset and use average rendering time per image of 800x800 resolution as the metric. As shown in Tab. 6, our method presents significantly faster rendering speeds, achieving an improvement of 15 times to BakedSDF \[88\] and more than 400 times to Neuralangelo \[32\] and NeuMesh \[83\]. This is attributed to our compact neural network and occupancy-guided efficient rendering for superior rendering efficiency while also achieving markedly better quality.

\begin{tabular}{cccc}
 & **PSNR**\(\uparrow\) & **SSIM**\(\uparrow\) & **LPIPS**\(\downarrow\)**(Vgg)** \\
w / distillation & 32.2740 & **0.9551** & 0.0537 \\
ours & **32.324** & 0.9550 & **0.0534** \\
\end{tabular}

\begin{tabular}{cc}
Time (sec.) & Per-frame Rendering\(\downarrow\) \\
Neuralangelo \[32\] & 28.029 \\
BakedSDF\* \[88\] & 1.317 \\
NeuMesh \[83\] & 99.001 \\
Ours & **0.067** \\
\end{tabular}

Original Object
Our Rendered Painted Objects
Semantic Selection on Original Object
Our Rendered Edited Objects
(a) More Results on Texture Painting
(b) More Results on Semantic-driven Texture Editing

PNSR w.r.t. KNN
SSIM w.r.t. KNN
LPIPS (Vgg) w.r.t. KNN
32.50
0.957
0.062
32.25
0.955
0.058
Avg. PSNR
32.00
Avg. SSIM
0.953
0.054
31.75
0.951
0.050
0
2
4
6
8
10
0
2
4
6
8
10
Queried vertex number (N)
Queried vertex number (N)
Queried vertex number (N)

Fig. 9: **Texture editing results.** We show more texture painting and semantic-guided editing examples on the DTU dataset \[20\] and the NeRF 360\(^\circ\) Synthetic dataset \[40\].

Fig. 10: **Ablation on KNN searching.** We compare rendering quality with different K-Nearest Neighboring Searching numbers.

TABLE 5: **Ablation on distillation.** We compare the rendering quality between training with distillation (w/ distillation) and training without distillation (ours) on NeRF 360\(^\circ\) synthetic dataset \[40\].

TABLE 6: **Time Comparison.** We compare the average time of the rendering with the Neuralangelo \[32\], BakedSDF\* \[88\], NeuMesh \[83\].

