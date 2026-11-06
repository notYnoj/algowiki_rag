<tbc>already more than halved and beyond which it collapses (7 edges at _p_=1000); support is only a proxy for trainability. Since \(c_e\in[0,1]\) here, _p_ is also \(p\Delta c\); the learned costs of Sects. 4.3-4.4 are trained at \(p\Delta c\lesssim 50\) (costs in \[0,1\] at \(p\le 50\), or a learned scale of 1.85 at _p_=20), inside this window. On noisy and natural images _x<sup>p</sup>_ approaches the limit slowly (a few per cent of the free pixels still differ at _p_=500) while \(\kappa\) goes far beyond what any solver can resolve. The iteration counts grow far more slowly than \(\sqrt{\kappa}\), because the ill-conditioning sits in a few near-isolated pixels that barely affect the residual. The double-precision factorisation itself fails beyond _p_≈500; an exact elimination confirms the table and shows the gap closing slowly beyond (`camera`: 1.2% at \(p=5\cdot 10^3\)), as 8-bit squared costs differ by as little as \(1.5\cdot 10^{-5}\). The last per cent of agreement are out of practical reach of a finite-_p_ solve; they come from the combinatorial step. In the refinement regime 20 unrolled CG steps disagree with the converged solve on 0.04% of the labels (2.9% on the noisy image), independently of the image size; in the global regime (30-px erosion, scribbles) no truncation works.

## 4.2 A tunable, spatially coupled softmax

Fig. 1 shows the WS layer on simulated network outputs. With the image edge on the true boundary and \(\alpha=0.1\), the boundary score BF<sub>2</sub> of the thresholded soft prediction, initially 0.958, becomes 1.000 at _p_=200 and in the limit on the clean scene, and 0.968 at _p_=200 (0.870 in the limit) on the noisy one. The output goes from 22% soft pixels to under 1%: a softmax whose sharpness is spatially coupled through the edges. The scale \(\alpha\) does matter: at \(\alpha=1\) the unaries of confident pixels compete with the noise edges and everything merges before any label attaches, so both large _p_ and the limit collapse. And when the true boundary is 4 px from the image edge, \(p\le 10\) is harmless but a larger _p_<tbc>

\begin{tabular}{cccccc}
image & _p_ & \(\kappa(L_U)\) & CG iters & labels \(\neq x^\infty\) (%) & edges, 90% grad. \\
clean, \(\sigma\)=0.05 & 10 & \(1.8\cdot 10^2\) & 39 & 0.7 & 14276 \\
 & 100 & \(4.7\cdot 10^2\) & 53 & 0.0 & 5945 \\
 & 200 & \(5.7\cdot 10^3\) & 63 & 0.0 & 844 \\
 & 1000 & \(2.3\cdot 10^{17}\) & 173 & 0.0 & 7 \\
noisy, \(\sigma\)=0.1 & 10 & \(2.0\cdot 10^2\) & 42 & 3.1 & 14645 \\
 & 100 & \(1.5\cdot 10^{10}\) & 89 & 2.2 & 8351 \\
 & 500 & \(1.0\cdot 10^{48}\) & 240 & 1.2 & 681 \\
`camera` & 10 & \(5.5\cdot 10^2\) & 62 & 9.8 & 23602 \\
 & 100 & \(1.7\cdot 10^7\) & 104 & 5.5 & 13044 \\
 & 500 & \(4.1\cdot 10^{33}\) & 154 & 4.1 & 5503 \\
\end{tabular}

** 1.** Refinement regime (512<sup>2</sup>, seeds eroded by 5 px). Condition number of _L<sub>U</sub>_, the Laplacian restricted to the unseeded pixels (ARPACK; values above 10<sup>16</sup> exceed double precision and are indicative only), iterations of plain, unpreconditioned conjugate gradients in single precision to a relative residual of 10<sup>-3</sup>, fraction of free pixels whose label differs from the limit, and the number of edges carrying 90% of the gradient of a squared loss to the reference labels.

