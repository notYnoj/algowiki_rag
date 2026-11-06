<tbc>_Definition 2:_ (Def. II.2 \[5\]) Let a linear dynamical system be of class A(_d_) and let \(\mathbf{x}_0=\mathbf{V}\alpha_0\in\mathbb{R}^n\) for some \(\alpha_0\in\mathbb{C}^{2d}\) be an arbitrary initial state of the system. We define the **attractor** of this linear dynamical system to be \(\mathcal{M}=\{\mathbf{x}\in\mathbb{R}^n|\mathbf{x}=\mathbf{V}e^{\unknown t}\alpha_0,t\in\mathbb{R}\}\).

### C. Time-Delay Embedding of Linear Systems

Suppose the dynamical system (2) is sampled using a linear observation function, represented by the vector \(\mathbf{h}\in\mathbb{R}^n\), at regular intervals of length \(\tau>0\), generating measurements \(\mathbf{y}(t)=\mathbf{h}^T\mathbf{x}(t)\in\mathbb{C}\) that form a collection \(\{\mathbf{y}(t-k\tau)\}_{k=0}^{\ell-1}\). The delay-coordinate map \(\Psi_{\{\mathbf{h},\Phi,\tau\}}:\mathbb{R}^n\rightarrow\mathbb{R}^\ell\) is defined as:

\(\Psi(\mathbf{x}(t))=\left[\begin{array}{ c }
\mathbf{y}(t) \\
\mathbf{y}(t-\tau) \\
\vdots \\
\mathbf{y}(t-(\ell-1)\tau)
\end{array}\right]=\left[\begin{array}{ c }
\mathbf{h}^T\mathbf{x}(t) \\
\mathbf{h}^T\Phi^{-\tau}\mathbf{x}(t) \\
\vdots \\
\mathbf{h}^T\Phi^{-(\ell-1)\tau}\mathbf{x}(t)
\end{array}\right]\) (3)

For a delay-coordinate map to faithfully represent the original dynamics of the system, the observation function **h** and the lag \(\tau\) must be chosen to avoid aliasing and ensure the uniqueness of each state is preserved. Ideally, we would like to have a way to quantify how accurately a particular delay-coordinate map represents the original dynamics, and the notion of stability becomes particularly important. The following definition provides a notion of a stable embedding and a way to quantify whether nearby points in the original state space remain close to each other under the delay-coordinate map and vice versa.

_Definition 3:_ (Def. II.3 \[6\]) Suppose we have a dynamical system in R_<sup>n</sup>_ that converges to an attractor M and a linear map \(\Psi:\mathbb{R}^n\rightarrow\mathbb{R}^\ell\). We say that \(\Psi\) is a stable embedding of M with conditioning \(\delta\) if for all \(\mathbf{x}_1,\mathbf{x}_2\in\mathcal{M}\) and for some scaling constant _C_, we have

\(C(1-\delta)\le\frac{\|\Psi(\mathbf{x}_1)-\Psi(\mathbf{x}_2)\|_2^2}{\|\mathbf{x}_1-\mathbf{x}_2\|_2^2}\le C(1+\delta).\) (4)

Yap and Rozell proved that delay-coordinate maps as in (3) using linear observation functions for solutions of linear systems evolving on their attractors form stable embeddings \[5\], \[6\]. The first theorem \[6\] proved establishes the existence of stable Takens’ embeddings for linear systems.

_Theorem 2:_ (Linear Takens’ Embedding; Theorem III.1 \[5\], \[6\]) Consider a class-A(_d_) linear dynamical system in R_<sup>n</sup>_ in steady-state. Let \(\tau>0\) be the sampling rate, \(\mathbf{h}\in\mathbb{R}^n\) be the observation function, and \(\Psi\) be the delay-coordinate map with \(\ell\) delays as in (3). Suppose that \(\ell\ge 2d\), the \(\mathcal{A}_\Phi\)-eigenvalues \(\{e^{\pm i\theta_j\tau}\}\) are distinct and purely imaginary, and \(\mathbf{v}_j^H\mathbf{h}\neq 0\) for all \(j\in\{1,\dots,d\}\). Then, for all distinct pairs of points \(\mathbf{x}_1,\mathbf{x}_2\in\mathcal{M}\), \(\Psi\) satisfies (4) for constants \(C:=d\left(\frac{\kappa_1^2}{A_2}+\frac{\kappa_2^2}{A_1}\right)\) and \(\delta:=\delta_0+\delta_1(\ell)\), where

In order to ensure the system frequencies are distinct, a sufficient, although not necessary, condition is \(\tau<\frac{\pi}{\theta_\mathrm{max}}\) where \(\theta_\mathrm{max}=\mathrm{max}_{j\in\{1,\dots,d\}}\{\theta_j\}\) \[6\]. The next theorem provides explicit conditions under which a time-delay embedding is stable and establishes explicit bounds on the quality of the<tbc>

