_Proof of Lemma 5.10._ Let \(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\) and \(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\) denote a feasible solution of the linear program in Definition 5.6. First, we claim the following equations hold for this feasible solution:

\(\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{valid}\text{with}\mathcal{E}\wedge\sigma\text{satisfied by}x}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=1,\text{for all}x\in\Omega^{\mathcal{C}\backslash\{c_0\}},\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{valid}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}^Y\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}=1,\text{for all}y\in\Omega^C.\text{(11)}\)

These equations follow directly from verifying Definition 5.6. By summing these equations over all \(x\in\Omega^{\mathcal{C}\backslash\{c_0\}}\) and all \(y\in\Omega^C\), we obtain:

\(|\Omega^{\mathcal{C}\backslash\{c_0\}}|=\sum_{x\in\Omega^{\mathcal{C}\backslash\{c_0\}}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{valid}\text{with}\mathcal{E}\wedge\sigma\text{satisfied by}x}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X,|\Omega^C|=\sum_{y\in\Omega^C}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{valid}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}^Y\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}.\text{(12)}\)

Thus, we can express \(|\Omega^{\mathcal{C}\backslash\{c_0\}}|\) as follows:

\(\text{(by (12))}|\Omega^{\mathcal{C}\backslash\{c_0\}}|=\sum_{x\in\Omega^{\mathcal{C}\backslash\{c_0\}}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{valid}\text{with}\mathcal{E}\wedge\sigma\text{satisfied by}x}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=\sum_{x\in\Omega^{\mathcal{C}\backslash\{c_0\}}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}\text{with}\mathcal{E}\wedge\sigma\text{satisfied by}x}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X+\sum_{x\in\Omega^{\mathcal{C}\backslash\{c_0\}}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{run}\text{with}\mathcal{E}\wedge\sigma\text{satisfied by}x}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\le\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}}|\Omega^{\mathcal{E}\wedge\sigma}|\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X+2^{-M}\cdot|\Omega^{\mathcal{C}\backslash\{c_0\}}|.\text{(by Claim 5.11)}\)

Thus, \(|\Omega^{\mathcal{C}\backslash\{c_0\}}|\) can be bounded as:

\(\left|\Omega^{\mathcal{C}\backslash\{c_0\}}\right|\in\left[\hat{z}^X,\left(1+2\cdot 2^{-M}\right)\hat{z}^X\right],\)<br>
\(\text{where}\hat{z}^X\unknown\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}}|\Omega^{\mathcal{E}\wedge\sigma}|\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X.\)

Similarly, \(|\Omega^C|\) can also be bounded as:

\(\left|\Omega^C\right|\in\left[\hat{z}^Y,\left(1+2\cdot 2^{-M}\right)\hat{z}^Y\right],\)<br>
\(\text{where}\hat{z}^Y\unknown\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}}|\Omega^{\mathcal{F}\wedge\tau}|\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y.\)

Consequently, the ratio \(|\Omega^{\mathcal{C}\backslash\{c_0\}}|/|\Omega^C|\) is bounded as:

\(\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^C|}\le\left(1+2\cdot 2^{-M}\right)\frac{\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}}|\Omega^{\mathcal{E}\wedge\sigma}|\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X}{\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}}|\Omega^{\mathcal{F}\wedge\tau}|\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y}\)<br>
\(\le\left(1+2\cdot 2^{-M}\right)r_+,\)

where the last inequality follows from the leaf constraints of the LP (Item III. in Definition 5.6).

