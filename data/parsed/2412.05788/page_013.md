<tbc>Despite our low success yield, we remain optimistic that future setups addressing our concerns can eventually narrow the gap between zero-shot and amortised scaffolding of multiple motifs, with our result as a demonstration of what is possible.

## 4.4 Symmetric Generation

Using replacement and reconstruction guidance methods, we tested our symmetric formulation by generating internally symmetric monomers for cyclic and dihedral point symmetries. Several met the designability criteria as shown in Fig. 5. Structures were less designable at higher orders of symmetry, as the subunits became increasingly short. Several designs were toroidal, with some resembling TIM barrels.

While, our method implicitly imposes symmetry, the generated backbones were all found to be symmetric. We attribute this to the tight inverse problem variance and the samplers guiding the backbone in sufficiently meeting the inverse problem formulation. This implicit approach has some advantages over explicitly symmetrising backbones at each step. It allows for control over looser symmetries by increasing the variance \(\sigma_v^2\). This widens the target space to include commonly observed monomeric proteins with non-exact internal symmetries. It is also composable with other constraints without having to orient the asymmetric subunits at fixed distances at each step.

## 4.5 Computational Costs

The samplers and guidance potentials used throughout our experiments incurred different computational costs. We outline their differences to inform future motif scaffolding experiments.

1 summarises the cost and estimated runtime of each sampler. We report the number of forward and backward passes to the score model, as it was the main bottleneck of the methods. TDS was the most expensive, having to backpropagate through the entire score model each time, regardless of its guidance potential pairing. Empirically, this resulted in runtimes up to three times longer than those of the next most expensive sampler in MCGDiff, with the backward passes taking about twice as long as the forward pass. While the rest of the samplers rely solely on forward passes to the model, we found that a subtle design choice in their weight computations resulted in significant speed-ups between them. FPS-SMC and BPF with the noised measurements do not use the score model (i.e. to get E\[**x**<sub>0</sub>|**x**_<sub>t</sub>_\] or E\[**x**<sub>_t_-1</sub>|**x**_<sub>t</sub>_\]) when calculating the weights. This enables the simple optimisation of only evaluating the score of the unique particles after resampling. Noting that the ESS (estimator) can be interpreted as a rough estimate of the unique particle count, we found that this optimisation evaluates the score of only a fraction of the _K_ particles each time, roughly equal to the average ESS across all time steps \(\widehat{\text{ESS}}_\text{avg}\). This led to speed-ups of up to _K_ times when the weights were consistently degenerate, a fairly common occurrence in a high-dimensional problem such as<tbc>

(A)
FPSSMC-128
TDS-MASK-128
FPSSMC-256
TDS-MASK-256
Unique Designable Scaffolds
10
5
0
20
Average scRMSD (L)
10
0
C-3
C-5
C-6
C-8
C-10
C-12
D-2
D-3
D-4
D-5
(B)
L 128:
C-3
C-5
D-2
D-3
D-4
L 256:
C-3
C-6
C-8
C-10
D-2

Figure 5: **(A) Designability of symmetric designs across several point symmetries**. Sixteen scaffolds with a maximum of 128 and 256 residues were sampled for each symmetry through FPSSMC and TDS-mask. The total number of designable scaffolds is dashed atop the unique count. The success threshold for scRMSD is indicated by the dashed line. **(B) Examples of the successfully designed scaffolds.** The first and second rows show designs with a maximum of 128 and 256 residues, respectively. The primary axis of symmetry points directly outwards of the page.

