Convergence is considered to be reached when \(\mathrm{Res}_j\le 10^{-5}\) for all desired eigenpairs.

This section is outlined as: In Subsection 4.1, we plot the band structures and analyze the differences adopting M<sub>Trivial</sub> and M<sub>CrossDoF</sub>. In Subsection 4.2 In Subsection 4.3 the iteration count, runtime and speedup by GPU acceleration efficiency are recorded and analyzed. Finally we simulate extreme cases to demonstrate the robustness of our scheme in Subsection 4.4. All programs are implemented on a platform equipped with NVIDIA GeForce RTX 4090 D GPUs, 24 GiB of memory, utilizing CUDA Version 12.4 and Driver Version 550.144.03 for GPU acceleration. The source code has been made publicly available on GitHub `https://github.com/Epsilon-79th/ linear-eigenvalue-problems-in-photonic-crystals`.

## 4.1. Band Structures of isotropic and Anisotropic Systems

The expression of \(\varepsilon_1\), which refers to the inverse of permittivity inside \(\Omega_1\) as we define in (1.5), is chosen to be

\(\varepsilon_1=\varepsilon_\mathrm{lattice}^{-1}I_3,\text{for isotropic systems,}\varepsilon_1=\varepsilon_\mathrm{lattice}^{-1}\left(\begin{array}{ c c } \sqrt{1+|\beta|^2} & -|\beta|\mathrm{i} \\ |\beta|\mathrm{i} & \sqrt{1+|\beta|^2} \end{array}\right),\text{for anisotropic systems,}\) (4.4)

where the external magnetic field intensity \(\beta=0.875\), \(\varepsilon_\mathrm{lattice}\) is a constant depending on the type of lattice. We set \(\varepsilon_\mathrm{lattice}=13\) for the SC and FCC lattice and \(\varepsilon_\mathrm{lattice}=16\) for the BCC lattice. We compute the first 10 smallest frequencies with grid division _N_=120 and discrete permittivity matrix \(\mathcal{M}_\varepsilon=\mathcal{M}_\mathrm{CrossDoF}\). The band structures are presented in

1 0.8 0.6 0.4 0.2 0
1 1
0.5 0.5 y
0 0
X (a) SC-CURV. (b) FCC. 1
0.8 0.6 0.4 0.2 0
1 1
0.5 0.5 y
0 0
X (c) BCC-SG. (d) BCC-DG. (e) BCC-SG. (e) BCC-DG.

**Figure 2:** Figures of material structures of four sample lattices in cubic domain [0,1]<sup>3</sup>.

