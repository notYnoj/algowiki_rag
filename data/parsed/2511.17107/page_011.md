Subsection 3.2 explains the numerical difficulty and presents two explicit solutions. Rigorous proofs of HPD properties are provided in Subsection 3.3. We specify the following notations to avoid ambiguity of subscripts:

\((\mathbf{A})_{ij}:\text{the}(i,j)\text{entry of matrix}\mathbf{A};(\mathbf{D})_i:\text{the}i\text{-th entry of diagonal matrix}\mathbf{D};\mathcal{M}_{ij}:\text{the}(i,j)\text{matrix block of a block matrix;}\mathbf{M}_k:\text{the}k\text{-th diagonal block of a block diagonal matrix.}\) (3.1)

The permittivity is denoted by \(\varepsilon_1=(\varepsilon_{ij})_{1\le i,j\le 3}\), where \(\varepsilon_{ij}\)’s denote the entries of \(\varepsilon_1\). We also introduce edge and volume indicator matrices \(\mathcal{I}_\mathcal{E}\in\unknown^{3N^3\times 3N^3},\mathcal{I}_\mathcal{Y}\in\unknown^{N^3\times N^3}\) to distinguish the DoFs located within the material subdomain \(\Omega_1\):

\((\mathcal{I}_\mathcal{E})_\beta=\left\{\begin{array}{ c c }
1, & \beta\text{-th edge DoF is located in}\Omega_1, \\
0, & \text{otherwise,}
\end{array}\right.\mathcal{I}_\mathcal{E}=\text{diag}(\mathcal{I}_1,\mathcal{I}_2,\mathcal{I}_3), \\
(\mathcal{I}_\mathcal{Y})_\beta=\left\{\begin{array}{ c c }
1, & \beta\text{-th volume DoF is located in}\Omega_1, \\
0, & \text{otherwise.}
\end{array}\right.\) (3.2)

Matrix **I**<sub>E</sub> can be naturally decomposed into three \(N^3\times N^3\) diagonal blocks, where each **I**_<sub>i</sub>_ corresponds to the indicator matrix for edge-DoFs aligned along the _i_-th axis.

## 3.1. Diagonal Cases

The construction is straightforward when the material permittivity \(\varepsilon_1\) is a diagonal matrix, i.e. \(\varepsilon_1=\text{diag}(\varepsilon_{11},\varepsilon_{22},\varepsilon_{33})\), \(\varepsilon_{ii}>0\). In this case the dielectric matrix \(\mathcal{M}_\varepsilon\) is also diagonal:

\(\mathcal{M}_\varepsilon=\text{diag}(\mathcal{M}_{11},\mathcal{M}_{22},\mathcal{M}_{33}),\mathcal{M}_{ii}=(\varepsilon_{ii}-1)\mathcal{I}_i+I_{N^3},\) (3.3)

where **I**_<sub>i</sub>_ is defined in (3.2). We adopt a direct pointwise evaluation of \((\mathcal{M}_{ii})_\beta\). While other approaches, such as that in [16], employ a local average of surrounding values, our simpler treatment is sufficient to maintain the accuracy of the scheme.

## 3.2. Misalignment of DoFs

A challenge arises when \(\varepsilon_1\) contains nonzero off-diagonal entries (e.g., \(\varepsilon_{12}=\varepsilon_{21}^*\neq 0\)), which couple different electric field components. The staggered nature of the grid leads to a misalignment of DoFs: The evaluation of the term for the _x_-component of the electric field requires the quantity \(\varepsilon_{12}E_2\), while _E_<sub>2</sub> is approximated by _y_-edge DoFs, a direct evaluation of _E_<sub>2</sub> on any _x_-aligned edge is not available. This misalignment problem occurs for all off-diagonal coupling terms. We propose a trivial solution and a more physically accurate interpolation-based method to address this numerical difficulty.

### 3.2.1. A Trivial Solution

The simplest approach is to completely neglect the spatial mismatch on the off-diagonal blocks and consider **I**<sub>1</sub>,**I**<sub>2</sub>,**I**<sub>3</sub> as equivalent with **I**<sub>Y</sub>. In this case we define

\(\mathcal{M}_\text{Trivial}:=\left(\begin{array}{ c c c }
\mathcal{M}_{11} & \varepsilon_{12}\mathcal{I}_\mathcal{Y} & \varepsilon_{13}\mathcal{I}_\mathcal{Y} \\
\varepsilon_{12}^*\mathcal{I}_\mathcal{Y} & \mathcal{M}_{22} & \varepsilon_{23}\mathcal{I}_\mathcal{Y} \\
\varepsilon_{13}^*\mathcal{I}_\mathcal{Y} & \varepsilon_{23}^*\mathcal{I}_\mathcal{Y} & \mathcal{M}_{33}
\end{array}\right).\) (3.4)

Although geometrically inaccurate, this approach produces a simply structured matrix, allowing matrix-free implementations of \(E_h\mapsto\mathcal{M}_\text{Trivial}E_h\).

### 3.2.2. Cross-DoF Transfer via Interpolation

A more physically faithful approach is to bridge the misalignment by interpolation. We can approximate the value of a field component at a desired location by averaging the values from its nearest neighbors on the staggered grid. We

