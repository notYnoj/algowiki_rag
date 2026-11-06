<tbc>signals are reformulated as a third-order tensor, and an efficient decomposition approach leveraging the inherent Vandermonde structure is developed to decouple the high- dimensional parameters. Subsequently, we propose a symmetric decoupling and real-domain manifold optimization (SD-RDMO) algorithm to estimate the angle of arrival (AoA), which effectively circumvents the high-dimensional search complexity induced by near-field effects. Furthermore, a baseband reconstruction and analytical exact gradient (BR-AEG) algorithm is developed for continuous- domain delay-Doppler estimation, fundamentally eliminating grid-mismatch errors in high-mobility scenarios. On this basis, angle of departure (AoD) is sequentially extracted. Simulation results verify that our scheme eliminates angular error floors and achieves orders-of- magnitude higher delay-Doppler accuracy than existing baselines.

## II. System Model

This paper considers a bistatic AFDM sensing architecture for 6G intelligent transportation systems. As shown in Fig. 1, there are _Q_ scattering targets with high dynamic characteristics in the mixed-field bistatic sensing region. The transmitter is equipped with an _N<sub>t</sub>_-element uniform linear array (ULA). The receiver is an intelligent RSU deployed at a traffic hub. To achieve ultra high- resolution spatial sensing, the RSU is equipped with an extremely large-scale ULA (XL-ULA) of size _N<sub>r</sub>_. Let _M_ be the number of subcarriers contained in a single symbol block, spanning a total bandwidth of _B_, which yields a subcarrier spacing of \(\Delta f=B/M\). For the _N<sub>t</sub>_ transmit antennas, they transmit the same Zadoff-Chu pilot sequence \(\mathbf{x}\in\mathbb{C}^{M\times 1}\) in the DAFT domain. To enable the extraction of transmit spatial signatures and facilitate the subsequent tensor formulation, time-division multiplexing (TDM) is employed at the transmitter.

### A. AFDM Modulation

According to AFDM modulation, the mapping process of the time-domain transmit sequence \(\mathbf{s}\in\mathbb{C}^{M\times 1}\) is defined as

\(\mathbf{s}=\unknown_{c_2}^H\mathbf{F}_M^H\unknown_{c_1}^H\mathbf{x},\) (1)

where \(\mathbf{F}_M\in\mathbb{C}^{M\times M}\) represents the normalized discrete Fourier transform matrix, \(\unknown_{c_1}\unknown\mathrm{diag}(e^{-j2\pi c_1m^2})_{m=0}^{M-1}\) and \(\unknown_{c_2}\unknown\mathrm{diag}(e^{-j2\pi c_2m^2})_{m=0}^{M-1}\) denote chirp phase rotation matrices. _c_<sub>1</sub> and _c_<sub>2</sub> represent the AFDM chirp parameters. To ensure the circular convolution property of the channel matrix in the discrete domain and to eliminate inter- carrier interference, a chirp periodic prefix (CPP) of length _L_<sub>cpp</sub> is appended to **s**. Its _i_-th prefix sample is mapped as \(\mathbf{s}[M+i]e^{-j2\pi c_1(M^2+2Mi)}\), where \(i\in\{-L_\mathrm{cpp},\dots,-1\}\).

### B. Delay-Doppler Representation and AFDM Demodulation

Let \(\tau_q\) and \(\nu_q\) denote the echo delay and Doppler shift corresponding to target _q_. Accordingly, the normalized delay and normalized Doppler shift are defined as \(\beta_q=\tau_qM\Delta f=l_q+\iota_q\) and \(\alpha_q=\nu_q/\Delta f=k_q+\mu_q\), respectively. Here, \(l_q\in(0,l_\mathrm{max}]\) and \(k_q\in[-k_\mathrm{max},k_\mathrm{max}]\) denote the integer parts, while \(\iota_q,\mu_q\in[-0.5,0.5)\) represent the corresponding fractional delay and fractional Doppler shifts. To prevent overlapping of distinct nonzero entries occupying the same position, _c_<sub>1</sub> is deliberately configured as (2(_k_<sub>max</sub>+_k<sub>v</sub>_)+1)/2_M_, where _k<sub>v</sub>_ is the guard parameter according to the Doppler spread. _c_<sub>2</sub> is set to be an arbitrary irrational number or a rational number sufficiently small \[3\].

At the receiver, the digital baseband processing first discards the redundant CPP of length _L_<sub>cpp</sub> and subsequently maps the discrete time-domain received signal back to the DAFT domain \[3\]. By incorporating the AFDM channel matrix structure, the manifold vector \(\mathbf{v}_\mathrm{DD}(\tau_q,\nu_q)\in\mathbb{C}^{M\times 1}\) for target _q_ can be analytically formulated as

\(\mathbf{v}_\mathrm{DD}(\tau_q,\nu_q)=\unknown_{c_2}\mathbf{F}_M\unknown_{c_1}\unknown_{\mathrm{CPP},q}\unknown(\nu_q)\unknown(\tau_q)\mathbf{s},\) (2)

where we define \(\unknown(\nu_q)\unknown\mathrm{diag}(e^{-j2\pi m\alpha_q/M})_{m=0}^{M-1}\) to represent the discrete mapping matrix of the time-domain continuous Doppler rotation within the diagonal space. Similarly, \(\unknown(\tau_q)\unknown\mathbf{F}_M^H\mathrm{diag}(e^{-j2\pi m\beta_q/M})_{m=0}^{M-1}\mathbf{F}_M\) captures the linear phase shift effect induced by the signal delay. Furthermore, due to the different signal periodicity of the discrete chirp signals, \(\unknown_{\mathrm{CPP},q}\) is introduced to make the channel seemingly lie in a periodic domain for the integer delay component _l<sub>q</sub>_. It is an \(M\times M\) diagonal matrix explicitly defined as

\(\unknown_{\mathrm{CPP},q}=\mathrm{diag}\left(\left\{\begin{array}{ c c }
e^{-j2\pi c_1(M^2-2M(l_q-m))} & m<l_q \\
1 & m\ge l_q
\end{array}\right),\) (3)

where _m_=0_,...,M_-1. From (3), we can see that whenever 2_Mc_<sub>1</sub> is an integer and _M_ is even, \(\unknown_{\mathrm{CPP},q}=\mathbf{I}_M\).

### C. Manifolds Representation at Transmitter and Receiver

Given that the aperture of the transmit antenna array is much smaller than the signal propagation distance, the transmitted signal is assumed to follow the far-field planar wavefront approximation. Letting the AoD of target _q_ be \(\phi_q\), then the _n<sub>t</sub>_-th component of the spatial steering vector

- th target parameter
Target 1
Rayleigh Limit
N, antennas
N, antennas
(XL-ULA)
Target Q
Far Field
Near Field

Fig. 1. Bistatic Sensing System Model with XL-MIMO

