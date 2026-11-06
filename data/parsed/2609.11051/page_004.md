To begin with, we obtain the mode-2 unfolding matrix of **Y**, which can be written as

\(\mathbf{Y}_{(2)}=\mathbf{A}_\text{DD}(\mathbf{A}_\text{T}\text{diag}(\unknown)\odot\mathbf{A}_\text{R})^T+\mathbf{N}_{(2)},\) (11)

and \(\mathbf{N}_{(2)}\in\mathbb{C}^{M\times N_tN_r}\) is the unfolding matrix of N along its second dimension. In (9), we observe that \(\tilde{\mathbf{v}}_\text{T}(\phi_q,\nu_q)\) constitutes a component of a steering vector, preserving the power series configuration. Consequently, the factor matrix **A**<sub>T</sub> demonstrates a Vandermonde structure with generators \(\{e^{j(2\pi\nu_qT_\text{sym}-\frac{2\pi}{\lambda}\Delta_tsin\phi_q)}\}_{q=1}^Q\). Building upon this insight, we incorporate the structural constraints inherent in factor matrices and introduce an algebraic-based estimation approach for these matrices. This method potentially circumvents the need for iterative processes and may even improve resolution when dealing with a larger number of targets \[13\]. Specifically, we construct a cyclic selection matrix \(\mathbf{J}_{l_3}=\left[\mathbf{0}_{K_3\times(l_3-1)}\mathbf{I}_{K_3}\mathbf{0}_{K_3\times(L_3-l_3)}\right]\otimes\mathbf{I}_{N_r}\in\mathbb{C}^{K_3N_r\times MN_r}\) and vary _l_<sub>3</sub> from 1 to _L_<sub>3</sub>, yielding

\(\mathbf{Y}_S=\left[\mathbf{J}_1\mathbf{Y}_{(2)}^T\mathbf{J}_2\mathbf{Y}_{(2)}^T,\dots,\mathbf{J}_{L_3}\mathbf{Y}_{(2)}^T\right]\)<br>
\(=\left(\mathbf{A}_\text{T}^{(K_3)}\odot\mathbf{A}_\text{R}\right)\text{diag}(\unknown)\left(\mathbf{A}_\text{T}^{(L_3)}\odot\mathbf{A}_\text{DD}\right)^T+\mathbf{N}_S,\) (12)

where _K_<sub>3</sub>+_L_<sub>3</sub>=_N<sub>t</sub>_+1, and \(\mathbf{A}_\text{T}^{(K)}\) denote the first _K_ rows of **A**<sub>T</sub>, and \(\mathbf{N}_S\in\mathbb{C}^{K_3N_r\times L_3M}\) is the corresponding noise term.

To estimate the factor matrices, we initiate the process with the computation of singular value decomposition (SVD). Specifically, we decompose **Y**_<sub>S</sub>_ as \(\mathbf{Y}_S=\mathbf{U}\unknown\mathbf{V}^H=\mathbf{U}_s\unknown_s\mathbf{V}_s^H+\mathbf{U}_n\unknown_n\mathbf{V}_n^H\), where the _K_ principal singular vectors in **U** and **V** respectively span the signal subspaces **U**_<sub>s</sub>_ and **V**_<sub>s</sub>_, and \(\unknown_s\) is a diagonal matrix composed of the _Q_ largest singular values. Define \(\mathbf{U}_1=[\mathbf{U}_s]_{1:(K_3-1)N_r::}\) and \(\mathbf{U}_2=[\mathbf{U}_s]_{N_r+1:K_3N_r::}\). We then compute the eigenvalue decomposition as \(\mathbf{U}_1^\dagger\mathbf{U}_2=\mathbf{MZM}^{-1}\). Consequently, the _q_- th column of the factor matrix **A**<sub>T</sub> can be reconstructed as<tbc>

\(\hat{\mathbf{v}}_{\text{T},q}=\left[1,\hat{z}_q,\dots,\hat{z}_q^{N_t-1}\right]^T,\) (13)

<tbc>where \(\hat{z}_q=[\mathbf{Z}]_{q,q}/\left|\left[\mathbf{Z}\right]_{q,q}\right|\) is the estimated generator. The other two factor matrices can be estimated, whose _q_-th columns can be obtained via<tbc>

\(\hat{\mathbf{v}}_{\text{R},q}=\left(\hat{\mathbf{v}}_{\text{T},q}^{(K_3)H}\otimes\mathbf{I}_{N_r}\right)\mathbf{U}_s\mathbf{m}_q,\) (14)

\(\hat{\mathbf{v}}_{\text{DD},q}=\big(\frac{\hat{\mathbf{v}}_{\text{T},q}^{(L_3)H}}{\hat{\mathbf{v}}_{\text{T},q}^{(L_3)H}\hat{\mathbf{v}}_{\text{T},q}^{(L_3)}}\otimes\mathbf{I}_M\big)\mathbf{V}_s^*\unknown_s\mathbf{t}_q,\) (15)

