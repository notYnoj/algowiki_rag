## 4 Results

### 4.1 Experimental Setup

Similar to existing works (Trippe et al., 2022; Watson et al., 2023; Lin and Alquraishi, 2023), we use an in silico _self-consistency pipeline_ for measuring the quality of protein backbones. The procedure involves an inverse-folding network and a structure prediction network. We use ProteinMPNN (Dauparas et al., 2022) and ESMFold (Lin et al., 2022), respectively. First, the inverse-folding network predicts each generated backbone’s representative amino-acid sequences. Then, the structure prediction network folds these sequences into structures. The _self-consistency root mean squared deviation (scRMSD)_ between the generated and predicted backbones are then computed, and the smallest is reported. The premise of this technique is that generated backbones possessing natural structures are likely to be represented consistently across orthogonal methods. We use the available in-silico design pipeline provided by the authors of Genie2<sup>1</sup>. The set-up is summarised in Fig. 2.

### Designability and Diversity Metrics.

We adopt a similar designability criterion as Lin et al. (2024). We consider a protein backbone as _designable_ if it deviates with the most similar predicted design by at most two Angstroms (\(\mathrm{scRMSD}\le 2\mathrm{A}\)) and if the designs are confidently predicted (\(\mathrm{pLDDT}\ge 70\)). For motif scaffolding tasks, we consider a scaffold to be successful if it is designable as above, the motif is present in the predicted backbone within one Angstrom in alignment deviation (\(\mathrm{motif RMSD}\le 1\mathrm{A}\)), and there is a low predicted alignment error (pAE) between residues (\(\mathrm{pAE}\le 5\)). For multi-motif scaffolding, every motif must be within one Angstrom. We remark that scRMSD in motif scaffolding differs from the unconditional setting, as inverse-folded sequences are conditioned to fix the motif’s sequence. Furthermore, as success rates can be misleading with identically designed structures, we also measure sample _diversity_. Designs are grouped using single-linkage hierarchical clustering with a distance threshold given by a TM-score of 0.6. We report the number of unique successful scaffolds for motif scaffolding tasks.

### Conditional Setup.

In our analyses, we use Genie (Lin and Alquraishi, 2023), an unconditional protein backbone diffusion model. Specifically, we use Genie-SCOPE-128 and Genie-SCOPE-256, models trained on proteins from the SCOPE dataset (Fox et al., 2014), capable of generating proteins of up to 128 and 256 residues, respectively. For single-motif problems, where the overall length is at most 128 residues, we use Genie-SCOPE-128 for quicker inference times. For the multi-motif case, with problems requiring longer samples, we use Genie-SCOPE-256. In each model, samples are denoised for _T_=1000 steps. We parallelise our setup across two NVIDIA GeForce RTX-3090 GPUs to accelerate the process but limit each motif problem to 32 backbones per posterior sampler.

<sup>1</sup>The repository is available at `https://github.com/aqlaboratory/insilico\_design\_pipeline`.

motif RMSD
Motif
MASDKFKLSFGDCA AHASDFKLSFPKKL RADWEFKLSFMWQE
Unconditional Diffusion Model
Inverse- Fold
Sample
Fold
p(x y) Posterior Sampler
Generated Structure
Predicted Structure
scRMSD

Figure 2: **An overview of the motif scaffolding experimental setup.** Protein backbones are first sampled from the conditional setup with the motif as an observation. These generated structures are then inverse-folded with the motif sequence fixed and folded back into structures. Finally, metrics such as self-consistency RMSD and motif RMSD are computed between the predicted structure and both the generated structure and the motif.

