**if** _i=j_ **then**<br>
Construct the leaf v associated with symbol s<sub>i</sub>.<br>
**return** v<br>
**else if** i+1=j **then**<br>
Construct a node v whose left child is the leaf s<sub>i</sub><br>
and whose right child is the leaf s<sub>j</sub>.<br>
**return** v<br>
**else**<br>
\(t=\lceil-log_2(\text{sum}(L,i)\oplus\text{sum}(L,j))\rceil\)<br>
Let \(k\in\{i,\dots,j-1\}\) be the index such that sum(L,k)<trunc(t,sum(L,i))+2<sup>-_t_</sup> and \(\text{sum}(L,k+1)\ge\text{trunc}(t,\text{sum}(L,i))+2^{-t}\).<br>
_l_ = SubTree(i,k)<br>
_r_ = SubTree(k+1,j)<br>
Construct a node v whose left child is the tree l<br>
and whose right child is the tree r.<br>
**return** v

**Input:** The list of lengths \(L=\langle\ell_1,\dots,\ell_m\rangle\)<br>
**Output:** An alphabetic code tree with codeword<br>
lengths \(\ell'_i\le min(\ell_i,m-1)\), for each<br>
_i_=1_,...,m_.<br>
Compute sum(L,i_) for each i=1_,...,n_.<br>
**return** SubTree(1,m)

`trunc`(_t,_sum(L,i_))+2<sup>-_t_</sup>. After log_s_ step we shall have located the value of _k_ we seek within an interval of size at most 2_s_. A successive binary search will exactly determine the value of _k_. All together, this procedure takes _O_(log_s_) steps. Similarly, if \(k\in\{r,\dots,j-1\}\), we apply the same procedure with the caveat that we start the exponential search from the right-end of the interval {_r,...,j_-1}. In this way, the procedure will take _O_(log(_j-s_)) time. Putting the two cases together, the whole operation takes _O_(logmin(_s,j-s_)) time.

Therefore, by denoting with _T(m_) the number of operations performed by the algorithm to construct the tree with _m_ leaves, because of Line 9, 10, and 11, we have that

\(T(m)\le max_{1\le k\le m-1}\{T(m-k)+T(k)+\alpha log_2min(k,m-k)+\beta\}\)<br>
\(=max_{1\le k\le m/2}\{T(m-k)+T(k)+\alpha log_2k+\beta\},\) (17)

for suitable constant values \(\alpha\) and \(\beta\).

One can see that the right-hand-side of (17) grows at most linearly with _m_ (e.g., Theorem 11, p. 185 of \[23\]); therefore the algorithm ConstructTree(_L_) requires total time _O(m_).

The tree produced by algorithm ConstructTree(_L_) is alphabetic by construction since the recursive bisections of the set<tbc>

\(\{\text{sum}(L,1),\text{sum}(L,2),\dots,\text{sum}(L,m)\}\)

<tbc>preserves the symbol order \(s_1\prec\cdots\prec s_m\). What is left to prove is that the procedure constructs a tree whose root-to- leaves paths (i.e., codewords) have length \(\ell'_a\le min(\ell_a,m-1)\), for each _a_=1_,...,m_.

The inequality \(\ell'_a\le m-1\) holds because the constructed binary tree is _full_, that is, each node internal node of the tree has two children. This is due to 2) of Lemma 1 and Line 9,10 and 11 of **Algorithm 1**.

We now prove that \(\ell'_a\le\ell_a\), for each _a_=1_,...,m_. Consider first the cases \(a\in\{2,\dots,m-1\}\). By definition of `sum`, we have that

\(\text{sum}(L,a)=\text{trunc}(\alpha_a,\text{sum}(L,a-1))+2^{-\alpha_a},\) (18)

where \(\alpha_a=min(\ell_{a-1},\ell_a)\). Therefore, since `trunc`(_b,x_) is the binary fraction one gets by considering only the first _b_ bits of the binary expression of _x_ (cfr. (11)), from (18) one obtains that the binary expansion of `sum`(_L,a_) differs from the binary expansion of `sum`(_L,a_-1) on at least the \(\alpha_a^{th}\) bit. Because of Line 9,10 and 11 of **Algorithm 1**, this implies that after at most \(\alpha_a\) bisection steps the value of `sum`(_L,a_) can no longer be in the same subset of `sum`(_L,a_-1). By symmetry, after at most \(\alpha_{a+1}\) steps the value `sum`(_L,a_) can no longer be in the same subset of `sum`(_L,a_+1). All together, after at most \(max(\alpha_a,\alpha_{a+1})\) bisection steps the value `sum`(_L,a_) does not belong to the same subset of either `sum`(_L,a_-1) or `sum`(_L,a_+1), that is, `sum`(_L,a_) must correspond to a leaf in the code-tree. Therefore, the corresponding root-to-leaves path has length

\(\ell'_a\le max(\alpha_a,\alpha_{a+1})=max(min(\ell_{a-1},\ell_a),min(\ell_a,\ell_{a+1}))\)<br>
\(\le\ell_a.\)

Analogously, for _a_=1 it holds that

\(\ell'_1\le\alpha_2=min(\ell_1,\ell_2)\le\ell_1,\)

and for _a=m_ it holds that

\(\ell'_m\le\alpha_m=min(\ell_{m-1},\ell_m)\le\ell_m.\)

Figure 1 shows the alphabetic trees produced on the list of lengths \(L=\langle 6,6,5,2,9,9,8,6,3,2\rangle\), by taking the first \(\ell_i\) bits of the binary expansion of `sum`(_L,i_) (as done by Nakatsu \[25\]) and by the application of our linear time algorithm, respectively. As an example, one can see how the codeword associated with the symbol _s_<sub>7</sub> in our code tree, which is 10001, is only a subsequence of the codeword associated with the symbol _s_<sub>7</sub> in the first tree, that is <u>10000001</u>, where the underlined bits are those that correspond to the codeword of our code tree.

Before presenting our results on the length of the optimal alphabetic code that improves upon the upper bound (5), we briefly show a problematic issue in the analysis of the bound (5) claimed in \[4\].

**Remark 1.** In the proof of the upper bound (5) presented in \[4\], the authors proceed in the following way: Starting from an input probability distribution \(\phi=(\phi_1,\dots,\phi_m)\), they first consider the fully extended distribution \(\nu'=\)<tbc>

**Algorithm 1:** SubTree(_i,j_)

**Algorithm 2:** ConstructTree(_L_)

