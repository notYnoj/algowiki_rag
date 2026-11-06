<tbc>Paint3D \[56\], and TexPainter \[57\] whose input text prompts are set to "a \*" and "\*’ is the name of corresponding category. Due to the relatively long time consumption, we only use 50 3D objects selected from the test set to evaluate the methods based on 2D diffusion models. We conduct only a qualitative comparison for TexPainter \[57\] for its lengthy processing time.  1 reports the comparison of FID and KID scores as well as average inference time on a single NVIDIA A100 (40G) GPU. It is worth noting that our model only takes about one second to predict the parameters of each 3D Gaussian and the rest of the time is used for texture baking. From  1, we have the following observation. First, our method obtains the best performance in terms of FID and KID. For example, our method outperforms TexOct \[26\], by an average of 9.69 in FID and 0.53 in KID. These improvements indicate that our method excels at generating high-quality textures. Second, TexGaussian achieves the fastest generative speed in all categories, which is much less time-consuming than other methods.

## Qualitative Comparison

Fig. 4 provides some qualitative results on the same input 3D meshes by different methods. Point-UV \[55\] and TexOct \[26\] use colored point clouds as supervision to train diffusion models. As a consequence, the generated texture map is relatively blurry due to the discreteness of the point cloud. For other methods that leverage pre-trained 2D diffusion prior, they can hardly comprehend the total geometry. The generated texture maps<tbc>

<tbc>by them are not consistent with the semantics of input 3D mesh, such as the chaotic stripes on the bench and chair in Fig. 4. On the contrary, our method generates smooth and colorful RGB textures on unseen objects, which align well with 3D meshes.

\begin{tabular}{cccccccccccc}
\multirow{2}{*}{Methods} & \multicolumn{2}{c}{Average} & \multicolumn{2}{c}{Bench} & \multicolumn{2}{c}{Car} & \multicolumn{2}{c}{Chair} & \multicolumn{2}{c}{} & \multirow{2}{*}{Time} \\
 & FID\(\downarrow\) & KID\(\downarrow\) & FID\(\downarrow\) & KID\(\downarrow\) & FID\(\downarrow\) & KID\(\downarrow\) & FID\(\downarrow\) & KID\(\downarrow\) & FID\(\downarrow\) & KID\(\downarrow\) & \\
Point-UV (1-Stage) \[55\] & 88.43 & 5.78 & 64.96 & 1.44 & 186.10 & 17.57 & 46.23 & 1.93 & 56.42 & 2.19 & 39.92s \\
Point-UV (2-Stage) \[55\] & 61.49 & 2.67 & 67.48 & 1.61 & 89.38 & 5.82 & 41.33 & 1.53 & 47.75 & 1.72 & 49.75s \\
TexOct \[26\] & 59.45 & 2.60 & 60.46 & 0.97 & 90.10 & 6.11 & 37.70 & 1.36 & 49.52 & 1.97 & 17.44s \\
Ours & **49.76** & **2.07** & **46.37** & **0.44** & **80.20** & **5.22** & **29.96** & **1.09** & **42.52** & **1.54** & **11.02s** \\
TEXTure \[41\] & 169.82 & 7.94 & 152.53 & 5.28 & 236.58 & 18.52 & 119.71 & 2.86 & 170.46 & 5.11 & 132.21s \\
Text2Tex \[8\] & 156.62 & 6.68 & 154.95 & 5.79 & 188.60 & 15.06 & 125.34 & 3.11 & 157.57 & 2.77 & 1005.58s \\
Paint3D \[56\] & 135.25 & 4.67 & 104.16 & 1.68 & 204.22 & 13.06 & 104.64 & 2.24 & 127.98 & 1.71 & 231.56s \\
Ours & **100.97** & **1.88** & **86.37** & **0.75** & **117.53** & **5.20** & **94.89** & **0.57** & **105.09** & **0.95** & **11.12s** \\
\end{tabular}



Point-UV
TexOct
Text2Tex
TEXTure
Paint3D
TexPainter
Ours

1. Quantitative comparison of the FID and KID (\(\times 10^2\)) score as well as the inference time of TexGaussian and other methods on the ShapeNet dataset \[7\]. The top part reports the comparison with methods that also train per-category models on ShapeNet. The bottom part reports the comparison with 2D diffusion-based methods, which select 50 samples from the test set of each category.

Figure 3. Unconditional RGB texture generative results on ShapeNet. Please zoom in for a better inspection of color details.

Figure 4. Examples of generated RGB textures obtained by Tex- Gaussian and other state-of-the-art models on the same 3D object. Please zoom in for a better inspection.

