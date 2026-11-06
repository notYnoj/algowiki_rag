### C.2 Ablations on Baking

Fig. A5 illustrates that while video generation provides dense, smooth, and reliable viewpoints, previous baking methods encounter two critical issues when voxels are presented with an abundance of candidate color values: _**(1)**_ Texture Blurring on Flat Geometries: Due to the inherent averaging across all viewpoints, increasing the number of views leads to blurrier texture results on flat surfaces. _**(2)**_ Color Bleeding on Complex Geometries: Color bleeding artifacts caused by view misalignment at complex geometric boundaries remain obvious. To address the blurring of high-frequency textures, we propose a GraphCut-based optimization algorithm that effectively mitigates this issue. Regarding color bleeding at complex boundaries, we leverage TRELLIS.2’s native 3D perception of intricate geometries. Specifically, we convert the model into an O-voxel representation and project multi-view colors directly into this voxel space for baking and following refinement, thereby preserving sharp boundary details.

## D Inference Cost/ Latency

On a single H100 GPU, OrbitPainter generates two 61-frame 512<sup>2</sup> orbit videos in ∼_12 minutes_ with _45G_ GPU memory, while TextureOptimizer takes ∼_1 minute_, resulting in a total cost of ∼_13 minutes_. The video generation dominates the overall latency. Using DMD2 acceleration can shorten video generation _from_ ∼_12 minutes to_ ∼_2 minutes_.

## E Limitations and Future Work

Like most approaches that rely on video generation models, our method inherits the high inference latency associated with generating high-resolution videos. Although Ink3D can synthesize highly complex textures, the video generation stage remains computationally expensive. Future work may explore acceleration techniques, such as DMD2 [58], to reduce inference cost.

## References

