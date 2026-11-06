<tbc>regardless of the differences in underlying physical systems. In this case, \(\mathcal{N}_{L16}^\mathrm{FNO}\) might have overfit to the global structure in configurations with _L_=8, but the seemingly strong dependency of the general mapping on global structures diminishes for larger lattice sizes. It is also possible that larger lattice sizes share similar global structures so that FNOs trained on a single size can still generalize.

_Remark._ We note that while the IChol-preconditioners still outperform the NN-preconditioners in terms of CG iterations, the NN-preconditioners offer the advantages of avoiding an additional linear solve at each step and eliminating the setup cost for linear systems with unseen operators. This is particular useful when only a few right hand sides _b_ to be solved for a given new _A_. Moreover, thanks to the volume transfer capability, the training time of the base NN (e.g., 72 minutes for \(\mathcal{N}_{L16}^\mathrm{FCN}\)) can be rapidly amortized when we apply the trained model to new _A_ generated from gauge fields with different sizes. In contrast, IChol preconditioners must incur the setup cost (decomposition) for each _A_, which can be computationally intensive for large problems. Therefore, the choice between the traditional IChol-preconditioner or the proposed framework depends on the specific characteristics of the linear systems to be solved. More concretely, using \(\mathcal{N}_{L16}^\mathrm{FCN}\) as the base model, we quantitatively compare the cost of training, NN-preconditioned CG solves, and IChol-preconditioned CG solves for _L_=8,16,32,64. Instead of wall-clock time, which depends heavily on implementation and hardware, we report FLOP counts as a reproducible baseline.<sup>3</sup> The \(\mathcal{N}_{L16}^\mathrm{FCN}\) model converges in about \(1.9\times 10^4\) gradient steps with each step costing \(2.1\times 10^7\) FLOPs, yielding a one-time training cost of \(4.1\times 10^{11}\) FLOPs. Using the per-step FLOP counts and average iteration numbers ( 8), we compute, for each _L_, the break-even number _n_ of distinct linear systems _A_ that must be solved for the NN preconditioner to amortize the training cost compared with IChol. Using the CG iteration counts from  2, we obtain \(n\approx 4.5\times 10^5,3.0\times 10^4,1.8\times 10^3,1.1\times 10^2\) for _L_=8,16,32,64, respectively (see Appendix C for calculation details). Thus, as the lattice size increases, fewer new systems are needed for the NN-preconditioner to amortize training. In practice, the number of<tbc>

<sup>3</sup>In our current implementation, the NN operations are carried out with dense kernels (e.g., dense convolutions), while the FLOP of IChol-preconditioning is estimated as sparse solves. Optimizing NN operations via quantization/pruning could potentially decrease the number of new systems needed to amortize the training cost.

(a) L = 8
(b) L = 32
101
Unprecond
102
Unprecond
N 16 - precond.
N 16 - precond.
109
N 16 - precond.
100
N 16 - precond.
10-1
From scratch
From scratch
10-2
10-2
Relative Residual
Relative Residual
10-3
10-4
10-4
10-5
10-6
10-6
10-7
0
20
40 Iterations
60
80
0
100
200
300 Iterations
400
500
600

Fig. 5. Zero-shot performance of N<sub>_L_16</sub> models on gauges configurations of (a) _L_=8 and (b) _L_=32. The figures show the CG solve residual norm vs. the number of iterations, where the neural preconditioner effective reduces the number iterations required for convergence. In particular, the \(\mathcal{N}_{L16}^\mathrm{FCN}\) model achieves the same level of reduction as the models trained from scratch using the test cases. The \(\mathcal{N}_{L16}^\mathrm{FNO}\) retains the performance for _L_=32, and, while still effective, results in an inferior iteration reduction compared with the model trained from scratch on the _L_=8 case.

