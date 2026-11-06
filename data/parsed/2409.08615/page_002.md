<tbc>as shown in Fig. 2 (results of Smith et al.). This intuitive limitation stems from the lack of a 3D sense. To afford 3D motions, a straightforward solution is to reconstruct 3D models as proxies from character drawings and then retarget 3D motions onto them. However, existing image-to-3D methods (e.g., One-2-3-45 [Liu et al. 2024b], One-2-3-45++ [Liu et al. 2024a], DreamGaussian [Tang et al. 2023], Wonder3D [Long et al. 2024], LRM [Hong et al. 2024]) always struggle to reconstruct visually pleasing results from amateur character drawings due to the domain gap between photo-realistic images and human-drawn sketches, as shown in Fig. 2 (results of DreamGaussian and Wonder3D).

Unlike photo-realistic images merely with texture details, we observe character drawings often exhibit diverse types of strokes, including interior lines and contour lines, as shown in Fig. 3 (b)-(c). Specifically, interior lines appear inside a character and represent texture patterns similar to those in photo-realistic images. Different from interior lines, contour lines represent stylized character boundaries, which are view- and motion-dependent lines and are absent in photo-realistic images. Existing image-to-3D models are always trained on photo-realistic images, thus tending to mistake artistic contour lines for internal texture details. This ambiguity can lead to appearance degradation and even affect shape reconstruction quality, as shown in Fig. 8 (c). Moreover, these methods (e.g., Wonder3D [Long et al. 2024]) generally generate several fixed- view images and then fuse them to get a 3D model. Because this pipeline inherently handles contours as view-independent textures, re-training/fine-tuning them on 3D shapes with contour rendering still fails to address contour issues. Additionally, single-line contours are commonly used to depict shapes and structures in an abstract manner, e.g., slim limbs in stick figures, as shown in Fig. 3 (d). Since such depiction is rarely seen in the training images, the models<tbc>

<tbc>pre-trained on photo-realistic images might fail to reconstruct such delicate structures.

Based on the above observations, we present _DrawingSpinUp_, the first 3D-aware animation system for generating non-planar animations from single character drawings given 3D motions. Our key idea is to recognize the contour lines and process them separately to adapt to the reconstruction prior of the pre-trained image-to-3D models. Specifically, we adopt a removal-then-restoration strategy to handle the contour lines. We first design a network to remove contour lines in a character drawing and inpain textures in the removed regions. Next, we utilize a pre-trained image-to-3D model to reconstruct a textured geometry as a proxy for 3D motion retargeting. Finally, we propose a geometry-aware stylization network to render view- and motion-dependent contour lines for each frame of the retargeted character and enhance the internal textures to match the style of the input image. In addition, to ensure the quality of geometry reconstruction, we develop a skeleton-based thinning deformation algorithm to refine the slim structures indicated by the single-line contours. We select 120 representative amateur character drawing samples of various styles as test inputs from the Amateur<tbc>

Input drawings
Target motions
Smith et al.
DreamGaussian
Wonder3D
Ours
Smith et al.
DreamGaussian
Wonder3D
Ours

(a) Input drawing
(b) Interior lines
(c) Contour lines
(d) Single-line contours

Fig. 2. Our _DrawingSpinUp_ produces visually more pleasing character animation results given input drawings and target motions than the existing 2D and 3D animation techniques.

Fig. 3. An example of a character drawing with diverse types of strokes, highlighted in blue (b), red (c) and green (d).

