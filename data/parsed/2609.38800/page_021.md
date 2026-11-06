## B.3 Proof of Lemma 2

_Proof._ Let the 1-sided estimator be defined as \(g(x,\Delta)=\frac{f(x+\nu\Delta)-f(x)}{\nu}\Delta\). The difference between two estimates using the same perturbation \(\Delta\) is:<tbc>

\(g(x,\Delta)-g(y,\Delta)=\frac{\left[f(x+\nu\Delta)-f(x)\right]-\left[f(y+\nu\Delta)-f(y)\right]}{\nu}\Delta\) (42)

<tbc>Define the auxiliary function \(h(z)=f(z+\nu\Delta)-f(z)\). The numerator of the estimator difference simplifies to _h(x_)-_h(y_). By the Mean Value Theorem, there exists a point \(\xi\) on the line segment between _x_ and _y_ such that:<tbc>

\(h(x)-h(y)=\nabla h(\xi)^\top(x-y)\) (43)

<tbc>Evaluating the gradient of _h_, we get \(\nabla h(\xi)=\nabla f(\xi+\nu\Delta)-\nabla f(\xi)\). Using the landscape smoothness guarantee, where the Lipschitz constant of the true gradient is globally bounded by \(L\le p\|H\|\), and the fact that the Rademacher vector norm is \(\|\Delta\|=\sqrt{p}\), we bound the norm of \(\nabla h(\xi)\):<tbc>

\(\|\nabla h(\xi)\|=\|\nabla f(\xi+\nu\Delta)-\nabla f(\xi)\|\le p\|H\|\|\nu\Delta\|=\nu p^{1.5}\|H\|\) (44)

<tbc>Applying the Cauchy-Schwarz inequality to the Mean Value Theorem equality yields:<tbc>

\(|h(x)-h(y)|\le\|\nabla h(\xi)\|\|x-y\|\le\nu p^{1.5}\|H\|\|x-y\|\) (45)

<tbc>Substituting this bounded numerator back into the squared norm of the estimator difference, and noting that \(\|\Delta\|^2=p\):

\(\|g(x,\Delta)-g(y,\Delta)\|^2=\frac{|h(x)-h(y)|^2}{\nu^2}\|\Delta\|^2\)<br>
\(\le\frac{(\nu p^{1.5}\|H\|\|x-y\|)^2}{\nu^2}p\)<br>
\(=\frac{\nu^2p^3\|H\|^2\|x-y\|^2}{\nu^2}p\)<br>
\(=p^4\|H\|^2\|x-y\|^2\)

Because the \(\nu^2\) terms perfectly cancel, taking the expectation over \(\Delta\) yields:

\(\mathbb{E}_\Delta[\|g(x,\Delta)-g(y,\Delta)\|^2]\le p^4\|H\|^2\|x-y\|^2\) (46)

By identifying \(L_g^2\le p^4\|H\|^2\), we confirm that the estimator inherently satisfies the stochastic Lipschitz condition with bounding constant \(L_g\le p^2\|H\|\). This formally demonstrates that the stochastic Lipschitz property is fundamentally bounded by the quantum physics of the landscape and remains strictly independent of the finite-difference shift \(\nu\).

## B.4 Proof of Lemma 3

_Proof._ The proof relies on the foundational variance properties of simultaneous perturbation stochastic approximation (SPSA) applied to strictly bounded quantum landscapes.

**Step 1: The Global Gradient Bound**<br>
Unlike classical machine learning objectives which can grow unbounded, a Variational Quantum Algorithm (VQA) objective is strictly bounded by the spectral norm of the target Hamiltonian. Because the quantum state \(|\psi(\theta)\rangle\) is normalized, \(|f(\theta)|=|\langle\psi(\theta)|H|\psi(\theta)\rangle|\le\|H\|\).

By the exact algebraic identity of the Parameter-Shift Rule, any analytical partial derivative evaluates to:<tbc>

\(\nabla_jf(\theta)=\frac{1}{2}\left[f\left(\theta+\frac{\pi}{2}e_j\right)-f\left(\theta-\frac{\pi}{2}e_j\right)\right]\) (47)

<tbc>Applying the triangle inequality and substituting the global objective bound yields a strict constraint on every gradient component:

\(|\nabla_jf(\theta)|\le\frac{1}{2}\left|f\left(\theta+\frac{\pi}{2}e_j\right)\right|+\frac{1}{2}\left|f\left(\theta-\frac{\pi}{2}e_j\right)\right|\le\|H\|\) (48)

Consequently, the true gradient components are globally bounded by a physical constant, mathematically preventing the parameter landscape gradients from diverging.

