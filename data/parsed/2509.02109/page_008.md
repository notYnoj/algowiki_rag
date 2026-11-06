### The Warm-Start Method for Iteration of Differentiable EM.

In many practical applications, we are interested in minimising a certain loss function L applied to the output \(\theta_T(X)\) of the EM algorithm<sup>2</sup>. In this case, after a (small) gradient descent step _X_<sub>_t_+1</sub> computed from _X<sub>t</sub>_, the output of the EM algorithm with data _X<sub>t</sub>_ will often be a good initialisation for the EM algorithm with data _X_<sub>_t_+1</sub>. As a result, we suggest operating the EM algorithm with only one iteration and using the output of the previous step as an initialisation. This leads to the following algorithm, which we refer to as the Warm-Start EM Flow of a loss \(\mathcal{L}:\Theta\longrightarrow\mathbb{R}\).

**Algorithm 3:** Warm-Start EM Flow

**Input:** \(\theta_0\in\Theta\), \(X_0\in\mathcal{X}\), \(T_\mathrm{GD}\in\mathbb{N}\), \(\mathcal{L}:\Theta\longrightarrow\mathbb{R}\).

**1** **for** \(t\in\unknown 0,T_\mathrm{GD}-1\unknown\) **do**

**2** \(\theta_{t+1}=F(\theta_t,X_t)\);

**3** \(X_{t+1}=X_t-\eta_t\frac{\partial\mathcal{L}}{\partial\theta}(\theta_{t+1})\frac{\partial F}{\partial X}(\theta_{t+1},X_t)\);

The gradient step at line 3 means that we perform automatic differentiation of the expression \(\mathcal{L}(F(\theta_{t+1},X_t))\) with respect to _X_ at _X<sub>t</sub>_, seeing \(\theta_{t+1}\) as a constant and storing its for the next iteration. In essence, the Warm-Start method corresponds to an online OS gradient, which does not suffer from the approximation error of the OS method (since only one step is performed), yet benefits from the low memory footprint of the OS method.

A possible intuition for the Warm-Start method is that it tackles the bi-level problem by alternating between the "inner" optimisation over \(\theta\) (using an EM step) and the "outer" optimisation over _X_ (by a gradient step). In practice, if \(\theta_{t+1}\approx\theta^\star(X_t)\) at line 2, then since _F_ is very regular, for a small step \(\eta_t\), the update _X_<sub>_t_+1</sub> will be close to _X<sub>t</sub>_ and thus \(\theta_{t+1}\) will be sufficiently close to \(\theta^\star(X_{t+1})\) for one EM step to suffice (in practice, EM converges in few iterations in many moderate-dimensional settings).

## 3 Gaussian Mixture Model Optimal Transport

### 3.1 Reminders on GMM-OT

This section summarises the main results from \[DD20\]. The quadratic Wasserstein distance between two probability measures \(\mu_0\) and \(\mu_1\) on R_<sup>d</sup>_ with finite second moments is defined by

\(\mathrm{W}_2^2(\mu_0,\mu_1):=\mathrm{inf}_{\pi\in\Pi(\mu_0,\mu_1)}\int_{\mathbb{R}^d\times\mathbb{R}^d}\|y_0-y_1\|_2^2\mathrm{d}\pi(y_0,y_1),\) (12)

where \(\Pi(\mu_0,\mu_1)\) denotes the set of probability measures with finite second moments on \(\mathbb{R}^d\times\mathbb{R}^d\) whose marginals are \(\mu_0\) and \(\mu_1\). A solution \(\pi^*\) to Eq. (12) is called an optimal transport plan between \(\mu_0\) and \(\mu_1\). This distance has been widely used over the past fifteen years for various applications in data science. Let GMM_<sub>d</sub>_ denote the set of probability measures that can be written as finite Gaussian Mixture Models (GMMs) on R_<sup>d</sup>_. Transport plans and barycentres between GMMs with respect to W<sub>2</sub> are generally not GMMs, which is a limitation when such representations are used for data analysis or generation. For this reason, the authors of \[DD20\] propose to modify the W<sub>2</sub> formulation<tbc>

<sup>2</sup>for example \(\mathcal{L}(\theta_T(X))=\mathrm{MW}_2^2(\mu(\theta_T(X)),\nu)\), where \(\nu\) is a target GMM, see Section 3.

\begin{tabular}{ccc}
Method & Time & Memory \\
Full Automatic Differentiation (AD) & O(_T(nKd_<sup>2</sup>+_Kd_<sup>3</sup>)) & O(_TKd_<sup>2</sup>+_nd_) \\
Approximate Implicit Gradient (AI) & O(_TnKd_<sup>2</sup>+_K_<sup>3</sup>_d_<sup>6</sup>+_nK_<sup>2</sup>_d_<sup>5</sup>) & O(_nK_<sup>2</sup>_d_<sup>4</sup>) \\
One-Step gradient (OS) & O(_T(nKd_<sup>2</sup>+_Kd_<sup>3</sup>)) & O(_Kd_<sup>2</sup>+_nd_) \\
\end{tabular}

1: Complexities of the `backward` passes (gradient computations) for _T_ EM iterations on _n_ points in R_<sup>d</sup>_ with _K_ components.

