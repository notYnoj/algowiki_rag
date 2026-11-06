### 4.3 Neural Deferred Shading

The rich high-dimensional signal yielded by the volume rendering of _Harmonic Textures_ enables a more efficient decoding strategy. We concatenate the accumulated harmonics with the ray direction **d** encoded using second-degree spherical harmonics \(\mathrm{SH}_2(\mathbf{d})\in\mathbb{R}^9\) as done in \[49\], and decode the final pixel color **c** using a shallow MLP, without further positional encoding. The resulting rendering equation is

\(\mathbf{c}=\mathrm{MLP}_\theta\left(\sum_{i\in\mathcal{G}}\alpha_iT_i\left[\begin{array}{ c }
\mathrm{sin}(\mathbf{f}_i) \\
\mathrm{cos}(\mathbf{f}_i)
\end{array}\right],k\cdot\mathrm{SH}_2(\mathbf{d})\right),\) (3)

where \(\mathbf{f}_i=\mathrm{interpolate}\big(\big[\mathbf{f}_i^0,\mathbf{f}_i^1,\mathbf{f}_i^2,\mathbf{f}_i^3\big],\mathbf{p}_i^*\big)\) denotes the primitive feature interpolated at the point \(\mathbf{p}_i^*\) of maximum response, G is the set of primitives intersected by the ray, and \(\alpha_i\) and _T<sub>i</sub>_ correspond to the primitive opacity and accumulated transmittance defined in Eq. (2).

### 5 Results

We present our results for radiance-field novel-view synthesis. Additionally, we demonstrate our method on two other reconstruction tasks: semantic scene reconstruction and high-resolution image fitting.

#### 5.1 Radiance Field Reconstruction

#### Optimization

We directly adopt the densification strategy, loss function and regularization terms of 3DGS-MCMC \[28\]. Specifically, they define the regularization terms on primitive opacity and scale as

\(\mathcal{R}_\alpha=\frac{1}{P}\sum_{i=1}^P\alpha_i,\mathcal{R}_s=\frac{1}{P}\sum_{i=1}^P\|\mathbf{s}_i\|_1,\) (4)

where _P_ is the number of primitives and **s**_<sub>i</sub>_ is the scale vector of primitive _i_. Our final loss function is the same as 3DGS-MCMC:

\(\mathcal{L}=(1-\lambda)\mathcal{L}_{\mathrm{L}_1}+\lambda\mathcal{L}_{\mathrm{D}-\mathrm{SSIM}}+\lambda_\alpha\mathcal{R}_\alpha+\lambda_s\mathcal{R}_s.\) (5)

Similarly to the exponential scheduling applied to primitive positions \[27\], we use a cosine annealing scheduler for the feature and MLP learning rates. We also apply an Exponential Moving Average (EMA) filter \[49\] to the MLP weights \(\theta\). This enhances robustness to noise and avoids overfitting to individual frames:

\(\bar{\theta}_t\leftarrow\gamma\bar{\theta}_{t-1}+(1-\gamma)\theta_t,\) (6)

where \(\bar{\theta}_t\) denotes the filtered weights at step _t_ and \(\gamma\) is the decay factor. Finally, we dedicate the last 3000 training iterations to optimize only the feature and MLP weights, disabling all regularization terms and freezing all other parameters. We found that this refinement step slightly improves color fidelity, particularly in large-scale scenes. Other hyperparameters are included in the supplementary material.

