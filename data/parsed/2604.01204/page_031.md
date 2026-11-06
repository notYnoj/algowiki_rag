<tbc>where <o>DSSIM</o><sub>t</sub> is the mean DSSIM (per-pixel structural dissimilarity) of tri- angle _t_ and \(\alpha=0.75\) is the area-weighting exponent. The area weighting prevents repeated splitting of tiny, high-error triangles and distributes vertices more evenly in proportion to their spatial impact. Triangles with fewer than 3 pixels are excluded from scoring.

At each densification step, we insert centroid vertices for the top-scoring triangles (up to \(0.35\times V\) new vertices, where _V_ is the current count), initialize their features by averaging the parent triangle’s vertex features, and re-run Delaunay triangulation on the full vertex set. We also detect when the mesh becomes degenerate (e.g. due to vertices becoming colinear) and re-mesh, although this rarely occurs in practice.

### 3.4 CUDA Rasterizer

All rasterization and interpolation operations are implemented as custom forward and backward CUDA kernels, supporting both full-image rendering and batched pixel-query modes. Training generally takes between 1-3 minutes in an RTXA6000 Ada.

### 3.5 Post-Training Compression

We also briefly explore the use of post-training compression techniques to further reduce storage requirements.

We compress vertex positions to `UInt16`, vertex features to uniform `Int8` (with a per-channel scale and offset), and MLP weights to `FP16`. An entropy coder (Zstandard, level 19) is applied to the serialized payload. Combining these techniques, the resulting images can be compressed by an additional factor of approximately 3\(\times\) beyond the training result, with negligible quality loss. Tab. 15 summarizes the results of the post-training compression techniques.

### 3.6 Per-Image Results

Tabs. 16 and 17 provide per-image results for the 2D image fitting experiment at 10\(\times\) and 100\(\times\) compression ratios, respectively. We provide visual comparisons in Fig. 7 and Fig. 4. Our method achieves competitive PSNR in both \(\mu\)-law and tonemapped spaces while substantially outperforming Instant NGP in perceptual quality (LPIPS). The advantage is most pronounced at high compression ratios, where the non-overlapping mesh topology and _C_<sup>1</sup> feature interpolation avoid the ringing and block artifacts that plague hash-grid methods.

Tab. 18 provides the full set of hyperparameters for the 2D image fitting experiment.

