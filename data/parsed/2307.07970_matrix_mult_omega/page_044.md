<tbc>_and_<tbc>

\(\alpha_t(+,+,k')=\sum_{i^\prime>0,j^\prime>0}\alpha_t(i',j',k'),\alpha_t(\text{\<,}\text{\<,}k')=\sum_{i^\prime<i_t,j^\prime<j_t}\alpha_t(i',j',k').\)

<tbc>_Furthermore,_

\(p_\text{comp}\le 2^{\sum_{t\in[s^\prime]}\big(\lambda_{Z,t}-H(\beta_{Z,t})+H(\gamma_{Z,t})+o_{1/\varepsilon}(1)\big)A_{t,1}\cdot n_t+o(n)}.\) (21)

_Proof._ Similar to before, it suffices to compute the following two quantities, and \(p_\text{comp}^*(\{\xi_{Z,t}\}_t)\) will be the ratio between them:

(1) the number of tuples \((I,J,K,\hat{K})\) where _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\), \(\hat{K}\in K\), \(\hat{K}\) has complete split distributions \(\{\xi_{Z,t}\}_t\), and \(Z_\hat{K}\) is compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_;<tbc>

(2) the number of \((I,J,K,\hat{K})\) where _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\), \(\hat{K}\in K\), and \(\hat{K}\) has complete split distributions \(\{\xi_{Z,t}\}_t\).

We first compute the second quantity. First, the number of \(Z_\hat{K}\) with the desired complete split distribu tions \(\{\xi_{Z,t}\}_t\) is \(2^{\sum_tH(\xi_{Z,t})\cdot A_{t,1}\cdot n_t\pm o(n)}\). Each of these \(Z_\hat{K}\) uniquely determines a level-\((\ell-1)\) block _Z<sub>K</sub>_. Also, for each _Z<sub>K</sub>_, the number of block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\) is \(\frac{N_\alpha}{N_\text{BZ}}=2^{\sum_t(H(\alpha_t)-H(\gamma_{Z,t}))\cdot A_{t,1}\cdot n_t\pm o(n)}\). Therefore, the second quantity is

\(2^{\sum_t(H(\xi_{Z,t})+H(\alpha_t)-H(\gamma_{Z,t}))\cdot A_{t,1}\cdot n_t\pm o(n)}.\) (22)

Then, we compute the first quantity, which does not exceed the number of \((I,J,K,\hat{K})\) where _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\), \(\hat{K}\in K\), and \(Z_\hat{K}\) is compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_. (We dropped the condition of having correct level-\(\ell\) complete split distributions \(\{\xi_{Z,t}\}_t\) and got an overestimation.)

First, the number of block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\) is \(N_\alpha\). Then, for each such block triple, we count the number of \(Z_\hat{K}\in Z_K\) that is compatible with it. If we fix some _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_, then we also have fixed the values of _S<sub>t,i,j,k</sub>_ for all _t,i,j,k_. Then it is not difficult to see that the following condition is equivalent to the condition for \(Z_\hat{K}\) being compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_:

**Definition 6.14** (Compatibility’)**.** For level-\((\ell-1)\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ consistent with \(\{\alpha_t\}_{t\in[s^\prime]}\), a level-1 block \(Z_\hat{K}\in Z_K\) is compatible with _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ if

• For every _t_ and every \((i',j',k')\in\mathbb{Z}_{\ge 0}^3\cap[0,i_t]\times[0,j_t]\times[0,k_t]\) with \(i'+j'+k'=2^{\ell-1}\), \(i'=0\) or \(j'=0\), there is \(\text{split}(\hat{K},S_{t,i^\prime,j^\prime,k^\prime})=\beta_{Z,t,i^\prime,j^\prime,k^\prime}\). (This is exactly Item 1 in Definition 6.9).<tbc>

• For every _t,k_, let \(S_{t,+,+,k}:=\bigcup_{i>0,j>0}S_{t,i,j,k}\). Then \(\text{split}(\hat{K},S_{t,+,+,k})=\overline{\beta_{Z,t,+,+,k}}\).

In this definition, there are constraints on the complete split distributions of \(\hat{K}\) on some disjoint subsets of level-\((\ell-1)\) positions, i.e., subsets of \(\big[2\sum_tA_{t,1}n_t\big]\). Therefore, we can count the number of valid sub sequences of \(\hat{K}\) for each of these subsets of indices, and multiply them together to get the number of valid \(\hat{K}\). For every _t_ and every \((i',j',k')\in\mathbb{Z}_{\ge 0}^3\cap[0,i_t]\times[0,j_t]\times[0,k_t]\) where \(i'+j'+k'=2^{\ell-1}\) with \(i'=0\) or \(j'=0\), we require that \(\text{split}(\hat{K},S_{t,i^\prime,j^\prime,k^\prime})=\beta_{Z,t,i^\prime,j^\prime,k^\prime}\), so the number of possibilities of \(\hat{K}\) on the subset of indices \(S_{t,i^\prime,j^\prime,k^\prime}\) is<tbc>

\(2^{H(\beta_{Z,t,i^\prime,j^\prime,k^\prime})\cdot|S_{t,i^\prime,j^\prime,k^\prime}|\pm o(n)}=2^{H(\beta_{Z,t,i^\prime,j^\prime,k^\prime})\cdot(\alpha_t(i^\prime,j^\prime,k^\prime)+\alpha_t(i_t-i^\prime,j_t-j^\prime,k_t-k^\prime))\cdot A_{t,1}n_t\pm o(n)}.\)

