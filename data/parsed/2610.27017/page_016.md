uses kernel functions to model the varying relationship between problem sizes and quasi-optimal parameters, and predicts near-optimal parameters at a low computational cost. Assume that we have a training set containing _d_ data:<tbc>

\(\mathcal{D}=\{(N_i,\omega_i)|i=1,2,\dots,d\}=:\{\mathbf{N},\boldsymbol{\unknown}\},\)

<tbc>where the pair \((N_i,\omega_i)\) denotes the _N<sub>i</sub>_-th mesh partition number and the corresponding optimal relaxation parameter. The goal of Gaussian process regression is to establish a mapping between the input set **_N_** and the output set \(\boldsymbol{\unknown}\), represented as \(\mathcal{F}(N):\mathbb{R}\rightarrow\mathbb{R}\), and to forecast the potential output value \(\tilde{\omega}_*=\mathcal{F}(N_*)\) at a new test point _N_<sub>∗</sub>. In practical linear regression scenarios, we model the observed value \(\omega\) as the result of a latent function F(_N_) perturbed by additive noise \(\xi\), i.e.,<tbc>

\(\omega=\mathcal{F}(N)+\xi.\) (4.1)

<tbc>Suppose that \(\xi\) follows a Gaussian distribution with a zero mean and variance \(\sigma^2\), that is \(\xi\sim\mathcal{N}\big(0,\sigma^2\big)\). The common range for \(\sigma\) is \[10<sup>-6</sup>,10<sup>-2</sup>\]. For this investigation, we have set \(\sigma=10^{-4}\). Without loss of generality, assume true function F(_N_) follows a zero mean Gaussian process:<tbc>

\(\left[\begin{array}{ c }
\mathcal{F}(N_1) \\
\vdots \\
\mathcal{F}(N_d)
\end{array}\right]\sim\mathcal{N}\left(\left[\begin{array}{ c }
0 \\
\vdots \\
0
\end{array}\right],\left[\begin{array}{ c c c }
\kappa\big(N_1,N_1\big) & \cdots & \kappa\big(N_1,N_d\big) \\
\vdots & \ddots & \vdots \\
\kappa\big(N_d,N_1\big) & \cdots & \kappa\big(N_d,N_d\big)
\end{array}\right]\right),\)

<tbc>where \(\kappa(N_i,N_j)\) defines the covariance between the function values corresponding to the input points _N<sub>i</sub>_ and _N<sub>j</sub>_. The kernel function plays a pivotal role in GPR, as it is responsible for generating the covariance matrix that quantifies the similarity between any two input variables. The closer the distance between inputs, the higher the correlation between their corresponding output variables. Hence, it is essential to select or construct kernel functions that meet the specific demands of the problem at hand. In this paper, we consider the Gaussian kernel function, which is given by<tbc>

\(\kappa(N_i,N_j)=\delta_\mathcal{F}^2exp\left(-\frac{\left\|N_i-N_j\right\|_2^2}{2\delta_\mathcal{L}^2}\right),\)

<tbc>where \(\delta_\mathcal{F}\), \(\delta_\mathcal{L}\) are hyperparameters,and the specific calculation of the hyperparameters is given in \[14\]. Define \(K\big(\mathbf{N},\mathbf{N}\big)=(\kappa(N_i,N_j))\in\mathbb{R}^{d\times d}\). Then, we can express the prior distribution of the observed values \(\boldsymbol{\unknown}\) as<tbc>

\(\boldsymbol{\unknown}\sim\mathcal{N}\left(\mathbf{0},K\big(\mathbf{N},\mathbf{N}\big)+\delta^2I_d\right).\) (4.2)

<tbc>The joint prior distribution of the observed value \(\boldsymbol{\unknown}\) and the predicted value \(\boldsymbol{\unknown}_*\) is given by<tbc>

\(\left[\begin{array}{ c }
\boldsymbol{\unknown} \\
\boldsymbol{\unknown}_*
\end{array}\right]\sim\mathcal{N}\left(\left[\begin{array}{ c }
\mathbf{0} \\
\mathbf{0}
\end{array}\right],\left[\begin{array}{ c c c }
K\big(\mathbf{N},\mathbf{N}\big)+\delta^2I_d & K\big(\mathbf{N},\mathbf{N}_*\big) \\
K\big(\mathbf{N}_*,\mathbf{N}\big) & K\big(\mathbf{N}_*,\mathbf{N}_*\big)
\end{array}\right]\right).\) (4.3)

<tbc>Then the conditional expectation and variance of F(_n_) is given by<tbc>

\(\mathbb{E}[\mathcal{F}(N)|\boldsymbol{\unknown}]=K\big(\mathbf{N}_*,\mathbf{N}\big)\left[K\big(\mathbf{N},\mathbf{N}\big)+\delta^2I_d\right]^{-1}\boldsymbol{\unknown},\) (4.4)

\(Var[\mathcal{F}(N)|\boldsymbol{\unknown}]=K\big(\mathbf{N}_*,\mathbf{N}_*\big)-K\big(\mathbf{N}_*,\mathbf{N}\big)\left[K\big(\mathbf{N},\mathbf{N}\big)+\delta^2I_d\right]^{-1}K\big(\mathbf{N},\mathbf{N}_*\big).\) (4.5)

<tbc>For the output \(\omega_*\) in the test set, we use the mean of the Gaussian regression as its estimate, i.e. \(\tilde{\omega}_*=\mathbb{E}(\mathcal{F}(N)|\boldsymbol{\unknown})\).

