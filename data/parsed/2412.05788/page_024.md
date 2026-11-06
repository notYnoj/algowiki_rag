## C.2 Diffusion Posterior Samplers

By defining the likelihoods appropriately, we can use the guidance potentials together with the SMC samplers. For FPS-SMC and MCGDiff, which operate on linear inverse problems only, they are confined to using the masking potential, and thereby the likelihood<tbc>

\(g_t(\mathbf{y}_t|\mathbf{x}_t)\propto exp\left(-\frac{1}{\eta_t}L_\text{mask}\left(\mathbf{x}_t;\mathbf{y}_t,\mathcal{M}\right)\right),\)

<tbc>with \(\eta_t=1/2\sigma_v^2\bar{\alpha}_t\) for FPS-SMC and, for MCGDiff, \(\eta_t=1/(1-\bar{\alpha}_t)\) when **x**_<sub>t</sub>_ is known and \(\eta_t=1/(\beta_{t+1}^2+1-\bar{\alpha}_t)\) when using \(\hat{\mathbf{x}}_t=\mathbb{E}[\mathbf{x}_t|\mathbf{x}_{t+1}]\) in the numerator of eq. (14). On the other hand, TDS uses the DPS likelihood approximation and adopts a general likelihood

\(g_t(\mathbf{y}_0|\mathbf{x}_t)\propto exp\left(-\frac{1}{\eta_t}L\left(\hat{\mathbf{x}}_0(\mathbf{x}_t,t);\mathbf{y}_t,\mathcal{M}\right)\right),\)

where \(\eta_t=1/\tilde{\sigma}_t^2\). Wu et al. (2023) recommend setting \(\tilde{\sigma}_t^2:=\text{Var}[\mathbf{x}_t|\mathbf{x}_0]\), leniently filtering early in the reverse process, when the reconstructed sample \(\hat{\mathbf{x}}_0\) is still unreliable, and gradually tightening the filter towards the end. To keep it non-zero we set \(\tilde{\sigma}_t^2=(1-\bar{\alpha}_t)+\sigma_v^2\) to match our inverse problem formulation at _t_=0.

In our implementation of the samplers, we make several optimisations. By partitioning particles into groups, we can run multiple trials simultaneously, making the most of throughput gains with increased model batch sizes. This is achieved by computing weights and resampling on a per-group basis. We further perform multiprocessing across several GPUs. Beyond parallelism, we minimise the number of calls made to the diffusion model--the main bottleneck. We cache the predicted noise (or score) between computing weights and sampling from the proposal. Moreover, we only compute the predicted noise of unique particles for BPF and FPS-SMC, where duplicate particles may be fed to the proposal. Different batches of Gaussian noise are added afterwards to differentiate the duplicate particles. Computationally, it is as if we set the number of particles equal to the mean of the ESS (estimator).

\begin{tabular}{cccc}
**Name** & **Description** & **Configuration** & **Length** \\
4JHW+5WN9 & Two epitopes & 10-40, **4JHW/F254-278{1}**, 20-50, **5WN9/A170-189{2}**, 10-40 & 85-175 \\
1PRW\_two & Two 4-helix bundles & 5-20, **1PRW/A16-35{1}**, 10-25, **1PRW/A52- 71{1}**, 10-30, **1PRW/A89-108{2}**, 10-25, **1PRW/A125-144{2}**, 5-20 & 120-200 \\
1PRW\_four & Four EF-hands & 5-20, **1PRW/A21-32{1}**, 10-25, **1PRW/A57- 68{2}**, 10-25, **1PRW/A94-105{3}**, 10-25, **1PRW/A125-144{4}**, 5-20 & 88-163 \\
3BIK+3BP5 & Two PD-1 binding motifs & 5-15, **3BIK/A121-125{1}**, 10-20, **3BP5/B110- 114{2}**, 5-15 & 30-60 \\
3NTN & Two 3-helix bundles & **3NTN/A342-348{1}**, 10, **3NTN/A367- 372{2}**, 10-20, **3NTN/B342-348{2}**, 10, **3NTN/B367-372{1}**, 10-20, **3NTN/C367- 372{1}**, 10, **3NTN/C342-348{2}** & 89-109 \\
2B5I & Two binding sites & 5-15, **2B5I/A11-23{2}**, 10-20, **2B5I/A35- 45{1}**, 10-20, **2B5I/A61-72{1}**, 5-15, **2B5I/A81-95{2}**, 20-30, **2B5I/A119-133{2}** & 116-166 \\
\end{tabular}

5: **Genie2 multi-motif scaffolding benchmark details.** The specification for each scaffolding problem is under "Configuration", with the motif structures in bold. Here, the motif structures are formatted as \<MOTIF\_NAME\>/\<CHAIN\_SEGMENT\>{\<MOTIF\_GROUP\>}, where structures belonging to the same motif group are fixed in their orientations relative to each other. Furthermore, the total length of the generated protein must fall in the range specified in the "Length" column.

