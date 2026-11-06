## D Additional Novel View Synthesis Results

We show qualitative novel view synthesis comparison using either 5,000 primitives or their originally suggested number of primitives for each method in Figure 15 and Figure 16. As shown, our method achieves rendering quality comparable to or better than the baselines while using only 30,000 primitives.

We further evaluate PointGT for novel view synthesis on the real-world scenes of the MipNeRF360 dataset [1].  3 reports per-scene PSNR, SSIM, and LPIPS. We compare against the 3D Gaussian Splatting [10], the textured Gaussian baselines, and the PAPR [31]. As full resolution training exceeds the memory of our GPUs, we evaluate both PAPR and PointGT at _half_ the resolution of the MipNeRF360 dataset. The numbers for the Gaussian splatting-based baselines are from their original papers.

Flag
Dress
Bird
Learned Texture Map from Texture-GS
Learned Gaussians
Rendering

**Fig.13:** Texture-GS [27] may fail to learn a reasonable texture map that is valid for texture editing.

