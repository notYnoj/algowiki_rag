### 2D image reconstruction.

Finally, we show results on 2D image fitting. To adapt our method to this application, we make two key changes with respect to the primitive-based approaches. First, we employ a connected 2D triangle mesh topology. This mesh is fully opaque: there is no alpha blending, no Gaussian or window kernel, simply interpolation of local features for a given pixel. Second, we change our barycentric interpolation to Clough-Tocher cubic interpolation. This makes interpolated features continuous over the triangle edges, which removes high frequency artifacts. The rest of the architecture is the same as described in Sec. 4, and we include further details on the optimization strategy in the Supplementary. We evaluate image reconstruction performance on a new curated dataset of high-resolution (45.7 MP) 14-bit HDR RAW images, and compare it against Instant NGP \[49\] and the JPEG-XL encoder \[26\], which supports high- dynamic range. We measure reconstruction quality at two compression ratios (10\(\times\) and 100\(\times\)), computing PSNR in \(\mu\)-law transformed space (PSNR\(_\mu\)), standard in HDR imaging pipelines. We also report metrics on tonemapped images (subscript "tm"). Results are shown in Tab. 5. Our method achieves comparable pixel-error quality to Instant NGP in both HDR and linear spaces, while substantially reducing perceptual error: at 100\(\times\) compression, NHT achieves an LPIPS of 0.048 compared to 0.078 for Instant NGP, a 38% relative improvement. JPEG- XL however still comes out on top, particularly in perceptual metrics, which is to be expected given its human-perception-based inductive biases. We can further compress our representation by a factor of 3 without noticeable loss in quality by aggressively reducing floating point precision of the implicit features, among other strategies. We include more details on this in the supplementary.

## 6 Discussion

### Limitations and future work

Our method focuses on increasing per-primitive expressivity, which has inherent downsides. In particular, our method can overfit to individual views in scenarios with very sparse supervision, leading to lower novel view synthesis performance. Furthermore, while our method consistently achieves 140+ frames per second at inference time, the additional neural decoder results in slightly slower rendering than pure 3DGS methods(Tab. 2).

\begin{tabular}{ccccccc}
Method & RGB\(_\text{PSNR}\uparrow\) & RGB\(_\text{SSIM}\uparrow\) & RGB\(_\text{LPIPS}\downarrow\) & LSEG\(_\text{P}\uparrow\) & LSEG\(_\text{C}\uparrow\) & FPS\(\uparrow\) \\
Feature 3DGS \[82\] & 26.27 & 0.785 & 0.262 & 43.68 & 0.985 & 3.02 \\
Neural Harmonic Textures (Ours) & **28.16** & **0.824** & **0.228** & **46.90** & **0.993** & **28.11** \\
\end{tabular}

** 4:** Joint RGB and LSEG semantic feature reconstruction on MipNeRF360 \[2\], (RTX A6000 Ada). LSEG<sub>P</sub> and LSEG<sub>C</sub> denote PSNR and cosine similarity of the 512-dim semantic features, respectively. We use 80 features per primitive and a 128\(\times\)3 MLP, while Feature 3DGS uses 176 features per primitive, 512\(\times\)128 CNN and 1.5\(\times\) the number of primitives we use, resulting in an approximately 3\(\times\) higher memory footprint.

