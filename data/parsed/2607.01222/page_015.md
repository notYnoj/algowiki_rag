### 5 Conclusion

We introduce Ink3D, a framework that bridges 3D generation and large-scale video generative models to synthesize extremely complex textures for 3D assets. Given a reference image, Ink3D first reconstructs a white-mesh geometry using an off-the-shelf 3D generation model, then employs a conditional video model, OrbitPainter, to generate dense 360° orbit-scan videos for comprehensive multi- view observations. These observations are integrated by TextureOptimizer, a neural baking framework that consolidates multi-view appearance while mitigating artifacts caused by geometric inconsistencies. Leveraging the strong visual modeling capability of large-scale video models, Ink3D produces rich textures that are difficult for existing 3D generation methods to achieve.

### Acknowledgements

This work is supported by the Zhongguancun Academy, (Grant No.s 20240307).

