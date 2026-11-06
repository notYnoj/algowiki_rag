<tbc>PSNR, LPIPS \[59\], and SSIM \[50\] metrics on the albedo map as well as the average number of 3D Gaussians of octant and full voxel aligned 3D Gaussian Splatting across our Objaveverse subset. Fig. 6 also presents some visual results of our Gaussian fitting. These results demonstrate that the proposed octant-aligned 3D Gaussian produces a much more reasonably compact and precise representation of diverse and complex 3D assets with much fewer 3D Gaussians compared to the full voxel version.

### Essentials of different losses

We verify the importance of different losses we proposed to train our model. We term all the losses calculated on 2D image space as _L_<sub>2D</sub>:

\(L_{2\mathrm{D}}=L_\mathrm{albedo}+L_\mathrm{R}+L_\mathrm{M}+L_\alpha.\) (7)

We train two additional TexGaussian models using only the _L_<sub>2D</sub> or _L_<sub>3D</sub> loss on ShapeNet `car` category due to its large variations and complexity of texture to validate their effectiveness. It is worth noting that in this dataset, \(L_{2\mathrm{D}}=L_\mathrm{albedo}+L_\alpha\) due to the lack of material information. The training curves of MSE loss and LPIPS loss between rendering images and ground-truth ones are shown<tbc>

<tbc>in Fig. 7, which demonstrate the effects of _L_<sub>2_D_</sub> and _L_<sub>3_D_</sub>. From the loss curves, we can conclude that _L_<sub>3D</sub> facilitates the process of convergence and _L_<sub>2_D_</sub> enhances the quality of synthesized images, as evidenced by the large margin of improvement in the LPIPS loss when introducing _L_<sub>2_D_</sub>. We also provide some qualitative results to verify the effectiveness of _L_<sub>2_D_</sub> on the test set of `car` category in Fig. 8. Only using _L_<sub>3_D_</sub> results in a relatively blurry texture map due to the discreteness of 3D Gaussian which is similar to the characteristic of 3D point clouds analyzed above.

## 5 . Conclusion

In this paper, we proposed TexGaussian, an octree-based 3D Gaussian Splatting model for high-quality PBR material generation on untextured meshes. We aligned each 3D Gaussian on the octant of the corresponding octree built from the input untextured object and extended the parameters of 3D Gaussian with additional channels to represent the roughness and metallic map. We trained our model with regression objectives, achieving faster inference speed compared to previous texture synthesis methods. Experimental results demonstrated that our method is capable of generating high-quality PBR materials that are readily usable in modern graphics engines for photo-realistic rendering, offering enhanced realism for a variety of applications.

### Limitations

The generalization of TexGaussian is still hindered by the scale of the training set. Thus it struggles to generate various textures for some extremely complex 3D objects beyond our training data. We are looking forward to training our TexGaussian model with more parameters and more data on a larger-scale GPU cluster in the future.

\begin{tabular}{cccccc}
\multirow{2}{*}{Methods} & \multicolumn{2}{c}{Albedo} & \multicolumn{2}{c}{PBR rendering} & \multirow{2}{*}{Time} \\
 & FID\(\downarrow\) & KID\(\downarrow\) & FID\(\downarrow\) & KID\(\downarrow\) & \\
Fantasia3D \[9\] & 213.21 & 0.96 & 209.87 & 0.48 & 22.7mins \\
FlashTex \[14\] & 185.24 & 1.13 & 186.82 & 0.42 & 20.3mins \\
DreamMat \[60\] & 152.63 & 1.09 & 145.49 & 0.19 & 48.2mins \\
Ours & **123.72** & **0.20** & **129.52** & **0.02** & **21.04s** \\
\end{tabular}

\begin{tabular}{ccccc}
Method & \multicolumn{4}{c}{PSNR \(\uparrow\) LPIPS \(\downarrow\) SSIM \(\uparrow\) 3D Gaussian Number} \\
Full voxel aligned & 23.75 & 0.17 & 0.92 & 16,777,216 (256<sup>3</sup>) \\
Octant-aligned & **32.60** & **0.039** & **0.97** & **79,480** \\
\end{tabular}

Ground truth
Octant-aligned
Voxel-aligned

MSE Loss
LPIPS Loss
0.030
0.16
Full Model
Full Model
0.025
Without L3D
Without L2D
0.14
Without L3D
Without L2D
0.020
0.12
0.015
0.10
0.010
0.08
0.005
0.06
0
10
20
30
40
50
0
10
20
30
40
50
Training Batches (1k)
Training Batches (1k)

w/o L2D
Full Model

2. Quantitative comparison of the FID and KID (\(\times 10^2\)) scores as well as the inference time of TexGaussian and other methods on our test set which consists of 200 3D objects with ground truth PBR materials.

3. Quantitative comparison of methods using different types of 3D Gaussian Fitting.

Figure 6. Visualization of different manners of Gaussian fitting. The rendering results demonstrate excellent reconstruction performance of the proposed octant-aligned 3D Gaussian Splatting.

Figure 7. The training loss curves of our model with different losses.

Figure 8. Results of our model trained with and without _L_<sub>2_D_</sub>.

