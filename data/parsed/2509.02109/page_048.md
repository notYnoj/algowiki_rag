<tbc>of i.i.d. entries of law N(0_,I<sub>C</sub>_). The initialisation is then a stationary Gaussian field with the same statistics as _u_, defined as T_<sub>H,W</sub>_ by _x_<sub>0</sub>:=_m+u⋆Z_, where \(m\in\mathbb{R}^C\) is the mean of _u_ and ⋆ denotes the discrete convolution with periodic boundary conditions.

Given a texture \(v\in\mathbb{R}^{H\times W\times C}\), we consider \(P_p(v)\subset[0,1]^{C\times p^2}\) the set of its \(p\times p\) patches (with periodic boundary conditions and indexing from the top-left corner). We also define the down- sampling operator _D<sub>s<sub>i</sub></sub>_ that shrinks the image by 2<sup>_s<sub>i</sub>_</sup>. The patch distribution of a texture _v_ is noted \(\mu_p^v=\frac{1}{|P_p(v)|}\sum_{y\in P_p(v)}\delta_y\).

For a given list of scales \(\mathcal{S}=\{(p_i,s_i)\}_{1\le i\le L}\), we aim to make the patch distributions \(\mu_p(x)\) of the optimised texture _x_ match the targets \(\mu_p(v)\). Each \(\mu_p^v\) is approximated by a Gaussian mixture \(\hat{\mu}_p^v\). The target mixture \(\hat{\mu}_p^u\) is fitted once by EM and fixed. We use the _Warm-Start EM_ (see Algorithm 3) variant during optimisation, and take \(\varepsilon_r=10^{-3}\). We solve the problem<tbc>

\(min_x\sum_{i=1}^L2^{2s_i}MW_2^2\left(\hat{\mu}_{p_i}^{D_{s_i}x},\hat{\mu}_{p_i}^{D_{s_i}u}\right).\)

















(a) Eiffel \(\rightarrow\) The Great Wave

(b) Tuebingen \(\rightarrow\) The Starry Night

(c) Tuebingen \(\rightarrow\) The Scream

Figure 28: Taking _K_=1 (top) gives results comparable to _K_=3 (bottom).

(a) Iteration 10

(b) Iteration 30

(c) Iteration 50

(d) Iteration 70

(e) Iteration 90

Figure 29: Evolution of the style transfer across iterations.

