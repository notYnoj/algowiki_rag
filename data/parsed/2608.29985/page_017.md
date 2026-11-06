<tbc>_From the spectral analysis presented in \[21\], the eigenvalues of W and T are known to lie within the following intervals_

\(\lambda(W)\in\left[-\frac{(3-\sqrt{3})\omega^2}{(m+1)^2}+4\left(1-\mathrm{cos}\frac{\pi}{m+1}\right),-\frac{(3-\sqrt{3})\omega^2}{(m+1)^2}+4\left(1-\mathrm{cos}\frac{m\pi}{m+1}\right)\right],\) (58)

_and_

\(\lambda(T)\in\left[\frac{(3+\sqrt{3})\tau^2}{(m+1)^2}+4\left(1-\mathrm{cos}\frac{\pi}{m+1}\right),\frac{(3+\sqrt{3})\tau^2}{(m+1)^2}+4\left(1-\mathrm{cos}\frac{m\pi}{m+1}\right)\right].\) (59)

_From these eigenvalue bounds, it can be readily verified that the matrix T is symmetric positive definite. Moreover, the matrix W is symmetric indefinite provided that the parameter_ \(\omega\) _satisfies the following condition_

\(2(m+1)\sqrt{\frac{1-\mathrm{cos}\frac{\pi}{m+1}}{3-\sqrt{3}}}<\omega<2(m+1)\sqrt{\frac{1-\mathrm{cos}\frac{m\pi}{m+1}}{3-\sqrt{3}}}.\) (60)

In our numerical experiments, the parameters are set to \(\omega=10,20\) and \(\tau=1\), which result in a symmetric indefinite matrix _W_. To evaluate the performance across different problem sizes, three grid levels with _m_=32, 64, and 128 are considered. The quasi-optimal parameters for the preconditioners P<sub>BS</sub>, P<sub>VHSS</sub>, P<sub>MBP</sub>, and P<sub>VBP</sub> are computed using the formulas given in (53), (52), (54), and (51), respectively. The corresponding parameter values are summarized in s 1 and 2.

Figure 1 illustrates the eigenvalue distribution of the preconditioned matrices corresponding to the four preconditioners under investigation--namely P<sub>BS</sub>, P<sub>VHSS</sub>, P<sub>MBP</sub>, and the proposed preconditioner P<sub>VBP</sub>. This figure is generated for a grid of size \(16\times 16\) using the quasi-optimal parameters for each preconditioner. For the proposed P<sub>VBP</sub> preconditioner, the parameter \(\gamma\) is set to 0.282. As can be observed, all four preconditioners yield a relatively favorable spectral distribution, indicating that each method effectively improves the conditioning of the original coefficient matrix. However, it is evident that the eigenvalues for the proposed preconditioner P<sub>VBP</sub> are significantly more tightly clustered around the point (1,0) in the complex plane compared to the other methods.

Furthermore, the eigenvalues associated with P<sub>VBP</sub> lie entirely within the positive real interval \[1,1.19\], which is fully consistent with the theoretical result established in Theorem 2.

The numerical results presented in s 3 and 4 demonstrate the performance of FGMRES with four different preconditioners (P<sub>BS</sub>, P<sub>VHSS</sub>, P<sub>MBP</sub>, and P<sub>VBP</sub>) in terms of iteration counts, CPU times, and optimal parameter \(\alpha\) for three grid sizes. These tables correspond to the parameter settings \((\tau=1,\omega=10)\) and \((\tau=1,\omega=20)\), respectively.

The results clearly indicate that the proposed preconditioner P<sub>VBP</sub> achieves the fastest convergence, requiring the fewest iterations and the shortest CPU time across all grid levels.<tbc>

