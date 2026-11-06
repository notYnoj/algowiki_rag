### Objective.

We combine the regularizers with PAPR’s rendering loss for pre- training:

\(\mathcal{L}_\text{rendering}+\gamma\mathcal{L}_\text{close2ray}+\eta\mathcal{L}_\text{close2surface},\) (7)

where L<sub>rendering</sub> is PAPR’s rendering loss, \(\gamma\) and \(\eta\) are the coefficients of the regularizers.

## 4.2 Learning UV Mapping

Building upon the regularized point cloud geometry, we extract ray-surface intersections to learn a multi-chart UV atlas and a 2D texture map. We sample foreground rays from the training views, compute their canonical-space intersection points \(\mathbf{x}_i^\text{can}\), and optimize a continuous neural UV parameterization over these surface samples.

### Distortion loss without normals (Jacobian regularization).

To enable consistent texture editing and encourage an even allocation of texture resolution across the scene, it is crucial to minimize the distortion of the learned UV mappings. While existing surface parameterization methods \[20\] typically rely on ground-truth geometry normals to compute conformal and stretch penalties, point-based representations natively lack this explicit geometric connectivity and normal information. To overcome this, we define a distortion loss directly over the Jacobians of the texture coordinate mappings.

Specifically, for each chart _k_ in our multi-chart texture maps, we compute the Jacobian matrix \(\mathbf{J}_{ik}\in\mathbb{R}^{2\times 3}\) of the UV mapping by taking the gradients of the texture coordinates \(\mathbf{u}_{ik}\in\mathbb{R}^2\) w.r.t. the 3D point coordinates **x**_<sub>i</sub>_. The Jacobian’s singular values \(\sigma_{ik}^1\) and \(\sigma_{ik}^2\) characterize the local scaling behavior of the mapping. To minimize anisotropic scaling distortion, we minimize the squared difference of the singular values across all charts:

\(\mathcal{L}_\text{scaling}=\frac{1}{Gn}\sum_{i=1}^G\sum_{k=1}^n\left(\sigma_{ik}^1-\sigma_{ik}^2\right)^2,\) (8)

where _G_ is the total number of 3D points. This encourages the texture coordinate network to learn mappings with isotropic scaling (where \(\sigma^1=\sigma^2\)). While L<sub>scaling</sub> minimizes anisotropy, it does not explicitly prevent area shrinkage or blow-up. To address this, we also define an area distortion penalty, \(\mathcal{L}_\text{area}=\frac{1}{Gn}\sum_{i=1}^G\sum_{k=1}^n(log(\sigma_{ik}^1\sigma_{ik}^2))^2\), which regularizes the local scale to remain close to 1 and heavily penalizes near-zero areas, preventing degenerate mappings. We define the distortion loss as the sum of these two terms:

\(\mathcal{L}_\text{distortion}=\mathcal{L}_\text{scaling}+\mathcal{L}_\text{area}.\) (9)

In practice, we optimize the UV atlas by minimizing a weighted sum of Nuvo \[20\]’s losses (excluding the normal-based distortion terms) and the proposed distortion loss L<sub>distortion</sub>. We jointly learn a 2D RGB texture map by supervising rays with PAPR-predicted colors using bilinear sampling on the atlas; we use the learned texture map for texture editing.

