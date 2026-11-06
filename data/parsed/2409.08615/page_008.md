### 4.4 Ablation Study

#### Contour Removal.

Fig. 12 shows the impact of contour removal. It can be seen that without this step, the contours would be considered as part of the internal texture, which cannot be solved by the following stylization step. In contrast, after contour removal, our method renders view-dependent contours to form a more plausible animation.

#### Cutting and Thinning.

We also present a comparison of three scenarios: no-cut-no-thin (Top), only-cut (Middle), and cut-and-thin (Bottom). As shown in Fig. 13, with no shape refinement or only cutting leads to inflated results for fine structures such as hair and limbs. In contrast, our cutting-and-thinning method can handle well the elongated structures depicted by slim strokes.

#### Rotation Invariance.

We compare the results without (Top) and with (Bottom) RIC convolution in Fig. 14. Vanilla convolution cannot work well with the head-down animation frames since it lacks the ability to align the feature maps of a transformed image with those of its original. In contrast, RIC convolution alleviates this issue, enhancing the stability of results.

## 5 Conclusion

This paper has presented the first system _DrawingSpinUp_ to generate vivid 3D animations by applying 3D motions to a single character drawing, while maintaining the contour style consistent with the input drawing. To reconstruct a 3D character as a proxy from the single drawing, our system borrows the reconstruction prior from a pre-trained image-to-3D diffusion model and makes it compatible

(a) Input drawings
(b) DreamGaussian
(c) Wonder3D
(d) Ours

(a) Input drawing
(b) Textured characters
(c) Stylized animation frames

(a) Input drawing
(b) Textured characters
(c) Stylized animation frames

Fig. 11. _DrawingSpinUp_ VS. other 3D-based animation methods.

Fig. 12. Comparison between w/o (Top) and w/ (Bottom) contour removal.

Fig. 13. Comparison of three scenarios: no-cut-no-thin (Top), only-cut (Middle), and cut-and-thin (Bottom).

