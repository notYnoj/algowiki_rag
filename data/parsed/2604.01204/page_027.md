<tbc>where _A_ is the total area of the triangle and _A<sub>i</sub>_ is the area of the sub-triangle formed by the evaluation point **p** and the edge opposite to vertex _i_. For a triangle with vertices **v**<sub>1</sub>,**v**<sub>2</sub>,**v**<sub>3</sub>:

\(A_1=\frac{1}{2}\left\|(\mathbf{v}_2-\mathbf{p})\times(\mathbf{v}_3-\mathbf{p})\right\|,\)<br>
\(A_2=\frac{1}{2}\left\|(\mathbf{v}_3-\mathbf{p})\times(\mathbf{v}_1-\mathbf{p})\right\|,\)<br>
\(A_3=\frac{1}{2}\left\|(\mathbf{v}_1-\mathbf{p})\times(\mathbf{v}_2-\mathbf{p})\right\|.\) (4)

For 2D connected triangles, this is similar to vertex features recently introduced in the context of neural global illumination \[57\]. Our formulation however is more general and extends to higher order topologies and disconnected meshes. For tetrahedra, barycentric weights are similarly computed as

\(\alpha_i=\frac{V_i}{V},V=\sum_{j=1}^nV_j\) (5)

where _V_ is the total volume of the tetrahedron and _V<sub>i</sub>_ is the volume of the sub- tetrahedron formed by the evaluation point **p** and the face opposite to vertex _i_.

\begin{tabular}{ccccccccccccc}
 & \multicolumn{3}{c}{3DGS-MCMC} & \multicolumn{3}{c}{3DGUT-MCMC + SH} & \multicolumn{3}{c}{3DGUT-MCMC + SV} & \multicolumn{3}{c}{3DGUT-MCMC + NHT (Ours)} \\
Scene & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) & PSNR\(\uparrow\) & SSIM\(\uparrow\) & LPIPS\(\downarrow\) \\
\multicolumn{13}{c}{_MipNeRF360 - Outdoor_} \\
bicycle & **25.61** & **0.774** & 0.246 & 25.51 & 0.771 & 0.250 & 25.21 & 0.758 & 0.255 & 25.43 & 0.771 & **0.243** \\
garden & 27.29 & 0.855 & 0.155 & 27.21 & 0.854 & 0.156 & 27.48 & 0.856 & 0.156 & **28.04** & **0.872** & **0.122** \\
stump & **26.93** & 0.788 & 0.250 & **26.93** & **0.789** & 0.251 & 25.95 & 0.757 & 0.270 & 26.58 & 0.772 & **0.249** \\
treehill & **23.45** & **0.665** & 0.366 & 23.30 & 0.663 & 0.368 & 23.16 & 0.653 & 0.371 & 23.13 & 0.660 & **0.340** \\
flowers & 22.04 & **0.628** & 0.362 & **22.07** & 0.627 & 0.363 & 21.76 & 0.616 & 0.367 & 21.60 & 0.615 & **0.351** \\
\multicolumn{13}{c}{_MipNeRF360 - Indoor_} \\
room & 32.33 & 0.938 & 0.245 & 32.36 & 0.937 & 0.246 & 32.67 & 0.939 & 0.243 & **33.03** & **0.943** & **0.234** \\
counter & 29.48 & 0.924 & 0.223 & 29.47 & 0.923 & 0.224 & 30.69 & **0.932** & 0.213 & **30.83** & 0.931 & **0.208** \\
kitchen & 31.67 & 0.935 & 0.144 & 31.72 & 0.935 & 0.144 & 32.38 & 0.938 & 0.140 & **32.98** & **0.942** & **0.132** \\
bonsai & 32.69 & 0.953 & 0.220 & 32.76 & 0.953 & 0.220 & 34.07 & 0.959 & 0.215 & **34.55** & **0.961** & **0.208** \\
\multicolumn{13}{c}{_Tanks \& Temples_} \\
train & 22.50 & 0.832 & 0.224 & 22.10 & 0.827 & 0.231 & 22.32 & 0.831 & 0.223 & **23.11** & **0.851** & **0.202** \\
truck & 26.00 & 0.891 & 0.151 & 25.88 & 0.890 & 0.153 & 26.04 & 0.891 & 0.151 & **26.48** & **0.898** & **0.135** \\
\multicolumn{13}{c}{_Deep Blending_} \\
drjohnson & 29.50 & 0.909 & 0.320 & 29.60 & 0.909 & 0.321 & 29.69 & 0.909 & 0.321 & **30.24** & **0.915** & **0.317** \\
playroom & 30.45 & 0.915 & 0.313 & 30.82 & 0.916 & 0.315 & 30.89 & 0.915 & 0.318 & **31.52** & **0.920** & **0.306** \\
M360 Outdoor Avg & **25.06** & **0.742** & 0.276 & 25.00 & 0.741 & 0.278 & 24.71 & 0.728 & 0.284 & 24.96 & 0.738 & **0.261** \\
M360 Indoor Avg & 31.54 & 0.938 & 0.208 & 31.58 & 0.937 & 0.209 & 32.45 & 0.942 & 0.203 & **32.85** & **0.944** & **0.196** \\
M360 Total Avg & 27.94 & 0.829 & 0.246 & 27.93 & 0.828 & 0.247 & 28.15 & 0.823 & 0.248 & **28.46** & **0.830** & **0.232** \\
T\&T Avg & 24.25 & 0.861 & 0.188 & 23.99 & 0.859 & 0.192 & 24.18 & 0.861 & 0.187 & **24.79** & **0.875** & **0.169** \\
DB Avg & 29.98 & 0.912 & 0.317 & 30.21 & 0.913 & 0.318 & 30.29 & 0.912 & 0.320 & **30.88** & **0.918** & **0.311** \\
\end{tabular}

** 6:** Per-scene results on MipNeRF360 \[2\], Tanks & Temples \[30\], and Deep Blending \[21\], from Tab. 2. This is the standardized setup limited to 1M primitives, 30k iterations, same number of appearance features per primitive (48) and same hyperparameters for all scenes, isolating entirely the effect of our approach from other variables.

