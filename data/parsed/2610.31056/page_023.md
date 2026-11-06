we obtain, for every fixed _i_ and _j_,

\(\mathbb{P}_{r_j,s_j}\left[\left|\frac{(\mathbf{x}^\prime^{(i)})_j/\tilde{\lambda}_n+s_j}{r_j}\right|\neq\left|\frac{((\mathbf{x}^\prime^{(i)})_j+(\mathbf{v}^*)_j)/\tilde{\lambda}_n+s_j}{r_j}\right|\right]\)<br>
\(\le\mathcal{O}\left(\frac{1}{N^2}+\frac{log(BN)logN}{N^3}\right).\)

Taking a union bound over all coordinates \(j\in[n]\), we get

\(\mathbb{P}_{\{r_j,s_j\}_{j\in[n]}}\left[f(\mathbf{x}^\prime^{(i)})\neq f(\mathbf{x}^\prime^{(i)}+\mathbf{v}^*)\right]\le\mathcal{O}\left(\frac{n}{N^2}+\frac{nlog(BN)logN}{N^3}\right).\)

Finally, taking a union bound over all \(i\in[N]\), we conclude that

\(\mathbb{P}\big[\exists i\in[N]:f(\mathbf{x}^\prime^{(i)})\neq f(\mathbf{x}^\prime^{(i)}+\mathbf{v}^*)\big]\le\mathcal{O}\left(\frac{n}{N}+\frac{nlog(BN)logN}{N^2}\right).\)

**Remark:** Note that for every good set of sampled vectors {**x**<sup>(_i_)</sup>} ( i.e., \(\|\mathbf{x}^{(i)}\|_\infty\le N^2B\tilde{\lambda}_n\) for all \(i\in[N]\) ), there exists a choice of \(\{r_j,s_j\}_{j\in[n]}\) satisfying the required properties. Since our reduction runs in subexponential time, it could, in principle, find such a choice deterministically. We nevertheless sample these values at random, as this leads to a simpler description of the reduction.

From this point onward, we condition on the following good event:

1. \(\|\mathbf{x}^{(i)}\|_\infty\le BN^2\tilde{\lambda}_n\) for all \(i\in[N]\), and<tbc>

2. \(f(\mathbf{x}^\prime^{(i)})=f(\mathbf{x}^\prime^{(i)}+\mathbf{v}^*)\) for all \(i\in[N]\).<tbc>

<tbc>By the previous parts of the proof, this conditioning fails with probability at most

\(2^{-n}+\mathcal{O}\left(\frac{n}{N}+\frac{nlog(BN)logN}{N^2}\right).\)

We now show that, under this good event, the modified reduction outputs a nonzero vector with probability at least 1/2.

Fix all randomness of the modified reduction except the bits \(\tau_1,\dots,\tau_N\). Under the good event, changing a bit \(\tau_i\) does not change the encoded value \(a_i=f(\mathbf{x}^\prime^{(i)}+\tau_i\mathbf{v}^*)\), because \(f(\mathbf{x}^\prime^{(i)})=f(\mathbf{x}^\prime^{(i)}+\mathbf{v}^*)\). Hence the multiset A={_a_<sub>1</sub>_,...,a<sub>N</sub>_} is independent of the choice of the bits \((\tau_1,\dots,\tau_N)\). Therefore, once the remaining randomness is fixed, the PESS algorithm returns the same unequal subsets \(X,Y\subseteq[N]\) for every choice of the bits.

Since \(X\neq Y\) , there exists an index \(t\in(X\backslash Y)\cup(Y\backslash X)\). Consider two executions that differ only in the value of _b<sub>t</sub>_. Because the input multiset A is unchanged, both executions produce the same subsets _X,Y_ . Let **v** and \(\mathbf{v}'\) denote the corresponding output vectors. Then flipping _b<sub>t</sub>_ changes exactly one sampled vector by \(\pm\mathbf{v}^*\), and therefore changes the output vector by \(\pm\mathbf{v}^*\). More precisely,

\(\mathbf{v}'-\mathbf{v}=\left\{\begin{array}{ c c }
\mathbf{v}^* & \text{if}t\in X\backslash Y, \\
-\mathbf{v}^* & \text{if}t\in Y\backslash X.
\end{array}\right.\)

In particular, \(\mathbf{v}'\neq\mathbf{v}\). Since \(\mathbf{v}^*\neq\mathbf{0}\), at most one of **v** and \(\mathbf{v}'\) can be equal to **0**. Thus, among each such paired choice of the bit _b<sub>t</sub>_, at least one yields a nonzero output vector. Because _b<sub>t</sub>_ is uniform in {0,1}, it follows that, conditioned on the good event, the modified reduction outputs a nonzero vector<tbc>

