where **v**<sub>R</sub> is an abbreviation for \(\mathbf{v}_\mathrm{R}(\unknown_q^{(k)})\).

Due to the limitations of complex-domain differentiation, the complex observation space is equivalently projected into the real domain to construct the real- domain residual and Jacobian matrices as<tbc>

\(\tilde{\mathbf{e}}^{(k)}=\left[\begin{array}{ c }
\Re(\mathbf{e}^{(k)}) \\
\unknown(\mathbf{e}^{(k)})
\end{array}\right],\tilde{\mathbf{J}}^{(k)}=\left[\begin{array}{ c }
\Re(\mathbf{J}_c^{(k)}) \\
\unknown(\mathbf{J}_c^{(k)})
\end{array}\right],\) (21)

<tbc>where \(\Re(\cdot)\) and \(\unknown(\cdot)\) denote the operations of taking the real and imaginary parts, respectively. Based on this real- domain model, an adaptive damping term is introduced to solve for the iteration update step \(\Delta\unknown\in\mathbb{R}^{4\times 1}\), given by

\(\Delta\unknown=\left((\tilde{\mathbf{J}}^{(k)})^T\tilde{\mathbf{J}}^{(k)}+\mu\mathbf{I}_4\right)^{-1}(\tilde{\mathbf{J}}^{(k)})^T\tilde{\mathbf{e}}^{(k)}.\) (22)

The state update \(\unknown_q^{(k+1)}=\unknown_q^{(k)}+[\Delta\unknown[1],\Delta\unknown[2]]^T\) is executed until convergence. The high-precision physical parameters \(\theta_q\) and _d<sub>q</sub>_ are recovered through the inverse mapping (6).

2) Delay-Doppler Estimation: For the DAFT domain effective time-frequency manifold estimation vector \(\hat{\mathbf{v}}_{\mathrm{DD},q}\in\mathbb{C}^{M\times 1}\), traditional grid-search-based algorithms are prone to severe grid-mismatch errors in high- mobility scenarios. Therefore, we propose the baseband reconstruction and analytical exact gradient (BR-AEG) algorithm to achieve joint estimation in the continuous parameter domain. To eliminate the discrete chirp phase coupling specific to the AFDM scheme, the observation vector \(\hat{\mathbf{v}}_{\mathrm{DD},q}\) is sequentially subjected to multiplication operations. This process equivalently restores the signal into the baseband time-domain observation sequence **y**_<sub>q</sub>_ as \(\mathbf{y}_q=\unknown_{c_1}^H\mathbf{F}_M^H\unknown_{c_2}^H\hat{\mathbf{v}}_{\mathrm{DD},q}\) This operation avoids the boundary energy leakage caused by fractional delay and Doppler jumps. Defining the baseband prediction model as \(\mathbf{v}(\beta,\alpha)=\unknown(\alpha)\unknown(\beta)\mathbf{s}\), a two-dimensional correlation search is performed over a low-resolution parameter grid set (B<sub>grid</sub>,A<sub>grid</sub>) to acquire the initial coordinates \([\beta_q^{(0)},\alpha_q^{(0)}]^T\) according to

\([\beta_q^{(0)},\alpha_q^{(0)}]^T=\mathrm{arg}\mathrm{max}_{\beta\in\mathcal{B}_\mathrm{grid},\alpha\in\mathcal{A}_\mathrm{grid}}\frac{\left|\mathbf{v}^H(\beta,\alpha)\mathbf{y}_q\right|^2}{|\mathbf{v}(\beta,\alpha)|^2}.\) (23)

To overcome the accuracy limitations of discrete grids, we then update the values of delay an Doppler through the procedures summarized in Algorithm 1.

3) AoD: The AoD information can be extracted from \(\hat{z}_q\) after the Doppler is estimated. Leveraging the bijective correspondence between variables \(\hat{z}_q\) and \(\hat{\phi}_q\), the param eter \(\hat{\phi}_q\) can be accurately estimated by extracting the phase component from the complex variable \(\hat{z}_q\), which is explicitly represented as<tbc>

\(\hat{\phi}_q=\mathrm{arcsin}(-\frac{\lambda}{2\pi\Delta_t}\angle\hat{z}_q+2\pi\hat{\alpha}_q\Delta f).\) (24)

<tbc>Algorithm 1 Delay and Doppler Updating in BR-AEG

