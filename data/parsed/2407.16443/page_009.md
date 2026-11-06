Thus, from (29) and since \(H(\phi)=H(\phi')\) we get that the average length of the new code _C_ obtained satisfies

\(\mathbb{E}[C]\le H(\phi)+2-\phi_\ell\left(2-log_2\phi_\ell-\lceil-log_2\phi_\ell\rceil\right)\)<br> \(-\phi_k\left(2-log_2\phi_k-\lceil-log_2\phi_k\rceil\right)\)<br> \(-\sum_{i=\ell}^{k-1}min(\phi_i,\phi_{i+1})+\phi_\ell+\phi_k.\)

3) \(\ell=1\) and _k\<m_: then \(\phi=(\phi_1,\dots,\phi_k,0,\dots,0)\) and we have to create the leaves for the symbols _s_<sub>_k_+1</sub>_,...,s<sub>n</sub>_. Therefore, proceeding similarly to case 2) we get that

\(\mathbb{E}[C]\le H(\phi)+2-\phi_\ell\left(2-log_2\phi_\ell-\lceil-log_2\phi_\ell\rceil\right)\)<br> \(-\phi_k\left(2-log_2\phi_k-\lceil-log_2\phi_k\rceil\right)\)<br> \(-\sum_{i=\ell}^{k-1}min(\phi_i,\phi_{i+1})+\phi_k\)<br> \(<H(\phi)+2-\phi_\ell\left(2-log_2\phi_\ell-\lceil-log_2\phi_\ell\rceil\right)\)<br> \(-\phi_k\left(2-log_2\phi_k-\lceil-log_2\phi_k\rceil\right)\)<br> \(-\sum_{i=\ell}^{k-1}min(\phi_i,\phi_{i+1})+\phi_\ell+\phi_k.\)

4) \(\ell>1\) and _k=m_: then \(\phi=(0,\dots,0,\phi_\ell,\dots,\phi_m)\) and we have to create the leaves for the symbols \(s_1,\dots,s_{\ell-1}\). Therefore, again proceeding similarly to case 2) we get a new code _C_ with

\(\mathbb{E}[C]\le H(\phi)+2-\phi_\ell\left(2-log_2\phi_\ell-\lceil-log_2\phi_\ell\rceil\right)\)<br> \(-\phi_k\left(2-log_2\phi_k-\lceil-log_2\phi_k\rceil\right)\)<br> \(-\sum_{i=\ell}^{k-1}min(\phi_i,\phi_{i+1})+\phi_\ell\)

\(<H(\phi)+2-\phi_\ell\left(2-log_2\phi_\ell-\lceil-log_2\phi_\ell\rceil\right)\)<br> \(-\phi_k\left(2-log_2\phi_k-\lceil-log_2\phi_k\rceil\right)\)<br> \(-\sum_{i=\ell}^{k-1}min(\phi_i,\phi_{i+1})+\phi_\ell+\phi_k.\)

We have proved Theorem 3 under the hypothesis that the probability distribution \(\phi=(\phi_1,\dots,\phi_m)\) is non-dyadic. One of the referees suggested the following way to extend Theorem 3 also to dyadic distributions.

**Corollary 4.1.** _For any dyadic probability distribution_ \(\phi=(\phi_1,\dots,\phi_m)\) _on the symbols_ \(s_1\prec\cdots\prec s_m\)_, we can construct in linear time an alphabetic code C with_

\(\mathbb{E}[C]\le H(\phi)+2-\phi_1\left(2-log_2\phi_1-\lceil-log_2\phi_1\rceil\right)\)<br> \(-\phi_m\left(2-log_2\phi_m-\lceil-log_2\phi_m\rceil\right)-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1})\)<br> (30)<br> \(=H(\phi)+2-2\phi_1-2\phi_m-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1}).\) (31)

_Proof._ Let \(m\ge 4\). For a given dyadic probability distribution \(\phi=(\phi_1,\dots,\phi_m)\), let us define

\(\hat{\phi}=(\hat{\phi}_1,\hat{\phi}_2,\hat{\phi}_3\dots,\hat{\phi}_m)=(\phi_1,\phi_2-\epsilon,\phi_3+\epsilon,\phi_4,\dots,\phi_m)\) (32)

for a sufficiently small \(\epsilon>0\). Since \(\hat{\phi}\) is a non-dyadic probability distribution, we obtain from Theorem 3 that we can construct in linear time an alphabetic code _C_ with

\(\mathbb{E}[C]\le H(\hat{\phi})+2-\hat{\phi}_1\left(2-log_2\hat{\phi}_1-\lceil-log_2\hat{\phi}_1\rceil\right)\)<br> \(-\hat{\phi}_m\left(2-log_2\hat{\phi}_m-\lceil-log_2\hat{\phi}_m\rceil\right)-\sum_{i=1}^{m-1}min(\hat{\phi}_i,\hat{\phi}_{i+1})\)<br> \(\le H(\hat{\phi})+2-\phi_1\left(2-log_2\phi_1-\lceil-log_2\phi_1\rceil\right)\)<br> \(-\phi_m\left(2-log_2\phi_m-\lceil-log_2\phi_m\rceil\right)\)<br> \(-min(\phi_1,\phi_2-\epsilon)-min(\phi_2-\epsilon,\phi_3+\epsilon)\)<br> \(-min(\phi_3+\epsilon,\phi_4)-\sum_{i=4}^{m-1}min(\phi_i,\phi_{i+1}).\)

Since the Shannon entropy \(H(\cdot)\) and the operator \(min(\cdot,\cdot)\) are continuous functions for \(\epsilon>0\), by letting \(\epsilon\rightarrow 0\) we obtain that

\(\mathbb{E}[C]\le H(\phi)+2-\phi_1\left(2-log_2\phi_1-\lceil-log_2\phi_1\rceil\right)\)<br> \(-\phi_m\left(2-log_2\phi_m-\lceil-log_2\phi_m\rceil\right)-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1}).\)

The probability distribution \(\hat{\phi}\) is not equal to \(\phi\) for \(\epsilon>0\). However, the code tree constructed for \(\hat{\phi}\) can be used for \(\phi\), provided that \(\epsilon>0\) is sufficiently small.

We remark that the bounds (20) and (30) are not comparable, in the sense that there are dyadic probability distributions \(\phi\) for which (20) is better than (30), and probability distributions \(\phi\) for which it holds the opposite. For instance, if a

SL T
SL Sk Sk T'

Figure 3. The figure shows the insertion of the subtrees _T_ and \(T'\), with leaves \(s_1,\dots,s_{\ell-1}\) and _s_<sub>_k_+1</sub>_,...,s<sub>n</sub>_, respectively.

