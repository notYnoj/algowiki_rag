<tbc>and for each \(\ell\ge 0\) we define<tbc>

\(\mathcal{S}_\ell(N,M):=\left\{(a_1,b_1),\dots,(a_{\ell+1},b_{\ell+1})\in(\mathbb{N}_{>0}^2)^{\ell+1}:\sum_{k=1}^{\ell+1}a_k=N+1,\sum_{k=1}^{\ell+1}b_k=M+1\right\}.\)

<tbc>Then writing \(L=\ell+1\), we have

(4.4) \(\overline{Z}=\sum_{L=1}^{M+1}\sum_{(X_1,\dots,X_L)\in\mathcal{S}_{L-1}(N,M)}\prod_{k=1}^Lw(X_k).\)

For a block tuple (_X_<sub>1</sub>_,...,X<sub>L</sub>_) define its empirical measure<tbc>

\(\mu=\frac{1}{L}\sum_{k=1}^L\delta_{X_k}.\)

<tbc>Let M_<sub>L</sub>_ denote the set of all empirical measures of the form above (i.e., _L_ atoms of weight 1_/L_, allowing repetitions). For \(\mu\in\mathcal{M}_L\), let \(\mathcal{S}_{L-1}(\mu)\) be the set of (ordered) tuples with empirical measure \(\mu\). Then we can rewrite

(4.5) \(\overline{Z}=\sum_{L=1}^{M+1}\sum_{\mu\in\mathcal{M}_L:\mathbb{E}_\mu[a]=\frac{N+1}{L},\mathbb{E}_\mu[b]=\frac{M+1}{L}}|\mathcal{S}_{L-1}(\mu)|exp\big(L\mathbb{E}_\mu[logw(a,b)]\big).\)

(The mean constraints are forced because \(\sum_kX_k=(N+1,M+1)\).)

## 4.3. Exponential scale of the entropy term.

Write<tbc>

\(n_{a,b}=n_{a,b}(\mu):=L\mu(a,b)\in\{0,1,\dots,L\}\)

<tbc>for the multiplicity of the value (_a,b_) under \(\mu\). Then the number of tuples with empirical measure \(\mu\) is the multinomial coefficient

(4.6) \(|\mathcal{S}_{L-1}(\mu)|=\frac{L!}{\prod_{(a,b)}n_{a,b}!}.\)

Recall the Shannon entropy

\(H(\mu):=-\sum_{a,b}\mu(a,b)log\mu(a,b),0log0:=0.\)

## 4.4. Entropy approximation and reduction to a variational problem.

Define the truncated-to-\(L\le M\) sum

(4.7) \(\overline{Z^{\le M}}:=\sum_{L=1}^M\sum_{\mu\in\mathcal{M}_L:\mathbb{E}_\mu[a]=\frac{N+1}{L},\mathbb{E}_\mu[b]=\frac{M+1}{L}}|\mathcal{S}_{L-1}(\mu)|exp\big(L\mathbb{E}_\mu[logw(a,b)]\big),\)

as well as the entropy-replaced sum

(4.8) \(\widetilde{Z}^{\le M}:=\sum_{L=1}^M\sum_{\mu\in\mathcal{M}_L:\mathbb{E}_\mu[a]=\frac{N+1}{L},\mathbb{E}_\mu[b]=\frac{M+1}{L}}exp\big(LH(\mu)+L\mathbb{E}_\mu[logw(a,b)]\big).\)

