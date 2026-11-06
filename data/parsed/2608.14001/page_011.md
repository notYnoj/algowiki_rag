<tbc>for stability as \(\ell\rightarrow\infty\) to show that \(\unknown\) can approach isometry.

_Theorem 8:_ (Stable Linear Takens’ Embedding with Non- uniform Sampling; Theorem III.2 \[6\]) Consider a linear system of class A(_d_) in R_<sup>n</sup>_ that is in steady-state. Let \(\{\tau_k\}_{k=1}^\ell>0\) be the sampling times, \(\mathbf{h}\in\mathbb{R}^n\) be the observation function such that \(\|\mathbf{h}\|_2^2=\frac{2d}{\ell}\) , and \(\unknown\) the delay-coordinate map with \(\ell\) delays defined as in (8). Suppose that \(\ell\gg 1\), the \(\mathcal{A}_\unknown\)-eigenvalues \(\{e^{\pm i\theta_j\tau_k}\}\) are distinct and purely imaginary, and \(\mathbf{v}_j^H\mathbf{h}\neq 0\) for all \(j\in\{1,\dots,d\}\). Then, for all distinct pairs of points \(\mathbf{x}_1,\mathbf{x}_2\in\mathcal{M}\), with probability one \(\unknown\) satisfies (4) in the limit as \(\ell\rightarrow\infty\) with constants _C_ and \(\delta\rightarrow\delta_0\):

\(C:=d\left(\frac{\kappa_1^2}{A_2}+\frac{\kappa_2^2}{A_1}\right)\delta_0:=\frac{A_2\kappa_2^2-A_1\kappa_1^2}{A_2\kappa_2^2+A_1\kappa_1^2}\) (48)

_Proof:_ The proof follows from the same approach as Theorem III.2 in \[6\], with the exception that we neglect the lag-dependent term \(\delta_1(\ell)\) because we are considering only the asymptotic behavior of the embedding.

The difficulty of establishing a \(\delta_1(\ell)\)-term in Theorem 8 equivalent to that of Theorem 3 chiefly lies in the non- geometric nature of the non-uniform time series data. Whereas uniformly-sampled delay coordinate maps generate a geometric sum of exponential terms when applying Gerschgorin’s theorem to \(\mathbf{S}=(m/\ell)\mathbf{T}^H\mathbf{T}\) as seen in Lemma A.1 in \[6\], the geometric structure is lost when using non-uniformly-sampled data, and the expression (23) does not readily simplify.

_Remark 2:_ To introduce an additional degree of non-uniform sampling in the linear setting beyond the lag intervals between each delay, we can also allow for the observation function to be time-dependent, similar to \[17\]. Consider a time-dependent observation function \(\mathbf{h}(t)\in\mathbb{R}^n\) for which \(\mathbf{v}_j^H\mathbf{h}(t)\neq 0\) for all \(j\in\{1,\dots,d\}\) and \(t\in\mathbb{R}\). The resulting non-uniformly-sampled delay-coordinate map would be:

\(\unknown_{\{\mathbf{h}(t),\unknown,\{\tau_k\}_{k=1}^\ell\}}(\mathbf{x}(t))=\left[\begin{array}{ c }
\mathbf{h}(t)^T\unknown^{-\tau_1}\mathbf{x}(t) \\
\mathbf{h}(t)^T\unknown^{-\tau_2}\mathbf{x}(t) \\
\vdots \\
\mathbf{h}(t)^T\unknown^{-\tau_\ell}\mathbf{x}(t)
\end{array}\right]\) (49)

Suppose **h**(_t_) is still normalized by requiring \(\|\mathbf{h}(t)\|_2^2=\frac{2d}{\ell}\) . The time-dependence of the linear observation vector implies the measurement apparatus may be rotating or translating in time as it samples the dynamics, and the normalization ensures there is no stretching or shrinking. This may well be applicable when using mobile sensors that move relative to the system being observed. In the linear setting, the dynamics described by the embedding matrix **G**(_t_) can still be decoupled into a Vandermonde matrix **T** exactly as in (14) and a diagonal matrix **H**(_t_) each element of which-\(\mathbf{v}_j^H\mathbf{h}(t)\) and \(\mathbf{v}_j^T\mathbf{h}(t)\)- is now time-dependent. Consequently, the stable embedding bounds for the delay-coordinate map with mobile sensors will also be time-dependent. To make them time independent, the bounds must account for the behavior of **h**(_t_) over time. Red- defining \(\kappa_1\) and \(\kappa_2\) as in (5) to be:

