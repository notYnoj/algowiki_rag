<tbc>UV space (across 4 atlas maps), and crops of the final renderings using varying loss weights. Without the on-ray loss, the predicted surface points collapse and cluster around discrete support points. Consequently, querying the texture map with these points fails to smoothly interpolate the texture, degrading the effective texture resolution. With the on-ray loss, the surface points are continuous and smoothly interpolate the surface, yielding much clearer details in the renderings.

### On-surface regularizer.

Figure 7a shows the ablation of the on-surface loss (close- to-surface). We visualize a depth map from a selected view alongside a side-view of the learned point cloud. Without the on-surface loss, the point cloud contains many noisy, off-surface points. Adding the on-surface loss significantly reduces these noisy points, resulting in a much smoother depth map with fewer holes.

### Evaluation of Distortion Loss

Figure 8 shows how the learned texture map depends on the weight of the proposed distortion loss in Sec. 4.2. Increasing the distortion-loss weight reduces UV distortion, which is crucial for preserving the shape of the edited texture.

### Correspondence Stability Under Deformation

We ablate the edit-time canonical correspondence used for UV lookup after deformation (Sec. 4.3). Specif

Xon-ray = 0
Xon-ray = 0.001
Xon-ray = 0.005
Xon-ray = 0.01

w/o on-surface loss
w/ on-surface loss
baseline
+ on-ray regularizer
+ deform-aware corr.
(a) The on-surface regularizer reduces noisy points and produces a smoother surface as shown in the depth maps.
(b) Ablation of canonical correspondence. Naïve correspondence (Eq. 11) exhibits texture drift while our deformation- aware correspondence (Eq. 13) improves stability.

**Fig.6:** Ablation of the on-ray regularizer with different weights. For each weight, we show the predicted surface points in 3D (left), the corresponding UV coordinates in the 2D atlas (middle), and the final rendered texture from texture maps (right). As shown, the on-ray loss ensures a better coverage of the surface, which leads to more uniform UV coordinates and gives a sharper texture in the renderings.

**Fig.7:** Ablation studies on geometry regularization and canonical correspondence.