<tbc>embedding. First, define \(A_1=\sigma_\mathrm{min}(\mathbf{V})\) and \(A_2=\sigma_\mathrm{max}(\mathbf{V})\), where \(\sigma(\cdot)\) denotes the singular value of a matrix. Let

\(\kappa_1=\mathrm{min}_{j\in\{1,\dots,d\}}\frac{\|\mathbf{v}_j^H\mathbf{h}\|}{\|\mathbf{h}\|_2}\kappa_2=\mathrm{max}_{j\in\{1,\dots,d\}}\frac{\|\mathbf{v}_j^H\mathbf{h}\|}{\|\mathbf{h}\|_2}\) (5)

which identify the attractor dimensions that are "least" and "most" observable by the particular observable **h**. Finally, let

\(\nu:=\mathrm{max}_{p\neq q}\left\{\frac{1}{|\mathrm{sin}(\theta_p\tau)|},\frac{1}{\mathrm{sin}\left(\frac{(\theta_p+\theta_q)\tau}{2}\right)},\frac{1}{\mathrm{sin}\left(\frac{(\theta_p-\theta_q)\tau}{2}\right)}\right\},\) (6)

a measure which quantifies the tendency of the embedding to introduce aliasing, a property that depends on the choice of delay \(\tau\) and the system frequencies \(\{\pm\theta_j\}_{j=1}^d\). With the above terms, the second theorem proved by \[6\] is as follows.

_Theorem 3:_ (Stable Linear Takens’ Embedding; Theorem III.2 \[6\]) Consider a class-A(_d_) linear system in R_<sup>n</sup>_ in steady- state. Let \(\tau>0\) be the sampling rate, \(\mathbf{h}\in\mathbb{R}^n\) be the observation function with \(\|\mathbf{h}\|_2^2=\frac{2d}{\ell}\) , and \(\Psi\) be the delay-coordinate map (3) with \(\ell\) delays. Suppose that \(\ell>\left(\left(2d-1\right)\frac{A_2\kappa_2^2}{A_1\kappa_1^2}\nu\right)\), the \(\mathcal{A}_\Phi\)-eigenvalues \(\{e^{\pm i\theta_j\tau}\}\) are distinct and imaginary, and \(\mathbf{v}_j^H\mathbf{h}\neq 0\) for all \(j\in\{1,\dots,d\}\). Then, for all distinct pairs of points \(\mathbf{x}_1,\mathbf{x}_2\in\mathcal{M}\), \(\Psi\) satisfies (4) for constants \(C:=d\left(\frac{\kappa_1^2}{A_2}+\frac{\kappa_2^2}{A_1}\right)\) and \(\delta:=\delta_0+\delta_1(\ell)\), where

\(\delta_0:=\frac{A_2\kappa_2^2-A_1\kappa_1^2}{A_2\kappa_2^2+A_1\kappa_1^2},\delta_1(\ell)=\frac{(2d-1)\nu}{\ell}\frac{2A_2\kappa_2^2}{A_2\kappa_2^2+A_1\kappa_1^2}\) (7)

Theorem 3 implies that the observation vector **h** must be able to observe each of the 2_d_ dimensions of the attractor on which solutions evolve, and that the system and sampling frequencies must be distinct to avoid aliasing. The embedding approaches isometry--a distance-preserving mapping- when \(\delta\rightarrow 0\). As \(\ell\rightarrow\infty\), \(\delta=\delta_0+\delta(\ell)\rightarrow\delta_0\), and for perfect isometry to occur, we must have \(\delta\rightarrow 0\), and thus \(\delta_0\rightarrow 0\). This occurs provided the dynamics of the system attractor uniformly fill the state space (i.e. _A_<sub>1</sub>≈_A_<sub>2</sub>) and provided the observation function captures information on each of the dimensions uniformly (i.e. \(\kappa_1\approx\kappa_2\)). With the stable linear Takens’ embedding theorems as references, we can extend the results to delay-coordinate maps using unevenly-spaced time- delays.

## III. THEORETICAL RESULTS

### A. Non-Uniform Delay-Coordinate Maps

Given a set of \(\ell\) times \(\{\tau_k\}_{k=1}^\ell\), define the non-uniformly- sampled delay-coordinate map \(\Psi_{\{\mathbf{h},\Phi,\{\tau_k\}_{k=1}^\ell\}}\) as:

\(\Psi(\mathbf{x}(t))=\left[\begin{array}{ c }
\mathbf{y}(t-\tau_1) \\
\mathbf{y}(t-\tau_2) \\
\vdots \\
\mathbf{y}(t-\tau_\ell)
\end{array}\right]=\left[\begin{array}{ c }
\mathbf{h}^T\Phi^{-\tau_1}\mathbf{x}(t) \\
\mathbf{h}^T\Phi^{-\tau_2}\mathbf{x}(t) \\
\vdots \\
\mathbf{h}^T\Phi^{-\tau_\ell}\mathbf{x}(t)
\end{array}\right]\) (8)

