## Compared Methods.

We group baselines into three categories: 1) _Backbone-only NVS without SR_: TensorRF \[4\], Instant-NGP \[26\], and 3D Gaussian Splitting (3DGS) \[16\]. Since these methods do not perform SR, we upsample their LR outputs using bicubic interpolation (\(\times 2\), \(\times 4\)). 2) _NeRF- based SR_: NeRF-SR \[33\] and FastSR-NeRF \[19\]. Both re<tbc>

<tbc>quire HR reference supervision, which limits their applicability in low-resolution only settings. As FastSR-NeRF is not open-sourced, we directly report the numbers from their paper; hence, no visual comparison is available. 3) _3DGS + video SR_: SuperGaussian \[30\], which adapts pretrained video SR models to upsample continuous 3DGS renderings.

TensoRF + Bicubic
Instant-NGP
3DGS
Nerf-SR
SuperGaussian
TensoRF + Ours
Instant-NGP + Ours
3DGS + Ours
LR+Ours
GT

TensoRF + Bicubic
Instant-NGP
3DGS
LR + Bicubic
NeRF-SR
3DSR
TensoRF + Ours
Instant-NGP + Ours
3DGS + Ours
LR + Ours
GT

Figure 3. The qualitative comparison of our method on the Blender datasets, with input images at 200\(\times\)200 resolution and \(\times 4\) super- resolution. The leftmost images show the low-resolution inputs, while the images highlighted in red correspond to our results. Compared with other methods that fail to recover fine structures, our approach successfully reconstructs sharp and detailed results. Notably, our method consistently enhances regions where other approaches produce blurred or low-frequency reconstructions.

Figure 4. The qualitative comparison of our method on the LLFF datasets, with input images at 200\(\times\)200 resolution and \(\times 4\) super- resolution.The leftmost images show the low-resolution inputs, while the images highlighted in red correspond to our results. Our method successfully reconstructs fine details in leaves and architectural structures, and consistently improves reconstruction quality in regions where other methods exhibit degraded results.

