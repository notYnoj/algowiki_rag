<tbc>among binary sequences. Moreover, neither _w<sub>i</sub>_ is a prefix of _w_<sub>_i_-1</sub> nor _w_<sub>_i_-1</sub> is a prefix of _w<sub>i</sub>_.

Nakatsu \[25\] proved the following important result (an equivalent result was independently given by Yeung \[29\]).

**Theorem 1.** _\[25\] Let_ \(L=\langle\ell_1,\dots,\ell_m\rangle\) _be a list of integers, associated with the ordered symbols_ \(s_1\prec\cdots\prec s_m\)_. There exists an alphabetical code for which the codeword assigned to symbol s<sub>i</sub> has length_ \(\ell_i\)_, for each i_=1_,...,m, if and only if_ sum(_L,m)\<_1.

Nakatsu proved the sufficient part of Theorem 1 by showing that the first \(\ell_i\) digits of the binary representation of sum(_L,i_), for _i_=1_,...,m_, (under the hypothesis that sum(_L,m)\<_1) give the alphabetic code for the ordered set of symbols \(s_1\prec\cdots\prec s_m\). In the following Lemma 2 we show that an alphabetic code, whose existence is guaranteed by Theorem 1, can be constructed in time _O(m_). We first need the following technical result, whose proof is given in Appendix A.

**Lemma 1.** _Let_ \(L=\langle\ell_1,\dots,\ell_m\rangle\) _be a list of integers such that_ sum(_L,m)\<_1_, let i, j be integers such that_ \(1\le i<j\le m\)_, and let_ {sum(_L,i),_sum(_L,i_+1)_,...,_sum(_L,j_)} _be a subset of consecutive elements of_ {sum(_L,_1)_,...,_sum(_L,m_)}_. For each k=i,...,j_-1_, let t<sub>k</sub> be the smallest integer s for which the binary expansion of_ sum(_L,k_) _differs from the binary expansion of_ sum(_L,k_+1) _on the s<sup>th</sup> bit, and define_ \(t_{ij}=min_{i\le k<j}t_k\)_. Then, it holds that:_

1) \(t_{ij}=\lceil-log_2(\sum(L,i)\oplus\sum(L,j))\rceil,\) (13)

_where_ \(\sum(L,i)\oplus\sum(L,j)\) _is the numerical value whose binary expansion is the result of the XOR operation between the binary expansions of_ sum(_L,i_) _and_ sum(_L,j), and_<tbc>

2) _there exists an index_ \(z\in\{i,\dots,j-1\}\) _such that_ sum(_L,z)\<_trunc(_t<sub>ij</sub>,_sum(_L,i_))+2<sup>-_t<sub>ij</sub>_</sup> and \(\sum(L,z+1)\ge\text{\textit{trunc}}(t_{ij},\sum(L,i))+2^{-t_{ij}}\).

For completeness, we recall that the XOR \(\sum(L,i)\oplus\sum(L,j)\) is easily computable, in most programming languages, with a single built-in instruction. Armed with Lemma 1, we now prove our constructive result. To avoid overburdening the notation, when the pair of integers (_i,j_) in (13) is clear from the context, we will simply denote _t<sub>ij</sub>_ with _t_.

**Lemma 2.** _Let_ \(L=\langle\ell_1,\dots,\ell_m\rangle\) _be a list of integers, associated with the ordered symbols_ \(s_1\prec\cdots\prec s_m\)_. If_ sum(_L,m)\<_1_, then one can construct in O(m_) _time an alphabetic code C for which the codeword assigned to symbol s<sub>i</sub> has length at most_ \(min(\ell_i,m-1)\)_, for each i_=1_,...,m._

_Proof._ To prove the lemma, we design a _O(m_) time algorithm to construct the binary tree associated with the code _C_, that is, the binary tree whose root-to-leaves paths give the codewords of _C_.

It is useful to recall that Nakatsu \[25, Theorem 1\] showed that the code constructed by taking the first \(\ell_i\) bits of the binary expansion of sum(_L,i_) as the codeword associated to the symbol _s<sub>i</sub>_, for each _i_=1_,...,m_, is alphabetic. Our algorithm constructs the binary code tree by using a _subset_<tbc>

