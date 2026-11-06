_Proof._ We iterate over all _t_ pseudosolutions, and for each one we estimate their quality separately. In the end we output the largest estimated value over all pseudosolutions. More precisely, we define \(p=\frac{1000t\mathrm{log}^4n}{\epsilon^4\lambda\sqrt{n}}\) and for each pseudosolution, we sample each of its subarrays with probability _p_. We then compute the LIS of the sampled subarrays subject to the range which corresponds to the pseudosolution. We then estimate the quality of the pseudosolution by scaling the sum of LIS’s by a factor 1_/p_. In what follows, we prove that the estimation error is negligible.

By Chernoff bound, for each pseudosolution, with probability \(1-\mathrm{exp}(-\Omega(\mathrm{log}^3n))\) at most \(2p\sqrt{n}=\frac{2000t\mathrm{log}^4n}{\epsilon^4\lambda}\) subarrays are sampled. For each pseudo-solution, Algorithm 10 computes the value of longest increasing subsequence subject to the corresponding range once for every sampled subarray. Hence, the total running time of the algorithm is \(O(t^2\sqrt{n}\mathrm{log}^{O(1)}n/\lambda)\).

Consider an arbitrary pseudo-solution \(\mathsf{ps}\in\{\mathsf{ps}_1,\dots,\mathsf{ps}_t\}\) and let \(\widetilde{\mathsf{q}}(\mathsf{ps})\) denote its estimated LIS. We show that

\(\mathrm{Pr}\left[\left(1-\frac{\epsilon}{4}\right)^2\left(\mathsf{q}(\mathsf{ps})-\frac{\epsilon\lambda^4n}{100t}\right)\le\widetilde{\mathsf{q}}(\mathsf{ps})\le\left(1+\frac{\epsilon}{4}\right)^2\mathsf{q}(\mathsf{ps})+\frac{\epsilon\lambda^4n}{100t}\right]\le 1-\mathrm{exp}(-\Omega(\mathrm{log}^3n)).\) (15)

Then the lemma holds by a union bound on all the pseudo-solutions.

Let _T_ be the set of subarray indices such that \(i\in T\) iff there is a non-empty interval \([\ell_i,r_i]\) of ps corresponding to subarray sa_<sub>i</sub>_. Let \(p=\frac{1000t\mathrm{log}^4n}{\epsilon^4\lambda\sqrt{n}}\) be the probability of sampling a subarray. For each \(i\in T\), let _X<sub>i</sub>_ denote a random variable such that<tbc>

\(X_i=\left\{\begin{array}{ c c }
1, & \text{with prob.}p; \\
0, & \text{with prob.}1-p.
\end{array}\right.\)

<tbc>and<tbc>

\(X=\sum_{i\in T}\frac{1}{p}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i.\)

<tbc>We have<tbc>

\(\mathbf{E}[X]=\mathbf{E}\left[\sum_{i\in T}\frac{1}{p}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i\right]=\sum_{i\in T}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)=\mathsf{q}(\mathsf{ps}).\)

<tbc>Let

\(T_j=\left\{i\in T:(1+\epsilon/4)^{j-1}\le\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)<(1+\epsilon/4)^j\right\}\)

for integer \(1\le j\in\left\lceil\mathrm{log}_{1+\epsilon}\sqrt{n}\right\rceil\).

Let \(\Delta=\frac{\epsilon^2\lambda\sqrt{n}}{1000t\mathrm{log}n}\). Consider _T<sub>j</sub>_’s such that \(|T_j|\ge\Delta\). The contribution of q(ps) mostly comes from _T<sub>j</sub>_ in the following sense

\(\sum_{j:|T_j|\ge\Delta}\sum_{i\in T_j}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\le\mathsf{q}(\mathsf{ps})\) (16)

and

\(\sum_{j:|T_j|\ge\Delta}\sum_{i\in T_j}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)=\mathsf{q}(\mathsf{ps})-\sum_{j:|T_j|<\Delta}\sum_{i\in T_j}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)\ge\mathsf{q}(\mathsf{ps})-\Delta\sqrt{n}\cdot\left\lceil\mathrm{log}_{1+\epsilon}\sqrt{n}\right\rceil\ge\mathsf{q}(\mathsf{ps})-\frac{\epsilon\lambda n}{100t}.\) (17)

