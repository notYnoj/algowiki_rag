<tbc>After obtaining the predicted contour mask _M<sub>c</sub>_, we remove the original contour by inpainting the masked region with the interior texture of the input drawing, as illustrated in Fig. 5. To eliminate the impact of the background color (always white) on the inpainting region, we extend _M<sub>c</sub>_ by adding the background region (1-_M_) into it to get the inpainting region mask _M<sub>inpaint</sub>_:<tbc>

\(M_{inpaint}=M_c\cup(1-M).\) (1)

<tbc>Next, we inpaint the pixels within _M<sub>inpaint</sub>_ heuristically based on a fast marching method \[Telea 2004\]. That is, each pixel in _M<sub>inpaint</sub>_ is replaced by a normalized weighted sum of the neighboring pixels in (1-_M<sub>inpaint</sub>_). In a word, we compute the inpainted drawing _I<sub>inpaint</sub>_ without contour by

\(I'_{inpaint}=FastMarching(I,M_{inpaint});I_{inpaint}=I'_{inpaint}\cdot M+I\cdot(1-M).\) (2)

Please refer to supplemental materials for more details and a comparison of different methods for contour removal.

## 3.2 3D Character Generation

### 3.2.1 Coarse Reconstruction.

To reconstruct a 3D character from a single contour-free drawing, we use a pre-trained diffusion model, Wonder3D \[Long et al. 2024\], to produce multi-view normal maps and color images. We choose Wonder3D as our backbone since it uses an orthographic camera setting, which helps to keep strong generalizations on amateur character drawings. We apply an off- the-shelf segmentation network, IS-Net \[Qin et al. 2022\], to segment these normal maps to get the corresponding foreground masks. Then we utilize a neural surface reconstructor, Instant-NSR \[Guo 2022; Zhao et al. 2022\], to reconstruct a textured geometry from these 2D representations. However, the obtained shape and texture are both far from satisfactory. As observed from Fig. 8 (d), the thin structures of the reconstructed shape might become much thicker than those in the input drawings. In some cases, there could even be adhesion on the surface, as shown in Fig. 6, leading to geometry artifacts. Besides, the predicted texture appears blurry and loses details. These phenomena may result from the roughness of mask prediction and the misalignment of multi-view information.

### 3.2.2 Shape Cutting.

To refine the reconstructed shape, we employ front-view cutting on the queried SDF using the front-view mask<tbc>

<tbc>_M_<tbc>

<tbc>. Thus, the trimmed geometry can be defined by the 0 level set:

\(\mathcal{G}=\left\{(x,y,z)\in\mathbb{R}^3|f(x,y,z)\le 0,M(X,Y)=1\right\},\) (3)

where \(f(\cdot)\) is the SDF and (_X,Y_) is the projected 2D coordinates on the front-view plane of any 3D sampling point (_x,y,z_). Then we pass the level set to the Marching Cubes algorithm \[Lorensen and Cline 1998\] to extract the trimmed geometry, as shown in Fig. 8 (e). However, the front-view cutting operation can only change the silhouette of the front but not the thickness of the side.

### 3.2.3 Skeleton-based Thinning Deformation.

To reduce the thickness of the side, we design a skeleton-based shape deformation algorithm to thin these regions without changing the front-view boundary. We solve it as a bi-harmonic problem \[Botsch and Kobbelt 2004\]. Given a trimmed geometry G, we denote its vertices as **v** and its faces as **f**. Thus, we can easily thin G by deforming it following

\(\mathbf{v}'=\mathbf{v}+\mathbf{d};\mathbf{d}=\mathcal{B}(\mathbf{v},\mathbf{f},\mathbf{h},\mathbf{d}_\mathbf{h}).\) (4)

where **d** represents a deformation field obtained from \(\mathcal{B}(\cdot)\) that computes bi-harmonic maps using a uniform Laplacian operator \[Jacobson et al. 2018\]. We estimate the whole deformation field _d_ based on the known displacements **d<sub>h</sub>**, where **h** denotes handle indices.

We next explain how we locate the handle vertices. We divide handle vertices into two categories (fixed and move-needed) to determine whether a local structure requires thinning. To distinguish them, as illustrated in Fig. 7, we extract a distance map _D_ and a skeleton _S_ from _M_ via a medial-axis extraction algorithm \[Lee et al. 1994\]. Based on them, we can filter two masks _M<sub>fix</sub>_ and _S<sub>mov</sub>_ respectively,<tbc>

FastMarching
Mc
Minpaint
I
I'inpaint
FFC-ResNet
Extend
M
Iinpaint





I
M
D
Mfix
S
S'mov
S'mov + Pinter
Smov

Fig. 5. The process of contour removal.

(a) Input drawing

(b) Animating the character reconstructed by Wonder3D

Fig. 6. An example of surface adhesion.

Fig. 7. An example of handling vertex locations.

