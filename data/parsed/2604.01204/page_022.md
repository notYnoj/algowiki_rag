**Supplementary Material**<br>
**Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction**

Jorge Condor<sup>1,2</sup><sup>\*</sup>, Nicolas Moënne-Loccoz<sup>1</sup><sup>\*</sup>, Merlin Nimier-David<sup>1</sup><sup>\*</sup>, Piotr<br>
Didyk<sup>2</sup><sup>\*</sup>, Zan Gojcic<sup>1</sup><sup>\*</sup>, and Qi Wu<sup>1</sup><sup>\*</sup>

<sup>1</sup> NVIDIA

`{nicolasm,mnimierdavid,zgojcic,qiwu}@nvidia.com`

<sup>2</sup> Università della Svizzera italiana, Lugano, Switzerland

`{jorge.condor,piotr.didyk}@usi.ch`

## 1 Additional Results

_Comparison with BBSplat._ Both BBSplat [59] and NHT are primitive-texturing methods, but BBSplat uses an _explicit_ per-primitive RGBA grid, whereas NHT uses _implicit_ textures obtained by interpolating features from a virtual scaffold and decoding them with a shared MLP in a single deferred pass. Tab. 1 compares the two on MipNeRF360 across primitive budgets, under both equal-primitive and equal-memory settings. NHT achieves substantially higher quality and faster rendering not only at equal memory, but also at equal primitive count.

In Tab. 6 we provide a detailed breakdown of Tab. 2 from the main paper, with per-scene results on MipNeRF360, Tanks and Temples and Deep Blending. For this comparison, we isolate completely the effect of our method by ensuring an even setup for all methods. All four approaches are implemented under the same framework (_gsplat_), trained for 30k iterations, using 1M primitives for all scenes, sharing training parameters among all scenes, and limiting to 48 features per primitive reserved for appearance. All results presented in this paper compute the LPIPs metric using the VGG model with normalized inputs to the range of [-1,1]. Tab. 2 reports the average wall-clock training time per dataset for all four methods on an RTX 5090, under this same controlled setup.

Furthermore, in Tab. 3 we provide another standardized comparison on all three benchmarks, only this time we match the same primitive count in each scene as the high-quality reported baselines in their respective papers, training for the same amount of iterations. We include our method with both 48 and 64 features per primitive (48F, 64F).

_Training dynamics and overfitting._ Fig. 2 shows eval-set PSNR during training on representative MipNeRF360 scenes. Highly expressive primitive appearance models can overfit when training for many epochs relative to dataset size, motivating the need to ensure equal training epochs rather than single frame iterations in Tab. 1.

Tab. 7 details the per-scene results of main Tab. 1, which uses our split indoor/outdoor training configuration. This is our higher quality setup, which<tbc>

