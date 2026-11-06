_Proof._ For the rightmost inclusion, suppose \(B(\sigma)=(y_{i_1},\dots,y_{i_k})\). Then,

\(\mathrm{env}(B(\sigma))=\mathrm{cone}(\{y_{i_{\ell+1}}-y_{i_\ell}\}_{1\le\ell\le k-1})\subseteq\mathrm{cone}(\{y_j-y_i\}_{1\le i\le j\le n})=\mathrm{env}(\sigma).\) (16)

For the leftmost inclusion, let \(\pi_t:=B(\sigma^{1:t})\) denote the basis of the prefix at time _t_. Consider any \(y_t\in\sigma\):

• If \(y_t\notin\pi_n=B(\sigma)\), then it was excluded by the base construction algorithm, meaning:<tbc>

<tbc>\(y_t-y_1\in\mathrm{env}(\pi_{t-1})\subseteq\mathrm{env}(\pi_n)=\mathrm{env}(B(\sigma)).\)<tbc>

• If \(y_t\in\pi_n\), then it is one of the elements of the basis, and we can write:

<tbc>\(y_t-y_1=\sum_{\ell:i_\ell\le t}(y_{i_{\ell+1}}-y_{i_\ell})\in\mathrm{cone}(\{y_{i_{\ell+1}}-y_{i_\ell}\}_{1\le\ell\le k-1})=\mathrm{env}(B(\sigma)).\)<tbc>

<tbc>Hence, in both cases, \(y_t-y_1\in\mathrm{env}(B(\sigma))\), completing the proof.

We can now relate the size of valid _x_<sup>∗</sup>-certificates to the conic dimension of the underlying point set.

**Lemma A.4.** _If some point set_ \(\mathcal{Y}\subseteq\mathbb{R}^d\) _has conic dimension k, and_ \(y^*=\mathrm{argmin}_{y\in\mathcal{Y}}\langle w^*,y\rangle\)_, then there exists a valid y_<sup>∗</sup>_-certificate_ C _of length_ \(|\mathcal{C}|\le k-1\).

_Proof._ Order the points in Y as the sequence \(\sigma=\langle y^*=y_1,y_2,\dots,y_n\rangle\) such that \(\langle w^*,y_i\rangle\le\langle w^*,y_{i+1}\rangle\) for all _i_, and let \(B(\sigma)=(y_{i_1},\dots,y_{i_k})\) be the basic subsequence corresponding to \(\sigma\). We claim that the induced certificate \(\mathcal{C}:=\mathcal{C}_{B(\sigma)}\) is a valid _y_<sup>∗</sup>-certificate. Notice that C is defined such that

\(\mathrm{env}(B(\sigma))=\mathrm{cone}(\{y_i-y_j\}_{(i,j)\in\mathcal{C}}).\)

Using Lemma A.3, we have \(\mathcal{Y}\subseteq y_1+\mathrm{cone}(\{y_i-y_j\}_{(i,j)\in\mathcal{C}})\), which means that C is a valid certificate using Lemma A.1. Moreover, by construction, \((i,j)\in C\) means \(\langle w^*,y_j-y_i\rangle\ge 0\), which in turn means that the certificate is valid.

## A.1.2 Proof of Lemma 2.3

**Lemma 2.3** (Sieving Lemma)**.** _The expected number of points that are eliminated from_ P _at step 1.4 is at least_ |P|/2.

_Proof of Lemma 2.3._ For the analysis, consider a sequence (_x_<sub>1</sub>_,...,x<sub>N</sub>_) be such that \(\langle w^*,x_i\rangle\le\langle w^*,x_{i+1}\rangle\) for all \(1\le i\le N-1\). Note that \(\sigma\) is distributed as a random subsequence of (_x_<sub>1</sub>_,...,x<sub>N</sub>_), where each element is selected independently with probability 2_k/N_.

Consider a slightly modified, more lenient version of the algorithm that eliminates a point \(x_t\in\mathcal{P}\backslash\{y\}\) in Step 1.4 only if \(x_t-y\in\mathrm{env}(B(\sigma_{t-1}))\) where \(\sigma_t\) is the prefix of \(\sigma\) restricted to elements \(\{x_i\}_{1\le i\le t}\); recall the definition of the basic subsequence \(B(\cdot)\) from Section A.1.1. This modification ensures that elimination of _x<sub>t</sub>_ depends only on the coin tosses at indices in \[_t_-1\] and the sequence (_x_<sub>1</sub>_,...,x<sub>t</sub>_). This modified algorithm eliminates no more points than the original algorithm because \(\mathrm{env}(B(\sigma_{t-1}))\subseteq\mathrm{env}(\sigma_{t-1})\subseteq\mathrm{env}(\sigma)\)--each inequality just uses that the cone of a smaller set of vertices is smaller. Hence, it suffices to prove that the expected number of points eliminated by the modified algorithm is at least _N/_2.

