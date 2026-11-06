\begin{tabular}{ccccccc}
Method & bicycle & counter & flowers & room & stump & Mean \\
\multicolumn{7}{c}{\(PSNR\uparrow\)} \\
3DGS \[10\] & 24.71 & 28.96 & 21.09 & 31.50 & 26.45 & 26.54 \\
GSTex \[16\] & 24.68 & 28.50 & 21.17 & 31.15 & 26.24 & 26.35 \\
Textured Gaussians \[3\] & - & - & - & - & - & 27.35 \\
NeST-Splatting \[30\] & 24.49 & 28.45 & 20.05 & 31.30 & 25.87 & 26.03 \\
PAPR<sup>‡</sup> \[31\] & 24.21 & 27.13 & - & 29.36 & 26.23 & 26.73 \\
PointGT (Ours)<sup>‡</sup> & **26.61** & **28.58** & **22.40** & **34.66** & **27.96** & **28.04** \\
\multicolumn{7}{c}{\(SSIM\uparrow\)} \\
3DGS \[10\] & 0.729 & 0.905 & 0.571 & 0.915 & 0.762 & 0.776 \\
GSTex \[16\] & 0.730 & 0.896 & 0.582 & 0.910 & 0.758 & 0.775 \\
Textured Gaussians \[3\] & - & - & - & - & - & 0.827 \\
NeST-Splatting \[30\] & 0.729 & 0.888 & 0.521 & 0.909 & 0.737 & 0.757 \\
PAPR<sup>‡</sup> \[31\] & 0.736 & 0.838 & - & 0.822 & 0.818 & 0.804 \\
PointGT (Ours)<sup>‡</sup> & **0.757** & **0.850** & **0.640** & **0.962** & **0.832** & **0.808** \\
\multicolumn{7}{c}{\(LPIPS\downarrow\)} \\
3DGS \[10\] & 0.265 & 0.201 & 0.377 & 0.219 & 0.266 & 0.266 \\
GSTex \[16\] & 0.265 & 0.221 & 0.365 & 0.237 & 0.248 & 0.267 \\
Textured Gaussians \[3\] & - & - & - & - & - & 0.186 \\
NeST-Splatting \[30\] & 0.236 & 0.202 & 0.358 & 0.194 & 0.246 & 0.247 \\
PAPR<sup>‡</sup> \[31\] & 0.201 & 0.226 & - & 0.209 & 0.202 & 0.210 \\
PointGT (Ours)<sup>‡</sup> & **0.199** & **0.184** & **0.303** & **0.049** & **0.182** & **0.183** \\
\end{tabular}

Chair
Hotdog
Scan 24
Scan 97
Texture-GS
GSTex
Textured-GS
NeST-Splat
PAPR
Ours
GT

**Fig.16:** Qualitative comparison of novel view synthesis with the original number of primitives proposed by the authors.

** 3:** Quantitative novel view synthesis on the MipNeRF360 \[1\] scenes. ‡ Both PAPR and PointGT were trained and rendered at the half-resolution of the dataset, as full resolution evaluation exceeds our GPU memory.

