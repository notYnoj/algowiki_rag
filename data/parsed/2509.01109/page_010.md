leveraged parametric 2D Gaussian distributions to model image content in a non-uniform and content- aware manner. Our method achieved strong performance using only 128 tokens per image, yielding rFID and FID scores of 0.65 and 1.50 on image reconstruction and generation tasks, respectively. By decoupling spatial layout from texture features, GPSToken enabled a two-stage generation pipeline that supports flexible control over both structural and appearance attributes.

**Limitations**. While our approach has shown promising results, its heuristic initialization of Gaussian parameters may not always ensure optimal configurations. Future work could explore learning- based initialization to address this limitation. Additionally, designing a specialized architecture for predicting Gaussian parameters in generative tasks could improve layout synthesis and potentially eliminate the need for post-processing calibration, thereby enhancing overall performance.

## References

60
50
SITXL/2 (baseline) two-stage generator one-stage generator
40
FID-10K (4)
30
5X
20
3X
10
0
0
200
400
600
800
Training Iterations (x109)

calibrated g init cal
final g
synthesized image

Figure 7: FID-10K training curves.

Figure 8: Illustration of two-stage generation pipeline.

