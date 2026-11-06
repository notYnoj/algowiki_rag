We attribute this to a distributed factorization parallelizing the independent subtrees of the elimination tree while the large separators at the top of the tree are still factored on a single device, which caps the speedup in three dimensions. The more significant gain is memory capacity, as pooling the devices enables problems that no longer fit on a single GPU, whereas spilling the factor into host memory keeps such problems feasible on one device at a much higher cost. Even so, the exact factorization eventually exceeds the combined memory of four devices, which sets the practical limit of this approach.

## 5. Applications to PDE-constrained Optimization

`diff-soup` combines physics modeling, differentiable simulation, and optimization in a single package that serves both classical and deep-learning based inference. In this section, we demonstrate end-to-end workflows implemented entirely in `diff-soup` for two different inference paradigms: a conventional Bayesian inference problem for learning the constitutive relationships of binary phase-separating materials, inspired by Zhao et al. [79] and Cohen et al. [25], and a modern deep learning problem in which a neural field is embedded in a packed bed reactor model and trained to represent its three-dimensional catalyst activity.

### 5.1. Inference with Uncertainty Quantification

First, we demonstrate `diff-soup` on a classic Bayesian inverse problem, in which the constitutive relationships of a phase-separating material are inferred from image data. We reproduce the results of Zhao et al. [79], inferring the composition-dependent tracer diffusivity _D(c_) and the homogeneous chemical potential \(\mu_h(c)\) from a single noisy movie of spinodal decomposition and quantifying the uncertainty by sampling the posterior. The composition _c_ evolves according to the Cahn-Hilliard equation

\(\frac{\partial c}{\partial t}=\nabla\cdot\big(D(c)c\nabla\mu\big),\mu=\mu_h(c)-\kappa\nabla^2c,\) (21)

where \(\mu\) is the chemical potential in units of _k<sub>B</sub>T_ per particle, \(\kappa\) is the gradient energy coefficient, and _D(c_) is the tracer diffusivity, related to the mobility<tbc>

