<tbc>to compare the sample’s relative rotations with those of the motif. We define

\(L_\mathrm{chiral}(\mathbf{x};\mathbf{y},\mathcal{M})=\|\mathbf{1}\mathbf{1}^\top-\mathbf{D}_{\mathbf{y},\mathbf{x}_\mathcal{M}}^\mathrm{cos}\|_F^2,\)<br>
\(\text{where}(\mathbf{D}_{\mathbf{y},\mathbf{x}_\mathcal{M}}^\mathrm{cos})_{ij}=d_\mathrm{cos}(\mathbf{R}_i\big(\mathbf{y}\big)^\top\mathbf{R}_j(\mathbf{y}),\mathbf{R}_i(\mathbf{x}_\mathcal{M})^\top\mathbf{R}_j(\mathbf{x}_\mathcal{M})).\)

We keep the angle in its cosine form due to the instability of arccosine gradients near one. Summing with the previous formulation, we have the potential

\(L_\mathrm{framedist}(\mathbf{x};\mathbf{y},\mathcal{M})=L_\mathrm{dist}(\mathbf{x};\mathbf{y},\mathcal{M})+\eta_\mathrm{chiral}\cdot L_\mathrm{chiral}(\mathbf{x};\mathbf{y},\mathcal{M}),\) (7)

where \(\eta_\mathrm{chiral}\) is a hyperparameter to scale the magnitude of the chiral contribution.

## Frame-Aligned Point Error (FAPE).

A similar idea of an SE(3)-invariant measure with chiral properties is the frame-aligned point error (FAPE)--the main component of the AlphaFold2 loss function (Jumper et al., 2021). FAPE defines a distance metric between two sets of rigid body frames of the same dimension and attains a value of zero when the two sets of frames are identical up to proper rigid transformations. To match the magnitude of the masking approach, we modify the original formulation to yield the potential

\(L_\mathrm{fape}(\mathbf{x};\mathbf{y},\mathcal{M})=\frac{1}{|\mathcal{M}|}\sum_{i=1}^{|\mathcal{M}|}L_\mathrm{mask}\big(\mathbf{T}_i(\mathbf{x}_\mathcal{M})^{-1}\circ\mathbf{x};\mathbf{T}_i(\mathbf{y})^{-1}\circ\mathbf{y},\mathcal{M}\big),\)

where **T**<sup>-1</sup> is the inverse of the transformation **T**. For each motif residue, we essentially set its C\(\alpha\) atom as the global reference, allowing both the specified backbone region and the motif to coincide at the residue and their deviation to be computed.

## Root Mean Squared Deviation (RMSD).

A common measure for structural similarity between protein structures is through their root mean squared deviation (RMSD). For protein backbones \(\mathbf{u},\mathbf{v}\in\mathbb{R}^{3n}\), each with _n_ residues, we have<tbc>

\(\mathrm{RMSD}(\mathbf{u},\mathbf{v})=\mathrm{min}_{\mathbf{T}^*\in\mathrm{SE}(3)}\frac{1}{\sqrt{n}}\|\mathbf{u}-\mathbf{T}^*\circ\mathbf{v}\|.\)

<tbc>Similarly, we define a potential matching the form and magnitude of masking

\(L_\mathrm{rmsd}(\mathbf{x};\mathbf{y},\mathcal{M})=|\mathcal{M}|\cdot\mathrm{RMSD}(\mathbf{x}_\mathcal{M},\mathbf{y})^2=\mathrm{min}_{\mathbf{T}^*\in\mathrm{SE}(3)}L_\mathrm{mask}(\mathbf{x};\mathbf{T}^*\circ\mathbf{y},\mathcal{M}).\)

Here, we can obtain the minimiser transformation **T**<sup>∗</sup>=(**R**<sup>∗</sup>,**t**<sup>∗</sup>) using the Kabsch algorithm (Kabsch, 1976) or directly compute the RMSD through quaternions (Coutsias et al., 2004). Both methods are differentiable.

A consequence of the proposed potentials’ SE(3)-invariance is their gradients, used in reconstruction guidance, maintain the equivariance of the denoising process--i.e. the global orientation of noisy samples do not affect how they are denoised.

## 3.2 Multi-Motif Scaffolding

Now, suppose the index sets {M<sup>1</sup>_,...,_M_<sup>M</sup>,_S} form a partition over the backbone coordinates and are each ordered according to residue number and coordinate axis. Given motifs **m**<sub>1</sub>_,...,_**m**_<sub>M</sub>_, we define the measurement \(\mathbf{y}\in\mathbb{R}^{3N}\) as **y**<sub>S</sub>=**0** and **y**<sub>M_<sup>i</sup></sub>=**m**_<sub>i</sub>_ for \(i\in[1,M]\). The multi-motif scaffolding problem requires sampling from the distribution _p_(**x**|**x**<sub>M<sup>1</sup></sub>=**y**<sub>M<sup>1</sup></sub>_,...,_**x**<sub>M_<sup>M</sup></sub>=**y**<sub>M_<sup>M</sup></sub>), with the conditioned equalities similar as before, i.e. there exists \(\mathbf{T}_i^*\in\mathrm{SE}(3)\) where \(\mathbf{x}_{\mathcal{M}^i}=\mathbf{T}_i^*\circ\mathbf{y}_{\mathcal{M}^i}\) for \(i\in[1,M]\).

Unlike in the single motif case, the masking approach fixes the motif-to-motif orientations and severely underrepresents the posterior distribution. Instead, we may use the other proposed approaches to keep each motif’s orientation independent of others. This can be achieved by summing the potentials

\(L^{\mathcal{M}^{1:M}}\big(\mathbf{x};\mathbf{y},\mathcal{M}^1,\dots,\mathcal{M}^M\big)=\sum_{i=1}^ML^{\mathcal{M}^i}\big(\mathbf{x};\mathbf{y}_{\mathcal{M}^i},\mathcal{M}^i\big),\)

where _L_<sup>M_<sup>i</sup></sup> is the chosen potential corresponding to the _i_th motif. While it is possible to use different potentials for each motif, we choose to keep it fixed in our analyses.

