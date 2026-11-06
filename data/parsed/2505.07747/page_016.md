SparseConv [13] and PointBERT [89] as backbone architectures. This yielded three distinct metrics for evaluating image-to-geometry alignment: Uni3D-I, OpenShape<sub>_sc_</sub>-I, and OpenShape<sub>_pb_</sub>-I, where higher scores indicate better geometric consistency with the input image. For texture evaluation, we adopted CLIP-Score [59] to measure semantic alignment. Specifically, we rendered multi-view images from textured 3D models at an elevation of \(30^\circ\) and azimuth angles of \(\{0^\circ,90^\circ,180^\circ,270^\circ\}\) for semantic consistency assessment with input images. Quantitative results are presented in Tab. 1, with top and second-highest scores highlighted. Step1X-3D achieved the highest CLIP-Score and multiple second-highest rankings in geometric-semantic matching metrics. These superior results further demonstrate Step1X-3D’s robust generation capabilities.

We conducted a user study with 20 participants evaluating all 110 uncurated test images. The assessment criteria for 3D models included: (1) geometric plausibility, (2) similarity to input images, (3) texture clarity, and (4) texture-geometry alignment. Participants rated each object on a 5-point Likert scale (1: lowest quality, 5: highest quality). As shown in Fig. 10, Step1X- 3D achieves comparable performance to the current best-performing methods. However, we observe that all evaluated algorithms still fall significantly short of the theoretical upper bound, indicating considerable room for improvement before reaching production-ready quality. These find-

ings underscore the importance of fostering open-source collaboration within the 3D research community to collectively advance the state-of-the-art.

Visual Comparisons across SOTA Methods Fig. 11 and Fig. 12 present comparative results of geometric and textural outputs across different methods. Unlike previous visual comparisons, we address pose inconsistencies in the generated 3D meshes by implementing a unified evaluation protocol: (1) aligning both untextured and textured models in Unreal Engine for consistent pose normalization, and (2) compositing multiple objects into a single rendered image for direct comparison. This standardized approach reveals that Step1X-3D achieves comparable or superior performance relative to the best available methods.

## 6 Conclusion

Step1X-3D advances 3D generation by introducing an open-source, high-fidelity framework that decouples geometry and texture synthesis. Through rigorous data curation (2M assets) and a hybrid VAE-DiT architecture, it achieves promising results while enabling 2D-to-3D control transfer. We will release the models, training code, as well as the training data (excluding self-collected assets) to bridge the gap between proprietary and open research, fostering community progress toward production-ready 3D generation.

## 7 Limitations

Currently, we convert mesh to TSDF with grid resolution 256<sup>3</sup>. In future work, we will increase the grid resolution to achieve more accurate geometric details. Meanwhile, for the texture component, our current implementation is limited to albedo generation. We plan to extend this pipeline to support input image relighting and physically based rendering (PBR) material texture generation.

## 8 Contributors

**Algorithm contributors:** Weiyu Li, Xuanyang Zhang, Zheng Sun, Di Qi, Hao Li, Wei Cheng, Weiwei Cai, Zeming Li, Gang Yu, Xiangyu Zhang, Daxin Jiang

**Data contributors:** Shihao Wu, Jiarui Liu, Zihao Wang, Xiao Chen, Feipeng Tian, Jianxiong Pan

**Corresponding authors:** Xuanyang Zhang (zhangxuanyang@stepfun.com), Gang Yu (yugang@step fun.com), Daxin Jiang (djiang@stepfun.com), Ping Tan (pingtan@ust.hk)

3.0 2.59 2.71 2.5 2.52 2.50 2.18 2.0 Average score 1.5 1.11 1.0 0.5 0.0 Step1X-3D Hunyuan3D 2.0 Tripo-v2.5 Rodin-v1.5 Trellis Meshy-4

Figure 10: **User study**. Average user preference score is reported.

