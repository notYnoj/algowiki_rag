with human-drawn drawings in terms of appearance and geometry. For appearance improvement, we adopt a removal-then-restoration strategy to first remove the view-dependent contour lines and then render them back after retargeting the reconstructed character. For shape refinement, we develop a cutting-and-thinning method to refine the slim structures represented by the single-line contours.

While our system can produce visually plausible 3D animations, it still has several limitations. First, we assume the characters in input drawings are approximately in a frontal A/T pose, without any self- occlusion. Some self-occlusion cases, such as crossed arms, would

result in the reconstructed geometry exhibiting surface adhesion or merging of body parts. Second, our contour rendering might produce artifacts when we extract edges with inappropriate thresholds (see Fig. 15 (a)-(b)). Third, when the contour lines of the input drawing are too thick, artifacts may appear in the generated results (see Fig. 15 (c)-(d)). Additionally, it might produce artifacts when the drawings are highly abstract and far away from bipedal characters (see Fig. 15 (e)).

In the future, we plan to extend our system for real-time performance, involving developing fast 3D reconstruction and auto- rigging methods, and investigate a generalized stylization network for acceleration. Although our method is not real-time, it benefits the community of character animation and non-photorealistic rendering. We envision its potential for drawing-to-animation storytelling by integrating text prompts and prototyping animation designs in cartoon films, games, VR/AR scenes, etc. We are also interested in extending our method to work for general human drawings, e.g., quadruped animals.

## Acknowledgments

We thank the anonymous reviewers for their constructive comments and suggestions, which greatly enhanced the quality of this work. Additionally, we appreciate the participants who took the time to engage in the user study. This research was supported by a startup fund by the Hong Kong University of Science and Technology (Project No. R9913) and the Chow Sang Sang Group Research Fund (Project No. 9229119).

## References

Pierre Bénard, Forrester Cole, Michael Kass, Igor Mordatch, James Hegarty, Martin Sebastian Senn, Kurt W Fleischer, Davide Pesare, and Katherine Breeden. 2013. Stylizing animation by example. _ACM Transactions on Graphics (TOG)_ 32, 4 (2013), 119-1. Blender Development Team. 2022. Blender (Version 3.1.0) [Computer software]. https: //www.blender.org Mario Botsch and Leif Kobbelt. 2004. An intuitive framework for real-time freeform modeling. _ACM Transactions on Graphics (TOG)_ 23, 3 (2004), 630-634. Philip Buchanan, Ramakrishnan Mukundan, and Michael Doggett. 2013. Automatic single-view character model reconstruction. In _Proceedings of the international symposium on sketch-based interfaces and modeling_. 5-14. John Canny. 1986. A computational approach to edge detection. _IEEE Transactions on pattern analysis and machine intelligence_ 6 (1986), 679-698. Caroline Chan, Shiry Ginosar, Tinghui Zhou, and Alexei A Efros. 2019. Everybody dance now. In _Proceedings of the IEEE/CVF international conference on computer_

(a) Input drawing (b) Stylized animation frames (c) Zoomed details

(a) (b) Input drawings Extracted edges and stylized animation frames (c) (d) Input drawings Stylized animation frames (e) Input drawing Stylized animation frames

Fig. 14. Comparison between w/o (Top) and w/ (Bottom) RIC convolution.

Fig. 15. Some failure cases.

