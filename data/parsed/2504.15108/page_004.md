<tbc>_i.e.,_ the structure estimation branch (SEB) and the texture estimation branch (TEB). Each incorporates an encoder and a decoder. Initially, we extract the features _F<sub>LR</sub>_ from the low-resolution input image using the encoder and then feed them into the Structure estimation branch and the texture estimation branch of the model.

In the Structure estimation branch, we enhance the aggregation of local knowledge through channel shift and mix operations (called pixel mixer, PM) and utilize image anisotropy for effective global dependency modelling, thereby obtaining richer structural features. Meanwhile, in the B-spline texture estimation branch, we improve the capability of the network to estimate texture information and local details, thereby enhancing texture features. Given that SCIs often have discontinuous tones and many similar text regions, we design a structure-texture fusion mod<tbc>

<tbc>ule to globally retrieve texture features and integrate the most relevant information into the structural features for feature-based texture enhancement. This module combines the image’s structural information with texture features, effectively enhancing image details and visual effects while preserving the structural integrity of the image, resulting in clearer and more vivid images. Finally, the fused features and texture features are reconstructed through decoders separately. The decoders are constructed with multi-layer perceptrons (MLPs) and predict the RGB values at queried coordinates. The predicted values are then added to produce the final reconstructed high-resolution un-warped image.

## 3.2. Structure Estimation Branch

As shown in Fig. 2, the Structure estimation branch consists of two types of transformer modules: the Local Trans<tbc>

Structure estimation branch
GTB
SWSA
MLP
Structure- Texture Fusion
LR
LTB
Cable memory
Crop
BN
PM
MLP
IWarp
LR-crop
Texture estimation branch
Local Grade (HxWx2)
Coef
Kont
B()
F SEB
S
Soft Attention
FSTF
Relevance Embedding
F TEB
K
A
Shape (HxWx10)
Dilation
C
Texture Retrieval
V
Feed Forward
Concate
Striped Window for SA
GTB/LTB
Global /Local Transformer Block
SWSA
PM
B-spline representation
B()
Element-wise subtraction
Element-wise Addition
Inner product
Inner product

Figure 2: The overall structure of the proposed STEN model is as follows: First, the low-resolution samples _I<sub>LR</sub>_ are subjected to an inverse transformation using the inverse transformation matrix _M_<sup>-1</sup>, followed by cropping to obtain _I<sub>LR</sub>_-Crop images. The entire model consists of two main branches: the Structure branch and the texture branch. The structure estimation branch allows us to obtain richer structural features, while the texture estimation branch enhances the ability of the proposed method to estimate texture information and local details more effectively, thus extracting texture features more efficiently. These features from both branches are then mapped into the Structure-Texture Fusion (STF) module for feature enhancement and subsequently decoded. By combining the Structure and texture branches, our STEN model can better handle deformation issues in screen content images.

