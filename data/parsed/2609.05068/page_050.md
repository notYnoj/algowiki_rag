## B.2 Proof of Lemma 5.3

_Proof._ First, observe that \(\lambda_{1-\frac{u_a}{c_a},\frac{b^k\gamma}{c_aS|P^k|}}=4\frac{\frac{b^k\gamma}{c_aS|P^k|}\frac{u_a}{c_a}}{(\frac{u_a}{c_a}+\frac{b^k\gamma}{c_aS|P^k|})^2}=\frac{4b^k\gamma u_aS|P^k|}{(u_aS|P^k|+b^k\gamma)^2}\). The derivative of this expression with respect to _b<sup>k</sup>_, \(\frac{\partial}{\partial b^k}\left(\lambda_{1-\frac{u_a}{c_a},\frac{b^k\gamma}{c_aS|P^k|}}\right)=\frac{4\gamma u_aS|P^k|(u_aS|P^k|+b^k\gamma)}{(u_aS|P^k|+b^k\gamma)^3}\) , is positive for \(b^k\le\frac{u_aS|P^k|}{\gamma}\) . Therefore, if \(u_a\ge\frac{b^k\gamma}{S|P^k|}\), \(\lambda_{1-\frac{u_a}{c_a},\frac{b^k\gamma}{c_aS|P^k|}}\) increases with _b<sup>k</sup>_ and \(\lambda_{1-\frac{u_a}{c_a},\frac{b^k\gamma}{c_aS|P^k|}}\ge\frac{4b\gamma u_aS|P^k|}{(uS|P^k|+b\gamma)^2}\) with \(b=min_{k\in K}b^k\).

Similarly, the derivative of \(\frac{4b\gamma u_aS|P^k|}{(u_aS|P^k|+b\gamma)^2}\) with respect to |_P<sup>k</sup>_| is negative if \(|P^k|\ge\frac{b\gamma}{Su_a}\). Notice that, under the assumption \(u_a\ge\frac{b^k\gamma}{S|P^k|}\), it follows that \(u_a\ge\frac{b\gamma}{S|P^k|}\). Therefore, \(\frac{4b\gamma u_aS|P^k|}{(u_aS|P^k|+b\gamma)^2}\) decreases with |_P<sup>k</sup>_| and \(\frac{4b\gamma u_aS|P^k|}{(u_aS|P^k|+b\gamma)^2}\ge\frac{4b\gamma u_aS|P|}{(u_aS|P|+b\gamma)^2}\) with \(|P|=max_{k\in K}|P^k|\).

Finally, the derivative of \(\frac{4b\gamma u_aS|P|}{(u_aS|P|+b\gamma)^2}\) with respect to _u<sub>a</sub>_ is negative if \(u_a\ge\frac{b\gamma}{S|P|}\). Hence, if \(u_a\ge\frac{b^k\gamma}{S|P^k|}\), \(\frac{4b\gamma u_aS|P|}{(u_aS|P|+b\gamma)^2}\) decreases with _u<sub>a</sub>_ and \(\frac{4b\gamma u_aS|P|}{(u_aS|P|+b\gamma)^2}\ge\frac{4b\gamma u_aS|P|}{(uS|P|+b\gamma)^2}\) with \(u=max_{a\in A}u_a\), and we get \(\lambda_{1-\frac{u_a}{c_a},\frac{b^k\gamma}{c_aS|P^k|}}\ge\frac{4ub\gamma S|P|}{(uS|P|+b\gamma)^2}\).

## B.3 Proof of Proposition 5.2

_Proof._ Let us consider a scalar _S\>_1 and a solution of DCMF<sub>env</sub> ; variable values of this solution are denoted by a tilde ( \(\checkmark\) ). We define, for every commodity \(k\in K\), the set of paths \(Q_S^k=\{p\in P^k:\tilde{x}_p^k\ge\frac{\tilde{\gamma}}{S|P^k|}\}\).

Let us construct a feasible solution \((\tilde{x}_p^k,\bar{y}_a,\bar{\gamma})\) of DCMCF as follows:

\(\tilde{x}_p^k=\left\{\begin{array}{ c c c }
\lambda_{\tilde{\gamma},S}^{post}\tilde{x}_p^k & \text{if} & p\in Q_S^k \\
0 & \text{if} & p\in P^k\backslash Q_S^k
\end{array}\right.\forall k\in K,p\in P^k\)<br>
\(\bar{y}_a=\sum_{k\in K,p\unknown a}b^k\bar{x}_p^k\forall a\in A\)<br>
\(\bar{\gamma}=min_{k\in K}\sum_{p\in P^k}\tilde{x}_p^k.\)

If \(p\in Q_S^k\), then \(\tilde{x}_p^k=\lambda_{\tilde{\gamma},S}^{post}\tilde{x}_p^k\), and \(\bar{y}_a\le\lambda_{\tilde{\gamma},S}^{post}\tilde{y}_a\) for \(a\in A\). Observe also that, for such a path _p_, \(\tilde{x}_p^k\ge\frac{\tilde{\gamma}}{S|P^k|}\) implies that \(u_a\ge\tilde{y}_a\ge b^k\tilde{x}_p^k\ge\frac{b^k\tilde{\gamma}}{S|P^k|}\) for<tbc>

