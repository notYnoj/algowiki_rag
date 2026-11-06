<tbc>into the the EDM formulation. However, we found that the inversion is unstable when the second-order Heun solver is used. This is because each denoising step is harder to invert and errors accumulate; therefore, we use the Euler solver in the context of image editing.

### 3.4.1 Localized updates.

Since the painted features are localized, there is an expectation that the image remains as close as possible to the original outside of the edited region; the painted feature should also be compatible with the initial texture (for example, the sugar spill should not alter the texture below, Fig. 12). We propose to solve this via **noise- mixing**: during inversion, we save the intermediate noise estimates \(\unknown(\mathbf{z}_i,\unknown;\sigma_i)\), for each level \(\sigma_i\). Then, to generate the new image from the inverted noise **_z_**_<sub>N</sub>_, we mix the noise estimates saved during inversion with the new noise estimates (\(\hat{\unknown}\)) that are conditioned by the label map **_c_**:

\(\hat{\mathbf{z}}_{i-1}=\hat{\mathbf{z}}_i+(\sigma_{i-1}-\sigma_i)\text{mix}(\hat{\unknown}(\hat{\mathbf{z}}_i,\mathbf{c};\sigma_i),\unknown(\mathbf{z}_i,\unknown;\sigma_i),i).\) (2)

Where \(\hat{\unknown}\) denotes the classifier-free guided direction: \(\hat{\unknown}(\mathbf{z},\mathbf{c},\sigma)=\unknown(\mathbf{z},\unknown,\sigma)+\gamma(\unknown(\mathbf{z},\mathbf{c},\sigma)-\unknown(\mathbf{z},\unknown,\sigma))\), with guidance \(\gamma=4\).

To strike a balance between preserving the original structure in the edited regions and being faithful to the new condition, we mix the scores adaptively depending on the step in the backward diffusion process:

\(\text{mix}(\hat{\unknown}_i,\unknown_i,i):=\hat{\unknown}_i+(\unknown_i-\hat{\unknown}_i)\left(\frac{i}{N}\right)^\alpha.\) (3)

The influence of the original (unconditional) noise estimates \(\unknown_i\) decreases from 1 to almost 0 over the _N_ steps. \(\alpha\) controls how fast the mixing factor decays, and it is set to 0.3 in our experiments. In<tbc>

<tbc>order to minimize the alteration of the texture outside the editing region, we set the mixing factor to 0 for the background (outside the editing mask).

### 3.4.2 Feature transfer.

Our noise-mixing editing method lends itself to another important capability: feature transfer. We demonstrate this function in Fig. 10, where we transfer features from their native class to another textures class from MVTec, as well as to a real image of the author’s desk. To transfer a feature from a texture class to a target image that is out-of-distribution (OOD), we first invert the image using the trained diffusion model. When the image is very different from the training distribution, the inversion process needs more steps to reconstruct the image with high accuracy; we use 250 in our experiments. We then perform the steps analogous to image editing, mixing the noise estimates from inversion with the predictions obtained under the desired label map **_c_**. Thanks to the classifier-free guidance mechanism, the direction of the noise estimates incorporates the difference between the feature and the normal texture, which minimizes the contamination of normal appearance from the training texture to the OOD target image.

## 3.5 Stationary infinite texture generation

Our method supports generating images at arbitrary resolutions and aspect ratios. A naive approach to high-resolution synthesis would be to simply run the denoising model \(\hat{\unknown}(\mathbf{z},\mathbf{c},\sigma)\) starting with a noise tensor **_z_**_<sub>N</sub>_ significantly larger than the size of the training images. This approach does not work on generic image synthesis \[Haji-Ali et al. 2024; He et al. 2023\] because it fails to retain the relationship between elements at a global level; however, textures are defined by local structures, which are well reproduced by the diffusion model even at a resolution well-outside the training range.

This trivial solution works well for image-sizes up to 2048\(\times\)2048, after which the inference requires more than 24_GB_ of VRAM. In general, the memory requirement of this approach scales poorly<tbc>

Photograph
Labels
[Wang et al. 2022b]
Ours

Independent
Same mean
Lanczos fc = 0.1
Lanczos fc = 0.2

Fig. 6. Editing results with our noise-mixing approach. The rows depict top to bottom: a real photograph, the conditioning label-map, the result obtained with TextureReformer \[Wang et al. 2022b\], and our edit.

Fig. 7. Comparison between images sampled independently (_top_) and different uniformization strategies. Rows 2 through 4 attempt to make all images follow the style of the first column, using the methods explained in Sec. 3.5.

