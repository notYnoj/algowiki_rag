\(\text{\textbf{Assumption 1.} There exists}(\theta_0,X_0)\in\Theta\times\mathcal{X}\text{such that}\theta^*(\theta_0,X_0):=lim_{t\longrightarrow+\infty} F_{X_0}^t(\theta_0)\text{exists in}\Theta\text{, with}\frac{\partial F}{\partial\theta}(\theta^*(\theta_0,X_0),X_0)-I\text{invertible.}\)

While convergence is typically observed in practice numerically, from a theoretical standpoint, it is a delicate matter. See \[MK07, Chapter 3\] for a reference on this field of research. We do not claim that the invertibility assumption holds in general and discuss counter-examples in Appendix A.1. We are now ready to formulate Proposition 2.1, which shows that the gradient of an EM solution with respect to the data is well-defined, using the implicit function theorem.

\(\text{\textbf{Proposition 2.1.} Under Assumption 1, there exist open neighbourhoods}\Theta^*,\mathcal{X}_0\text{such that}\theta^*(\theta_0,X_0)\in\Theta^*\subset\Theta\text{and}X_0\in\mathcal{X}_0\subset\mathcal{X}\text{, where there exists}\theta^*(\theta_0,\cdot)\in\mathcal{C}^\infty(\mathcal{X}_0,\Theta^*)\text{with:}\)<br>
\(\forall(\theta,X)\in\Theta^*\times\mathcal{X}_0,F(\theta,X)=\theta\Longleftrightarrow\theta=\theta^*(\theta_0,X).\) (6)

_Proof._ Let \(G:=\left\{\begin{array}{ c c }
\Theta\times\mathcal{X} & \longrightarrow \\
(\theta,X) & \longmapsto F(\theta,X)-\theta
\end{array}\right.\). Thanks to the regularity of _F_, _G_ is of class \(\mathcal{C}^\infty\). Assumption 1 implies that \(G(\theta^*(X_0),X_0)=0\), with \(\frac{\partial G}{\partial\theta}(\theta^*(X_0),X_0)\) invertible.

By the implicit function theorem, there exist open neighbourhoods \(\Theta^*,\mathcal{X}_0\) such that \(\theta^*(\theta_0,X_0)\in\Theta^*\subset\Theta\) and \(X_0\in\mathcal{X}_0\subset\mathcal{X}\), and there exists \(g:\mathcal{X}_0\longrightarrow\Theta^*\) of class \(\mathcal{C}^\infty\) such that \(g(X_0)=\theta^*(\theta_0,X_0)\), and:

\(\forall(\theta,X)\in\Theta^*\times\mathcal{X}_0,F(\theta,X)=\theta\Longleftrightarrow\theta=g(X).\)

For \(X\in\mathcal{X}_0\), we define \(\theta^*(\theta_0,X):=g(X)\).

To alleviate notation, we will write simply \(\theta^*(X):=\theta^*(\theta_0,X)\) and continue with Assumption 1 and the map \(\theta^*\) from Proposition 2.1. For the sake of completeness and to pave the way for future theoretical study, we provide the explicit expressions of the partial differentials of _F_ in Appendix A.6. Note that from a statistical viewpoint, the parameter \(\theta^*\) is not a Maximum-Likelihood Estimator (which, in fact, does not exist for GMMs), it is only the output of the EM algorithm which is often a local maximum of the likelihood.

## 2.3 Gradient Computation Methods

In this section, we are concerned with practical implementation of the computation of the gradient of the EM algorithm with respect to the data \(\partial_X[F_X^T(\theta_0)]\), given some initialisation \(\theta_0\in\Theta\) and number of iterations \(T\ge 1\). In addition to the automatic differentiation method, we present two alternative approximate strategies which rely only on the last parameter \(\theta_T\). These methods work under the assumption that \(\theta_T(X)\approx\theta^*(X)\), where \(\theta^*\) is defined in Proposition 2.1 and refers to the fixed point \(lim_{t\longrightarrow+\infty} F_X^t(\theta_0)\), assuming convergence.

### Full Automatic Differentiation (AD).

The most naïve approach consists in computing the gradient through all iterations using the backpropagation algorithm (for instance, using PyTorch’s automatic differentiation \[Pas+19\]). In other words, the "full automatic gradient" corresponds to letting automatic differentiation compute \(\partial_X[F_X^T(\theta_0)]\) directly, using an automatically differentiable implementation of the EM algorithm. For a large number of iterations _T_, AD can be considered as a natural baseline for computing the exact gradient, up to numerical precision. It is still an approximation, due to propagation of numerical errors, but is to the best of our knowledge the best available approximation of the true gradient, as discussed in Appendix A.4. Nevertheless, we use AD as a natural baseline method for comparisons. The AD method may be costly (both in time and memory) if the number of iterations _T_ is very large.