<tbc>respectively, where **m**_<sub>q</sub>_ is the _q_-th column of **M** and **t**_<sub>q</sub>_ is the _q_-th column of (**M**<sup>-1</sup>)<sup>∗</sup>.

## B. Sensing Parameters Extraction

Up to now, our task has been transformed to extract the sensing parameters from aforementioned factor matrices, which necessitates addressing the three factor matrices.

1) Mixed Field Parameters at the Receiver: After obtaining the receive spatial manifold estimation vector \(\hat{\mathbf{v}}_{\text{R},q}\in\mathbb{C}^{N_r\times 1}\) for the _q_-th target via tensor decomposition, the nonlinear coupling between the AoA and distance in the near-field spherical wavefront model incurs prohibitive computational complexity for direct two- dimensional spectral peak searching. To address this, we propose an estimation algorithm named symmetric decoupling and real-domain manifold optimization (SD-RDMO) to achieve high-precision parameter extraction through algebraic dimensionality reduction and continuous-domain optimization.

Exploiting the physical symmetry of the XL-ULA at the RSU, a spatial difference observation sequence is constructed. By extracting and conjugately multiplying the corresponding elements from the positive semi-axis \(n_r\in\{1,\dots,\frac{N_r-1}{2}\}\) and the negative semi-axis -_n<sub>r</sub>_ of the array, the decoupled observation value _h<sub>n<sub>r</sub></sub>_ is obtained via<tbc>

\(h_{n_r}=[\hat{\mathbf{v}}_{\text{R},q}]_{n_r}([\hat{\mathbf{v}}_{\text{R},q}]_{-n_r})^*=exp\left(j\frac{4\pi}{\lambda}n_r\Delta_r\vartheta_q\right).\) (16)

<tbc>This operation eliminates the quadratic term \(\rho_q\) containing the distance information. It is worth noting that \(\Delta_r\) should be set to \(\lambda/4\) to avoid phase ambiguities. To suppress the impact of additive noise, a phase smoothing method is adopted to acquire the initial estimation of the angle mapping parameter \(\vartheta_q^{(0)}\), which is expressed as<tbc>

\(\vartheta_q^{(0)}=\frac{\lambda}{4\pi\Delta_r}\angle\left(\sum_{n_r=2}^{(N_r-1)/2}h_{n_r}h_{n_r}^*-1\right).\) (17)

<tbc>Subsequently, by performing quadratic phase compensation on the positive semi-axis signal, the phase observation value _w<sub>n<sub>r</sub></sub>_ modulated solely by distance is extracted by<tbc>

\(w_{n_r}=\frac{[\hat{\mathbf{v}}_{\text{R},q}]_{n_r}}{[\hat{\mathbf{v}}_{\text{R},q}]_0}\cdot exp\left(-j\frac{2\pi}{\lambda}n_r\Delta_q^{(0)}\right)\) (18)

<tbc>After extracting the continuous unwrapped phase of _w<sub>n<sub>r</sub></sub>_, a weighted least squares fitting model is established to calculate the initial distance mapping parameter \(\rho_q^{(0)}\):

\(\rho_q^{(0)}=argmin_{\rho_q}\sum_{n_r=1}^{(N_r-1)/2}\left(\angle w_{n_r}+\frac{2\pi}{\lambda}n_r^2\Delta_r^2\rho_q\right)^2.\) (19)

To further improve parameter estimation accuracy and eliminate the cumulative error of phase unwrapping, a nonlinear optimization model is constructed with the state variable \(\unknown_q=[\vartheta_q,\rho_q]^T\). We define the predicted signal at the _k_-th iteration as \(\mathbf{m}_\text{R}^{(k)}=\delta_{1q}^{(k)}\mathbf{v}_\text{R}(\unknown_q^{(k)})\) and the complex residual vector as \(\mathbf{e}^{(k)}=\hat{\mathbf{v}}_{\text{R},q}-\mathbf{m}_\text{R}^{(k)}\cdot\delta_{1q}^{(k)}\) is the scale ambiguity factor caused by tensor decomposition, and is updated by \(\delta_{1q}^{(k)}=\frac{(\mathbf{v}_\text{R}(\unknown_q^{(k)}))^H\hat{\mathbf{v}}_{\text{R},q}}{\|\mathbf{v}_\text{R}(\unknown_q^{(k)})\|_2^2}\) . By deriving the partial derivatives of the predicted signal with respect to the physical parameters, the complex Jacobian matrix \(\mathbf{J}_c^{(k)}\in\mathbb{C}^{N_r\times 4}\) is formulated as

\(\mathbf{J}_c^{(k)}=\left[\delta_{1q}^{(k)}\frac{\partial\mathbf{v}_\text{R}}{\partial\vartheta_q},\delta_{1q}^{(k)}\frac{\partial\mathbf{v}_\text{R}}{\partial\rho_q},\mathbf{v}_\text{R},j\mathbf{v}_\text{R}\right].\) (20)

