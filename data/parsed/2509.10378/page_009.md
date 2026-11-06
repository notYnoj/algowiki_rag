<tbc>During training, for all listed models, we fixed the network hyperparameters and randomly sampled _K_=128 vectors from standard isotropic multivariate Gaussian distribution to compute and minimize the loss, defined in (8). A detailed description of the network architecture, the choice of hyperparameters, and model training choices can be found in Appendix A.

### 4.1 Action-specific neural preconditioners

We train the proposed model using lattice gauge fields associated with various lattice sizes (_L_=8,16,32,64) and investigate the impact of applying the resulting preconditioners to solve the Wilson-Dirac normal equations. An overview of the models for the four lattice sizes can be found in  1.

#### Impact on condition number.

We apply the preconditioning operator \(\Gamma\) obtained from the two types of trained learners (FNO and FCN) to precondition the linear systems arising from the listed gauge field configurations. We then compute the condition number of the unpreconditioned and preconditioned linear operators (_A_ and \(\Gamma A\), where \(A=D^\dagger D[U_\mu(x)]\)) to evaluate the impact of the resulting preconditioners. The condition number of a matrix _A_ is defined as \(\kappa(A)=|\sigma_\mathrm{max}|/|\sigma_\mathrm{min}|\) where \(\sigma_\mathrm{max}\) and \(\sigma_\mathrm{min}\) are the maximum and minimum singular values. To compute the singular values of the unpreconditioned and preconditioned systems reliably, we explicitly construct the associated matrices and compute the condition numbers. Figure 3 compares the condition numbers of the linear systems in the testing set before and after applying the FNO- and FCN-based, as well as IChol preconditioners. The \(\Gamma\) generated from the neural network outputs \(\tilde{U}_\mu(x)\) considerably and consistently reduces the condition numbers across all lattice sizes. Although the IChol preconditioners achieve lower condition numbers, the construction of neural network-based preconditioners does not require explicit matrices or their decomposition for new linear systems in the testing set. Furthermore, the results indicate that the FNO- and FCN-based neural preconditioners exhibit comparable performance, suggesting they have likely learned similar mappings.

#### Accelerating CG solve.

With the proposed framework, the trained neural network-based preconditioners can be directly integrated into preconditioned CG solvers as linear operators. We set up the linear systems with random right-hand sides (sampled from an isotropic Gaussian distribution for both real and imaginary parts and fixed across models) and solve them using unpreconditioned CG, as well as CG with IChol, FNO-, and FCN-based preconditioners. With the relative tolerance set to 10<sup>-8</sup>, we compare the average number of iterations and the time required to reach convergence. Since the FNO- and FCN-based preconditioners exhibit comparable performance, we report only the results for the FNO-based preconditioners. Figure 4a shows the solver convergence to the specified tolerance for different lattice sizes. The proposed preconditioning method effectively reduces the number of iterations required for convergence, approximately halving the total steps. Moreover, unlike IChol (or even-odd) preconditioners, the trained FNO-based preconditioners require neither a setup step (e.g., IChol decomposition) nor an additional triangular solve per CG iteration; instead, they involve only a forward matrix-vector product, thereby reducing computational complexity<tbc>

\begin{tabular}{cccccc}
Models & \(\kappa\) & \(\beta\) & #train & #val & #test \\
N<sub>_L_8</sub>,N<sub>_L_16</sub>,N<sub>_L_32</sub>,N<sub>_L_64</sub> & 0.276 & 2.0 & 1280 & 320 & 200 \\
\end{tabular}

1. Overview of ensembles of the two-flavor lattice Schwinger model with Wilson fermions used for the numerical study. _L_ is the lattice sizes for both space and time dimensions. \(\kappa\) and \(\beta\) are the hopping parameter and gauge coupling used during generation of the gauge field configurations. The number of configurations used for training, validation and testing is also listed for each model.

