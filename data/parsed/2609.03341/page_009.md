### 4.3 Geometry and Texture Editing

#### Texture editing in UV space.

PointGT supports texture editing by directly modifying the 2D texture atlas. Given an edited texture map \(\mathbf{T}'\), we generate a mask map \(\mathbf{M}\in[0,1]^{n\times h\times w}\) by comparing the original atlas **T** and the edited atlas \(\mathbf{T}'\), where the pixel values are marked as 1 in edited regions and 0 otherwise. During rendering, for each ray we compute the UV coordinate **u**_<sub>i</sub>_ of its intersection and replace the sampled color with the edited texture when _m<sub>i</sub>_=**M**(**u**_<sub>i</sub>)\>_0.95 (both using bilinear interpolation on the atlas).

#### Geometry editing and the correspondence problem.

Geometry editing applies a non-rigid deformation to the learned point cloud, producing deformed point positions \(\mathbf{p}_j^\mathrm{def}\) from canonical positions \(\mathbf{p}_j^\mathrm{can}\) (Sec. 3.1). Rendering after deformation produces a deformed-space ray-surface point by interpolating deformed neighbor positions with deformed-space attention weights:

\(\hat{\mathbf{x}}_i^\mathrm{def}=\sum_{j=1}^Ka_{ij}^\mathrm{def}\mathbf{p}_{ij}^\mathrm{def},\) (10)

where the top-_K_ neighbors \(\mathbf{p}_{ij}^\mathrm{def}\) are selected by ray proximity in the deformed point cloud, and the weights \(a_{ij}^\mathrm{def}\) are _re-inferred_ in deformed space (i.e., both the neighbor set and weights are recomputed after deformation). However, the UV atlas is trained in canonical space, so we must transfer \(\hat{\mathbf{x}}_i^\mathrm{def}\) back to a canonical coordinate before UV lookup.

#### Why a naïve transfer fails.

A natural approach is to reuse the deformed attention weights to directly interpolate _canonical_ neighbor positions:

\(\mathbf{x}_{i,\mathrm{naive}}^\mathrm{can}=\sum_{j=1}^Ka_{ij}^\mathrm{def}\mathbf{p}_{ij}^\mathrm{can}.\) (11)

In practice, attention weights in PAPR are often sparse; Eq. 11 therefore collapses many rays’ canonical lookup points onto a small subset of support points, causing discontinuous UV jumps across neighboring rays and visible texture popping/drift under deformation. While the on-ray regularizer (Sec. 4.1) improves training stability, it does not guarantee that intersections remain exactly on rays under extreme non-rigid, non-training deformations.

#### Deformation-aware canonical correspondence.

To address this, we propose an edit-time transfer rule that maps each deformed-space ray-surface point back to canonical space while keeping samples well-distributed. **Step 1 (point-to-ray projection).** We strictly enforce the on-ray constraint by orthogonally projecting \(\hat{\mathbf{x}}_i^\mathrm{def}\) onto its ray **r**_<sub>i</sub>_:

\(\mathbf{x}_i^\mathrm{def}=\Pi_{\mathbf{r}_i}\big(\hat{\mathbf{x}}_i^\mathrm{def}\big),\) (12)

