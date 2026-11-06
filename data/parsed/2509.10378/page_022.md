<tbc>equivalently _A_<sup>†</sup>_Ay=A_<sup>†</sup>_c_) where _y=Lx_ and _c=U_<sup>-1</sup>_b_ and then plug in _y_ to obtain the original solution _x=L_<sup>-1</sup>_y_. We treat _A_<sup>†</sup>_Ay=A_<sup>†</sup>_c_ as the preconditioned _D_<sup>†</sup>_Dx=b_. Since we are only interested in the condition number and CG convergence rate, instead of solving the exact systems, we use the random right hand side for both cases. That is, we are using CG solver to solve _D_<sup>†</sup>_Dx=b_ and _A_<sup>†</sup>_Ax=b_ and compare the number of iterations required for convergence.

9 reports the condition numbers and CG iteration counts for even-odd preconditioning on the same example problems shown in  1. Even-odd preconditioning yields lower condition numbers than the trained NN-based preconditioner, and thus requires fewer CG iterations. However, compared to the NN-preconditioning approach, the reduction in both the condition number and CG iterations is only _marginally_ improved. Moreover, like IChol, constructing the even-odd decomposed form and forming _UAL_ (and computing _U_<sup>-1</sup> and _L_<sup>-1</sup>) requires extra work, namely permutation and inverting _D<sub>oo</sub>_, which becomes costly for large systems. Moreover, the CG solve with even-odd preconditioning does not directly produce the full solution; it still demands a back-substitution step, adding further overhead. By contrast, our NN-preconditioning framework avoids all of these additional decompositions and solves, and it generalizes across system sizes without retraining.

\begin{tabular}{ccccccc}
 & \multicolumn{3}{c}{**Condition number (median)**} & \multicolumn{3}{c}{**CG iterations (max)**} \\
 & Unprecond. & FNO-precond. & Even-odd precond. & Unprecond. & FNO-precond. & Even-odd precond \\
_L_=8 & 340.38 & 86.09 & 56.51 & 86 & 46 & 40 \\
_L_=16 & 3708.84 & 901.44 & 607.98 & 241 & 121 & 103 \\
_L_=32 & 30640.93 & 7714.55 & 5093.46 & 662 & 329 & 277 \\
\end{tabular}

9. Comparison between the unpreconditioned, neural network-preconditioned, and even-odd preconditioned systems in the condition number and CG solver iterations.

