### Vertex gradient estimation.

The Clough-Tocher scheme requires per-vertex gradients. We estimate these via a per-vertex least-squares fit over the one-ring neighborhood: for each vertex _v_, we gather all neighbor vertices \(\{v_j\}_{j\in\mathcal{N}(v)}\) and solve

\(\nabla f_v=\mathbf{A}_v^{-1}\mathbf{b}_v,\mathbf{A}_v=\sum_j\Delta\mathbf{p}_j\Delta\mathbf{p}_j^\top,\mathbf{b}_v=\sum_j\Delta f_j\Delta\mathbf{p}_j,\) (8)

where \(\Delta\mathbf{p}_j=\mathbf{p}_j-\mathbf{p}_v\) and \(\Delta f_j=f_j-f_v\). The \(2\times 2\) system is solved analytically per vertex in a CUDA kernel. This operation is differentiable and computed at every forward pass, enabling gradients to flow through the vertex topology.

### Feature encoding and MLP.

Feature encoding and MLP decoding are the same as in the main scene reconstruction task.

## 3.2 Training

### Pixel sampling.

At each iteration, we sample a batch of pixels via stratified sampling. Ground-truth values at sub-pixel coordinates are obtained via bilinear interpolation on the target image, implemented as a CUDA texture lookup for efficiency.

### Optimizers and schedules.

We use Adam \[29\] with separate parameter groups for positions (lr=10<sup>-4</sup>), features (\(\mathrm{lr}=5\times 10^{-3}\)), and MLP weights (\(\mathrm{lr}=5\times 10^{-5}\)). An exponential decay schedule is applied after 20000 iterations with a factor of 0.33 every 10000 steps, following Instant NGP \[49\].

### Loss function.

We train with a pixel-wise MSE loss in \(\mu\)-law encoded space. We found this to produce better results than using the relative L2 loss suggested in the Instant NGP paper. Raw 14-bit sensor values _x_ are transformed as \(f(x)=\mathrm{log}(1+\mu x/w)/\mathrm{log}(1+\mu)\) with \(\mu=5000\) and _w_=2<sup>14</sup>-1=16,383 (the white level of 14-bit data). This compresses the dynamic range before supervision, placing relatively more emphasis on shadow detail, which is standard in HDR imaging pipelines.

## 3.3 Coarse-to-Fine Densification

Training begins from a sparse mesh initialized via _edge-aware sampling_: we compute Sobel gradient magnitudes on a downsampled version of the target image and sample initial vertex positions proportionally to edge strength, with a small uniform floor for coverage. The result is a Delaunay triangulation of the sampled points, with boundary vertices ensuring full image coverage.

The mesh is progressively refined through densification. Every 500 iterations (starting at iteration 1500 and ending at 15000), we score each triangle by

\(\mathrm{score}_t=\overline{\mathrm{DSSIM}_t}\cdot|\mathrm{pixels}_t|^\alpha,\) (9)

