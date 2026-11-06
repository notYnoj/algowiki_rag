that satisfy recurrence (6) only with some \((1\pm 1/O(logn))\)-approximation. Then, the movements are given by

\(\mathbf{H}^t\approx_{1/O(logm)}(\mathbf{A}^\top(\overline{\mathbf{T}^t})^{-1}\Phi''(x^{t-1})^{-1}\mathbf{A})\) (9)

\(\delta_x^t=\Phi''(x^{t-1})^{-1/2}g^t-(\overline{\mathbf{T}^t})^{-1}\Phi''(x^{t-1})^{-1}\mathbf{A}(\delta_y^t+\delta_c^t)\)<br>
\(\delta_y^t=(\mathbf{H}^t)^{-1}\mathbf{A}^\top\Phi''(x^{t-1})^{-1/2}g^t\)<br>
\(\delta_s^t=\mu^t\mathbf{A}\delta_y^t\)<br>
\(\delta_c^t=(\mathbf{H}^t)^{-1}(\mathbf{A}^\top x^{t-1}-b)\)<br>
\(g^t=argmax_{w:\|w\|_{\overline{\tau}+\infty}}\langle w,-\nabla\Psi\left(\frac{s+\mu\overline{\tau}(x)\phi'(x)}{\mu\overline{\tau}(x)\sqrt{\phi''(x)}}\right)\rangle\)

where **H**_<sup>t</sup>_ is a spectral approximation, allowing us to solve the linear system approximately (i.e., we can use fast Laplacian system solvers). Because of this approximation, we can no longer guarantee \(\mathbf{A}^\top x=b\), but inclusion of vector \(\delta_c^t\) guarantees \(\mathbf{A}^\top x\) stays close to _b_. Here _g<sup>t</sup>_ is essentially the gradient of our potential function \(\Psi\) (since we want to reduce that potential in each iteration), but we are taking a step that is bounded in a certain \((\tau+\infty)\)-norm<sup>5</sup> (Definition 4.6). Calculation of this _g<sup>t</sup>_ in low space will later be one of the main issues discussed in Section 3.3.

In \[LS14\] it was shown that \(\widetilde{O}(\sqrt{n})\) iterations of the central path method (9) suffice, i.e. one must compute (9) for \(t=1,2,\dots,\widetilde{O}(\sqrt{n})\). The naive implementation of (9) takes \(\Omega(m)\) space which is \(\Omega(n^2)\) in worst-case, since the vectors \(x^t,s^t,g^t\in\mathbb{R}^m\) are _m_-dimensional. However, _O(n_<sup>2</sup>) space for min-cost flow is trivial, because then we could solve the problem in a single pass by storing the entire input graph. Therefore, our goal is to implement (9) using less than _O(n_<sup>2</sup>) space.

In the following, we outline how we can implement all calculations in (9) in the semi-streaming model. In particular, we show that for any one _t_, (9) can be calculated in just \(\widetilde{O}(1)\) passes over the input. Since we have \(t=1,2,\dots,\widetilde{O}(\sqrt{n})\), our algorithm takes \(\widetilde{O}(\sqrt{n})\) passes in total.

## 3.3 Streaming Implementation

Our goal is to calculate (9) a total of \(\widetilde{O}(\sqrt{n})\) times in a semi-streaming setting with \(\widetilde{O}(1)\) passes over the input per iteration, and using only \(\widetilde{O}(n^{1.5})\) total space.

We already outlined in Section 3.1 that we can store the values of the _t_-th iteration in total space \(\widetilde{O}(nt)\) by storing each iteration in \(\widetilde{O}(n)\) space. The precise values being stored are:

• \(y^\ell,\delta_y^\ell,\delta_c^\ell\in\mathbb{R}^n\) for \(\ell=1,\dots,t\). This uses _O(nt_) space.<br>
This implicitly represents \(s^\ell\in\mathbb{R}^m\) because for any edge _e_=(_w,z_) and its cost _c<sub>e</sub>_, we can compute \(s_e^\ell=c_e-(\mathbf{A}y^\ell)_e=c_e-(y_z^\ell-y_w^\ell)\).<tbc>

• We store \(\tau^\ell\) for \(\ell=1,\dots,t\) implicitly in \(\widetilde{O}(nt)\) space via a certain recursive JL-sketch.<tbc>

• We store _g<sup>t</sup>_ for \(\ell=1,\dots,t\) implicitly in \(\widetilde{O}(t)\) space. (Details to be discussed further below).<br>
This implicitly represents \(x^\ell\in\mathbb{R}^m\) because for any edge _e_=(_w,z_) and its cost/capacity _c<sub>e</sub>,u<sub>e</sub>_, we can recursively compute

\(x_e^\ell=x_e^{\ell-1}+\phi''_e(x_e^{\ell-1})^{-1/2}g_e^\ell-(\overline{\tau_e^\ell})^{-1}\phi''_e(x_e^{\ell-1})(\mathbf{A}(\delta_y^\ell+\delta_c^\ell))_e.\)

The main remaining question is how to compute the above \(\widetilde{O}(n)\) representation for the next iteration _t_+1 in the streaming model with only \(\widetilde{O}(1)\) passes over the input.

<sup>5</sup>\(\|v\|_{\tau+\infty}:=\|v\|_\infty+Clog(4m/n)\cdot\|v\|_\tau\) where \(\|v\|_\tau=(\sum_i\tau_i\cdot v_i^2)^{1/2}\) and _C_ is some large constant.

