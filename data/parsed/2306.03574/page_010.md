**Proof:** By Lemma 1, \(\mathcal{C}_\alpha\in\mathcal{Q}(mn)\). It is well-known that the image \(s(\mathbb{C}\backslash(-\infty,0])\) is a subset of C<sub>+</sub>. Then, by definition of \(\mathcal{C}_\alpha^{1/2}\) and by the fact that \(\sigma(\mathcal{C}_\alpha)\subset\mathbb{C}\backslash(-\infty,0]\), we have \(\sigma(\mathcal{C}_\alpha^{1/2})\subset\mathbb{C}_+\). Then, Lemma 2 implies that \(s(\mathcal{C}_\alpha)=\mathcal{C}_\alpha^{1/2}\). Moreover, \(\mathcal{C}_\alpha\) is clearly real-valued. Hence, \(\mathcal{C}_\alpha^{1/2}\) is real-valued by part (c) of Lemma 2. Part (a) is shown.

The proof of part (b) of Lemma 4 is similar to the proof of part (c) of Lemma 3. We skip it here.

## 2.2. Convergence analysis of the proposed PMINRES method

In this subsection, we show that the MINRES solver for the preconditioned system (1.10) has a linear convergence rate independent of both \(\tau\) and _h_.

We first provide the following lemma, which will be used to investigate the convergence rate.

For a square matrix **C**, denote by \(\sigma(\mathbf{C})\) the spectrum of **C**. For a real symmetric matrix **H**, denote by \(\lambda_\mathrm{min}(\mathbf{H})\) and \(\lambda_\mathrm{max}(\mathbf{H})\) the minimal and the maximal eigenvalue of **H**, respectively.

**Lemma 5.** _\[8, Theorem 6.13\] Let_ \(\mathbf{P}\in\mathbb{R}^{N\times N}\) _and_ \(\mathbf{A}\in\mathbb{R}^{N\times N}\) _be a symmetric positive definite matrix and a symmetric nonsingular matrix, respectively. Suppose_ \(\sigma(\mathbf{P}^{-1}\mathbf{A})\in[-a_1,-a_2]\cup[a_3,a_4]\) _with_ \(a_4\ge a_3>0\), \(a_1\ge a_2>0\) _and a_<sub>1</sub>-_a_<sub>2</sub>=_a_<sub>4</sub>-_a_<sub>3</sub>_. Then, the MINRES solver with_ **P** _as a preconditioner for the linear system_ \(\mathbf{Ax}=\mathbf{y}\in\mathbb{R}^{N\times 1}\) _has a linear convergence as follows_

\(||\mathbf{r}_k||_2\le 2\left(\frac{\sqrt{a_1a_4}-\sqrt{a_2a_3}}{\sqrt{a_1a_4}+\sqrt{a_2a_3}}\right)^{[k/2]}||\mathbf{r}_0||_2,\)

_where_ **r**_<sub>k</sub>_=**P**<sup>-1</sup>**y**-**P**<sup>-1</sup>**Ax**_<sub>k</sub> denotes the residual vector at the kth iteration with_ **x**_<sub>k</sub> (_\(k\ge 1\)_) being the kth iterative solution by MINRES;_ **x**<sub>0</sub> _denotes an arbitrary real-valued initial guess;_ \(\lfloor k/2\rfloor\) _denotes the integer part of k/_2.

To apply Lemma 5 to (1.10), we will first need to investigate the spectrum of the preconditioned matrix \(\mathcal{P}_\alpha^{-1}\mathcal{YT}\) . By matrix similarity, we know that<tbc>

\(\sigma(\mathcal{P}_\alpha^{-1}\mathcal{YT})=\sigma(\mathcal{P}_\alpha^{-\frac{1}{2}}\mathcal{YT}\mathcal{P}_\alpha^{-\frac{1}{2}}).\)

<tbc>Hence, it suffices to study the spectral distribution of \(\mathcal{P}_\alpha^{-\frac{1}{2}}\mathcal{YT}\mathcal{P}_\alpha^{-\frac{1}{2}}\). To this end, we decompose the preconditioned matrix \(\mathcal{P}_\alpha^{-\frac{1}{2}}\mathcal{YT}\mathcal{P}_\alpha^{-\frac{1}{2}}\) as<tbc>

\(\mathcal{P}_\alpha^{-1/2}\mathcal{YT}\mathcal{P}_\alpha^{-1/2}=\mathcal{Q}_\alpha-\mathcal{E}_\alpha,\) (2.1)

<tbc>where

\(\mathcal{Q}_\alpha=\mathcal{P}_\alpha^{-1/2}\mathcal{YC}_\alpha\mathcal{P}_\alpha^{-1/2},\mathcal{E}_\alpha=\mathcal{P}_\alpha^{-1/2}\mathcal{Y}\mathcal{R}_\alpha\mathcal{P}_\alpha^{-1/2},\mathcal{R}_\alpha:=\mathcal{C}_\alpha-\mathcal{T}.\)

In the lemma below, we will show that \(\mathcal{Q}_\alpha\) is a real symmetric orthogonal matrix (i.e., \(\sigma(\mathcal{Q}_\alpha)\subset\{-1,1\}\)) and that \(\mathcal{E}_\alpha\) is a small-norm matrix for a properly chosen small \(\alpha\).

