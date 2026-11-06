Now we bound random variable \(\sum_{j:|T_j|<\Delta}\sum_{i\in T_j}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i/p\). If \(|T_j|<\Delta\), then by Chernoff bound we have<tbc>

\(\mathrm{Pr}\left[\sum_{i\in T_j}X_i\le\frac{2\mathrm{log}^3n}{\epsilon^2}\right]\ge 1-\mathrm{exp}(-\Omega(\mathrm{log}^3n)).\)

<tbc>By union bound we have

\(\mathrm{Pr}\left[\sum_{j:|T_j|<\Delta}\sum_{i\in T_j}\frac{1}{p}\mathsf{lis}^{[\ell_i,r_i]}(\mathsf{sa}_i)X_i\le\frac{2\mathrm{log}^3n}{\epsilon^2}\cdot\frac{\sqrt{n}}{p}\cdot\left\lceil\mathrm{log}_{1+\epsilon}\sqrt{n}\right\rceil<\frac{\epsilon\lambda n}{100t}\right]\ge\) (22)

\(1-\mathrm{exp}(-\Omega(\mathrm{log}^3n))).\) (23)

By Equation (21) and Equation (22), we obtain Equation (15).

Putting all the previous lemmas together gives the following result:

**Corollary 6.7** (algorithm for LIS decision problem)**.** _Given a length-n sequence A, let_ \(\lambda\in[1/n,1]\)_. There is a randomized algorithm that runs in time_ \(O(\lambda^{-7}\sqrt{n}\mathrm{log}^{O(1)}n)\) _such that with probability_ 1-1/poly(_n_)

• _The algorithm accepts if_ \(\mathsf{lis}(A)\ge n\lambda\).<tbc>

• _The algorithm rejects if_ \(\mathsf{lis}(A)=O(n\lambda^4)\).

_Proof._ The correctness follows from Lemma 6.6, Lemma 6.4, and Lemma 6.5.

**Running time:** The running time is

\(\text{time}=\underbrace{O(tk^2\sqrt{n}\mathrm{log}^{O(1)}n)}_\text{Lemma 6.5}+\underbrace{O(t^2\lambda^{-1}\sqrt{n}\mathrm{log}^{O(1)}n)}_\text{Lemma 6.6}\)<br>
\(=O(t^2\lambda^{-1}\sqrt{n}\mathrm{log}^{O(1)}n)\text{since}t\le O(k^2/\lambda)\)<br>
\(=O(k^4\lambda^{-3}\sqrt{n}\mathrm{log}^{O(1)}n)\text{since}k\le O(1/\lambda)\)<br>
\(=O(\lambda^{-7}\sqrt{n}\mathrm{log}^{O(1)}n)\)

Thus, we complete the proof.

Finally, by starting with \(\lambda=1\) and iteratively multiplying \(\lambda\) by a \(1/(1+\epsilon)\) factor until a solution is found, we can approximate lis(_A_) within an approximation factor of \(O(\lambda^3)\).

**Theorem 6.8** (polynomial approximation for LIS)**.** _Given a length-n sequence A such that_ \(\mathsf{lis}(A)=n\lambda\) _where_ \(\lambda\in[1/n,1]\) _is unknown to the algorithm. There is an algorithm that runs in time_ \(\widetilde{O}(\lambda^{-7}\sqrt{n})\) _and outputs a number_ est _such that_

\(\Omega(\mathsf{lis}(A)\lambda^3)\le\mathsf{est}\le O(\mathsf{lis}(A)).\)

_with probability at least_<br>
1-1/poly(_n)._

We remark that one can turn Theorem 6.8 into an algorithm with running time \(\widetilde{O}(n^{17/20})\) by considering two cases separately. If \(\lambda<n^{-1/20}\) we sample the array with a rate of _n_<sup>-3/20</sup> and compute the LIS for the sampled array. Otherwise, the running time of the algorithm is already bounded by \(\widetilde{O}(n^{17/20})\).

