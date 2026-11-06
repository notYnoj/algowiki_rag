# Unwarping Screen Content Images via Structure-texture Enhancement Network and Transformation Self-estimation

Zhenzhen Xiao, Heng Liu*, and Bingwen Hu

**Abstract**

While existing implicit neural network-based image unwarping methods perform well on natural images, they struggle to handle screen content images (SCIs), which often contain large geometric distortions, text, symbols, and sharp edges. To address this, we propose a structure-texture enhancement network (STEN) with transformation self-estimation for SCI warping. STEN integrates a B-spline implicit neural representation module and a transformation error estimation and self-correction algorithm. It comprises two branches: the structure estimation branch (SEB), which enhances local aggregation and global dependency modeling, and the texture estimation branch (TEB), which improves texture detail synthesis using B-spline implicit neural representation. Additionally, the transformation self- estimation module autonomously estimates the transformation error and corrects the coordinate transformation matrix, effectively handling real-world image distortions. Extensive experiments on public SCI datasets demonstrate that our approach significantly outperforms state-of-the-art methods. Comparisons on well- known natural image datasets also show the potential of our approach for natural image distortion.

**_Keywords: Image warping, B-spline neural representation, Structure-texture, Transformation Self-estimation._**

### 1. Introduction

Image warping [33, 19] is a vital image processing technique that alters the spatial positions of pixels to achieve specific visual effects or changes in image morphology. This process involves adjusting the coordinates of each pixel in the image and mapping them to the new positions, thereby changing the shape or perspective of the image. In practice, image warping is often combined with other image processing techniques, such as image correction [9, 8],repositioning [30, 38], and lens distortion correction [3, 29, 23], to achieve comprehensive visual enhancement. The technique relies on mathematical models and algorithms to compute the necessary pixel mappings, mak-<tbc>

<tbc>ing it a versatile and crucial tool in visual effects processing and real-world image correction.

Image warping aims to deform images defined on a rectangular grid into continuous shapes. By using the precise transformation or mapping function, one can effectively reconstruct the spatial structure of an image with an arbitrary shape and scale to achieve the desired image transformation effect. SRwarp [33] first redefines the image warping problem as a spatial variation of generalized super- resolution and effectively addresses the reconstruction of high-frequency detail images by utilizing a deep single- image super-resolution (SISR) [43, 12, 25]architecture as the backbone.

In recent years, inspired by implicit neural functions [32, 20, 27], implicit neural representations have shown significant potential and effectiveness in handling image distortions. LIIF [7] parameterizes the implicit neural representation using multi-layer perceptrons (MLP), mapping the input coordinates and corresponding latent variables to RGB values, thereby achieving super-resolution reconstruction at arbitrary scales. However, due to a lack of spatial variation considerations, LIIF [7] has limitations in addressing image warping. Although the above methods can achieve rather good effects in dealing with natural image distortions, they often lose their effectiveness when facing Screen Content Images(SCIs) with huge deformations, in-<tbc>

Warped Image SRWarp[33] LTEW[19] STEN(Ours)

Figure 1: Real-world screen content image correction employs the proposed STEN method. The image is captured by a camera, and both SRWarp[33] and LTEW[19], along with our proposed STEN, utilize the predicted transformation matrix to achieve super-resolution (SR).

