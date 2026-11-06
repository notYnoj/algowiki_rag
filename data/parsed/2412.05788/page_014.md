<tbc>motif scaffolding. For completeness, we also report the cost of BPF using the likelihood in (4). We did not evaluate it on the full benchmark, as its twisted version is a special case of TDS with a guidance scale of zero, and we found this to be sub-par to larger scale values in our hyperparameter search.

The calculation of guidance potentials also contributes to the overall runtime, notably going through automatic differentiation, albeit considerably less than the score model invocations. How the runtime complexity scales with the motif length is listed in  2. Depending on the problem, the motif may have a total length more than half the entire protein (e.g. 1PRW). However, we found the quadratic complexity to be a non-issue given the relatively small maximum number of residues. In any case, masking, which maintains the problem’s linearity, and RMSD, which has the most promising results, both scale linearly. With multiple motifs, the complexity is in terms of the longest motif.

## 5 Discussion

We proposed a set of guidance potentials and evaluated various SMC samplers for the motif scaffolding problem. We produced successful scaffolds for several single-motif and multi-motif problems in zero-shot. On single-motif problems, our proposed potentials perform comparably to masking while generalising to the multi-motif case, and reconstruction guidance outperformed replacement methods when aided by SMC. Internally symmetric monomers were also successfully designed by our setup, and their composition with motifs is left for subsequent work.

Our assessments were limited in the number of backbones sampled and motif placements considered. We welcome further exploration of the performance of various potentials with larger sample sizes and uniform sampling of valid motif placements. With scaffolding performance being only as good as the underlying unconditional model, the model-agnostic quality of the methods allows future, more performant models to be swapped in. Another major point of future work is incorporating sequence information in our setup to specify the correct target distribution and thereby improve the efficiency of samplers. Unlike structure, where bespoke potentials can be crafted, sequence information must likely come from pre-trained models with an inherent understanding of amino acid interactions. We have shown that it is possible to address multi-motif scaffolding without sequence information but believe it is essential to make zero-shot practices viable. Finally, several guidance potentials were motivated by work within the backbone modelling space and were rooted in the rigid body assumption involving idealised bond lengths and angles. With all-atom diffusion models on the horizon, additional work can be done to support these more general protein representations.

### Acknowledgements

J.M.Y. would like to thank Joshua Southern for insightful discussions and a warm welcome to the world of protein design.

\begin{tabular}{cccc}
\multirow{2}{*}{**Sampler**} & \multicolumn{2}{c}{**# Model Passes**} & **Est. Speedup** \\
 & **FW** & **BW** & **over TDS** \\
BPF (with noised \(\{\mathbf{y}_t\}_{t=1}^T\)) & \(\approx\widehat{\text{ESS}}_\text{avg}T\) & 0 & \(\frac{3K}{\widehat{\text{ESS}}_\text{avg}}\)x \\
BPF (with approx. in (4)) & _KT_ & 0 & 3x \\
FPS-SMC & \(\approx\widehat{\text{ESS}}_\text{avg}T\) & 0 & \(\frac{3K}{\widehat{\text{ESS}}_\text{avg}}\)x \\
MCGDiff & _KT_ & 0 & 3x \\
TDS & _KT_ & _KT_ & 1x \\
\end{tabular}

\begin{tabular}{cc}
**Potential** & **Runtime** \\
**Complexity** \\
Mask & _O_(|M|) \\
Distance & _O_(|M|<sup>2</sup>) \\
Frame-Distance & _O_(|M|<sup>2</sup>) \\
FAPE & _O_(|M|<sup>2</sup>) \\
RMSD & _O_(|M|) \\
\end{tabular}

1: **The number of score model passes and estimated runtime speedup over TDS for each sampler.** Here, _K_ is the number of particles, _T_ is the number of denoising time steps, and \(\widehat{\text{ESS}}_\text{avg}\) is the average ESS taken across all time steps.

2: **The runtime complexity of guidance potential calculations in terms of motif length.**

