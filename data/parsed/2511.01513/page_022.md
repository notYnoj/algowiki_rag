While the throughput of EDM2 is similar to EDM, the latency is significantly higher, despite using the smallest (XS) variant of EDM2. It can be reduced to 1166 milliseconds by using the same model for guidance, which allows computing the conditional and non- conditional noise directions in parallel. Overall, these experiments suggest that EDM is a good choice for our use-case, considering the high-quality synthesis with a low latency. Finally, we emphasize

that even though we show that our choice of diffusion model is sound, and that good results can be obtained with a relatively small model with very little pretraining, we do not claim to have found the best possible model for this part of the pipeline, as this is not the scope of our work.



Fig. 22. High-resolution (4096\(\times\)4096) editing examples. **Please zoom in for full resolution.**

