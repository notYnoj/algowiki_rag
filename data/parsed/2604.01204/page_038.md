\begin{tabular}{cc}
\multicolumn{2}{c}{**Representation**} \\
Mesh topology & Delaunay triangulation (shared vertices) \\
Interpolation & Clough-Tocher _C_<sup>1</sup> cubic \\
Feature activation & SinCos: \[sin(_f),_cos(_f_)\] \\
Feature dim. per vertex & 4-16 \\
MLP hidden dim. \(64-128\times 2-4\) layers & \\
\multicolumn{2}{c}{**Training**} \\
Total iterations & 25000 \\
Pixel sampling & Stratified, 160000 pixels/batch \\
Loss function & MSE \\
\multicolumn{2}{c}{**Learning rates (initial)**} \\
Vertex positions & \(1\times 10^{-4}\) \\
Vertex features & \(5\times 10^{-3}\) \\
MLP weights & \(5\times 10^{-5}\) \\
\multicolumn{2}{c}{**LR schedule**} \\
All parameters & Exponential decay: \\
 & \(\eta(t)=\eta_0\cdot 0.33^{max(0,(t-20k)/10k)}\) \\
\multicolumn{2}{c}{**Densification**} \\
Strategy & Coarse-to-fine Delaunay re-meshing \\
Schedule & Steps 1500-15000, every 500 steps \\
Growth rate & \(0.35\times\) current vertex count per step \\
Scoring & DSSIM-based, area-weighted: \\
 & score\(_t=\overline{\text{DSSIM}_t}\cdot|\text{pixels}_t|^{0.75}\) \\
Min. triangle size & 3 pixels (skip smaller triangles) \\
Initialization & Edge-aware sampling (Sobel) \\
\multicolumn{2}{c}{**HDR pipeline**} \\
Input & 14-bit RAW (Nikon NEF), 45.7 MP \\
Encoding space & \(\mu\)-law: \(f(x)=log(1+\mu x/w)/log(1+\mu)\) \\
\(\mu\) parameter & 5000 \\
White level _w_ & 2<sup>14</sup>-1=16383 \\
GT pixel lookup & Bilinear interpolation \\
\end{tabular}

** 18:** Hyperparameters and optimization details for the 2D image fitting experiment. The parameter budget (maximum vertices, MLP size) is derived from the target compression ratio and image dimensions and bitrate.

