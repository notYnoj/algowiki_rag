\(\alpha(\mathsf{+},\mathsf{+},k)=\sum_{i,j>0}\alpha(i,j,k),\overline{\beta_{Z,\mathsf{+},\mathsf{+},k}}=\frac{1}{\alpha(\mathsf{+},\mathsf{+},k)}\sum_{i,j>0}\alpha(i,j,k)\cdot\beta_{Z,i,j,k},\)

<tbc>_and_

\(\overline{\beta_{Z,\mathsf{∗},\mathsf{∗},\mathsf{∗}}}=\sum_{i,j,k}\alpha(i,j,k)\cdot\beta_{Z,i,j,k}.\)

_Proof._ By symmetry, it suffices to compute the following two quantities, and _p_<sub>comp</sub> will be the ratio between them: (1) the number of tuples \((I,J,K,\hat{K})\) where _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is consistent with \(\alpha\), \(\hat{K}\in K\), \(Z_\hat{K}\) is typical, and \(Z_\hat{K}\) is compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_; (2) the number of \((I,J,K,\hat{K})\) where _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is consistent with \(\alpha\), \(\hat{K}\in K\), and \(Z_\hat{K}\) is typical.

We first compute the second quantity. First, the number of typical \(Z_\hat{K}\) is \(2^{H(\overline{\beta_{Z,\mathsf{∗},\mathsf{∗},\mathsf{∗}}})\cdot A_1\cdot n\pm o(n)}\). Each of these \(Z_\hat{K}\) uniquely determines a level-\(\ell\) block _Z<sub>K</sub>_. Also, for each _Z<sub>K</sub>_, the number of block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ consistent with \(\alpha\) is \(\frac{N_\alpha}{N_\mathrm{BZ}}=2^{(H(\alpha)-H(\alpha_Z))\cdot A_1\cdot n\pm o(n)}\). Therefore, the second quantity is

\(2^{(H(\overline{\beta_{Z,\mathsf{∗},\mathsf{∗},\mathsf{∗}}})+H(\alpha)-H(\alpha_Z))\cdot A_1\cdot n\pm o(n)}.\) (9)

Next, we compute the first quantity, which is the number of \((I,J,K,\hat{K})\) where _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is consistent with \(\alpha\), \(\hat{K}\in K\), \(Z_\hat{K}\) is typical, and \(Z_\hat{K}\) is compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_. By Item 2 in Definition 5.8, if \(Z_\hat{K}\) is compatible with any level-\(\ell\) block triple, then it is typical. Thus, we can drop the condition that \(Z_\hat{K}\) is typical, and equivalently count the number of \((I,J,K,\hat{K})\) where _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is consistent with \(\alpha\), \(\hat{K}\in K\), and \(Z_\hat{K}\) is compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_.

First, the number of block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ consistent with \(\alpha\) is \(N_\alpha\). Then, for each such block triple, we count the number of \(Z_\hat{K}\in Z_K\) that is compatible with it. If we fix some _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_, then we also have fixed the values of _S<sub>i,j,k</sub>_ for all _i,j,k_. Then we can rewrite the condition for \(Z_\hat{K}\) being compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ equivalently as follows:

**Definition 5.15** (Compatibility’)**.** For level-\(\ell\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ consistent with \(\alpha\), a level-1 block \(Z_\hat{K}\in Z_K\) is compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ if

• For every \(\{(i,j,k)\in\mathbb{Z}_{\ge 0}^3|i+j+k=2^\ell,i=0\text{or}j=0\}\), \(\mathrm{split}(\hat{K},S_{i,j,k})=\beta_{Z,i,j,k}\). (This is exactly Item 1 in Definition 5.8).<tbc>

• For every _k_, let \(S_{\mathsf{+},\mathsf{+},k}:=\bigcup_{i>0,j>0}S_{i,j,k}\). Then \(\mathrm{split}(\hat{K},S_{\mathsf{+},\mathsf{+},k})=\overline{\beta_{Z,\mathsf{+},\mathsf{+},k}}\).

Item 1 and the second condition above imply the original condition \(\mathrm{split}(\hat{K},S_{\mathsf{∗},\mathsf{∗},k})=\overline{\beta_{Z,\mathsf{∗},\mathsf{∗},k}}\) in Item 2,<tbc>

