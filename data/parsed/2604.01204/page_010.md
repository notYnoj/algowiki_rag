### Implementation

We implement our method in _gsplat_ [75], using the 3DGUT [70] formulation, to which we add custom CUDA kernels for the forward and backward logic described in Sec. 4. To reduce register pressure, we use half-precision memory fetches on feature vectors during rasterization, for both forward and backward kernels. Our neural network uses tiny-cuda-nn’s [49] JIT-compiled cooperative vector MLPs, trained and evaluated in half precision (FP16). We apply an automatic scaling factor to the loss values in order to improve half-precision training stability [45].

### Results

We present the results of our method against a number of previous works using pure neural fields [2], hashgrid-encoded neural fields [3, 49], pure primitive-based methods [23,24,28,37,70] with regular Spherical Harmonics (SH) appearance or more complex appearance models [4,11], and closer to us, methods mixing primitives (e.g. for acceleration) and neural fields [41,80] (Tab. 1). In this table, we use the originally provided JPEG images for proper comparison with previous works in MipNeRF360; every other result presented in this section, unless otherwise stated, uses _gsplat_’s default downscaling for all methods tested. We measure the performance delta of this choice in the supplementary (Tab. 5). We consistently outperform all previous works in a varied set of real datasets [2, 21,30]. We include a selection of views in Fig. 6. Our method particularly excels at high-frequency detail modelling, capturing specular highlights and reflections with superior fidelity.

In order to isolate the impact of our method, we include a controlled experiment in Tab. 2. We compare between 3DGS-MCMC, 3DGUT-MCMC, and different appearance models for the latter: regular SH, current state-of-the-art Spherical Voronoi [11] (SV) and ours (NHT). We implement all four under the same framework (_gsplat_), 1M primitives cap, 30k iterations, identical per-scene hyperparameters, and the same opacity and scale regularizers. This isolates the appearance model from training-schedule choices in Tab. 1. Tab. 2 shows that our method consistently outperforms both SH and SV across all benchmarks, while using less storage, without sacrificing real-time performance. NHT takes around 14.5 minutes to train up to 30k iterations on MipNeRF360 on average (1M primitives, RTX 5090); training times for all methods across datasets are reported in the supplementary material (Tab. 2). Per-scene breakdowns and more details are provided in the supplementary material (Tabs. 6 and 7). We also compare against a close texture-based method (BBSplat [59]) in the supplementary material (Tab. 1). NHT achieves substantially higher quality and faster rendering not only at equal memory, but also at equal primitive count.

## Ablations

We ablate the design of our method on the MipNeRF360 dataset.

### Optimization choices.

Supplementary Tab. 10 isolates the individual contributions of the training strategies: learning rate scheduling, EMA on the MLP weights, loss scaling, the color-refinement phase, and opacity and scale regularization.