\(\kappa_1=min_{t\in\mathbb{R}}min_{j\in\{1,\dots,d\}}\frac{|\mathbf{v}_j^H\mathbf{h}(t)|}{\|\mathbf{h}(t)\|_2}\kappa_2=max_{t\in\mathbb{R}}max_{j\in\{1,\dots,d\}}\frac{|\mathbf{v}_j^H\mathbf{h}(t)|}{\|\mathbf{h}(t)\|_2}\)

would allow the conclusions of Theorem 7 and 8 to apply with these new definitions of \(\kappa_1\), \(\kappa_2\), and **h**(_t_).

## D. Numerical Simulations

In this section, we implement simulated numerical experiments to assess whether delay-coordinate maps for linear systems with unevenly-spaced delays actually approach the asymptotic embedding quality \(\delta_0\). The approach to the experiments is mostly consistent with \[6\]. We generate a dynamical system of ambient dimension _n_=50 with attractor frequencies \(\{\pm\theta_j\}_{j=1}^d\), with _d_=4 for our example system and where each \(\theta_j\) is drawn from a random uniform distribution over \((0,2\pi)\). Considering that a sufficient condition on the sampling frequency to guarantee that \(\unknown\) will embed the dynamics of the original system is to choose \(\tau^*<\frac{\pi}{\theta_\mathrm{max}}\) , we selected the sampling interval to be \(\tau=0.8\tau^*\) for the deterministic, uniformly-sampled delay coordinate map, which serves as a baseline comparison for the non-uniformly-spaced case. (For the numerical simulations, \(\tau=0.9864\).)

For the delay-coordinate maps with unevenly-spaced delays, we generated the delays by initializing a length \(\ell_\mathrm{max}=500\) delay vector with entries drawn randomly from the following distributions: uniform, exponential, or normal. For each \(\ell\in\{1,\dots,\ell_\mathrm{max}\}\), a delay-coordinate map was generated using the first \(\ell\) lags of the \(\ell_\mathrm{max}\) total entries of the delay vector. This ensured that each lag test was consistent, in that it preserved the previous time lags when generating a delay-coordinate embedding with additional delay coordinates.

### 1) Uniform:

To ensure the distribution was contained in the interval \([0,\ell]\) for various choices of \(\ell\), we drew a length \(\ell_\mathrm{max}\) vector uniformly from \[0,1\] and then scaled the first \(\ell\) entries used for the particular iteration by \(\ell\).

### 2) Exponential:

Instead of using a typical exponential distribution, the domain of which is \([0,\infty)\), we used a truncated exponential distribution (using SciPy’s `truncxpon` function) contained in the interval \[0,1\] as a means to initialize a length-\(\ell_\mathrm{max}\) vector the first \(\ell\)-elements we would scale by \(\ell\) for the particular test iterate.

### 3) Normal:

As opposed to using a typical normal distribution, we used a truncated normal distribution (using SciPy’s `truncnorm` function) with \(\mu=0.5\) and \(\sigma^2=0.2\) and with the lower and upper bounds being 0 and 1, respectively.

To empirically measure how stable a particular embedding is, we consider the embedding conditioning:

\(Q(\mathbf{x}_1,\mathbf{x}_2)=\frac{\|\unknown(\mathbf{x}_1)-\unknown(\mathbf{x}_2)\|_2^2}{\|\mathbf{x}_1-\mathbf{x}_2\|_2^2}\) (50)

To empirically compute _Q_(**x**<sub>1</sub>,**x**<sub>2</sub>) for a particular \(\ell\), we perform 5,000 trials comparing the difference of pairs of states **x**<sub>1</sub> and **x**<sub>2</sub> under the delay-coordinate map. For each trial, we generate random pairs of points **x**<sub>1</sub> and **x**<sub>2</sub> from the same solution trajectory on the attractor. To do so, we draw pairs of random sample times _t_<sub>**x**<sub>1</sub></sub> and _t_<sub>**x**<sub>2</sub></sub> uniformly from \[0,10000\], and initialize the trajectory with the initial condition \(\mathbf{x}_0=\mathbf{V}\unknown_0\), where the coefficient vector \(\unknown_0=\left[11\cdots 11\right]\in\mathbb{C}^{2d}\) to ensure that the chosen solution

