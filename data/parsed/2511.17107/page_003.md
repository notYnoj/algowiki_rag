## 2.1. Yee’s Scheme

In this subsection, we set the primitive lattice vectors to be the standard orthonormal basis of R<sup>3</sup>, i.e., **_a_**_<sub>i</sub>=e<sub>i</sub>_ and \(\Omega=(0,1)^3\). We uniformly partition the domain \(\Omega\) into a cubic grid with division \(N\in\mathbb{N}^*\), grid size _h_=1_/N_ in each _x,y,z_ direction. Although the generalization to distinct divisions along each axis is straightforward, it does not yield improvements. The distributions of node, edge, face and volume DoFs are shown in Figure 1.

In Yee’s staggered grid \[19\] the magnetic field **_H_**=(**_H_**<sub>1</sub>_,H_**<sub>2</sub>_,H_**<sub>3</sub>) is approximated by face DoFs, while electric field **_E_**=(_E_<sub>1</sub>_,E_<sub>2</sub>_,E_<sub>3</sub>) by edge DoFs:

\(E\mapsto E_h:=\left(E_h^1,E_h^2,E_h^3\right)^\top:=\left(E_{i-\frac{1}{2},j,k}^1,E_{i,j-\frac{1}{2},k}^2,E_{i,j,k-\frac{1}{2}}^3\right)^\top,H\mapsto H_h:=\left(H_h^1,H_h^2,H_h^3\right)^\top:=\left(H_{i,j-\frac{1}{2},k-\frac{1}{2}}^1,H_{i-\frac{1}{2},j,k-\frac{1}{2}}^2,H_{i-\frac{1}{2},j-\frac{1}{2},k}^3\right)^\top,\) (2.1)

where \(1\le i,j,k\le N\). Subscripts represent discrete coordinates on the Cartesian grid where the function is evaluated. The image of the divergence operator \(\nabla_\mathbf{k}\cdot\) acting on an arbitrary periodic scalar function \(\psi\), for example, is approximated by volume DoFs:

\(\psi\mapsto\psi_h:=\left(\psi_{i-\frac{1}{2},j-\frac{1}{2},k-\frac{1}{2}}\right).\) (2.2)

Therefore we introduce discrete spaces of edge, face and volume DoFs as

\(\mathcal{E}_h:=\left\{\left(E_{i-\frac{1}{2},j,k}^1,E_{i,j-\frac{1}{2},k}^2,E_{i,j,k-\frac{1}{2}}^3\right):E\text{is a periodic field on}\Omega\right\}\simeq\mathbb{C}^{3N^3},\mathcal{F}_h:=\left\{\left(H_{i,j-\frac{1}{2},k-\frac{1}{2}}^1,H_{i-\frac{1}{2},j,k-\frac{1}{2}}^2,H_{i-\frac{1}{2},j-\frac{1}{2},k}^3\right):H\text{is a periodic field on}\Omega\right\}\simeq\mathbb{C}^{3N^3},\mathcal{V}_h:=\left\{\left(\psi_{i-\frac{1}{2},j-\frac{1}{2},k-\frac{1}{2}}\right):\psi\text{is a periodic scalar function on}\Omega\right\}\simeq\mathbb{C}^{N^3}.\) (2.3)

In the double curl problem (1.4), the discrete outer curl operator maps edge DoFs to face DoFs. Crucially, the inner curl operator is derived as the adjoint of the outer operator, mapping face DoFs to edge DoFs. We denote the matrix representations for the outer curl operator \(\nabla_\mathbf{k}\times\), the permittivity \(\varepsilon\) and the divergence operator \(\nabla_\mathbf{k}\cdot\) as A, \(\mathcal{M}_\varepsilon\) and B, respectively. Then due to the adjoint relation \[8, 12\], matrix representation of the inner curl operator \(\nabla_\mathbf{k}\times\) is simply A<sup>†</sup>, where "†" denotes the conjugate transpose. We have

\(\mathcal{A}:\mathcal{E}_h\rightarrow\mathcal{F}_h,\mathcal{M}_\varepsilon:\mathcal{E}_h\rightarrow\mathcal{E}_h,\mathcal{A}^\dagger:\mathcal{F}_h\rightarrow\mathcal{E}_h,\mathcal{B}:\mathcal{F}_h\rightarrow\mathcal{V}_h.\) (2.4)

For any \(E_h\in\mathcal{E}_h\), the image A**_E_**_<sub>h</sub>_ along each axis has the following expressions:

\(\left(\mathcal{A}E_h\right)_{i,j-\frac{1}{2},k-\frac{1}{2}}=\frac{E_{i,j,k-\frac{1}{2}}^3-E_{i,j-1,k-\frac{1}{2}}^3}{h}-\frac{E_{i,j-\frac{1}{2},k}^2-E_{i,j-\frac{1}{2},k-1}^2}{h}\)

Node DoFs
Edge DoFs
Face DoFs
Volume DoFs
Z
Z
Z
Z
X
y
X
y
X
y
X
y

**Figure 1:** DoFs of scalar and vector grid functions on a single cell

