<tbc>dataset, we can not compare our method with NeuManifold on the DTU dataset. As shown in Tab. 3, our method surpasses other methods except for Neuralangelo \[32\] on the real-world dataset. DVGO struggles to accurately reconstruct the geometry of real-world scenes under complex lighting conditions. Similarly, BakedSDF \[88\], which utilizes a mesh-based rasterization approach, exhibits inferior rendering quality when applied to real-world scenes with intricate lighting conditions. Instead, we build the radiance field upon the explicit mesh scaffold and attach the neural codes tightly to the surface, which maintains high-quality rendering.

## 4.3 Experiment on Geometry Editing

We now show the result of mesh-guided geometry editing in Fig. 7 (a), where we simply deform meshes in the proposed GUI, and the rendered objects are deformed simultaneously. As shown in Fig. 7 (b), we also compare our editing with NeuMesh. After deformation, our method still renders clear and high-fidelity images. On the contrary, the results of NeuMesh are much jaggier than ours due to the insufficient spatial smoothness of its local space parameterization, which proves the superiority of our representation. Besides,<tbc>

<tbc>we combine our method with some physical simulation algorithms and render the images of the object’s behaviors at different moments under force conditions. In Fig. 7 (c), the chair descends from an elevated position and subsequently rebounds upon impact with the ground, and the ficus is swaying in the wind. Please refer to our supplementary video for a vivid animation of these editing results.

## 4.4 Experiment on Texture Editing

We compare with NeuMesh \[83\] in three different texture editing tasks as illustrated in Fig. 8. Then we show more results of texture painting and semantic texture editing in Fig. 9.

**Texture swapping.** We present 2 examples of texture swapping in Fig. 8 (a), where the textures of the golden rabbit’s body and the packaging of cans have been seamlessly swapped while the geometry is kept unchanged. Compared to the NeuMesh, our method clearly preserves more details of the transferred texture, e.g., texts on the cans and bear’s fur, while NeuMesh tends to produce blurry and distorted texture after swapping. This demonstrates that our representation has a better disentanglement of the geometry<tbc>

