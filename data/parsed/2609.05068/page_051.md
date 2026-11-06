<tbc>any \(a\in p\). One can then apply Lemma 5.3 and Proposition 5.1 for every \(k\in K\) and \(p\in Q_S^k\):

\(\sum_{a\in p}\frac{b^k\bar{x}_p^k}{c_a-\bar{y}_a}\le\sum_{a\in p}\frac{b^k\lambda_{\tilde{\gamma},S}^{post}\bar{x}_p^k}{c_a-\lambda_{\tilde{\gamma},S}^{post}\bar{y}_a}\le\lambda_{\tilde{\gamma},S}^{post}\sum_{a\in p}\dot{f}_x\frac{c_a-u_a}{c_a}\cdot\frac{l_{a_p}^k}{c_a}\cdot\frac{c_a-b^ku_p^k}{c_a}\cdot\frac{l_a}{c_a}(\frac{b^k\bar{x}_p^k}{c_a},\frac{\bar{y}_a}{c_a})\le\lambda_{\tilde{\gamma},S}^{post}b^kd^k\bar{x}_p^k=b^kd^k\bar{x}_p^k\)

proving that constraints (6) are satisfied for all \(k\in K\) and \(p\in Q_S^k\).

If \(p\in P^k\backslash Q_S^k\) then \(\bar{x}_p^k=0\) and the constraint is trivially satisfied.

It is straightforward to check that all other constraints of the DCMCF problem are satisfied, so the constructed solution is feasible.

Since _S\>_1, \(Q_S^k\) contains at least one path. Consequently, the following lower bound holds for any \(k\in K\): \(\sum_{p\in Q_S^k}\bar{x}_p^k\ge\frac{S|P^k|-(|P^k|-1)}{S|P^k|}\tilde{\gamma}\), implying that

\(\bar{\gamma}=\mathrm{min}_{k\in K}\sum_{p\in P^k}\bar{x}_p^k=\mathrm{min}_{k\in K}\sum_{p\in Q_S^k}\lambda_{\tilde{\gamma},S}^{post}\bar{x}_p^k\ge\mathrm{min}_{k\in K}\lambda_{\tilde{\gamma},S}^{post}\frac{S|P^k|-(|P^k|-1)}{S|P^k|}\tilde{\gamma}\)

Observe that \(\frac{\partial}{\partial|P^k|}\left(\frac{S|P^k|-(|P^k|-1)}{S|P^k|}\right)\le 0\) on R<sup>+</sup> ; therefore \(\frac{S|P^k|-(|P^k|-1)}{S|P^k|}\ge\frac{S|P|-(|P|-1)}{S|P|}\) and \(\tilde{\gamma}\ge\lambda_{\tilde{\gamma},S}^{post}\frac{S|P|-(|P|-1)}{S|P|}\tilde{\gamma}=\frac{4b\tilde{\gamma}u\frac{S|P|}{(uS|P|+b\tilde{\gamma})^2}\frac{S|P|-(|P|-1)}{S|P|}\tilde{\gamma}\).

Finally, let \(S^*=2-\frac{2}{|P|}+\frac{b\tilde{\gamma}}{u|P|}>1\) be the value of _S_ maximizing the lower bound of \(\bar{\gamma}\). One can then deduce that:

\(\tilde{\gamma}\ge\frac{4b\tilde{\gamma}uS^*|P|}{(uS^*|P|+b\tilde{\gamma})^2}\frac{S^*|P|-(|P|-1)}{S^*|P|}\tilde{\gamma}=\frac{4b\tilde{\gamma}u(S^*|P|-(|P|-1))}{(uS^*|P|+b\tilde{\gamma})^2}\tilde{\gamma}=\frac{4b\tilde{\gamma}u\left((2-\frac{2}{|P|}+\frac{b\tilde{\gamma}}{u|P|})|P|-(|P|-1)\right)}{\left(u(2-\frac{2}{|P|}+\frac{b\tilde{\gamma}}{u|P|})|P|+b\tilde{\gamma}\right)^2}\tilde{\gamma}=\frac{l}{u(|P|-1)}\)

This shows that, given the solution of the DCMCF<sub>env</sub> problem with objective value \(\tilde{\gamma}\), there exists a solution of DCMCF with objective value \(\tilde{\gamma}\ge\frac{b\tilde{\gamma}}{u(|P|-1)+b\tilde{\gamma}}\tilde{\gamma}\).

## B.4 Proof of Lemma 5.4

_Proof._ Let us consider an instance of DCMCF and a scalar \(\alpha>1\). We denote by \(u_a^0\) the upper bound of variable _y<sub>a</sub>_ for \(a\in A\). Such bounds can be derived analytically as described in Section 3.6. Upper bounds of variables \(x_p^k\) can similarly be computed for every \(k\in K\) and \(p\in P^k\), and lower bounds _l<sub>a</sub>_ and \(l_{a_p}^k\) can be set to zero.

