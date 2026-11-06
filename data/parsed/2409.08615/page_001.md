# _DrawingSpinUp:_ 3D Animation from Single Character Drawings

JIE ZHOU, City University of Hong Kong, China

CHUFENG XIAO, Hong Kong University of Science and Technology, China

MIU-LING LAM, City University of Hong Kong, China

HONGBO FU\*, Hong Kong University of Science and Technology, China

Animating various character drawings is an engaging visual content creation task. Given a single character drawing, existing animation methods are limited to flat 2D motions and thus lack 3D effects. An alternative solution is to reconstruct a 3D model from a character drawing as a proxy and then retarget 3D motion data onto it. However, the existing image-to-3D methods could not work well for amateur character drawings in terms of appearance and geometry. We observe the contour lines, commonly existing in character drawings, would introduce significant ambiguity in texture synthesis due to their view-dependence. Additionally, thin regions represented by single-line contours are difficult to reconstruct (e.g., slim limbs of a stick figure) due to their delicate structures. To address these issues, we propose a novel system, _DrawingSpinUp_, to produce plausible 3D animations and breathe life into character drawings, allowing them to freely spin up, leap, and even perform a hip-hop dance. For appearance improvement, we adopt a removal-then- restoration strategy to first remove the view-dependent contour lines and then render them back after retargeting the reconstructed character. For geometry refinement, we develop a skeleton-based thinning deformation algorithm to refine the slim structures represented by the single-line contours.

The experimental evaluations and a perceptual user study show that our proposed method outperforms the existing 2D and 3D animation methods and generates high-quality 3D animations from a single character drawing. Please refer to our project page (https://lordliang.github.io/DrawingSpinUp) for the code and generated animations.

CCS Concepts: • **Computing methodologies** \(\rightarrow\) **Animation**; _Non-photorealistic rendering._

Additional Key Words and Phrases: Character Drawing, 3D Animation, Non- photorealistic Rendering, Style Transfer

**ACM Reference Format:**

Jie Zhou, Chufeng Xiao, Miu-Ling Lam, and Hongbo Fu\*. 2024. _DrawingSpinUp_: 3D Animation from Single Character Drawings. In _SIGGRAPH Asia 2024 Conference Papers (SA Conference Papers ’24), December 3–6, 2024, Tokyo, Japan._ ACM, New York, NY, USA, 10 pages. https://doi.org/10.1145/3680528.3687593

## 1 Introduction

Character drawing plays a crucial role in art and design, significantly enhancing storytelling, gaming, and animation [Huang 2018; Lasseter and Rafael 1987; Librande 1992]. Beyond professionals, character drawing is a popular medium for amateurs, including children [Cox 2013; Smith et al. 2023], to unleash their inspiration by creating imagined characters like superheroes and fairy creatures. Given such a single drawing, could we bring the human-drawn character to life, e.g., making it run, leap, and dance on paper?

To animate a character drawing, existing methods (e.g., [Hornung et al. 2007] and [Smith et al. 2023]) typically retarget 2D motions onto the character by deforming its shape in 2D image space via as-rigid-as-possible (ARAP) [Igarashi et al. 2005]. Unfortunately, these methods cannot work well for 3D motions beyond the 2D image plane, e.g., rotating the character’s body or tilting its head,

\*Corresponding author. Authors’ Contact Information: Jie Zhou, jzhou67-c@my.cityu.edu.hk, City University of Hong Kong, China; Chufeng Xiao, chufengxiao@outlook.com, Hong Kong University of Science and Technology, China; Miu-Ling Lam, miu.lam@cityu.edu.hk, City University of Hong Kong, China; Hongbo Fu\*, fuplus@gmail.com, Hong Kong University of Science and Technology, China.

Drawing SpinUp

Fig. 1. Our _DrawingSpinUp_ produces visually vivid 3D character animations (Right) given single input drawings (Bottom-Left) and target motions (Top-Left).

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. _SA Conference Papers ’24, December 3–6, 2024, Tokyo, Japan_ © 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-1131-2/24/12 https://doi.org/10.1145/3680528.3687593

