<tbc>In future work, we would like to investigate the feasibility of extracting automatic Level of Detail from a finer-grained harmonic decomposition. Given the generality of Neural Harmonic Textures, applications beyond novel view synthesis such as radiance caching, neural physically-based rendering and geometric reconstruction are also of great interest. Finally, our work opens the possibility of removing kernel functions entirely, as we can still propagate derivatives to explicit geometry without the spatially decaying opacity function, potentially enabling drastic performance gains.

### Conclusion

We presented Neural Harmonic Textures, which combine particle- anchored feature vectors, harmonic activations, and a single image-space decoding pass to achieve state-of-the-art results in novel view synthesis. Our method consistently outperforms baselines across different particle counts, trains rapidly, and has high inference performance. Moreover, it is compatible with existing deferred-shading rendering pipelines and supports a wide range of applications, from lifting semantic fields to high-resolution image reconstruction and beyond.

### Acknowledgements

We would like to thank Ruilong Li and Martin Bisson for helpful discussions. Jorge Condor and Piotr Didyk acknowledge funding from the Swiss National Science Foundation (SNSF, Grant 200502) and an academic gift from Meta.

\begin{tabular}{cccccc}
Ratio & Method & PSNR\(_\mu\uparrow\) & PSNR\(_\mathrm{tm}\uparrow\) & SSIM\(_\mathrm{tm}\uparrow\) & LPIPS\(_\mathrm{tm}\downarrow\) \\
\multirow{3}{*}{10\(\times\)} & JPEG-XL \[26\] & **45.31** & **44.66** & **0.994** & **0.001** \\
 & Instant NGP \[49\] & 37.63 & 38.91 & 0.949 & 0.061 \\
 & NHT (Ours) & 37.16 & 39.87 & 0.963 & 0.023 \\
\multirow{3}{*}{100\(\times\)} & JPEG-XL \[26\] & **38.53** & 35.54 & **0.971** & **0.017** \\
 & Instant NGP \[49\] & 35.17 & 36.39 & 0.923 & 0.078 \\
 & NHT (Ours) & 35.06 & **36.43** & 0.927 & 0.048 \\
\end{tabular}

Original
Original
Instant NGP
Instant NGP
Ours
Ours
Ours
Ours

** 5:** High-resolution (45.7 MP) 14-bit HDR RAW image fitting, averaged over 15 images. We report PSNR in \(\mu\)-law transformed space (PSNR\(_\mu\)), common in HDR pipelines. PSNR, SSIM, and LPIPS are also computed on tonemapped images (subscript "tm"). All methods use the same memory budget per compression ratio.

**Fig.7:** Comparison of our work vs Instant NGP on a 100\(\times\) compression task. Original images are 45.7 MP 14-bit HDR RAW files. We achieve substantially superior perceptual quality at equal compression and similar training times.

