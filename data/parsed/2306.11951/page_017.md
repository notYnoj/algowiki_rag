<tbc>\(\sigma_i\). Now we consider a summation \(\sum_{i\in[K!],j\in[K-1]}\mathbb{E}[T_{\sigma_i(j),\sigma_i(j+1)}]\). For each pair (_i,j_), E\[_T<sub>i,j</sub>_\] is counted 2(_K_-1)! times in the summation. Furthermore, we know that \(\sum_{i<j}\mathbb{E}[T_{i,j}]=T\). Thus we have<tbc>

\(\sum_{i\in[K!],j\in[K-1]}\mathbb{E}[T_{\sigma_i(j),\sigma_i(j+1)}]=2T(K-1)!\)

<tbc>We know that there must exists some _i_ such that<tbc>

\(\sum_{j\in[K]}\mathbb{E}[T_{\sigma_i(j),\sigma_i(j+1)}]\le\frac{2T(K-1)!}{K!}=\frac{2T}{K}.\)

<tbc>Now we design _K_ instances \(\theta_0,\cdots,\theta_{K-1}\). We let \(\theta_0=(X_{\sigma_i(1)},\cdots,X_{\sigma_i(K)})\), and \(\theta_l\) be the instance that switches the element \(X_{\sigma_i(l)}\) with \(X_{\sigma_i(l+1)}\) based on \(\theta_0\), where \(l\in[K-1]\). From Le Cam’s two point lemma, we have

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{SORT}(\theta))\)<br>
\(\ge inf_\hat{\mu}sup_{\theta\in\{\theta_l\}_{l\in[K]}}\mathbb{P}(\hat{\mu}\neq\mathsf{SORT}(\theta))\)<br>
\(\ge inf_\Psi\frac{1}{2K}\sum_{l\in[K]}\mathbb{P}_{\theta_l}(\Psi\neq l).\)

Now by Fano’s inequality, we have

\(inf_\Psi\frac{1}{2K}\sum_{l\in[K]}\mathbb{P}_{\theta_l}(\Psi\neq l)\)<br>
\(\ge\frac{1}{2}\cdot\left(1-\frac{I(V;X)+log(2)}{log(K)}\right)\)<br>
\(=\frac{1}{2}\cdot\left(1-\frac{\sum_{l\in[K]}D_\mathsf{KL}(\mathbb{P}^l,\bar{\mathbb{P}})/K+log(2)}{log(K)}\right).\)

Here \(\bar{\mathbb{P}}=\frac{1}{K}\sum_{l\in[K]}\mathbb{P}^l\). We can compute

\(D_\mathsf{KL}(\mathbb{P}^l,\bar{\mathbb{P}})\)<br>
\(\le\mathbb{E}[T_{\sigma_i(l),\sigma_i(l+1)}]D_\mathsf{KL}\left(1-p\|\frac{(K-1)p+(1-p)}{K}\right)\)<br>
\(+\sum_{m\neq l}\mathbb{E}[T_{\sigma_i(m),\sigma_i(m+1)}]D_\mathsf{KL}\left(p\|\frac{(K-1)p+(1-p)}{K}\right)\)<br>
\(\le\frac{K-1}{K}\cdot\mathbb{E}[T_{\sigma_i(l),\sigma_i(l+1)}]D_\mathsf{KL}\left(p\|1-p\right)\)<br>
\(+\frac{1}{K}\sum_{m\neq l}\mathbb{E}[T_{\sigma_i(m),\sigma_i(m+1)}]D_\mathsf{KL}\left(p\|1-p\right).\)

Now summing over all _l_, we have

\(\frac{1}{K}\sum_{l\in[K]}D_\mathsf{KL}(\mathbb{P}^l,\bar{\mathbb{P}})\le\frac{2D_\mathsf{KL}\left(p\|1-p\right)}{K}\cdot\sum_{l\in[K]}\mathbb{E}[T_{\sigma_i(l),\sigma_i(l+1)}]\)<br>
\(\le\frac{4TD_\mathsf{KL}\left(p\|1-p\right)}{K^2}.\)

This gives

\(inf_\hat{\mu}sup_{\theta\in\{0,1\}^K}\mathbb{P}(\hat{\mu}\neq\mathsf{OR}(\theta))\ge\frac{1}{2}\cdot\left(1-\frac{4T\cdot D_\mathsf{KL}(p\|1-p)}{K^2log(K)}\right).\)

This shows that to output the correct answer with probability at least 2/3, one needs at least \(C\cdot K^2log(K)/D_\mathsf{KL}(p\|1-p)\) queries for some universal constant _C_.

