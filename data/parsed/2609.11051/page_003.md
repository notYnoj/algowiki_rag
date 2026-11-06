<tbc>\(\mathbf{v}_\mathrm{T}(\phi_q)\in\mathbb{C}^{N_t\times 1}\) for the transmit array is analytically expressed as

\([\mathbf{v}_\mathrm{T}(\phi_q)]_{n_t}=\mathrm{exp}\left(-j\frac{2\pi}{\lambda}n_t\Delta_ts\mathrm{sin}\phi_q\right),\) (4)

where \(\lambda\) and \(\Delta_t\) denote the wavelength and the spacing between transmit antennas.

Due to the extremely large physical aperture of the XL-ULA at the RSU, the classical Rayleigh distance is significantly extended. Consequently, the _Q_ targets may scatter across both the near-field and far-field regions. To formulate a unified representation for this mixed-field scenario, we reconstruct the physical state space using a polar algebraic mapping manifold \(\unknown_q\unknown[\vartheta_q,\rho_q]^T\), so that the element of the mixed-field array manifold \(\mathbf{v}_\mathrm{R}(\unknown_q)\in\mathbb{C}^{N_r\times 1}\) at the RSU is defined as

\([\mathbf{v}_\mathrm{R}(\unknown_q)]_{n_r}=\mathrm{exp}\left(j\frac{2\pi}{\lambda}\left(n_r\Delta_r\vartheta_q-n_r^2\Delta_r^2\rho_q\right)\right),\) (5)

where \(\Delta_r\) denotes the spacing between receiving antennas, \(n_r\in\{-\frac{N_r-1}{2},\dots,\frac{N_r-1}{2}\}\), indicating that e center antenna serves as the phase reference \[8\]. The parameters \(\vartheta_q\) and \(\rho_q\) are explicitly determined by

\(\vartheta_q\unknown\mathrm{sin}\theta_q,\rho_q\unknown\frac{1-\vartheta_q^2}{2d_q}.\) (6)

Here, \(\theta_q\) is the physical AoA of target _q_ relative to the RSU array center, _d<sub>q</sub>_ is the distance between the _q_-th target and the reference antenna. This unified expression fundamentally originates from the exact spherical wavefront topology. If target _q_ falls in the far-field region, the distance _d<sub>q</sub>_ is sufficiently large such that \(\rho_q\) approximates to zero. In this case, the manifold smoothly degenerates into the classical far-field planar wavefront steering vector just like (4).

Considering TDM framework, the _N<sub>t</sub>_ transmit antennas emit the AFDM pilot sequence sequentially rather than concurrently. Each antenna \(n_t\in\{1,2,\dots,N_t\}\) occupies a dedicated time slot of duration _T_<sub>sym</sub>. This temporal orthogonality guarantees that the echoes corresponding to different transmit antennas can be perfectly isolated at the ISAC receiver. Thus, the observation matrix \(\mathbf{Y}_{n_t}\in\mathbb{C}^{N_r\times M}\) of the _n<sub>t</sub>_ transmit antenna can be comprehensively modeled as

\(\mathbf{Y}_{n_t}=\sum_{q=1}^Q\gamma_qe^{j\Omega_{q,n_t}}[\mathbf{v}_\mathrm{T}(\phi_q)]_{n_t}\mathbf{v}_\mathrm{R}(\unknown_q)\mathbf{v}_\mathrm{DD}^T(\tau_q,\nu_q)+\mathbf{N}_{n_t},\) (7)

where \(\Omega_{q,n_t}=2\pi(n_t-1)\nu_qT_\mathrm{sym}\) denotes the phase shift caused by the _q_-th target at the _n<sub>t</sub>_-th slot. \(\mathbf{N}_{n_t}\in\mathbb{C}^{N_r\times M}\) denotes the additive white Gaussian noise (AWGN) matrix and \(\gamma_q\in\mathbb{C}\) denotes the complex scattering coefficient.

## III. Proposed Tensor-Based Parameters Estimation Algorithm

