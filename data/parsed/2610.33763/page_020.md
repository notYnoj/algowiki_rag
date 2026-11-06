## Chapter 1

### Fractional operators and Mittag-Leffler type functions

This chapter presents the fundamental concepts of FC, encompassing both fractional operators and Mittag-Leffler type functions, which constitute the analytical foundation of this thesis. We review several widely used definitions of fractional integrals and derivatives, which play a central role in the modeling, analysis, and numerical approximation of FDEs.<br>
FC generalizes classical differential calculus by allowing differentiation and integration of non-integer order. Formally, this extension is expressed as

\(\frac{\partial^nu}{\partial z^n}\longrightarrow\frac{\partial^\alpha u}{\partial z^\alpha},n\in\mathbb{N},\alpha\in\mathbb{C},\)

where the resulting operators exhibit intrinsic nonlocality and memory effects. These properties distinguish fractional derivatives from their integer order counterparts and make them particularly suitable for modeling anomalous transport and diffusion processes in heterogeneous and complex media \[105, 110, 93\].<br>
The origins of FC can be traced back to the seventeenth century, when L’Hôpital raised the question of interpreting derivatives of non-integer order. Subsequent contributions by Euler, Lacroix, Fourier, and Abel gradually clarified the analytical structure of such operators, while the work of Liouville and Riemann in the nineteenth century provided a rigorous integral-based framework. These developments led to the classical Riemann-Liouville formulation and, later, to alternative definitions such as the Caputo, Grünwald-Letnikov, and Riesz derivatives, each tailored to different analytical and modeling requirements \[94, 105, 74\].<br>
In addition to fractional operators, special functions play a fundamental role in the theory of FDEs. In particular, Mittag-Leffler type functions naturally arise in the explicit representation of solutions of FDEs and multi-term FDEs. They generalize the exponential function and govern the temporal behavior, stability, and long-time dynamics of fractional models \[46\]. For this reason, this chapter also introduces Mittag-Leffler function (MLF) and generalized MLF, which provide essential analytical tools for the theoretical and numerical developments presented in the subsequent chapters.

### 1.1 Fractional operators

**Definition 1.1** _\[105\] Let_ \(\xi>0\)_, and_ \(u(z)\in L^1([a,b])\)_. Then, the left- and right-sided Riemann-Liouville fractional integrals are defined as_

\(\mathcal{D}_{a+,z}^{-\xi} u(z)=\frac{1}{\Gamma(\xi)}\int_a^z\frac{u(\sigma)}{(z-\sigma)^{1-\xi}}d\sigma,\)<br>
\(\mathcal{D}_{b-,z}^{-\xi} u(z)=\frac{1}{\Gamma(\xi)}\int_z^b\frac{u(\sigma)}{(\sigma-z)^{1-\xi}}d\sigma.\)