Require: **y**_<sub>q</sub>_, **s**, \(\beta_q^{(0)},\alpha_q^{(0)}\), regularization parameter \(\mu\), tolerance threshold \(\epsilon\)<br>
Ensure: Estimated parameters \(\hat{\beta}_q\) and \(\hat{\alpha}_q\)<br>
Initialize iteration index k=0<br>
Initialize scale ambiguity factor<br>
\(\delta_{2q}^{(0)}=\frac{(\mathbf{v}(\alpha_q^{(0)},\beta_q^{(0)}))^H\hat{\mathbf{v}}_{\mathrm{DD},q}}{\|(\mathbf{v}(\alpha_q^{(0)},\beta_q^{(0)}))\|_2^2}\)<br>
Construct initial joint state vector<br>
\(\unknown_q^{(0)}=[\beta_q^{(0)},\alpha_q^{(0)},\Re(\delta_{2q}^{(0)}),\unknown(\delta_{2q}^{(0)})]^T\)<br>
repeat<br>
Compute the predicted signal<br>
\(\mathbf{m}_\mathrm{DD}^{(k)}=\delta_{2q}^{(k)}\mathbf{v}(\beta_q^{(k)},\alpha_q^{(k)})\)<br>
Construct the complex Jacobian matrix<br>
\(\mathbf{J}_\mathrm{DD}^{(k)}=[\frac{\partial\mathbf{m}_\mathrm{DD}^{(k)}}{\partial\beta_q},\frac{\partial\mathbf{m}_\mathrm{DD}^{(k)}}{\partial\alpha_q},\mathbf{v},j\mathbf{v}]\)<br>
and residual vector \(\mathbf{e}_\mathrm{DD}^{(k)}=\mathbf{y}_q-\mathbf{m}_\mathrm{DD}^{(k)}\)<br>
Compute \(\tilde{\mathbf{J}}_\mathrm{DD}^{(k)}\) and \(\tilde{\mathbf{e}}_\mathrm{DD}^{(k)}\) similar to (21)<br>
Calculate the update step:<br>
\(\Delta\unknown=\left((\tilde{\mathbf{J}}_\mathrm{DD}^{(k)})^T\tilde{\mathbf{J}}_\mathrm{DD}^{(k)}+\mu\mathbf{I}_4\right)^{-1}(\tilde{\mathbf{J}}_\mathrm{DD}^{(k)})^T\tilde{\mathbf{e}}_\mathrm{DD}^{(k)}\)<br>
Update the state variables \(\unknown_q^{(k+1)}=\unknown_q^{(k)}+\Delta\unknown\)<br>
k=k+1<br>
until \(\|\Delta\unknown\|_2<\epsilon\)<br>
return \(\hat{\beta}_q=\unknown_q^{(k)}[1]\) and \(\hat{\alpha}_q=\unknown_q^{(k)}[2]\)

### C. Complexity Analysis

In this subsection, the computational burden of the proposed tensor-based sensing scheme is provided. The calculation of the truncated SVD for **Y**_<sub>S</sub>_ requires O(_QK_<sub>3</sub>_L_<sub>3</sub>_N<sub>r</sub>M_) operations. Indeed, O(_K_<sub>3</sub>_N<sub>r</sub>Q_<sup>2</sup>) operations are needed to compute the pseudo-inverse of the signal subspace **U**<sub>1</sub>, while the eigenvalue decomposition procedure takes O(_Q_<sup>3</sup>) operations. Furthermore, the SD- RMO algorithm for AoA estimation takes O(_QN<sub>r</sub>+QI_<sub>AoA</sub>_N<sub>r</sub>_) operations, with _I_<sub>AoA</sub> being the total number of iterations. Additionally, in the process of BR- AEG, the computational complexity connected with the baseband reconstruction and initial correlation search is O(_QM_log<sub>2</sub>_M+QGM_), where _G_ denotes the total number of low-resolution grid points. Similarly, the computational complexity of the refinement in Algorithm 1 is O(_QI_<sub>DD</sub>_M_), with _I_<sub>DD</sub> denoting the associated number of iterations required for convergence.

## IV. Simulation Results

In this section, simulation results are presented to evaluate the performance of the proposed tensor-based sensing scheme. The carrier frequency of our V2I system is set to 60 GHz, with a bandwidth of _B_=10.24 MHz, and _M_=256. For the transmitter, there are _N<sub>t</sub>_=8 antennas, while there are 200 antennas on each side of the reference antenna at the receiver, making the Rayleigh distance for the XL-ULA approximately 100 meters. To strictly prevent spatial-Doppler ambiguity, the<tbc>

