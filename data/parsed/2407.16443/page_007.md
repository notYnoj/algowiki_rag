From Lemma 2, the code _C_ can be constructed in _O(m_) time.

Using the additional hypothesis that \(\phi\) is a dyadic distribution we have that \(\lceil-log_2\phi_i\rceil=-log_2\phi_i\) for each _i_=1_,...,m_. Therefore, the average length of the alphabetic code _C_ with lengths _L_ is

\(\mathbb{E}[C]\le\sum_{i=1}^m\phi_i\ell_i\)<br>
\(=\phi_1\left(-log_2\phi_1\right)+\phi_m\left(-log_2\phi_m\right)\)<br>
\(+\sum_{i=2}^{m-1}\phi_i\left(-log_2\phi_i+1\right)\)<br>
\(=-\sum_{i=1}^m\phi_ilog_2\phi_i+\sum_{i=2}^{m-1}\phi_i\)<br>
\(=H(\phi)+1-\phi_1-\phi_m.\)

We now turn our attention to the general case of non-dyadic probability distributions \(\phi=(\phi_1,\dots,\phi_m)\).

Let us first consider the case in which \(\phi_1\) and \(\phi_m\) are positives. We also need the following property of the function `sum`.

**Lemma 3.** _Let_ \(\ell_1,\dots,\ell_m\) _be a sequence of positive integers, and let_ \(k\ge max_i\ell_i\)_. The function_ `sum` _on the list_ \(L=\langle f_1,f_2,\dots,f_{2m-1}\rangle=\langle\ell_1,k,\ell_2,k,\dots,k,\ell_m\rangle\) _of_ 2_m_-1 _elements satisfies the following inequality:_

\(\mathtt{sum}(L,2m-1)\le 2^{-\ell_1}+2^{-\ell_m}+2\sum_{i=2}^{m-1}2^{-\ell_i}.\) (21)

_Proof._ By the definition of number \(\alpha_i\) (see Definition 1), it holds that<tbc>

\(\alpha_2=min(f_1,f_2)=\ell_1,\)

<tbc>and<tbc>

\(\alpha_{2m-1}=min(f_{2m-2},f_{2m-1})=\ell_m.\)

<tbc>For each \(i\in\{3,5,\dots,2m-3\}\), it holds that<tbc>

\(\alpha_i=min(f_{i-1},f_i)=min(f_i,f_{i+1})=\alpha_{i+1}=\ell_\frac{i+1}{2}.\)

<tbc>By the definition of the function `sum`, for each index _i_ we have that

\(\mathtt{sum}(L,i)=\mathtt{trunc}(\alpha_i,\mathtt{sum}(L,i-1))+2^{-\alpha_i}\)<br>
\(\le\mathtt{sum}(L,i-1)+2^{-\alpha_i}.\)

Thus, noticing that `sum`(_L,_1)=0, we have that

\(\mathtt{sum}(L,2m-1)\le\sum_{i=2}^{2m-1}2^{-\alpha_i}\)<br>
\(=2^{-\ell_1}+2^{-\ell_m}+2\sum_{i=2}^{m-1}2^{-\ell_i}.\)

**Theorem 3.** _For any non-dyadic probability distribution_ \(\phi=(\phi_1,\dots,\phi_m)\) _on the symbols_ \(s_1\prec\cdots\prec s_m\) _with_ \(\phi_1,\phi_m>0\)_, we can construct in linear time an alphabetic code C with_

\(\mathbb{E}[C]\le H(\phi)+2-\phi_1\left(2-log_2\phi_1-\lceil-log_2\phi_1\rceil\right)\)

\(-\phi_m\left(2-log_2\phi_m-\lceil-log_2\phi_m\rceil\right)\)<br>
\(-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1})\) (22)

\(<H(\phi)+2-\phi_1-\phi_m-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1}).\) (23)

_Proof._ We first show that there exists an alphabetic code \(C'\) for the partially extended distribution<tbc>

\(\nu=(\nu_1,\nu_2,\dots,\nu_{2m-1})=(\phi_1,0,\dots,0,\phi_m),\)

<tbc>with average length upper bounded by

\(H(\phi)+2-\phi_1\left(2-log_2\phi_1-\lceil-log_2\phi_1\rceil\right)\)<br>
\(-\phi_m\left(2-log_2\phi_m-\lceil-log_2\phi_m\rceil\right).\) (24)

Successively, we will prune the binary tree representing \(C'\) by removing the additional _m_-1 leaves (corresponding to the _m_-1 null probabilities in \(\nu\)), thus reducing the quantity (24) to (22).

Let _k_ be an integer greater than \(max_{j:\phi_j>0}\lceil-log_2\phi_j\rceil+1\) (the value of _k_ will be chosen later, in order to satisfy necessary inequalities), and let \(L=\langle\ell_1,\dots,\ell_{2m-1}\rangle\) be the lengths of the codewords for the distribution \(\nu=(\phi_1,0,\dots,0,\phi_m)\), defined as follows:

\(\ell_i=\left\{\begin{array}{ c c }
k & \text{if}\nu_i=0, \\
\lceil-log_2\nu_i\rceil & \text{if}i=1\text{or}i=2m-1, \\
\lceil-log_2\nu_i\rceil+1 & \text{if}\nu_i>0.
\end{array}\right.\) (25)

From Lemma 3 we have that

\(\mathtt{sum}(L,2m-1)\le 2^{-\lceil-log_2\phi_1\rceil}+2^{-\lceil-log_2\phi_m\rceil}\)<br>
\(+2\sum_{i\neq 1,m:\phi_i>0}2^{-(\lceil-log_2\phi_i\rceil+1)}+2\sum_{i:\phi_i=0}2^{-k}\)<br>
\(=\sum_{i:\phi_i>0}2^{-\lceil-log_2\phi_i\rceil}+2\sum_{i:\phi_i=0}2^{-k}<1,\)

where the last inequality holds because \(\sum_{i:\phi_i>0}2^{-\lceil-log_2\phi_i\rceil}<1\) since \(\phi\) is _a non-dyadic_ distribution<sup>1</sup>, and we can choose a sufficiently large value for _k_.

By Theorem 1 there exists an alphabetic code with lengths \(\ell_i\) defined in (25), and from Lemma 2 we can construct a code \(C'\) in linear time. The average length of such a code satisfies

\(\mathbb{E}[C']\le\phi_1\lceil-log_2\phi_1\rceil+\phi_m\lceil-log_2\phi_m\rceil\)<br>
\(+\sum_{i\neq 1,m:\phi_i>0}\phi_i(\lceil-log_2\phi_i\rceil+1)\)<br>
\(\le\phi_1\lceil-log_2\phi_1\rceil+\phi_m\lceil-log_2\phi_m\rceil\)<br>
\(+\sum_{i\neq 1,m:\phi_i>0}\phi_i(-log_2\phi_i+2)\)<br>
\(\text{(since}\lceil x\rceil<x+1\)<br>
\(=-\phi_1(-log_2\phi_1+2-\lceil-log_2\phi_1\rceil)\)

<sup>1</sup>Notice that if the distribution is dyadic, this inequality might not hold. However, as we will see later the theorem can be extended to dyadic distributions.

