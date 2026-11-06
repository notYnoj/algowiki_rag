<tbc>new systems to be solved exceeds these reported numbers, and it could become infeasible to form matrices to use IChol preconditioners for larger lattice sizes. This is precisely where our proposed matrix-free framework holds significant advantages.

#### Higher powers of \(\Gamma\).

Constructing a linear operator by repeatedly applying \(\Gamma\) produces a less sparse matrix and provides more degrees of freedom in approximating the inverse. In the _L_=16_,d_=2 case, at _p_=4, the corresponding matrix of the linear operator becomes fully dense. We investigate the effect of using \((\Gamma)^p\), where _p_=1,2,3,4, as the preconditioning operators to train N<sub>_L_16</sub> and report their impact on the preconditioned CG solver. s 4 show the number of iterations required for the CG solver to reach convergence on various systems where the trained N<sub>_L_16</sub> is applied as the preconditioner. The results show a further reduction in the number of iterations as _p_ increases in all cases with FCN-based neural preconditioners and in most cases with FNO-based ones. In particular, the FNO-based models at _p_=2 achieve fewer iterations than at _p_=3 and _p_=4. Meanwhile, the FCN-based models consistently show that higher powers lead to fewer iterations. This validates our assumption that a denser matrix, even with repeating entries, is able to better approximate the inverse of \((D^\dagger D)[U_\mu(x)]\). Nevertheless, the gain in reducing the number of iterations can be offset by increased computational complexity per step, as higher powers of \(\Gamma\) require additional matrix-vector products. This trade-off might be more pronounced when solving larger systems, which we are interested in quantifying in future investigations. Given this trade-off, the choice of the power _p_ should depend on specific needs and the computational resources available.

### 4.3 The learned mappings

The results of the numerical experiments support our conjecture that the mapping between the input gauge configurations and preconditioner-generating configurations is general and does not dependent on the specific action parameters or lattice geometries. Moreover, given the performance discrepancy between the \(\mathcal{N}_{L16}^\mathrm{FNO}\) and \(\mathcal{N}_{L16}^\mathrm{FCN}\) models for _L_=8 cases, such mapping might depend only on the local structures of the gauge fields. To this end, we further examine the trained models in  1 by comparing model weights to obtain a proxy of distances among learned mappings. We compare the element-wise weights of models trained with specific action parameters, as listed in  1, where models with similar parameters are expected to approximate similar mappings.<tbc>

\begin{tabular}{ccccc}
**Lattice Sizes** & **Unprecond CG** & **NN-precond CG** & **IChol-precond CG** & **IChol Setup** \\
_L_=8 & \(1.1\times 10^4\) & \(2.0\times 10^4\) & \(2.9\times 10^4\) & \(1.1\times 10^6\) \\
_L_=16 & \(4.4\times 10^4\) & \(7.9\times 10^4\) & \(1.2\times 10^5\) & \(1.6\times 10^7\) \\
_L_=32 & \(1.8\times 10^5\) & \(3.2\times 10^5\) & \(4.7\times 10^5\) & \(2.6\times 10^8\) \\
_L_=64 & \(7.1\times 10^5\) & \(1.3\times 10^6\) & \(1.9\times 10^6\) & \(4.2\times 10^9\) \\
\end{tabular}

\begin{tabular}{cccccccccc}
 & **Unprecond.** & \multicolumn{2}{c}{_p_=1} & \multicolumn{2}{c}{_p_=2} & \multicolumn{2}{c}{_p_=3} & \multicolumn{2}{c}{_p_=4} \\
**Model** & iters & FNO & FCN & FNO & FCN & FNO & FCN & FNO & FCN \\
_L_=8 & \(78\pm 4\) & \(60\pm 3\) & \(40\pm 2\) & \(56\pm 3\) & \(35\pm 2\) & \(62\pm 4\) & \(33\pm 2\) & \(73\pm 5\) & \(32\pm 2\) \\
_L_=16 & \(201\pm 14\) & \(99\pm 7\) & \(99\pm 7\) & \(80\pm 7\) & \(86\pm 7\) & \(109\pm 9\) & \(81\pm 6\) & \(79\pm 6\) & \(79\pm 6\) \\
_L_=32 & \(548\pm 41\) & \(267\pm 21\) & \(267\pm 21\) & \(212\pm 17\) & \(232\pm 18\) & \(221\pm 18\) & \(219\pm 17\) & \(221\pm 16\) & \(212\pm 16\) \\
\end{tabular}

3. Operation FLOP count comparison (per step)

4. Iteration counts (mean \(\pm\) one standard deviation rounded to integers) for the preconditioned CG solver on various lattice sizes using N<sub>_L_16</sub> trained with \((\Gamma)^p\) for _p_=1,2,3,4 as the preconditioning operators.

