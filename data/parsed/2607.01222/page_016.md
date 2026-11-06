<tbc>**Supplementary Material**

We provide supplementary material for a deeper understanding and more analysis related to the main paper, arranged as follows:

1. Qualitative Comparison (Appendix A)<tbc>

2. Variety Test (Appendix B)<tbc>

3. Ablations (Appendix C)<tbc>

4. Inference Cost/ Latency (Appendix D)<tbc>

5. Limitations and Future Work (Appendix E)

## A Qualitative Comparison

Fig. A1 and Fig. A2 presents a qualitative comparison with recent SOTA methods, including TRELLIS.2 [54], HY2.1 [25], SeqTex [60], TEXGEN [59], and Paint3D [61]. Among these, TRELLIS.2 is a native 3D approach; however, due to the scarcity of high-quality 3D texture data, it struggles to render complex textures on flat geometries. HY2.1, SeqTex, and Paint3D, like our method, follow a multi-view generate-then-bake paradigm. Nevertheless, our approach achieves superior fidelity in high-frequency texture details--especially for text. This is attributed to three key factors: _**(1)**_ maximal preservation of WAN’s powerful generative capabilities, _**(2)**_ frame-to-frame smoothness ensured by video generation, and _**(3)**_ an optimization-based baking strategy applied directly in native 3D space. Additionally, both SeqTex and TEXGEN opt to generate textures directly in UV space instead of baking. This imposes stringent requirements on the viewpoints of reference images. The references must be well-aligned in viewpoint to enable reliable back-projection into UV space for subsequent completion. Otherwise, it is likely to produce unsatisfactory results. While SeqTex markedly reduces the pressure of texture completion compared to TEXGEN by leveraging video generation, it faces limitations because such models are ill-suited for generating fast-spinning sequences of orthogonal views. Consequently, this results in compromised detail fidelity and consistency across the generated multi-views.

## B Variety Test

Fig. A3 presents additional generation results. Leveraging the powerful capabilities of WAN [49], Ink3D demonstrates strong generalization across a diverse range of styles. Furthermore, thanks to its 3D-space baking strategy, Ink3D effectively preserves complex texture details, achieving high fidelity even for text, which is particularly sensitive to distortion.

## C Ablations

### C.1 Ablations on Video Generation

For clearer evaluation of multi-view consistency, we use a flat-geometry asset (tent) edited via nanobanana to generate a grid-textured reference image. In

