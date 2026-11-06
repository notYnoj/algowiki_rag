1. We will first introduce a regularization term \(\eta\|x\|^2\) to our objective function, and coordinate the players to maximize the regularized objective. The purpose of adding this regularization term is to make the objective function _strongly concave_, which will cause it to have the property that an optimal dual solution will uniquely specify the optimal primal solution.<tbc>

2. Then we will show that the resulting optimal solution to the regularized problem is close to being optimal for the original (unregularized) problem. The weight of the regularization has to be traded off against the bit precision to which we need to communicate the optimal dual variables.

## 4.1 Coordination through Regularization

In the first step, we add a small regularization term to our original objective function. Consider the following convex optimization problem:

\(max_{x\in\mathcal{F}\text{and}\sum_{i=1}^nc_j^{(i)}(x^{(i)})\le b_j\text{for all}j}v'(x)=\sum_{i=1}^nv^{(i)}(x^{(i)})-\frac{\eta}{2}\|x\|^2\)

**Claim 2.** _The objective function_ \(v'\) _is_ \(\eta\)_-strongly concave._

To solve the convex program, we will work with the partial _Lagrangian_ \(\mathcal{L}(x,\lambda)\), which results from bringing only the coupling constraints into the objective via Lagrangian dual variables, but leaving the personal constraints to continue to constrain the primal feasible region:

\(\mathcal{L}(x,\lambda)=\sum_{i=1}^n\left(v^{(i)}\left(x^{(i)}\right)-\frac{\eta}{2}\|x^{(i)}\|^2-\sum_{j=1}^k\lambda_j\left(\sum_{i=1}c_j^{(i)}\left(x^{(i)}\right)-b_j\right)\right)\)<br>
\(=\sum_{i=1}^n\left(\left[v^{(i)}\left(x^{(i)}\right)-\frac{\eta}{2}\|x_i\|^2\right]-\sum_{j=1}^k\lambda_j\left(\sum_{i=1}c_j^{(i)}\left(x^{(i)}\right)-b_j\right)\right)\)

Let \(OPT'\) denote the optimum of the convex program, and by _strong duality_ we have

\(max_{x\in\mathcal{F}}min_{\lambda\in\mathbb{R}_+^k}\mathcal{L}(x,\lambda)=min_{\lambda\in\mathbb{R}_+^k}max_{x\in\mathcal{F}}\mathcal{L}(x,\lambda)=OPT'\)

Fixing the optimal dual variables, \(\lambda\), the optimal primal solution _y_ satisfies

\(y=argmax_{x\in\mathcal{F}}\mathcal{L}(x,\lambda)\)

Note that the result of moving the coupling constraints into the Lagrangian is that we can now write the primal optimization problem over a feasible region defined only by the personal constraints. Because of this fact, and because the Lagrangian objective is linearly separable across players, given \(\lambda\), each player’s portion of the solution _y_<sup>(_i_)</sup> is

\(argmax_{x\in\mathcal{F}_i}\left[v^{(i)}\left(x^{(i)}\right)-\frac{\eta}{2}\|x^{(i)}\|^2-\sum_{j=1}^k\lambda_jc_j^{(i)}\left(x^{(i)}\right)\right].\) (1)

