**Primer on Protein Structure.** A protein’s _tertiary_ structure--its three-dimensional arrangement in space--is often the modality of choice for generative modelling. A key reason is that applications are centred around designing proteins with some function, and while the sequence defines the protein, its function is more evident in its structure. Fig. 6 illustrates this structure, which comprises the backbone and side chains. Like most generative efforts, we limit our scope to monomeric (i.e., single-chain) protein backbones. Only after the backbone is modelled are the side chains predicted.

Since protein backbones are high-dimensional, an efficient representation incorporating their symmetries is ideal for making their associated learning problems more tractable. First, we may assume idealised bond lengths and angles, allowing the C\(\alpha\) coordinates to be representative of the entire backbone. Next, we note that rotations and translations in three-dimensional space do not change the inherent structure of the protein. These symmetries, as well as the _chiral_ properties of proteins, associate them with the _three-dimensional special Euclidean group_, SE(3), where each transformation \(\mathbf{T}=(\mathbf{R},\mathbf{t})\in\mathrm{SE}(3)\) is a pair of a rotation matrix \(\mathbf{R}\in\mathbb{R}^{3\times 3}\) and a translation vector \(\mathbf{t}\in\mathbb{R}^3\). Given the C\(\alpha\) coordinates \(\mathbf{x}\in\mathbb{R}^{N\times 3}\) of a protein backbone with _N_ residues, we denote \(\mathbf{T}\circ\mathbf{x}\) as the backbone resulting from the transformation, where \((\mathbf{T}\circ\mathbf{x})_i=\mathbf{Rx}_i+\mathbf{t}\).

The _frame_ representation (Jumper et al., 2021) incorporates the above symmetry group by treating each N - C\(\alpha\) - C substructure as a rigid body, whose orientation and position are indicated by a transformation in SE(3) with respect to a global reference frame. Here, we denote the _i_th residue of the backbone as \(\mathbf{T}_i(\mathbf{x})=(\mathbf{R}_i(\mathbf{x}),\mathbf{t}_i(\mathbf{x}))\in\mathrm{SE}(3)\), derived from the C\(\alpha\) coordinates **x** via the Gram- Schmidt process (Alg. 2). This formulation is used by several diffusion models (Watson et al., 2023; Yim et al., 2023; Lin et al., 2024) to learn the distribution of protein backbones efficiently.

**Algorithm 2:** Frame Construction from Atom Coordinates (Adapted from Supplementary Material Algorithm 21 of Jumper et al. (2021))

**input :**coordinates of _i_th N, C-\(\alpha\), and C atoms **x**<sub>_i,N_</sub>,**x**<sub>_i,CA_</sub>,**x**<sub>_i,C_</sub> **output**:frame representation of _i_th residue (**R**_<sub>i</sub>,_**t**_<sub>i</sub>_) **# Get vectors pointing from C-**\(\alpha\) **to N and C** Set \(\mathbf{v}_{i,1}\leftarrow\mathbf{x}_{i,C}-\mathbf{x}_{i,CA}\) Set \(\mathbf{v}_{i,2}\leftarrow\mathbf{x}_{i,N}-\mathbf{x}_{i,CA}\) **# Do Gram-Schmidt process** Set \(\mathbf{e}_{i,1}\leftarrow\mathbf{v}_{i,1}/\|\mathbf{v}_{i,1}\|\) Set \(\mathbf{u}_{i,2}\leftarrow\mathbf{v}_{i,2}-\mathbf{e}_{i,1}\left(\mathbf{e}_{i,1}^\top\mathbf{v}_{i,2}\right)\) Set \(\mathbf{e}_{i,2}\leftarrow\mathbf{u}_{i,2}/\|\mathbf{u}_{i,2}\|\) Set \(\mathbf{e}_{i,3}\leftarrow\mathbf{e}_{i,1}\times\mathbf{e}_{i,2}\) **# Construct frame components** Set \(\mathbf{R}_i\leftarrow(\mathbf{e}_{i,1}|\mathbf{e}_{i,2}|\mathbf{e}_{i,3})\) Set \(\mathbf{t}_i\leftarrow\mathbf{x}_{i,CA}\)

(A) Generic Protein Backbone (B) Rigid Body Frame Representation Resi-1 H
O
Resi+1 N
C Cai-1 ti N
C Cai N
C Cai Ri H
O Resi H
O

Figure 6: **The protein backbone illustrated**. **(A)** The backbone is linear, with a repeating N - C\(\alpha\) - C atomic structure. Each side chain residue is anchored at a C\(\alpha\) atom, varying structurally depending on its amino acid type. **(B)** Fixing the N - C\(\alpha\) - C substructures as rigid bodies, the _i_th residue can be represented as a (triangular) frame, defined by a rotation matrix **R**_<sub>i</sub>_ and a translation vector **t**_<sub>i</sub>_ with respect to a global reference frame.

