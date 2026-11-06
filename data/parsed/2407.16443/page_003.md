More importantly, we design a _O(m_) time algorithm to construct alphabetic codes of average length at most the right- hand side of (7). The _O(m_) time algorithm that we design will be instrumental in deriving the results on binary search trees of Section V. We derive further improvements to (5) in Section IV.

In Section V we turn our attention to binary search trees. Binary search trees have been extensively investigated (e.g., \[5\], \[21\], \[22\], \[26\]). Knuth \[17\] gave an _O(n_<sup>2</sup>) time and _O(n_<sup>2</sup>) space complexity algorithm to construct an optimum binary search tree, i.e., a binary search tree with minimum cost, as defined in (1). The quadratic complexity of the algorithm designed in \[17\] may be prohibitive in many applications, as Mehlhorn remarked in \[21\]. Therefore, Mehlhorn \[21\] proposed a linear time algorithm to construct a binary search tree for an arbitrary probability distribution<tbc>

\(\sigma=(\sigma_1,\dots,\sigma_{2n+1})=(p_0,q_1,p_1,q_2,\dots,q_n,p_n),\)

<tbc>where the _p<sub>i</sub>_’s are probabilities of unsuccessful searches and the _q<sub>i</sub>_’s are probabilities of successful searches, whose cost is not greater than<tbc>

\(H(\sigma)+1+\sum_{i=0}^np_i.\) (8)

<tbc>De Prisco and De Santis \[5\] proposed a different linear time algorithm for constructing binary search trees and they claimed an upper bound on their cost given by

\(H(\sigma)+1-p_0-p_n+p_{max},\) (9)

where _p_<sub>max</sub> is the maximum value among _p_<sub>0</sub>_,...,p<sub>n</sub>_. Unfortunately, the bound (9) does not hold in general, as pointed out in \[4\], \[19\].

In Section V we correct the analysis of the algorithm derived in \[5\], and we explicitly estimate the cost of the produced binary search trees. The simplest of our bounds states that the cost E\[_T_\] of the tree _T_ constructed by the algorithm of \[5\] is upper bounded by

\(\mathbb{E}[T]\le H(\sigma)+1+\sum_{i=0}^np_i-\big(p_0+p_n+\sum_{i=0}^{n-1}min(p_i,q_{i+1})\)<br>
\(+\sum_{i=1}^nmin(q_i,p_i)+\sum_{i=0}^{n-1}min(p_i,p_{i+1})\big)\)<br>
\(=H(\sigma)+1+\sum_{i=0}^np_i-\big(1-\sum_{i=0}^{n-1}\frac{|p_i-q_{i+1}|}{2}\)<br>
\(-\sum_{i=1}^n\frac{|q_i-p_i|}{2}+\sum_{i=0}^np_i-\sum_{i=0}^{n-1}\frac{|p_i-p_{i+1}|}{2}\big).\) (10)

It is apparent that (10) significantly improves the Melhorn bound (8). We derive additional and better upper bounds than (10) in Section V. Clearly, our results also represent upper limits on the cost of optimal binary search trees. The new bounds on the cost of binary search trees are crucially dependent on the new results on alphabetic codes that we derive in Section IV.

## IV. ON ALPHABETIC CODES

We first develop some useful machinery. Given a probability distribution \(\phi=(\phi_1,\dots,\phi_m)\), let us denote with<tbc>

\(\nu=(\nu_1,\dots,\nu_{2m-1})=(\phi_1,0,\phi_2,\dots,0,\phi_m)\)

<tbc>its _partially extended_ distribution, and with

\(\nu'=(\nu_1,\dots,\nu_{2m+1})=(0,\phi_1,0,\phi_2,\dots,0,\phi_m,0)\)

its _fully extended_ distribution.

We also need some auxiliary tools and results from Nakatsu \[25\].

**Definition 1.** \[25\] Let \(L=\langle\ell_1,\dots,\ell_m\rangle\) be a list of positive integers. For a binary fraction _x_ and integer \(i\ge 1\), let the function `trunc` be defined as

\(\mathtt{trunc}(i,x)=\frac{\left|2^ix\right|}{2^i}\) (11)

that is, `trunc`(_i,x_) is the fraction obtained by considering only the first _i_ bits in the binary representation of _x_.

Let \(\alpha_i=min(\ell_{i-1},\ell_i)\), for _i_=2_,...,m_. The recursive function `sum` is defined as

\(\mathtt{sum}(L,i)=\left\{\begin{array}{ c c }
\mathtt{trunc}(\alpha_i,\mathtt{sum}(L,i-1))+2^{-\alpha_i} & \text{if}i\ge 2, \\
0 & \text{if}i=1.
\end{array}\right.\) (12)

To better comprehend the functions `trunc` and `sum` defined above, let us work out a small numerical example. Let _L_={4,2,3,3} be a list of integers. We have \(\alpha_2=min(4,2)=2\), \(\alpha_3=min(2,3)=2\) and \(\alpha_4=min(3,3)=3\). Now, we can compute the value of `sum` for _L_. By definition `sum`(_L,_1)=0. It holds that

\(\mathtt{sum}(L,2)=\mathtt{trunc}(\alpha_2,\mathtt{sum}(L,1))+2^{-\alpha_2}\)<br>
\(=\mathtt{trunc}(2,0)+2^{-2}=2^{-2},\)

since `trunc`(2,0) takes the value whose binary expansion is the same of the first 2 bits of the binary representation of 0 (that are all 0’s). Similarly, we have

\(\mathtt{sum}(L,3)=\mathtt{trunc}(\alpha_3,\mathtt{sum}(L,2))+2^{-\alpha_3}\)<br>
\(=\mathtt{trunc}(2,2^{-2})+2^{-2}=2^{-2}+2^{-2}=2^{-1},\)

since `trunc`(2,2<sup>-2</sup>) takes the value whose binary expansion is the same of the first 2 bits of the binary representation of \(2^{-2}=\frac{1}{4}\), which correspond to the same value 2<sup>-2</sup> since the binary representation of \(\frac{1}{4}\) is \(0\frac{1}{2}+1\frac{1}{4}\). Finally, we have

\(\mathtt{sum}(L,4)=\mathtt{trunc}(\alpha_4,\mathtt{sum}(L,3))+2^{-\alpha_4}\)<br>
\(=\mathtt{trunc}(3,2^{-1})+2^{-3}=2^{-1}+2^{-3}.\)

Intuitively, when `sum`(_L,i)\<_1, one can see that `sum`(_L,i_) enjoys the property of being the smallest value strictly greater than `sum`(_L,i_-1) that differs from `sum`(_L,i_-1) on at least the \(\alpha_i^{th}\) bit of their binary expansion, where \(\alpha_i=min(\ell_{i-1},\ell_i)\). Thus, by denoting with _w<sub>i</sub>_ the first \(\ell_i\) bits of the binary expansion of `sum`(_L,i_) and with _w_<sub>_i_-1</sub> the first \(\ell_{i-1}\) bits of the binary expansion of `sum`(_L,i_-1), the property ensures that _w_<sub>_i_-1</sub> _comes_ before _w<sub>i</sub>_ in the standard alphabetic order<tbc>

