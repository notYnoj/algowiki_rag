where \(\vec{E}\) contains one orientation (_x,y_) of every edge \(xy\in E\), chosen so that \(H_u(x)\le H_u(y)\). Next, we will upper-bound \(\int_{s\in I}\Phi_sds\). Node \(x\in V\) contributes at most \(2L\eta_x\cdot\frac{w(x)}{2}=L\eta_xw(x)\) to this bound, while edge \((x,y)\in\vec{E}\) contributes at most<tbc>

\(\left(|H_u(x)-H_u(y)|-L\eta_x-L\eta_y\right)_+\cdot w(xy)\le\left(L\underbrace{\varrho(x,y)}_{\le\xi_{xy}=\eta_x+\eta_{xy}+\eta_y}-L\eta_x-L\eta_y\right)_+\cdot w(xy)\le L\eta_{xy}w(xy)\)

<tbc>where we used _L_-Lipschitzness of _H<sub>u</sub>_. We conclude that<tbc>

\(\int_{s\in I}\Phi_sds\le L\sum_{x\in V}\eta_xw(x)+L\sum_{xy\in E}\eta_{xy}w(xy)+|I|\Psi\le 2LJ+|I|\Psi\)

<tbc>Note that \(\Psi\le\mu\left(|S-S^*|+N_\mathsf{bad}\right)\le\mu|S-S^*|+\frac{c'n\mu}{2}\le J+\frac{c'n\mu}{2}\) . We can now obtain the desired bound of _F_ as follows:

\(F\le min_{s\in I}\Phi_s\le\frac{2LJ}{|I|}+J+\frac{c'n\mu}{2}\le\left(\frac{2L}{\sigma/2}+1\right)\cdot 12\alpha/\varepsilon+\frac{c'n\mu}{2}\le\frac{c'n\mu}{2}+\frac{c'n\mu}{2}\le c'n\mu\)

### 6.5 Wrap-up: proof of the first oracle bound

We now collect the complexity, width, and sparsity bounds for the first implementation of the reduced oracle.

**Lemma 21.** _Let_ \(\varepsilon\in[\Theta(1/logn),\Theta(1)]\)_, and suppose that the parameters_ \(\Gamma\) _and_ \(\beta\in[1,O(\sqrt{logn})]\) _of the padding bound are known. The oracle described above runs in_ \(m^{1+o(1)}n^{O(\varepsilon)}\text{polylog}(n)\) _time and produces either a_ \(\Theta(1)\)_-balanced element cut of cost_ \(O(\alpha\sqrt{\beta}/\varepsilon)\) _or a valid feedback matrix with spectral norm_ \(O(\alpha\sqrt{\beta}/(\varepsilon n))\)_, with probability at least_ \(1-n^{-\Theta(1)}\)_. Moreover, every feedback matrix has_ \(O(mn^{O(\varepsilon)}\text{polylog}(n))\) _non-zero entries._

_Proof._ Choose parameters \(\Delta=\Theta(1)\) and \(\mu=\Theta\left(\frac{\alpha\sqrt{\beta}}{\varepsilon n}\right)\) as described above. Note that \(\mu\) can be chosen as a ratio _a/b_ of two polynomially-bounded integers within a constant factor of the required value, since \(\frac{\alpha\sqrt{\beta}}{\varepsilon n}\in[n^{-\Theta(1)},n^{\Theta(1)}]\). The graphs constructed inside the oracle may have non-integral rational weights of the form \(\mu\) and \(\frac{w(x)}{2}\) ; they can be converted to polynomially-bounded integers by multiplying all weights by 2_b_, and then scaling the result back.

By Corollary 16 and Theorem 17 a rectangular cover Q with \(q=n^{O(\varepsilon)}\text{polylog}(n)\) rectangles and a corresponding Q-flow can be constructed in \(m^{1+o(1)}q^{2+o(1)}=m^{1+o(1)}n^{O(\varepsilon)}\text{polylog}(n)\) time, with probability of failure at most \(n^{-\Theta(1)}\). In the case of a large flow Lemma 18 gives a feedback matrix _N_ with \(\|N\|\le 2\mu=O(\alpha\sqrt{\beta}/(\varepsilon n))\) and at most \(O(mq^2)=O(mn^{O(\varepsilon)}\text{polylog}(n))\) non-zero entries. In the case of a small flow calling procedure in Lemma 19 \(\Theta(logn)\) times gives \(\Theta(1)\)-balanced cut of cost at most \(O(\alpha\sqrt{\beta}/\varepsilon)\) with probability at least \(1-n^{-\Theta(1)}\).

Taking \(\tau=\Theta(1)\) sufficiently small and \(\gamma=\Theta(\varepsilon)\) meets Lemma 18, and the assumed range of \(\varepsilon\) gives \(\gamma=\Omega(1/logn)\).

## 7 Second approach: chaining with correlated Gaussians

In this section we describe an alternative implementation of the reduced oracle. It follows very closely the oracle in \[24\].

