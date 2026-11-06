Thus, if the argmax were unique, this means that the optimal dual variables \(\lambda\) would be sufficient to coordinate each of the parties to find their portion of the optimal solution, without the need for further communication (the problem, in general, is that the argmax need not be unique, and ties may need to be broken in a coordinated fashion). However, because we have added a strongly concave regularizer, the argmax is unique in our setting:

**Claim 3.** _The solution to_

\(\mathrm{argmax}_{x\in\mathcal{F}_i}v^{(i)}\left(x^{(i)}\right)-\frac{\eta}{2}\|x^{(i)}\|^2-\sum_{j=1}^k\lambda_j\left(\sum_{i=1}c_j^{(i)}\left(x^{(i)}\right)\right)\)

_is unique._

_Proof._ This follows from the fact that the function \(v^{(i)}\left(x^{(i)}\right)-\frac{\eta}{2}\|x^{(i)}\|^2\) is strongly concave.

This gives rise to our simple coordination mechanism ReC. The mechanism first computes the optimal dual variables in our regularized partial Lagrangian problem, rounds them to finite precision, and then publishes these variables. Then each individual player finds her part of the near optimal solution by performing the optimization in Equation (1). The details are in Algorithm 4.1.

**Algorithm 1** Coordination Protocol for Linearly Separable Convex Programs \(\text{ReC}(\eta,\varepsilon)\)

**Input:** a linearly separable convex program instance _I_, regularization parameter \(\eta\) and target accuracy \(\varepsilon\)

Initialize: \(\alpha=\frac{\eta\varepsilon^2}{4\sqrt{nk}}\)

Modify the objective of _I_ into

\(\mathrm{max}_{x\in\mathcal{F}}v(x)-\frac{\eta\|x\|^2}{2}\)

Compute the optimal dual solution \(\lambda^\bullet\) for the modified convex program

Round each coordinate of \(\lambda^\bullet\) into a multiple of \(\alpha/\sqrt{k}\) and obtain \(\widehat{\lambda}\)

Broadcast the rounded dual solution \(\widehat{\lambda}\). To decode, each player _i_ computes:

\(\widehat{x}^{(i)}(\lambda)=\mathrm{argmax}_{x\in\mathcal{F}_i}\left[v^{(i)}\left(x^{(i)}\right)-\frac{\eta}{2}\|x^{(i)}\|^2-\sum_{j=1}^k\widehat{\lambda}_jc_j^{(i)}\left(x^{(i)}\right)\right]\)

Next we show that the resulting solution is close to the optimal solution of the regularized convex program (i.e. that we do not lose much by truncating the dual variables to have finite bit precision). Let \((x^\bullet,\lambda^\bullet)\) be an optimal primal-dual pair for the regularized convex program. Note that since the objective of the program is strongly concave, \(x^\bullet\) is unique. First, we will show that if the broadcast dual vector \(\widehat{\lambda}\) is close to an optimal dual solution \(\lambda^\bullet\), the resulting solution \(\widehat{x}\) will also be close to the optimal primal solution \(x^\bullet\).

**Lemma 4.** _Suppose we have a dual vector_ \(\widehat{\lambda}\) _such that_ \(\|\lambda^\bullet-\widehat{\lambda}\|\le\alpha\)_. Let_ \(\widehat{x}=\mathrm{argmax}_{x\in\mathcal{F}}\mathcal{L}(x,\widehat{\lambda})\)_, then_

\(\|\widehat{x}-x^\bullet\|\le\frac{2\sqrt{\alpha}(nk)^{1/4}}{\sqrt{\eta}}\)

