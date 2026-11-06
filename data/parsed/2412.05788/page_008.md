## 3.3 Symmetric Generation

For some point symmetry group in R<sup>3</sup>, define \(\mathcal{G}=\{\mathbf{g}_k\}_{k=0}^{n-1}\) as the set of all its symmetry operations. We consider designing internally symmetric monomers as we focus on diffusion models that produce a single chain. However, our formulation can analogously be applied to models supporting multiple chains to design symmetric oligomers by treating each subunit as a monomer. Suppose the chain is composed of _n_ identical subunits with _N_ divisible by _n_. In dealing with 3D atom coordinates, G is a set of transformation matrices in \(\mathbb{R}^{3\times 3}\). Without loss of generality, we select **g**<sub>0</sub> as the identity matrix. We can then construct the potential<tbc>

\(L_\mathcal{G}(\mathbf{x})=\|(\mathbf{A}_\mathcal{G}-\mathbf{I}_{3N})\mathbf{x}\|^2,\)

<tbc>where our measurement is implicitly set to **y**=**0** and \(\mathbf{A}_\mathcal{G}\in\mathbb{R}^{3N\times 3N}\) is given by

\(\mathbf{A}_\mathcal{G}=\left[\begin{array}{ c }
\mathrm{diag}(\mathbf{g}_0,\dots,\mathbf{g}_0) \\
\vdots \\
\mathrm{diag}(\mathbf{g}_{n-1},\dots,\mathbf{g}_{n-1})
\end{array}\right|0\right],\)

composed of block diagonals \(\mathrm{diag}(\mathbf{g}_k,\dots,\mathbf{g}_k)\in\mathbb{R}^{3N/n\times 3N/n}\). Effectively, this constrains the generated protein to be identical to several symmetric projections of its first subunit. This partitions the chain into _n_ contiguous segments representing each subunit. However, one can shuffle the block diagonals between group operations to render the subunits discontinuous. We demonstrate this process for cyclic and dihedral symmetries.

### 3.3.1 Cyclic and Dihedral Symmetries

Proteins with cyclic symmetry _C<sub>n</sub>_ are invariant to any integer multiple rotations of \(2\pi/n\) with respect to a given axis. Without loss of generality, we choose to work with the _z_-axis and accordingly translate **x** so its CoM lies on it. Denote \(\mathbf{R}_{a,\theta}\in\mathbb{R}^{3\times 3}\) as the rotation matrix that rotates a vector anti-clockwise about the _a_-axis by an angle of \(\theta\). As such, we have the set of rotations \(\mathcal{G}_{C_n}=\{\mathbf{R}_{z,2\pi k/n}\}_{k=0}^{n-1}\). While any ordering of the set G is conducive to producing a cyclic protein, it may be favourable to have adjacent angles for adjacent sub-sequences, e.g. \(\mathbf{g}_k=\mathbf{R}_{z,2\pi k/n}\).

Proteins with dihedral symmetry _D<sub>n</sub>_ similarly have _C<sub>n</sub>_ symmetry in one axis but have _C_<sub>2</sub> symmetry in another axis orthogonal to the first. We choose the _z_- and _y_-axes as primary and secondary axes of symmetry and translate **x** to have its CoM at the origin. Thus, we have \(\mathcal{G}_{D_n}=\mathcal{G}_{C_n}\cup\{\mathbf{R}_{z,2\pi k/n}\mathbf{R}_{y,2\pi}\}_{k=0}^{n-1}\). We may then substitute **A**<sub>G<sub>_C<sub>n</sub>_</sub></sub> and **A**<sub>G<sub>_D<sub>n</sub>_</sub></sub> into our symmetry potential to impose cyclic and dihedral symmetries.

### 3.3.2 Symmetric Motif Scaffolding

In addition to symmetric constraints, we may also condition the existence of a motif. Note that we can assume the motif is local to exactly one subunit and _n_-1 copies exist in the others. Otherwise, if the motif lies on the boundary between subunits, we can redefine the motif to be the residues entirely situated in one subunit. Suppose then that the motif is in the first subunit, i.e. \(\mathcal{M}_i\le 3N/n\) for all _i_.

We may adapt the masking approach with a motif measurement **y**=**m** and define the potential

\(L_{\mathcal{G},mask}(\mathbf{x};\mathbf{y},\mathcal{M})=\left\|\left[\mathbf{e}_{\mathcal{M}_1}\dots\mathbf{e}_{\mathcal{M}_{|\mathcal{M}|}}\right]\mathbf{y}-(\mathbf{A}_\mathcal{G}-\mathbf{I}_{3N}+\mathrm{diag}(\unknown_\mathcal{M}))\mathbf{x}\right\|^2\)

where \(\mathbf{e}_i\in\mathbb{R}^N\) is the _i_th standard basis vector. The additional diagonal term unmasks the motif indices and asserts it is equal to the chosen motif **y**. We remark that this preserves the linearity of the inverse problem. More generally, e.g. for the distance approaches, we can simply add the symmetry potential _L_<sub>G</sub> onto the motif potential. For masking, however, we choose to combine the linear measurement functions so a single matrix may be supplied for supporting posterior samplers.

