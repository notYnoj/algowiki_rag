## 3 Guidance Potentials for Motif Scaffolding

The motif scaffolding problem has structure and sequence requirements, only the former of which is accessible to a typical backbone diffusion model. Hence, our focus is on the structural aspect of the problem. In this section, we provide different ways (in particular a number of potential functions) to encode the scaffolding problems to be solved by diffusion posterior samplers.

For convenience, we work with the flattened representation \(\mathbf{x}\in\mathbb{R}^{3N}\), a protein backbone with _N_ residues, each represented by its three-dimensional \(\mathrm{C}\alpha\) coordinates. From these coordinates, we may represent the protein as a set of rigid body frames, where the _i_th residue is given by \(\mathbf{T}_i(\mathbf{x})=(\mathbf{R}_i(\mathbf{x}),\mathbf{t}_i(\mathbf{x}))\in\mathrm{SE}(3)\), a pair of a rotation matrix and a translation vector with respect to a global reference frame. For a proper rigid transformation \(\mathbf{T}\in\mathrm{SE}(3)\), we denote by \(\mathbf{T}\circ\mathbf{x}\) the result of applying the transformation to each of the residue coordinates of the protein.

### 3.1 Single-Motif Scaffolding

We define the motif and scaffold index sets (M,S) as a partition over all the backbone coordinate values, with each residue’s coordinates belonging to the same set. Furthermore, we assume an ordering on \(\{\mathcal{M}_i\}_{i=0}^{|\mathcal{M}|}\) and \(\{\mathcal{S}_i\}_{i=0}^{|\mathcal{S}|}\), first according to residue number and then coordinate axis. Given the \(\mathrm{C}\alpha\) coordinates of a motif \(\mathbf{m}\in\mathbb{R}^{|\mathcal{M}|}\), we set our measurement to be **y**=**m**. The (single-) motif scaffolding problem requires sampling from the distribution _p_(**x**|**x**<sub>M</sub>=**y**), where the conditioned equality holds when the motif, oriented in whichever way, appears in the backbone region specified by the motif index set, i.e. there exists a \(\mathbf{T}^*\in\mathrm{SE}(3)\) where \(\mathbf{x}_\mathcal{M}=\mathbf{T}^*\circ\mathbf{y}\).

This task is commonly framed as a linear inverse problem by fixing the motif’s orientation and conditioning on a partial view of the backbone. Here, we use a linear transformation \(\mathcal{A}:=\mathbf{A}_\mathcal{M}\in\mathbb{R}^{|\mathcal{M}|\times 3N}\), given by \((\mathbf{A}_\mathcal{M})_{ij}=\delta_{\mathcal{M}_i,j}\), to mask the backbone and allow a direct comparison with the motif, which is translated to share the same centre-of-mass (CoM). The corresponding potential is thus given by

\(L_\mathrm{mask}(\mathbf{x};\mathbf{y},\mathcal{M})=\|\mathbf{y}-\mathbf{A}_\mathcal{M}\mathbf{x}\|^2.\) (5)

Throughout, we equivalently use **x**<sub>M</sub> in place of **A**<sub>M</sub>**x**. This approach is taken in several posterior sampling works (Trippe et al., 2022; Wu et al., 2023), drawing parallels to image inpainting. However, unlike images, a protein motif can further be oriented in 3D space, and fixing it disrupts the equivariance of the denoising process while posing questions on how multiple motifs may be handled. To address these concerns, we now introduce guidance potentials we develop in this work as alternatives to the masking potential (5).

### Distance.

Notably, Wu et al. (2023) improved masking performance by parameterising over a finite set of possible motif orientations. This is likely because we impose a narrower path towards the posterior distribution without the additional degree of freedom. Motivated by this, we consider conditioning on the full pairwise \(\mathrm{C}\alpha\) distances of the unmasked backbone. Denote the pairwise Euclidean distance matrix derived from two flattened 3D coordinate vectors \(\mathbf{u},\mathbf{v}\in\mathbb{R}^{3n}\) as \(\mathbf{D}_{\mathbf{u},\mathbf{v}}^\mathrm{euc}\in\mathbb{R}^{n\times n}\), where \((\mathbf{D}_{\mathbf{u},\mathbf{v}}^\mathrm{euc})_{ij}=\|\mathbf{t}_i(\mathbf{u})-\mathbf{t}_j(\mathbf{v})\|\). We define the potential as

\(L_\mathrm{dist}(\mathbf{x};\mathbf{y},\mathcal{M})=\|\mathbf{D}_{\mathbf{y},\mathbf{y}}^\mathrm{euc}-\mathbf{D}_{\mathbf{x}_\mathcal{M},\mathbf{x}_\mathcal{M}}^\mathrm{euc}\|_F^2\) (6)

where \(\|\cdot\|_F\) is the Frobenius norm. Contrary to masking, this approach yields an orientation-free motif representation. Its indifference to reflections, however, violates the chirality of proteins, and we explore this drawback in our experiments. The above is akin to an unnormalised dRMSD metric (AlQuraishi, 2019).

### Frame-Distance.

We propose to break the reflection-invariance of the distance potential (6) by further conditioning on the backbone’s pairwise orientation deviations within its frame representation. Similarly, we define distances between the rotation matrices **R**_<sub>i</sub>_(**x**). First, we remove the dependence on the protein’s current orientation by computing the relative rotations \(\mathbf{R}_j(\mathbf{x})^\top\mathbf{R}_k(\mathbf{x})\) for every residue pair (_j,k_). Then, we use the result measuring the cosine of the angular difference between two rotation matrices<tbc>

\(d_\mathrm{cos}(\mathbf{R}_1,\mathbf{R}_2)=\frac{1}{2}(\mathrm{Tr}\left(\mathbf{R}_1\mathbf{R}_2^\top\right)-1),\)

