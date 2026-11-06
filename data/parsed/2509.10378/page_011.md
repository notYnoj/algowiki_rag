<tbc>sets. In addition, we investigate the effect of using models trained with higher powers of \(\Gamma\), as described in Section 3.

### Zero-shot performance.

We expect that the trained networks have learned the general mapping discussed in Section 3 where they are applicable for unseen gauge configurations. We directly use the trained N<sub>_L_16</sub> model in the previous section and obtain preconditioning operators for new \(U_\mu(1)\) configurations with varying lattice sizes, hopping parameters \(\kappa\), and gauge coupling \(\beta\). Figures 5a and 5b show the zero-shot performance of N<sub>_L_16</sub> (both FNO- and FCN-based) on data with _L_=8, or _L_=32 in terms of the convergence in the CG solve. Without any training on the new data with different lattice size, the model still reduces the number of iteration required compared to the unpreconditioned case, making it immediately applicable and effective. In particular, the zero-shot application of the FCN-based model on gauge configurations with _L_=8 and _L_=32, as well as the FNO-based model applied to _L_=32, achieves the same level of acceleration as models trained specifically on the respective configurations. This demonstrates the volume transfer capability of the trained model, potentially eliminating the need of retraining or finetuning. This transferability also allows the training costs of the NN-preconditioners to be amortized over solutions for many geometries and parameter sets.  2 presents the zero-shot performance of the N<sub>_L_16</sub> model on different sets of testing configurations where \(\kappa\) and \(\beta\) are also changed. Both FNO- and FCN-based N<sub>_L_16</sub> lead to significant reduction in the number of iterations required for convergence of the CG solver. Meanwhile, with larger systems (\(L\ge 32\)), the FNO- and FCN-based N<sub>_L_16</sub> models have almost identical performance regarding the number of iterations.

Interestingly, although still managing to decrease the number of iterations, the \(\mathcal{N}_{L16}^\mathrm{FNO}\) model under-performs on _L_=8 cases compared to the \(\mathcal{N}_{L16}^\mathrm{FCN}\) model and models specifically trained for these systems. Such performance gap disappears for larger systems. As described in Section 3, both FNO and FCN are considered operator learners but with different kernels for conduct kernel integration. While FNO performs convolution operations in the frequency domain, essentially having global convolutional kernels, FCN only utilizes spatially localized convolutional kernels. This mechanism difference forces FCN to rely on local features of the input function whereas FNO learns from both global and local features. Therefore, it is likely that the learned general mapping \(\mathcal{G}_\theta\) in (7) for these systems depends mostly on local structures of the gauge configurations,<tbc>

\begin{tabular}{ccccc}
\multicolumn{2}{c}{**Configuration**} & **Unprecond.** & **IChol Precond.** & **FNO**<sub>16</sub> & **FCN**<sub>16</sub> \\
_L_=8, \(\kappa=0.276\), \(\beta=2.0\) & 78 \(\pm\) 4 & 22 \(\pm\) 1 & 60 \(\pm\) 3 & 40 \(\pm\) 2 \\
_L_=8, \(\kappa=0.276\), \(\beta=1.843\) & 80 \(\pm\) 4 & 23 \(\pm\) 2 & 62 \(\pm\) 3 & 42 \(\pm\) 3 \\
_L_=8, \(\kappa=0.260\), \(\beta=2.0\) & 76 \(\pm\) 2 & 21 \(\pm\) 1 & 59 \(\pm\) 2 & 40 \(\pm\) 1 \\
_L_=16, \(\kappa=0.276\), \(\beta=2.0\) & 201 \(\pm\) 14 & 44 \(\pm\) 4 & 99 \(\pm\) 7 & 99 \(\pm\) 7 \\
_L_=16, \(\kappa=0.276\), \(\beta=3.124\) & 166 \(\pm\) 10 & 33 \(\pm\) 2 & 78 \(\pm\) 5 & 78 \(\pm\) 5 \\
_L_=32, \(\kappa=0.276\), \(\beta=2.0\) & 548 \(\pm\) 41 & 111 \(\pm\) 9 & 267 \(\pm\) 21 & 267 \(\pm\) 21 \\
_L_=32, \(\kappa=0.276\), \(\beta=5.555\) & 260 \(\pm\) 19 & 44 \(\pm\) 3 & 117 \(\pm\) 9 & 117 \(\pm\) 9 \\
_L_=64, \(\kappa=0.276\), \(\beta=2.0\) & 1540 \(\pm\) 91 & 300 \(\pm\) 17 & 719 \(\pm\) 47 & 719 \(\pm\) 47 \\
\end{tabular}

2. Number of iteration in CG solve over the test sets (mean \(\pm\) one standard deviation rounded to integers) for different lattice sizes (_L_), hopping \(\kappa\), and coupling \(\beta\), comparing **(a)** unpreconditioned CG, **(b)** incomplete-Cholesky preconditioner (IChol), **(c)** neural network-based preconditioner using a pretrained \(\mathcal{N}_{L=16}^\mathrm{FNO}\), and **(d)** neural network-based preconditioner using a pretrained \(\mathcal{N}_{L=16}^\mathrm{FCN}\).

