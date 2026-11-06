# Ink3D Sculpting 3D Assets with Extremely Complex Textures via Video Generative Models

**Abstract.** Recent 3D generative models can synthesize high-quality geometry but often struggle to reproduce intricate textures from reference images, largely due to the scarcity of large-scale 3D training data with rich surface appearance. In contrast, visual generative models are trained on datasets several orders of magnitude larger and excel at modeling complex visual patterns. Motivated by this gap, we introduce Ink3D, a framework that bridges 3D generation with large-scale video generative models to synthesize _extremely complex textures_. Ink3D first reconstructs a white-mesh geometry using an off-the-shelf 3D generation model. It then employs OrbitPainter, a conditional video generative model, to produce dense orbit-scan videos capturing object appearance across viewpoints.

<sup>∗</sup> Equal contribution. \(^\boxtimes\) Corresponding author.



Yue Han<sup>1,3⋆</sup>, Chong Li<sup>2⋆</sup>, Zhening Liu<sup>4</sup>, Cong Huang<sup>1</sup>, Fang Deng<sup>1</sup>, Yong Liu<sup>3</sup>, Fangyun Wei\(^{2\boxtimes}\), Yan Lu<sup>2</sup>

<sup>1</sup>ZGCA & ZGCI <sup>2</sup>Microsoft Research <sup>3</sup>Zhejiang University <sup>4</sup>HKUST <sup>1</sup>https://github.com/YueHan99/Ink3D.TextureGen

**Fig.1:** Ink3D introduces geometry-aware video generation into the 3D generation pipeline to synthesize 3D assets with extremely complex textures such as intricate clothing patterns and high-frequency decorative details.

arXiv:2607.01222v1 [cs.CV] 1 Jul 2026

