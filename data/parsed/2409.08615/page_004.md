<tbc>system _DrawingSpinUp_ generates a vivid 3D animation while preserving the consistent artistic style with the input drawing. Fig. 4 shows the pipeline of _DrawingSpinUp_. We first remove and inpain the contour regions of the input drawing via an image-to-image translation network (Section 3.1). Next, we use a pre-trained diffusion model and a neural surface reconstructor to generate a coarse 3D geometry (Section 3.2.1). Then we develop a shape refinement strategy to deal with the noisy surface and elongated structures depicted by thin strokes (Section 3.2.3). We automatically rig the character based on the predicted joint keypoints and then retarget the given 3D motion onto it to generate an initial animation (Section 3.3). Finally, we propose a geometry-aware stylization network to restore the original drawing style for each animation frame (Section 3.4). We will present the details in the following subsections.

## 3.1 Contour Removal

The style and thickness of contours vary significantly across different drawings and can even be non-uniform within a single drawing.<tbc>

<tbc>Therefore, using a distance transform with fixed parameters to extract contours is inadequate for all cases, leading to unclear results or excessive removal. To address this, we structure the contour prediction task as an image-to-image translation problem. Given an input drawing _I_ and its segmented foreground mask _M_, we predict the corresponding contour mask _M<sub>c</sub>_. We use an FFC-ResNet [Su vorov et al. 2022] as the generator of our contour removal network. We choose FFC-ResNet because contour lines are typically found at the boundaries of objects, and Fast Fourier Convolution (FFC) [Chi et al. 2020] has a large receptive field that covers the entire image, allowing for more accurate predictions of contour regions compared to vanilla convolution.

We use the 3DBiCar dataset [Luo et al. 2023] as the training dataset. We render front-view images and contour lines of different thicknesses from textured 3D biped cartoon characters in 3DBiCar with Blender [Blender Development Team. 2022]. Next, we stylize the contour lines with random colors and add them to the images to imitate the styles of amateur drawings.

(a) Contour Removal
(b) Textured Character Generation
Refinement
Wonder3D
I
I
inpaint
Loss
Stylization Network Utexture
(F, G mask, Gpos)
O'
Iinpaint
Loss
Stylization Network Ucontour
G edge
(O' + G edge, G mask, Gpos)
O
I
Rendered animation frames F = {F1, F2, , FN}
Stylization Network Utexture & Ucontour
Stylized animation frames O = {O1, O2, ON}
(c) Stylized Contour Restoration

Fig. 4. The pipeline of our _DrawingSpinUp_. (a) We first remove and inpain the contour region of the input drawing via an FFC-ResNet. (b) We use a pre-trained Wonder3D to generate a coarse 3D geometry and then refine its shape and texture. (c) We propose a two-stage geometry-aware stylization network to restore the original drawing style (including texture details and contour lines) for each animation frame.