<tbc>of the first \(\ell_i\) bits of the binary expansion of sum(_L,i_), for each _i_=1_,...,m_. The algorithm builds the desired tree in a top-down fashion, proceeding by iterated bisections of the set

\(\mathcal{S}=\{\sum(L,1),\sum(L,2),\dots,\sum(L,m)\}.\) (14)

Initially, the root of the tree is associated to the whole set S. To perform the first bisection, we proceed as follows.

For each _a_=1_,...,m_-1, let _t<sub>a</sub>_ be the smallest integer for which the binary expansions of the pair sum(_L,a_) and sum(_L,a_+1) differ on the \(t_a^{th}\) bit, and let \(t=t_{1m}=min_{1\le a<m}t_a\). From Lemma 1, we have that \(t=\lceil-log_2(\sum(L,1)\oplus\sum(L,m))\rceil\). We now compute the index \(k\in\{1,\dots,m-1\}\) for which it holds that

\(\sum(L,k)<\text{\textit{trunc}}(t,\sum(L,1))+2^{-t}\) (15)

and

\(\sum(L,k+1)\ge\text{\textit{trunc}}(t,\sum(L,1))+2^{-t}.\) (16)

We associate the left child of the root to the subset<tbc>

\(\{\sum(L,1),\dots,\sum(L,k)\},\)

<tbc>and the right child of the root to the subset

\(\{\sum(L,k+1),\dots,\sum(L,m)\}.\)

By 2) of Lemma 1, both {sum(_L,_1)_,...,_sum(_L,k_)} and {sum(_L,k_+1)_,...,_sum(_L,m_)} are non empty. The subset {sum(_L,_1)_,...,_sum(_L,k_)} represents the nodes that are in the left subtree of the root. Moreover, by the definition of the function `trunc` and from (15) and (16), each numerical value \(\sum(\cdot,\cdot)\in\{\sum(L,1),\dots,\sum(L,k)\}\) has a binary expansion with 0 in the _t<sup>th</sup>_ position. Analogously, the subset {sum(_L,k_+1)_,...,_sum(_L,m_)} represents the nodes that are in the right subtree of the root and each value \(\sum(\cdot,\cdot)\in\{\sum(L,k+1),\dots,\sum(L,m)\}\) has a binary expansion with 1 in the _t<sup>th</sup>_ position. The algorithm proceeds recursively on the _left_ subset {sum(_L,_1)_,...,_sum(_L,k_)} and _right_ subset {sum(_L,k_+1)_,...,_sum(_L,m_)}. It stops when the cardinality of the subset is equal to 1, in such a case we have just a leaf, or when it is equal to 2, where we have a final subtree with two sibling leaves. The complete pseudo-code of the algorithm is presented in **Algorithm 2**.

The procedure presented above for the construction of the binary tree can be implemented to work in _O(m_) time and space, by exploiting a technique devised in \[7\]. In fact, the crucial operation in Line 9 of Algorithm 1 can be implemented in _O_(logmin(_s,j-s_)) time, where _s=k-i_+1, by first checking if sum(_L,r)\<_trunc(_t,_sum(_L,i_))+2<sup>-_t_</sup> with \(r=\lceil(j-1+i)/2\rceil\) to discover whether the index _k_ belongs to {_i,...,r_-1} or to {_r,...,j_-1}. Successively, we use an exponential search to find the interval in which the value _k_ is located, and, finally, a binary search in such interval to find _k_. More precisely, we proceed in the following way: if \(k\in\{i,\dots,r-1\}\), we check the validity of the inequality sum(_L,i_+2_<sup>v</sup>)\<_trunc(_t,_sum(_L,i_))+2<sup>-_t_</sup> in Line 9 for increasing values _v_=0,1,2,3_,..._, till we find the first value of _v_ that satisfies the inequality \(\sum(L,i+2^v)\ge\)<tbc>

