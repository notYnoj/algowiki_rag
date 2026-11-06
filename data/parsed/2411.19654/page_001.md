# TexGaussian: Generating High-quality PBR Material via Octree-based 3D Gaussian Splatting

Bojun Xiong<sup>1∗†</sup>, Jialun Liu<sup>2∗</sup>, Jiakui Hu<sup>3†</sup>, Chenming Wu<sup>2</sup>, Jinbo Wu<sup>2</sup>, Xing Liu<sup>2</sup>, Chen Zhao<sup>2</sup>, Errui Ding<sup>2</sup>, Zhouhui Lian<sup>1‡</sup>

<sup>1</sup>Wangxuan Institute of Computer Technology, Peking University, China

<sup>2</sup>Baidu VIS

<sup>3</sup>Institute of Medical Technology, Peking University, China

**Abstract**

Physically Based Rendering (PBR) materials play a crucial role in modern graphics, enabling photorealistic rendering across diverse environment maps. _Developing an effective and efficient algorithm that is capable of automatically generating high-quality PBR materials rather than RGB texture for 3D meshes can significantly streamline the 3D content creation. Most existing methods leverage pre-trained 2D diffusion models for multi-view image synthesis, which often leads to severe inconsistency between the generated textures and input 3D meshes. This paper presents TexGaussian, a novel method that uses octant-aligned 3D Gaussian Splatting for rapid PBR material generation. Specifically, we place each 3D Gaussian on the finest leaf node of the octree built from the input 3D mesh to render the multi-view_<tbc>

<tbc>_images not only for the albedo map but also for roughness and metallic. Moreover, our model is trained in a regression manner instead of diffusion denoising, capable of generating the PBR material for a 3D mesh in a single feed-forward process. Extensive experiments on publicly available benchmarks demonstrate that our method synthesizes more visually pleasing PBR materials and runs faster than previous methods in both unconditional and text- conditional scenarios, exhibiting better consistency with the given geometry. Our code and trained models are available at `https://3d-aigc.github.io/TexGaussian`._

### 1. Introduction

Traditional 3D asset creation relies heavily on the expertise and extensive effort of professional designers [23], posing a significant barrier for casual users interested in creating 3D models independently. In the 3D design process, geometry creation typically represents only a small portion of the overall time, while the majority is dedicated to developing textures and appearances, which are far more time-consuming. Achieving a delicate appearance for a 3D<tbc>

∗Denotes equal contribution. †This work was partly done when Bojun and Jiakui interned in Baidu. ‡Corresponding author. E-mail: lianzhouhui@pku.edu.cn This work was supported by the National Natural Science Foundation of China (Grant No.: 62372015), Center For Chinese Font Design and Research, and Key Laboratory of Intelligent Press Media Technology.

Textual Descriptions Input Mesh Albedo Roughness Metallic Rendering 1 Rendering 2 Rendering 3 A wooden box with gold accents +
TexGaussian Astronomical telescope +
TexGaussian A green jug with a handle and rope +
TexGaussian

Figure 1. Our proposed TexGaussian is capable of generating high-quality materials for given input 3D meshes based on the corresponding textual descriptions. The generated results are naturally compatible with modern graphical engines for photo-realistic rendering under different environment maps.

