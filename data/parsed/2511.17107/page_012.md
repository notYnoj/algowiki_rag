adopt the notations in (2.4): for any **_E_**_<sub>h</sub>_ consisting of edge-DoFs, there holds:

\(E_{i-\frac{1}{2},j,k}^1=\frac{1}{4}\left(E_{i-1,j-\frac{1}{2},k}^2+E_{i-1,j-\frac{1}{2},k}^2+E_{i,j-\frac{1}{2},k}^2+E_{i,j+\frac{1}{2},k}^2\right)+O(h^2),\) (3.5)

where _O(h_<sup>2</sup>) is the accuracy guaranteed by the smoothness of the original field **_E_**. Due to periodicity, (3.5) has a matrix representation using **D**<sub>0</sub> defined in (2.5):

\(E_h^1=(\mathbf{D}_0\otimes\mathbf{D}_0^\top\otimes I_N)E_h^2+O(h^2).\) (3.6)

Likewise, we obtain a set of cross-DoF transfer matrices \(\{\mathcal{T}_{ij}\}_{1\le i,j\le 3}\) as follows:

\(E_h^i=\mathcal{T}_{ij}E_h^j+O(h^2),E_h^j=\mathcal{T}_{ij}^\top E_h^i+O(h^2),1\le i<j\le 3,\mathcal{T}_{12}=\mathbf{D}_0\otimes\mathbf{D}_0^\top\otimes I_N,\mathcal{T}_{13}=\mathbf{D}_0\otimes I_N\otimes\mathbf{D}_0^\top,\mathcal{T}_{23}=I_N\otimes\mathbf{D}_0\otimes\mathbf{D}_0^\top.\) (3.7)

With these transfer operators, one might think it is sufficient to simply apply the edge indicator matrices **I**<sub>1</sub>,**I**<sub>2</sub>,**I**<sub>3</sub> afterwards. However, a naive construction of the off-diagonal block, \(\varepsilon_{12}\mathcal{I}_1\mathcal{T}_{12}\) for example, would lead to a non- Hermitian \(\mathcal{M}_\varepsilon\), as \((\varepsilon_{12}\mathcal{I}_1\mathcal{T}_{12})^\dagger=\varepsilon_{12}^*\mathcal{T}_{12}^\top\mathcal{I}_1\) does not equal the corresponding (2,1) block \(\varepsilon_{12}^*\mathcal{I}_2\mathcal{T}_{12}^\top\). To ensure Hermiticity, we construct symmetrized cross-DoF transfer operators and formulate the matrix as:

\(\mathcal{M}_\mathrm{CrossDoF}:=\left(\begin{array}{ c c c }
\mathcal{M}_{11} & \varepsilon_{12}S_{12} & \varepsilon_{13}S_{13} \\
\varepsilon_{12}^*S_{12}^\top & \mathcal{M}_{22} & \varepsilon_{23}S_{23} \\
\varepsilon_{13}^*S_{13}^\top & \varepsilon_{23}^*S_{23}^\top & \mathcal{M}_{33}
\end{array}\right),S_{ij}=\frac{\mathcal{I}_i\mathcal{T}_{ij}+\mathcal{T}_{ij}\mathcal{I}_j}{2},1\le i<j\le 3.\) (3.8)

In practice, M<sub>CrossDoF</sub> is explicitly assembled as a sparse matrix due to its relatively complicated structure. Although this solution consumes slightly more storage, the efficiency is barely affected, as is shown in the experiments.

## 3.3. Proof of HPD Property

We provide analysis for the HPD properties of the discrete permittivity matrix M<sub>Trivial</sub> and M<sub>CrossDoF</sub>, which are expected to be HPD whenever the \(3\times 3\) matrix \(\varepsilon_1\) is HPD. Unfortunately, the HPD property may not be preserved without the following assumptions:

**Assumption 3.1.** _Eigenvalues of_ \(\varepsilon_1\) _lie in_ (0,1].

**Assumption 3.2.** _Matrix_ \(\varepsilon_1\) _is strictly diagonally dominant (SDD):_ \(\varepsilon_{ii}>\sum_{j\neq i}|\varepsilon_{ij}|\)_, i_=1,2,3.

**Assumption 3.3.** _At least one off-diagonal entry of_ \(\varepsilon_1\) _is zero._

The above assumptions are reasonable in physics. The \(3\times 3\) matrix \(\varepsilon_1\) represents the inverse of the normalized permittivity tensor \(\varepsilon\) within the material domain \(\Omega_1\). For any physical material, \(\varepsilon\) must have eigenvalues no less than 1, with 1 corresponding to the vacuum. Consequently, the spectrum of \(\varepsilon_1\) must lie in (0,1], as is illustrated by Assumption 3.1. In anisotropic media, off-diagonal entries in \(\varepsilon_1\) often arise from a rotation of the material’s principal axes. A common case involves a material with anisotropy rotated only in the _xy_-plane, which leads to \(\varepsilon_{13}=\varepsilon_{23}=0\). Assumption 3.3 is thus satisfied in this case. Assumption 3.2 is also reasonable since many anisotropic materials exhibit strong diagonal dominance.

In Subsubsection 3.3.1 we prove that M<sub>Trivial</sub> is HPD under Assumption 3.1 alone; Subsubsection 3.3.2 proves that M<sub>CrossDoF</sub> is HPD if Assumption 3.1 is combined with either Assumption 3.2 or 3.3.

### 3.3.1. Positive Definiteness for Matrix M<sub>Trivial</sub>

In the proofs that follow, we adhere to the notations displayed in (3.1).

**Lemma 3.4.** _For any matrix_ \(A\in\mathbb{C}^{N\times N}\) _and permutation_ \(\sigma\) _over_ \(\{1,\cdots,N\}\)_, if matrix_ \(\hat{A}\) _satisfies_ \((\hat{A})_{ij}=(A)_{\sigma(i),\sigma(j)}\)_, then_ \(\hat{A}=PAP^\top\) _where permutation matrix P is such that_ \((P)_{ij}=\delta_{\sigma(i),j}\) (\(\delta\) _is the Kronecker delta)._

