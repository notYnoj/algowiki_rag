We have shown that these existing works are merely differentiated by their design choices.  3 gives an overview. While they all target the same distribution under the right assumptions, their efficiencies, or lack thereof, are more prominent in the finite particle setting. Even more, the high cost of the score model can impose significantly smaller particle counts. The high-dimensional nature of inverse problems, such as motif scaffolding, compounds the effect so that the weights become almost always degenerate. As a consequence, virtually all samplers will return multiple copies of the same sample. This is because particles have less room to diversify towards the end of the reverse process, and resampling in the later stages becomes detrimental to diversity. Some workarounds include resampling only until a certain point and running parallel instances of samplers. In any case, utilising the optimal proposal and twisted targets has become commonplace in the most performant samplers.

\begin{tabular}{cccc}
**Sampler** & **Proposal (**_q<sub>t</sub>_**)** & **Twist Function (**\(\psi_t\)**)** & **Measurement Model** \\
BPF & \(p_\theta(\mathbf{x}_t|\mathbf{x}_{t+1})\) & 1 & Any \\
FPS-SMC & \(q_t^*(\mathbf{x}_t|\mathbf{x}_{t+1},\mathbf{y}_t)\) (eq. (13)) & 1 & Sequential \\
MCGDiff & \(q_t^*(\mathbf{x}_t|\mathbf{x}_{t+1},\mathbf{y}_t)\) (eq. (13)) & _g<sub>t</sub>_(**y**_<sub>t</sub>_|**x**_<sub>t</sub>_) & Terminal \\
TDS & \(q_t^{TDS}(\mathbf{x}_t|\mathbf{x}_{t+1},\mathbf{y}_0)\) (eq. (15)) & \(g_t(\mathbf{y}_0|\hat{\mathbf{x}}_0(\mathbf{x}_t,t))\) & Terminal \\
\end{tabular}

3: **The design choices of each SMC sampler for diffusion posterior sampling.** To define their intermediate measurements, FPS-SMC samples from the measurement noising process (11), and MCGDiff takes the expectation of the same process conditioned on the terminal measurement.