### A. Tensor Reformulation and Decomposition

To prevent the destruction of physical structural information and the coupling of multi-dimensional parameters caused by traditional matrix dimensionality reduction, we construct the observation model directly in a multi-dimensional algebraic space. By performing high- order stacking of the independent observation matrices \(\{\mathbf{Y}_{n_t}\}_{n_t=1}^{N_t}\) \[14\], the global bistatic sensing observation tensor \(\mathcal{Y}\in\mathbb{C}^{N_r\times M\times N_t}\) can be constructed as<tbc>

\(\mathcal{Y}=\sum_{q=1}^Q\gamma_q\mathbf{v}_\mathrm{R}(\unknown_q)\circ\mathbf{v}_\mathrm{DD}(\tau_q,\nu_q)\circ\tilde{\mathbf{v}}_\mathrm{T}(\phi_q,\nu_q)+\mathcal{N},\) (8)

<tbc>where \([\tilde{\mathbf{v}}_t(\phi_q,\nu_q)]_{n_t}=e^{j\Omega_{q,n_t}}[\mathbf{v}_t(\phi_q)]_{n_t}\) denotes the coupling term between Doppler and AoD induced by TDM, \(\circ\) represents the tensor outer product operator, and \(\mathcal{N}\in\mathbb{C}^{N_r\times M\times N_t}\) is the corresponding global noise tensor. To provide a more compact algebraic representation, we define the factor matrices associated with the three dimensions as

\(\mathbf{A}_\mathrm{R}\unknown[\mathbf{v}_\mathrm{R}(\unknown_1),\dots,\mathbf{v}_\mathrm{R}(\unknown_Q)]\in\mathbb{C}^{N_r\times Q}\mathbf{A}_\mathrm{DD}\unknown[\mathbf{v}_\mathrm{DD}(\tau_1,\nu_1),\dots,\mathbf{v}_\mathrm{DD}(\tau_Q,\nu_Q)]\in\mathbb{C}^{M\times Q}.\mathbf{A}_\mathrm{T}\unknown[\tilde{\mathbf{v}}_\mathrm{T}(\phi_1,\nu_1)),\dots,\tilde{\mathbf{v}}_\mathrm{T}(\phi_Q,\nu_Q)]\in\mathbb{C}^{N_t\times Q}\) (9)

By further defining the scattering coefficient vector as \(\unknown\unknown[\gamma_1,\dots,\gamma_Q]^T\), the observation tensor can be succinctly expressed using the Kruskal operator as \(\mathcal{Y}=\unknown\unknown\unknown;\mathbf{A}_\mathrm{R},\mathbf{A}_\mathrm{DD},\mathbf{A}_\mathrm{T}\unknown+\mathcal{N}\).

Define the full-dimensional physical parameter set to be estimated for the targets in the bistatic system as \(\{\theta_q,d_q,\phi_q,\tau_q,\nu_q,\gamma_q\}_{q=1}^Q\). The joint parameter estimation process is equivalent to minimize the global Frobenius norm reconstruction error, which is given by

\(\mathrm{minimize}\left\|\mathcal{Y}-\sum_{q=1}^Q\gamma_q\mathbf{v}_\mathrm{R}(\unknown_q)\circ\mathbf{v}_\mathrm{DD}(\tau_q,\nu_q)\circ\tilde{\mathbf{v}}_\mathrm{T}(\phi_q,\nu_q)\right\|_F^2.\) (10)

Thus, a potent strategy for parameter estimation involves leveraging the factor matrices, enabling the extraction of desired parameter information via canonical polyadic decomposition (CPD). A well-established method is the alternative least square (ALS) algorithm \[13\], which iteratively optimizes by updating one factor matrix at a time while keeping other parameters constant, albeit with high computational demands. Although the ALS- based approach provides an effective way to estimate the factor matrices, it fails to incorporate their structural constraints, thereby limiting the maximum number of resolvable targets. We propose to resolve the issue by fully leveraging the Vandermonde structure property of the factor matrices.

