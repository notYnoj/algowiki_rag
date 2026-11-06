## Motif Scaffolding.

A protein’s function is characterised by several of its structural domains. As a result, motifs from known domains can act as a foundation that, when scaffolded, can give rise to proteins with specific functional or conformational properties. The process of fixing a substructure is non-trivial, however, as the protein’s folding dynamics must be respected. Generative models on protein structure can be leveraged, given their inherent understanding of well-folded structures. RFDiffusion (Watson et al., 2023) and Genie2 (Lin et al., 2024) are current state-of-the-art diffusion models for this task, capable of scaffolding several benchmark motifs (Watson et al., 2023), from small molecule binding sites to viral epitopes. More generally, one can also scaffold multiple motifs simultaneously, e.g., to map out different functional domains. _Multi-motif scaffolding_ is more challenging as interactions between motifs must be accommodated by the scaffold. This differs from scaffolding a single motif with fixed discontiguous segments, as each motif can be oriented independently.

Another useful task is the generation of oligomers embodying some point symmetry, i.e. through the self- assembly of multiple identical monomers (Watson et al., 2023; Ingraham et al., 2023). We additionally bring attention to the design of internally symmetric monomers which fits with current monomeric generative efforts. _Symmetric motif scaffolding_ demands a symmetric protein structure with each asymmetric subunit containing a copy of the motif. For example, the SARS-CoV-2 spike protein, a _C_<sub>3</sub> symmetric trimer, may be inhibited by attaching a similarly symmetric binder--a feat RFDiffusion demonstrated in-silico.

In these scaffolding tasks, it is common to sample from a range of positions in the backbone and fix the motif in place. Wu et al. (2023) explored allowing multiple motif placements to be jointly considered during the denoising process. We refer to this as _scaffolding with degrees of freedom_. All the scaffolding tasks are illustrated in Fig. 1.

## Related Work.

We focus on solving motif scaffolding problems using an unconditional protein backbone diffusion model without additional training. Several works have previously explored the single-motif case in a similar vein. SMC-based methods include SMCDiff, a replacement method paired with ProtDiff (Trippe et al., 2022), and TDS, a reconstruction guidance method paired with FrameDiff (Yim et al., 2023). A similar work, Chroma (Ingraham et al., 2023), provides a suite of conditioners built around an unconditional model and addresses substructure motifs through reconstruction guidance and a root mean square deviation (RMSD) metric. We believe the latter idea can be incorporated without additional scaling hyperparameters.

On scaffolding multiple motifs, diffusion models have been trained to condition on pairwise residue C\(\alpha\) distances, allowing motifs to be represented independently of each other. Genie2, an extension of Genie (Lin and Alquraishi, 2023) under this scheme, achieves in-silico success on some of its curated multi-motif benchmarks. On the other hand, Castro et al. (2024) demonstrate experimental success in jointly scaffolding three epitope motifs using RFJoint2 (Wang et al., 2021), a modified RoseTTAFold network for in-painting. Taking inspiration from these efforts while side-stepping the requirement for training, we explore using distances as part of the inverse problem.

Lastly, on diffusion posterior sampling, replacement methods such as FPS-SMC (Dou and Song (2023)) and MCGDiff (Cardoso et al. (2023)) have not been explored in the motif scaffolding setting. SMC methods in general have also yet to be compared with a baseline such as the bootstrap particle filter (BPF). Formalising the scaffolding inverse problems, we aim to investigate which samplers and formalisations perform best for the tasks.

Scaffold
MM-NNN
PPP
MMM?NNN?
?PPP?
?PPP?PPP?NNN
?PPP?PPP?PPP?
?PPP ?PPP? PPP?
Motifs
Single-Motif
Multi-Motif
Symmetric
With DoF

Figure 1: **Different motif scaffolding tasks.** The motif in blue is contiguous, and the other in red is discontiguous. Scaffolds are illustrated in white.

