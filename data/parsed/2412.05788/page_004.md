<tbc>First, _twisting_ (Pitt and Shephard, 1999; Johansen and Doucet, 2008) is an SMC technique that improves sampler efficiency by accounting for measurements in future iterations. It involves tilting the intermediate targets by some twist function \(\psi_t\), with \(\psi_0=\psi_T=1\), maintaining the initial and final targets. Twisting allows the terminal measurement to be accounted for earlier in the process and for smoother transitions between sequential measurements. Second, the reverse diffusion kernel proposal can be further tilted by the likelihood to obtain the (locally) optimal proposal _q<sub>t</sub>_(**x**_<sub>t</sub>_|**x**<sub>_t_+1</sub>,**y**_<sub>t</sub>_), a choice that minimises the variance of importance weights. This permits the conditional signal to be present beyond just the resampling steps. These building blocks are especially important when working in high dimensions, where a correct but inefficient sampler may face frequent weight degeneracies. Alg. 1 provides a general recipe for SMC diffusion posterior samplers.

The replacement method precisely creates the sequence of measurements that can be used together with SMC. Trippe et al. (2022) apply filtering with the replacement method as part of their SMCDiff algorithm to solve in-painting problems. They maintain the original reverse kernel as their proposal, but replace the masked segment with a noisy version of the measurement. For linear inverse problems in general, Dou and Song (2023) employ the optimal proposal and a noise-sharing technique in their method, FPS-SMC. In the in-painting case, their proposal smoothly interpolates the masked segments with the noisy measurements, which share the same noise applied to their latent counterparts. The consistency of both methods, however, relies on the forward and reverse processes having the same joint distribution, which is often untrue in practice (see (Trippe et al., 2022, App. D.2) and (Dou and Song, 2023, Prop. 4.1)). Maintaining consistency without this assumption, Cardoso et al. (2023) use the same optimal proposal but adopt a terminal measurement model with targets tilted by the likelihood of sequential measurements. Their MCGDiff algorithm solves general linear inverse problems. While they do not explicitly noise the measurements, they use the mean of the measurement distribution as a single sample approximation in eq. (3). In parallel, Wu et al. (2023) use reconstruction guidance together with filtering for solving general inverse problems. They similarly adopt a terminal measurement model but have twist functions and an optimal proposal approximation based on eq. (4). Their method, TDS, provides state-of-the-art performance in motif scaffolding among training-free methods. Specific choices in proposals and twist functions of each sampler, together with their weight updates, are laid out in App. A.2.

Other works that fit within this framework include SVDD (Li et al., 2024), an instance of the bootstrap particle filter (BPF) equipped with the likelihood in eq. (4) which avoids backpropagating through the score model, and PDDS (Phillips et al., 2024), a sampler that reframes the sampling problem as diffusion posterior sampling, leveraging well-behaved diffusion paths, and uses SMC with twisting to correct for errors. A unique feature of these SMC methods is their increasingly accurate posterior sampling at the controlled expense of a larger number of particles.

input : measurement y<sub>0</sub>, proposal q<sub>t</sub>, likelihood g<sub>t</sub>,<br>
reverse diffusion transition kernel p<sub>\theta</sub>,<br>
no. of particles K, no. of time steps T,<br>
(if replacement method) noisy measurement dist. \(\nu\),<br>
(if twisting) twist functions \(\psi_t\) (otherwise set \(\psi_t=1\))<br>
output: approximate posterior samples \(\mathbf{x}_0^{1:K}\)<br>
# Create a sequence of measurements<br>
Sample y<sub>t</sub>∼\(\left\{\begin{array}{ c c }
\delta_{\mathbf{y}_0} & \text{for reconstruction guidance} \\
\nu(\cdot|\mathbf{y}_0) & \text{for replacement method}
\end{array}\right.\),<br>
for t=1,...,T<br>
# Define transition between targets<br>
Set \(\tilde{f}_{t-1}(\mathbf{z}_{t-1}|\mathbf{z}_t)\)<br>
:= \(\left\{\begin{array}{ c c }
p_\theta(\mathbf{z}_{t-1}|\mathbf{z}_t) & \text{if}t>1 \\
p_\theta(\mathbf{z}_{t-1}|\mathbf{z}_t)g_0(\mathbf{y}_0|\mathbf{z}_{t-1}) & \text{if}t=1
\end{array}\right.\) for a terminal measurement \\
p_\theta(\mathbf{z}_{t-1}|\mathbf{z}_t)g_{t-1}(\mathbf{y}_{t-1}|\mathbf{z}_{t-1}) & \text{for sequential measurements}
\end{array}\right.\)<br>
# Generate samples guided by measurements<br>
Sample \(\tilde{\mathbf{x}}_T^{1:K}\sim\mathcal{N}(\mathbf{0},\mathbf{I})\)<br>
Set \(\tilde{w}_T^i\leftarrow g_T(\mathbf{y}_T|\tilde{\mathbf{x}}_T^i)\), for i=1,...,K<br>
for t=T,...,1 do<br>
   Set \(w_t^i\leftarrow\tilde{w}_t^i/\sum_{j=1}^K\tilde{w}_t^j\), for i=1,...,K<br>
   Resample \(\mathbf{x}_t^{1:K}\sim\text{Multinomial}(w_t^{1:K},\tilde{\mathbf{x}}_t^{1:K})\)<br>
   for i=1,...,K do<br>
   Sample \(\tilde{\mathbf{x}}_{t-1}^i\sim q_{t-1}(\cdot|\mathbf{x}_t^i)\)<br>
   Set \(\tilde{w}_{t-1}^i\leftarrow\frac{\tilde{f}_{t-1}(\tilde{\mathbf{x}}_{t-1}^i|\mathbf{x}_t^i)}{q_{t-1}(\tilde{\mathbf{x}}_{t-1}^i|\mathbf{x}_t^i)}\frac{\psi_{t-1}(\tilde{\mathbf{x}}_{t-1}^i)}{\psi_t(\mathbf{x}_t^i)}\)<br>
   end<br>
end

**Algorithm 1:** Recipe for an SMC Diffusion Posterior Sampler

