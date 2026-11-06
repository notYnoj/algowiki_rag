because

\(\text{split}(\hat{K},S_{*,*,k})=\frac{1}{\sum_{i,j\ge 0}\alpha(i,j,k)}\sum_{i,j\ge 0}\alpha(i,j,k)\cdot\text{split}(\hat{K},S_{i,j,k})\)<br>
\(=\frac{1}{\sum_{i,j\ge 0}\alpha(i,j,k)}\left(\sum_{i,j>0}\alpha(i,j,k)\cdot\text{split}(\hat{K},S_{i,j,k})+\sum_{i=0\text{or}j=0}\alpha(i,j,k)\cdot\text{split}(\hat{K},S_{i,j,k})\right)\)<br>
\(=\frac{1}{\sum_{i,j\ge 0}\alpha(i,j,k)}\left(\sum_{i,j>0}\alpha(i,j,k)\cdot\text{split}(\hat{K},S_{+,+,k})+\sum_{i=0\text{or}j=0}\alpha(i,j,k)\cdot\beta_{Z,i,j,k}\right)\)<br>
\(=\frac{1}{\sum_{i,j\ge 0}\alpha(i,j,k)}\left(\sum_{i,j>0}\alpha(i,j,k)\cdot\overline{\beta_{Z,+,+,k}}+\sum_{i=0\text{or}j=0}\alpha(i,j,k)\cdot\beta_{Z,i,j,k}\right)\)<br>
\(=\frac{1}{\sum_{i,j\ge 0}\alpha(i,j,k)}\sum_{i,j\ge 0}\alpha(i,j,k)\cdot\beta_{Z,i,j,k}=\overline{\beta_{Z,*,*,k}}.\)

Similarly, Item 1 and Item 2 together imply the second condition in Definition 5.15. Therefore, Definition 5.15 is an equivalent definition of compatibility.

In Definition 5.15, there are constraints on the complete split distributions of \(\hat{K}\) on some disjoint subsets of \[_A_<sub>1</sub>_n_\]. Therefore, we can count the number of valid subsequences of \(\hat{K}\) for each of these subsets of indices, and multiply them together. For every \((i,j,k)\in\mathbb{Z}_{\ge 0}^3\) where \(i+j+k=2^\ell\) while _i_=0 or _j_=0, we require that \(\text{split}(\hat{K},S_{i,j,k})=\beta_{Z,i,j,k}\), so the number of possibilities of \(\hat{K}\) on the subset of indices _S<sub>i,j,k</sub>_ is \(2^{H(\beta_{Z,i,j,k})\cdot|S_{i,j,k}|\pm o(n)}=2^{H(\beta_{Z,i,j,k})\cdot\alpha(i,j,k)\cdot A_1n\pm o(n)}\). For every _k_, we require that \(\text{split}(\hat{K},S_{+,+,k})=\overline{\beta_{Z,+,+,k}}\), so the number of possibilities of \(\hat{K}\) on _S_<sub>+,+_,k_</sub> is \(2^{H(\overline{\beta_{Z,+,+,k}})\cdot|S_{+,+,k}|\pm o(n)}=2^{H(\overline{\beta_{Z,+,+,k}})\cdot\alpha(+,+,k)\cdot A_1n\pm o(n)}\). Overall, the number of possible compatible \(\hat{K}\), multiplied by the number of block triples _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_, is

\(N_\alpha\cdot\prod_{i,j,ki=0\text{or}j=0}2^{H(\overline{\beta_{Z,i,j,k}})\cdot\alpha(i,j,k)\cdot A_1n\pm o(n)}\cdot\prod_k2^{H(\overline{\beta_{Z,+,+,k}})\cdot\alpha(+,+,k)\cdot A_1n\pm o(n)}=2^{(H(\alpha)+\lambda_Z)\cdot A_1n\pm o(n)}.\) (10)

Finally, as mentioned, _p_<sub>comp</sub> is the ratio between (10) and (9), so

\(p_\text{comp}=\left(2^{(H(\alpha)+\lambda_Z)\cdot A_1n\pm o(n)}\right)\big/\left(2^{(H(\overline{\beta_{Z,*,*,*}})+H(\alpha)-H(\alpha_Z))\cdot A_1\cdot n\pm o(n)}\right)=2^{\left(\lambda_Z-H(\overline{\beta_{Z,*,*,*}})+H(\alpha_Z)\right)A_1\cdot n\pm o(n)}\)

as desired.

**Claim 5.16.** _For every_ \(b\in B\)_, every level-_\(\ell\) _block triple X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub> consistent with_ \(\alpha\)_, and for each typical_ \(Z_\hat{K}\in Z_K\)_, the probability that_ \(Z_\hat{K}\) _is compatible with multiple triples in_ T<sub>comp</sub> _is at most_

\(\frac{N_\alpha\cdot p_\text{comp}}{N_\text{BZ}\cdot M_0},\)

_conditioned on h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b._

_Proof._ By the definition of _p_comp, the total number of level-\(\ell\) block triples \(X_{I^\prime} Y_{J^\prime} Z_K\) that is compatible with \(Z_\hat{K}\) is \(\frac{N_\alpha}{N_\text{BZ}}\cdot p_\text{comp}\). For each \(X_{I^\prime} Y_{J^\prime} Z_K\) different from _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_, the probability that \(X_{I^\prime} Y_{J^\prime} Z_K\) is mapped to<tbc>

