<tbc>ping its texture with shiny golden material. Meanwhile, the painted lion shows rich details and high fidelity. In the real-world bear scene, we paint a pair of sunglasses on its face and lift its arms. The swapped golden material on its legs exhibits vivid interactions between geometry and light. Please refer to our supplementary video for a vivid animation of these effects.

### 4.8 Comparisons of Rendering on Unbounded Scenes

We evaluate our method with BakedSDF \[88\] in a more complex dataset Mip-NeRF 360 \[3\]. As the official code for BakedSDF \[88\] is not publicly available, we utilize its unofficial implementation BakedSDF\* \[90\] for this comparison. Due to the challenges of extracting the complete mesh for an unbounded scene, we extract the foreground mesh enclosed within a unit cube from Neuralangelo \[32\] to serve as the input for NeuMesh++. For an unbounded background, we follow NeuS \[74\] to learn an additional implicit hash grid. The novel view is rendered by:

\(\hat{C}(\mathbf{r})_\mathrm{comp}=\hat{C}(\mathbf{r})*T+\hat{C}(\mathbf{r})_\mathrm{bg}*(1-T),\) (10)

where \(\hat{C}(\mathbf{r}),\hat{C}(\mathbf{r})_\mathrm{bg},\hat{C}(\mathbf{r})_\mathrm{comp}\) are the volume-rendered color of NeuMesh++, the volume-rendered color of background model and final rendered color respectively. _T_ is the accumulated transmittance of NeuMesh++. As shown in Tab. 8, our method quantitatively outperform BakedSDF \[88\]. As depicted in Fig. 15, our method demonstrates superior synthesis of high-frequency details compared to BakedSDF\[88\], including the sharp grass in Bicycle, the detailed appearance of snacks in Counter, the vibrant flowers and grass in Flowers, and the undistorted objects in Room. This improvement is primarily attributed to our vertex-bounded local features, which effectively enhance the representation of high-frequency scene content.

## 5 DISCUSSIONS

In this section, we provide a detailed analysis of the limitations of our method.

**Texture Swapping.** Texture swapping requires that the template and edited region possess similar shapes, ensuring proper alignment of the edited region with the template in Euclidean space. This ensures the accurate retrieval of the corresponding template texture codes for each modified vertex, thereby swapping the appearance of the template texture to the edited regions.

**Texture Filling.** Texture filling overcomes the shape assumption of texture swapping by transferring the codes within UV space using the tile-based pattern. However, to prevent checkerboard artifacts in the filled texture, the tile- based filling method requires the template texture to have a uniform color or be applied with a larger scale factor _s_.

**Completeness of Input Mesh.** If the input mesh lacks the geometry of the fine local structure, our method is unable to allocate sufficient neural codes onto the mesh to synthesize this fine structure. For instance, if the input mesh entirely loses the geometry of a branch in the Ficus of Fig. 7, we cannot synthesize the missing branch in novel views.

**Multiscale Dataset.** Furthermore, our method does not account for the level of detail when the scene is captured from multi-scale viewpoints. Our fixed-resolution occupancy grid is not adaptable to cameras with multiple scales. For example, when the occupancy grid is applied to large scene<tbc>

\begin{tabular}{cccc}
 & **PSNR**\(\uparrow\) & **SSIM**\(\uparrow\) & **LPIPS**\(\downarrow\)**(Alex)** \\
BakedSDF\* \[88\] & 23.31 & 0.651 & 0.277 \\
Ours & **26.34** & **0.731** & **0.216** \\
\end{tabular}

Geo.+Color Dim and Network Width vs PSNR
Geo.+Color Dim and Network Width vs SSIM
Geo.+Color Dim and Network Width vs LPIPS
12+24
Geo.+Color Dim
12+24
Geo.+Color Dim
12+24
Network Width
120
120
100
100
100
6+15
80
80
6+15
Network Width
Network Width
6+15
Network Width
6+15
80
60
60
60
3+9
40
40
3+9
Network Width
Network Width
3+9
3+9
Geo.+Color Dim
Geo.+Color Dim
32.0
32.1
32.2
32.3
32.4
32.5
32.6
32.7
0.952
0.953
0.954
0.955
0.956
0.957
0.958
0.050
0.052
0.054
0.056
0.058
PSNR
SSIM
LPIPS

Bicycle
Counter
Flowers
Room
BakedSDF
Ours
Ground-truth

Fig. 13: **Ablation on the size of our model.** We show the quantitative ablation on the size of MLP decoders and neural codes. The evaluated sizes of MLP decoders are 32, 64, 128. The evaluated size of geometry and texture codes are (#Geo.+#Tex.): 3+9, 6+15, and 12+24.

TABLE 8: **Quantitative comparison.** We show quantitative comparisons with BakedSDF\* \[88\] on Mip-NeRF 360 \[3\] dataset.

Fig. 15: **Qualitative comparison.** We show qualitative comparisons with BakedSDF\* \[88\] on Mip-NeRF 360 \[1\] dataset.

