**Lemma 14** (Total Initialization Complexity)**.** _By applying a union bound over the K arms and allocating a failure budget of_ \(\gamma=\delta/(2K)\) _to each_ MEDIANEST _instance, the total initialization burn-in phase is bounded by:_<tbc>

\(T_{init}=O\left(K\left(log\frac{\lambda}{\sigma}+log\frac{K}{\delta}\right)\right).\)

<tbc>_Proof._ For each of the _K_ arms, we run the MEDIANEST routine. With our fixed \(\varepsilon'\) and the grid size \(n=\Theta(\lambda/\sigma)\), the sample complexity per arm is bounded by \(M(n,\varepsilon',\delta/(2K))\). The additive terms in the query complexity are:<tbc>

\(O\left(logn+log^{2/3}nlog^{1/3}\frac{1}{\gamma}+log\frac{1}{\gamma}\right).\)

<tbc>By Young’s inequality, the cross term is bounded by the linear combination of the individual logarithmic terms:

\(log^{2/3}nlog^{1/3}\frac{1}{\gamma}\le\frac{2}{3}logn+\frac{1}{3}log\frac{1}{\gamma}=O\left(logn+log\frac{1}{\gamma}\right).\)

Thus, the sample complexity per arm simplifies to \(O\left(logn+log(1/\gamma)\right)\). Substituting \(n=\Theta(\lambda/\sigma)\) and \(\gamma=\delta/(2K)\) yields \(O\left(log\frac{\lambda}{\sigma}+log\frac{K}{\delta}\right)\) samples per arm. Multiplying this per-arm cost by the _K_ parallel instances gives the total bound _T_init. Because _T_init scales strictly with the number of arms _K_ and is entirely independent of the arm gaps \(\Delta_k\), it operates as a purely additive initialization cost.

