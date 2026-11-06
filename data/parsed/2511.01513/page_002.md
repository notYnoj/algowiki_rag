## 1 Introduction

In visual content creation, automatic image generation and texturing methods seek to assist artists, reducing the time and effort required to develop photo-realistic texture assets. Many of the existing tools, however, are biased toward an idealized, pristine appearance, so that texture artists spend significant time to augment their textures with the type of blemishes and imperfections characteristic to real- world surfaces. Our work offers an automated framework to analyze texture samples, separating their characteristic (stationary) statistics from sporadic irregularities, that are equally characteristic, feeding an interactive system to paint such prominent features on top of the underlying pristine texture.

Our system takes as input a small number of (unannotated) images representative of a certain material, which include both normal appearance and irregular features (stains, cracks, holes, and abrasions, etc.). The user then specifies the locations of irregularities, and our method synthesizes arbitrarily large textures that resemble the texture in the input images, with the user-specified features naturally blending into the surrounding texture. We present the first framework that simultaneously holds the following capabilities:

(1) **Automatically** extracts the normal and irregular texture appearance from a small number of images.<tbc>

(2) Generates textures with **spatial** and **semantic** control, that is also **interactive**.<tbc>

(3) Facilitates **painting features** on both synthesized textures and real images through **feature transfer**.<tbc>

(4) Creates **arbitrarily large** textures without distribution drift.

## 2 Related Work

Painting features on textures is a task traditionally undertaken by artists that design digital assets. The toolbox (e.g., Substance 3D painter [Adobe 2023b]) generally includes a library of carefully crafted materials that covers frequently occurring effects, such as dirt accumulation, or cracks. Alongside the materials, there usually are pre-made alpha-masks that represent a realistic distribution of the desired features. An artist would then select an appropriate combination to overlay on the canvas as needed. This process can be time-consuming and it is generally limited to the available pool of materials and patterns, which may not be easy to customize for a specific application. In order to extend their capabilities, digital creation software (_e.g._, Photoshop [Adobe 2023a], Gimp [GNU 2024], Substance 3D painter [Adobe 2023b]) include clone stamp brushes; however, the features are simply copied over the canvas, making it difficult to ensure realistic effects and transitions.

### 2.1 Example-based feature synthesis

Several research projects directly or indirectly target the replication of image features into a new context. In the seminal work of image analogies [Hertzmann et al. 2001], the texture-by-numbers method is used to create a new instance of a texture and paint the prominent features as guided by a layout map. The same can be achieved using single-image generative models and image reshuffling techniques. SinGAN [Shaham et al. 2019] and SinDiffusion [Wang et al. 2022a] train a generative adversarial network (GAN) and a diffusion model [Dhariwal and Nichol 2021] respectively from a single<tbc>

<tbc>image. The models can then be used to generate similar, realistic patches in a new configuration. GPNN [Granot et al. 2022], Image style transfer [Gatys et al. 2016], Sliced Wasserstein [Heitz et al. 2021], and GPDN [Elnekave and Weiss 2022] are non-parametric generative methods that can be used to paint features by mimicking the patches and statistics from a given source image. Neural Texture Synthesis with Guided Correspondence [Zhou et al. 2023], Non- Stationary Textures using Self-Rectification [Zhou et al. 2024], and Texture Reformer [Wang et al. 2022b] focus specifically on textures with non-stationary regions. These approaches showcase different ways to condition the generation in order to improve the authoring process: orientation and progression control, content image, and a collage of crops. Painting With Texture [Ritter et al. 2006], Painting by Feature [Lukáč et al. 2013], Brushables [Lukáč et al. 2015], and Neural Brushstroke [Shugrina et al. 2022] propose different ways to create brushes from images, enabling painting of the extracted textural features on a canvas. Recently, Diffusion Painting [Hu et al. 2024] displayed remarkable capabilities in terms of the texture complexity controllable by a brush. Using a diffusion model pretrained on a large dataset, the method hallucinates realistic variations and transitions from a single texture image, albeit with limited fidelity to the input mask.

While the above-mentioned approaches share the advantage of being able to work from a single image, it is desirable to incorporate the information from multiple source images of the same texture class if available, as a single image often does not cover the appearance of a feature type in its fullness, or does not contain all transition types that are characteristic for the given material. That being said, in most cases it is not straight forward to extend the methods to accept multiple images in a way that actually improves the generation process. Our method is fine-tuned on multiple images from a single texture class in order to learn from several instantiations of a certain prominent feature type.

A limitation of previous methods is the requirement to manually select and indicate the relevant features from the input images. As we want to capture the entire distribution of a texture and/or the possible prominent features (stains, cuts, etc), several dozen images might be needed. In this case, manual segmentation would put an unreasonable burden on the user. Therefore, in this work we also address a preprocessing part in the asset-creation process, by automatically finding and grouping the relevant features.

### 2.2 Anomaly Localization and Classification

In order to automatically detect the prominent features, which are non-stationary regions in the texture, we pose the problem as an anomaly detection task. Since the input consists of a mix of (unlabeled) normal and anomalous features, we find ourselves in a fully unsupervised setting. This is more challenging than the one-class classification task employed by most anomaly detection methods, where the normal instances are labeled [Batzner et al. 2024; Deng and Li 2022; Roth et al. 2022].

Fully unsupervised anomaly localization is framed as normality- supervised detection with contamination [Liu et al. 2022; Patel et al.<tbc>