\begin{tabular}{cccccccccc}
Method & Avg. & _chair_ & _drums_ & _ficus_ & _hotdog_ & _lego_ & _materials_ & _mic_ & _ship_ \\
\multicolumn{10}{c}{**PSNR**\(\uparrow\)} \\
DVGO \[65\] & 31.95 & 34.09 & 25.44 & 32.78 & 36.74 & 34.64 & <u>29.57</u> & 33.20 & 29.13 \\
NeuS \[74\] & 28.13 & 30.09 & 23.93 & 25.67 & 34.45 & 26.33 & 27.59 & 30.21 & 26.73 \\
Neuralangelo \[32\] & 31.74 & 33.44 & **26.32** & 32.65 & 36.98 & 32.46 & **30.59** & 30.43 & **31.04** \\
NeuTex \[79\] & 21.99 & 24.34 & 18.51 & 20.13 & 27.66 & 21.58 & 19.91 & 22.64 & 21.11 \\
NeuManifold \[78\] & 31.26 & 34.39 & 25.39 & 31.91 & 35.69 & 34.00 & 26.69 & 33.40 & 28.63 \\
BakedSDF\* \[88\] & 30.57 & 32.26 & 25.10 & 32.56 & 34.82 & 32.57 & 25.60 & 32.55 & 29.07 \\
NeuMesh \[83\] & 26.21 & 30.38 & 24.09 & 13.39 & 34.12 & 27.85 & 24.99 & 31.74 & 23.10 \\
Ours w/o normal & **32.32** & <u>34.86</u> & <u>25.87</u> & **33.09** & **37.21** & **35.39** & 27.67 & <u>34.10</u> & 30.37 \\
Ours early interp. & <u>32.17</u> & 34.60 & 25.71 & 32.85 & 36.85 & 35.20 & 27.62 & **34.35** & 30.18 \\
Ours LITE & 32.06 & 34.48 & 25.66 & 32.83 & 36.72 & 35.27 & 27.82 & 33.59 & 30.09 \\
Ours & **32.32** & **34.88** & 25.83 & <u>33.07</u> & <u>36.99</u> & <u>35.37</u> & 27.76 & 34.25 & <u>30.42</u> \\
\multicolumn{10}{c}{**SSIM**\(\uparrow\)} \\
DVGO \[65\] & <u>0.957</u> & 0.977 & 0.930 & 0.978 & <u>0.980</u> & 0.976 & <u>0.951</u> & 0.983 & 0.879 \\
NeuS \[74\] & 0.934 & 0.936 & 0.921 & 0.939 & 0.968 & 0.918 & 0.947 & 0.967 & 0.872 \\
Neuralangelo \[32\] & **0.975** & **0.982** & **0.954** & **0.986** & **0.989** & **0.981** & **0.974** & <u>0.985</u> & **0.950** \\
NeuTex \[79\] & 0.875 & 0.896 & 0.841 & 0.884 & 0.939 & 0.846 & 0.874 & 0.918 & 0.804 \\
NeuManifold \[78\] & 0.955 & <u>0.981</u> & <u>0.939</u> & 0.978 & 0.979 & 0.977 & 0.924 & **0.986** & 0.875 \\
BakedSDF\* \[88\] & 0.945 & 0.962 & 0.927 & <u>0.980</u> & 0.973 & 0.955 & 0.910 & 0.981 & 0.871 \\
NeuMesh \[83\] & 0.903 & 0.937 & 0.917 & <u>0.781</u> & 0.967 & 0.926 & 0.912 & <u>0.974</u> & 0.809 \\
Ours w/o normal & 0.955 & 0.978 & 0.927 & 0.976 & <u>0.980</u> & <u>0.978</u> & 0.928 & <u>0.985</u> & 0.889 \\
Ours early interp. & 0.956 & 0.977 & 0.929 & 0.975 & 0.979 & 0.977 & 0.931 & **0.986** & 0.889 \\
Ours LITE & 0.953 & 0.976 & 0.924 & 0.974 & 0.979 & 0.977 & 0.928 & 0.983 & 0.886 \\
Ours & 0.955 & 0.978 & 0.927 & 0.976 & <u>0.980</u> & 0.977 & 0.929 & **0.986** & <u>0.890</u> \\
\multicolumn{10}{c}{**LPIPS**\(\downarrow\) **(Vgg)**} \\
DVGO \[65\] & 0.053 & 0.027 & 0.077 & 0.024 & 0.034 & 0.028 & <u>0.058</u> & 0.017 & 0.161 \\
NeuS \[74\] & 0.082 & 0.070 & 0.094 & 0.066 & 0.054 & 0.090 & 0.056 & 0.035 & 0.190 \\
Neuralangelo \[32\] & **0.030** & <u>0.022</u> & **0.044** & <u>0.014</u> & **0.017** & **0.020** & **0.030** & 0.018 & **0.072** \\
NeuTex \[79\] & 0.167 & 0.123 & 0.200 & 0.129 & 0.126 & 0.194 & 0.151 & 0.111 & 0.304 \\
NeuManifold \[78\] & 0.059 & **0.014** & 0.072 & 0.028 & 0.036 & <u>0.024</u> & 0.115 & **0.012** & 0.168 \\
BakedSDF\* \[88\] & <u>0.043</u> & 0.044 & <u>0.059</u> & **0.013** & <u>0.029</u> & 0.029 & 0.062 & <u>0.016</u> & <u>0.089</u> \\
NeuMesh \[83\] & 0.158 & 0.076 & 0.112 & 0.312 & <u>0.062</u> & 0.094 & 0.131 & 0.031 & <u>0.447</u> \\
Ours w/o normal & 0.054 & 0.028 & 0.079 & 0.031 & 0.032 & <u>0.024</u> & 0.080 & 0.020 & 0.135 \\
Ours early interp. & 0.053 & 0.029 & 0.074 & 0.031 & 0.033 & 0.026 & 0.073 & 0.019 & 0.139 \\
Ours LITE & 0.057 & 0.030 & 0.084 & 0.034 & 0.035 & 0.026 & 0.081 & 0.021 & 0.141 \\
Ours & 0.053 & 0.028 & 0.080 & 0.031 & 0.031 & 0.025 & 0.077 & 0.019 & 0.136 \\
\end{tabular}

TABLE 2: **Quantitative comparison.** We compare the rendering quality on NeRF \(360^\circ\) Synthetic dataset \[40\]. The compared methods shaded in antique white represent neural implicit field approaches that lack editing capabilities, while the compared methods shaded in apricot correspond to neural rendering techniques with editing functionality. Compared to all editable methods, our method reaches the best rendering quality.

