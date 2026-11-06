<tbc>**Step 2 (attention-weighted displacement fusion).** Since point identity is preserved under deformation, each deformed neighbor \(\mathbf{p}_{ij}^\mathrm{def}\) has a corresponding canonical position \(\mathbf{p}_{ij}^\mathrm{can}\). We compute per-neighbor displacements and fuse them using the _same_ deformed-space attention weights, then transfer the ray-projected deformed intersection back to canonical space:

\(\mathbf{t}_i=\sum_{j=1}^Ka_{ij}^\mathrm{def}\left(\mathbf{p}_{ij}^\mathrm{can}-\mathbf{p}_{ij}^\mathrm{def}\right),\mathbf{x}_i^\mathrm{can}=\mathbf{x}_i^\mathrm{def}+\mathbf{t}_i.\) (13)

We then query the UV atlas at \(\mathbf{x}_i^\mathrm{can}\) and sample the (edited) texture map to render appearance. Intuitively, even if attention weights are sparse, ray projection keeps \(\mathbf{x}_i^\mathrm{def}\) distributed along rays, and the fused displacement provides a stable canonical transfer for UV lookup.

_Edit-order interchangeability._ PointGT supports flexible and simultaneous geometry and texture editing; the order of applying geometry and texture edits is interchangeable, which is important for applications such as 3D character design where edits are applied iteratively in varying order.

## 5 Experiments

We evaluate PointGT along two axes: (i) **simultaneous geometry and texture editing** under _non-rigid deformation_, where texture edits should persist without drifting (Sec. 4.3), and (ii) **novel view synthesis** quality compared to recent textured Gaussian splatting baselines.

### 5.1 Implementation Details

When pre-training PAPR with geometry regularization (Sec. 4.1), we use \(\gamma=0.002\) and \(\eta=0.01\) for the close-to-ray and close-to-surface losses. Since geometry is unreliable early in training, we start applying the regularizers at step 25,000

Top K points around ray Deformed Space Canonical Space UV Space Ray in deformed space Translation vectors Predicted surface point = + a def

**Fig.3:** Illustration of the deformation-aware canonical correspondence. In deformed space (left), a ray intersects the deformed point cloud to predict a surface point (red). Each deformed neighbor (dark blue) has a stored canonical counterpart (light blue); the per-neighbor displacements (dashed gray arrow) are fused with the deformed-space attention weights to transfer the intersection back to canonical space (middle), where UV lookup retrieves the texture (right).

