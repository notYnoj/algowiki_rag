_Proof._ If at least one off-diagonal entries of \(\varepsilon_1\) vanish, then \(\varepsilon_1\) is either tridiagonal or similar to a tridiagonal matrix due to Lemma 3.4. Thus by shrinking diagonal entries of \(\mathcal{M}_\varepsilon\) to \(min\{1,\varepsilon_{ii}\}=\varepsilon_{ii}\), applying Proposition 3.7 and Lemma 3.9, we conclude that \(\mathcal{M}_\varepsilon\) is HPD. \(\square\)

## 4. Numerical experiments

All calculations are carried out based on the matrix-free kernel compensation formulation (2.32) with penalty coefficient \(\gamma\) set by (2.26). We consider the simple cubic (SC), face-centered cubic (FCC) and body-centered cubic (BCC) lattices. The primitive lattice vectors (**_a_**<sub>1</sub>_,**a**_<sub>2</sub>_,**a**_<sub>3</sub>) of the lattice types, which can be found in [9], are specified as:

\(\left\{\begin{array}{ c c } SC\text{lattice:} & a_1=(1,0,0)^\top,a_2=(0,1,0)^\top,a_3=(0,0,1)^\top, \\ FCC\text{lattice:} & a_1=(0,\frac{1}{2},\frac{1}{2})^\top,a_2=(\frac{1}{2},0,\frac{1}{2})^\top,a_3=(\frac{1}{2},\frac{1}{2},0)^\top, \\ BCC\text{lattice:} & a_1=(-\frac{1}{2},\frac{1}{2},\frac{1}{2})^\top,a_2=(\frac{1}{2},-\frac{1}{2},\frac{1}{2})^\top,a_3=(\frac{1}{2},\frac{1}{2},-\frac{1}{2})^\top.\end{array}\right.\) (4.1)

The wave number vector **k** in model problem (1.4) is derived from symmetry points and partition points on their connecting lines in the Brillouin zone. These symmetry points are:

\(\left\{\begin{array}{ c c } SC: & K(0,0,0),L(\pi,0,0),M(\pi,\pi,0),N(\pi,\pi,\pi), \\ FCC: & X(0,2\pi,0),U(\frac{\pi}{2},2\pi,\pi),L(\pi,\pi,\pi),\Gamma(0,0,0),W(\pi,2\pi,0),K(\frac{3\pi}{2},\frac{3\pi}{2},0), \\ BCC: & H'(2\pi,0,0),\Gamma(0,0,0),P(\pi,\pi,\pi),N(\pi,0,\pi),H(0,2\pi,0).\end{array}\right.\) (4.2)

The primitive lattice vectors (4.1) and symmetry points (4.2) are given in dimensionless units, which corresponds to setting the lattice constant to unity. This choice is independent of any physical scaling and is made without loss of generality, as such a scaling constant does not affect the results or efficiency. We investigate four different lattice structures, the unit cells of which are visually presented in Figure 2. These models can be found in [6, 13, 17]. For simplicity, we will refer to these structures by abbreviations:

\(\bullet\) **SC-CURV (SC lattice with curved surface)**: The SC lattice shown in Figure 2a is composed of a sphere with radius 0.345 and four cylinders with base radius 0.11.

\(\bullet\) **FCC**: The FCC lattice in Figure 2b adopts a diamond structure. Its material configuration is _sp_<sup>3</sup>-like, consisting of spheres with radius of 0.12 and connecting spheroids of minor axis 0.11. The foci of the spheroids are located at the centers of the spheres.

\(\bullet\) **BCC-SG (BCC lattice with single gyroid surface)**: The BCC lattice in Figure 2c has its material domain specified by \(\{x\in\Omega:g(x)>1.1\}\), where

\(g(x,y,z)=sin(2\pi x)cos(2\pi y)+sin(2\pi y)cos(2\pi z)+sin(2\pi z)cos(2\pi x).\)

\(\bullet\) **BCC-DG (BCC lattice with double gyroid surface)**: Similar to BCC-SG, the material domain of BCC lattice shown in Figure 2d is specified by \(\{x\in\Omega:|g(x)|>1.1\}\).

The matrix eigenproblem (2.32) is solved by a custom-implemented LOBPCG (Locally Optimal Block Preconditioned Conjugate Gradient) solver with soft locking [11] in Python. We define the relative residual for the _j_-th eigenvalue-eigenvector pair \((\omega_{h,j}^2,x_j)\) as

\(Res_j:=\frac{\left\|(\mathcal{M}_\varepsilon\mathcal{A}^\dagger+\gamma\mathcal{B}^\dagger\mathcal{B})x_j-\omega_{h,j}^2x_j\right\|_2}{\left\|x_j\right\|_2},\left\|\cdot\right\|_2\text{refers to the 2-norm.}\) (4.3)

