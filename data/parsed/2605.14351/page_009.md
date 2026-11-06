<tbc>poles and logarithmically spaced time constants may be more appropriate. For systems with known bandwidth, the angular support can be restricted before optimization, reducing both computation and false discoveries.

The number of atoms _M_ controls a bias-variance- conditioning trade-off. Small _M_ gives fast, well- conditioned regressions but may miss relevant poles. Large _M_ improves coverage but creates coherent columns, especially when poles are close in pseudo- hyperbolic distance or when the input signal does not sufficiently distinguish their responses. In practice, column normalization, group penalties, and iterative resampling are important. One can start with a moderate global dictionary, solve the convex problem, retain active or nearly active regions, and resample locally. This produces a multiresolution search over the disk without ever solving a large nonconvex pole-placement problem.

### 8.2 Complexity

For SISO data with _N_ samples and _M_ atoms, forming the convolved design matrix costs _O(NM_) using direct recursions

\(x_m(t+1)=p_mx_m(t)+u(t+1),X_{t,m}=x_m(t),\) (70)

up to conventions on initial conditions and delays. The basic ridge or Lasso problem then scales like a standard dense regression in _M_ variables. Additional SOCP constraints for epigraph variables, impulse settling, BIBO budgets, time-domain windows, and directional frequency bounds scale linearly with the number of atoms and grid points. Exact MIMO frequency-gain constraints introduce LMIs whose size is determined by input/output dimension; directional SOCP relaxations are often preferable when the number of grid points is large. Passivity constraints introduce a storage matrix whose dimension equals the number of active states in the parallel realization, so it may be advantageous to impose passivity after an initial sparsifying solve or on a pruned dictionary.

### 8.3 Comparison with related methods

RAFs should not be viewed as replacing kernel regularization or atomic norm methods; rather, they occupy a useful middle ground. Compared with kernel regularization, RAFs make the features explicit and allow direct coefficient constraints, but they require a sampled dictionary and can be sensitive to dictionary coherence. Compared with gridless atomic norm formulations, RAFs trade exact continuous convex geometry for a scalable finite problem that can incorporate many engineering constraints. Compared with classical PEM, RAFs are less tied to a fixed parametric order and can exploit convex priors before nonlinear refinement.  1 summarizes this positioning.

### 8.4 MIMO and structured extensions

For MIMO systems, the sampled pole set can be shared across channels while residues become matrices. A common-pole model has

\(G(z)=D+\sum_{m=1}^M\frac{C_m}{1-p_mz^{-1}},\) (71)

where _C<sub>m</sub>_ is an output-by-input residue matrix. Group penalties on \(\|C_m\|_F\) promote a small number of shared modes, while channel-specific penalties allow different sparsity patterns across inputs and outputs. Frequency- domain gain constraints and passivity constraints are naturally matrix-valued in this setting. The same disk-kernel viewpoint applies, but the scalar measure is replaced by an operator-valued or matrix-valued measure when one interprets the full MIMO covariance structure. In the finite RAF implementation, however, the optimization remains a structured regression over residue matrices.

### 8.5 Limitations

The framework has several limitations. First, the quality of the finite dictionary matters: no sparse regularizer can identify modes outside the sampled region, and local refinement can only help when the active support provides a meaningful warm start. Second, highly coherent disk-Vandermonde or input-filtered columns can lead to unstable support estimates even when prediction error is small. Third, active atoms are not certified pole estimates; pole localization requires additional separation, excitation, signal-strength, and noise assumptions. Fourth, the current theory is clearest for linear time-invariant impulse responses; nonlinear, LPV, and closed-loop extensions require additional assumptions on scheduling variables, excitation, and noise. Fifth, hard priors can introduce bias. The appropriate interpretation is therefore set- membership or physics-guided identification rather than purely data-driven model discovery. These limitations are also opportunities: adaptive sampling, posterior pole distributions, robust conic formulations, and closed-loop instrumental-variable versions are natural extensions.

## 9. NUMERICAL EXAMPLE

We illustrate the method on a SISO system composed of two underdamped modes. The system is excited by a low-bandwidth input, and 100 samples are collected. The output is corrupted by additive white Gaussian noise with SNR approximately 30 dB. Preliminary prediction-error fits reveal that the data are not sufficiently informative to identify the true impulse response uniquely: many stable models fit the measured output but extrapolate differently and recover different pole locations.

This is the intended use case for physics-informed RAF identification. We impose pole-sector priors with radii in [0.85,0.95] and angles in [0.3,1], a BIBO budget _h_<sub>max</sub>=55, a DC-gain bound _G_<sub>max</sub>=4, and the frequency- response gain mask shown in Fig. 2. These priors need not all be used simultaneously; rather, they demonstrate

\begin{tabular}{ccccc}
Property & PEM & KRM & ANM & RAF \\ Explicit modes & yes & no & yes & yes \\ Convex main fit & local & yes & yes & yes \\ Kernel/RKHS view & no & yes & partial & yes \\ Continuous pole search & yes & implicit & yes & refinement \\ Hard side constraints & limited & moderate & moderate & broad \\ Random-feature scalability & no & no & partial & yes \\ \end{tabular}

1. Qualitative comparison of identification approaches.

