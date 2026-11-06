<tbc>denotes the usual binary entropy function. Hence, understanding the _limiting free energy density_

\(f_\mathrm{pl}(\alpha):=\mathrm{lim}_{N,M\rightarrow\infty M/N=\alpha}\frac{1}{N}\mathbb{E}\left[\mathrm{log}Z_{X,Y}\right]\)

of this model is equivalent to computing the maximum rate achieved by uniformly random codes in the deletion channel.

Finally, we note that the null variant of the Random Subsequence Model is relevant to uniformly random codes for the deletion channel as well, and refer the reader to \[Mit09\] for additional discussion in this direction. Indeed, let \(\mathcal{C}\subseteq\{0,1\}^N\) be a uniformly-random code, with all elements of C drawn i.i.d. uniformly from {0,1}_<sup>N</sup>_. Let _X_∼C be a uniformly-random codeword and _Y_ the output of the deletion channel on input _X_. The maximum-likelihood decoder outputs<tbc>

\(\hat{x}(Y)=\mathrm{argmax}_{x\in\mathcal{C}}\mathbb{P}(Y|X=x)=\mathrm{argmax}_{x\in\mathcal{C}}Z_{x,Y},\)

<tbc>since as a function of \(x\in\{0,1\}^N\), it holds that \(\mathbb{P}(Y|X=x)\propto Z_{x,Y}\). Thus, we have that<tbc>

\(\mathbb{P}\left(\hat{x}(Y)\neq X\right)\le\mathbb{P}\left(Z_{x^\prime,Y}\ge Z_{X,Y}\text{for some}x'\in\mathcal{C}\backslash\{X\}\right)\le(|\mathcal{C}|-1)\mathbb{P}\left(Z_{X^\prime,Y}\ge Z_{X,Y}\right).\)

<tbc>But note that, since \(X'\) is independent of _X_, \(Z_{X^\prime,Y}\) and _Z<sub>X,Y</sub>_ are exactly distributed as the partition functions of the null and planted variants of the Random Subsequence Model, respectively. Hence, if one shows that the planted partition function is greater than the null partition function with high probability, that gives a bound on the maximum-likelihood decoder’s probability of failure. This maximum likelihood decoding strategy, combined with the sub-optimal bound

\(\mathbb{P}\left(Z_{X^\prime,Y}\ge Z_{X,Y}\right)\le\mathbb{P}\left(Z_{X^\prime,Y}\ge 1\right),\)

is the heart of the argument of \[Gal61; Zig69; DG01\], which gave one of the early lower bounds on the capacity of the deletion channel.

## 1.1.2. _Longest common subsequence of two random strings._

A second source of motivation for the Random Subsequence Model comes from the longest common subsequence (LCS) problem. If _X_<sub>1</sub> and _X_<sub>2</sub> are independent uniformly random binary strings of respective lengths _N_<sub>1</sub> and _N_<sub>2</sub>, we let LCS(_X_<sub>1</sub>_,X_<sub>2</sub>) denote the length of their longest common subsequence. A classical open problem of more than fifty years is to determine the limit<tbc>

\(f(\gamma):=\mathrm{lim}_{N_1,N_2\rightarrow\infty N_2/N_1=\gamma}\frac{1}{N_1}\mathbb{E}\left[\text{LCS}(X_1,X_2)\right].\)

<tbc>The case \(\gamma=1\), proposed by \[CS75\], has been the subject of intensive study \[Dek79; Ste82; Ale94; DP95; Hei+24\]. Following \[Bou99\], one may instead study the partition function<tbc>

\(Z_{N_1,N_2,M}:=|\{\sigma^1\in\Sigma_{N_1,M},\sigma^2\in\Sigma_{N_2,M}:(X_1)_{\sigma^1}=(X_2)_{\sigma^2}\}|,\)

<tbc>which counts common length-_M_ subsequences of _X_<sub>1</sub> and _X_<sub>2</sub>. So in particular, _Z_<sub>_N_<sub>1</sub>_,N_<sub>2</sub>_,M_</sub>_\>_0 if and only if there exists a common subsequence between _X_<sub>1</sub> and _X_<sub>2</sub> of length _M_. Then one can compute the associated free energy<tbc>

\(g(\gamma,\alpha):=\mathrm{lim}_{N_1,N_2,M\rightarrow\infty N_2/N_1=\gamma,M/N_1=\alpha}\frac{1}{N_1}\mathbb{E}\left[\mathrm{log}(1+Z_{N_1,N_2,M})\right].\)

<tbc>This free energy encodes the LCS constant, as it is easy to show that<tbc>

\(f(\gamma)=\mathrm{sup}\left\{\alpha:g(\gamma,\alpha)>0\right\}.\)

<tbc>The null variant of our Random Subsequence Model corresponds to the special case where \(\gamma=\alpha\). Indeed, in that case one has _M=N_<sub>2</sub>, and then the second ambient string is itself the candidate subsequence, so

\(Z_{N_1,N_2,M}=|\{\sigma\in\Sigma_{N_1,M}:(X_1)_\sigma=X_2\}|=Z_{X_1,X_2},\)

