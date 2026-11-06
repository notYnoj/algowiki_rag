node in \(i_s\times[1..(n'+1)]\) and a node in \(i_r\times[1..(n'+1)]\). Therefore, we obtain

\(dist_\tilde{G}(\bar{u},\bar{v})=max\big\{dist_{\tilde{G}_{\backslash s}}(\bar{u},\bar{v}),max_{\bar{w}\in i_s\times[1..(n'+1)]\bar{z}\in i_r\times[1..(n'+1)]}\big\{dist_\tilde{G}(\bar{u},\bar{w})+dist_\tilde{G}(\bar{w},\bar{z})+dist_\tilde{G}(\bar{z},\bar{v})\big\}\big\}.\)

These computation can be done by taking the maximum between outputs of the \((w,F_{\backslash s},F')\)-LRBBD instance, and a max-plus product between three matrices. The entries of these matrices can be retrieve from outputs of the other three LRBBD instances at our disposal. Note that the matrices have shape \((n'+1)\times(n'+1)\), \((n'+1)\times(n'+1)\) and \((n'+1)\times(n_r+1)\) so that the multiplications require \(\mathcal{O}(T_{MUL}(n',n',n))\) time.

As before, if the diameter is at most \(\mathcal{O}(n')\), we have that the matrices are monotone and have entries bounded by \(\mathcal{O}(n')\). Thus, we may compute the necessary matrix products in time \(\mathcal{O}(T_{MonMUL}(n',n',n,n'))\).

## 5 Reduction from Spine Edit Distance to APSP

In this section, we focus on proving Main Theorem 3.

**Main Theorem 3.** _Suppose there exists an algorithm computing the min-plus product of two_ \(m\times m\) _matrices in time_ T<sub>_MUL_</sub>(_m). Then, there is an algorithm for SED running in time_ O(T<sub>_MUL_</sub>(_n_)+_n_<sup>2+_o_(1)</sup>)_, where_ \(n=max(|F|,|F'|)\).

Similar to the previous one, we assume that there exists an algorithm computing the min/max-plus product of two \(m\times m\) matrices in time T<sub>MUL</sub>(_m_). We use T<sub>MUL</sub>(_a,b,c_) to the denote the time required to multiple an \(a\times b\) matrix and a \(b\times c\) matrix. As in Section 4, we describe our algorithm for general weighted tree edit distance instances, describing modifications for the unweighted case where necessary. To this end, recall that we use T<sub>MonMUL</sub>(_a,b,c,d_) to denote the time required to multiply an \(a\times b\) matrix with a \(b\times c\) matrix where both matrices have entries bounded by _d_ and the latter matrix is row or column-monotone.

To formulate an algorithm for SED, we assume that **F** and \(F'\) are trees. If they are not, we add virtual roots _t_ and \(t'\), each labeled with a unique symbol, and include these in **S** and \(S'\) respectively. This allows us to assume that the first nodes in **S** and \(S'\) correspond to the first nodes in the pre-order traversals of **F** and \(F'\), respectively. For such new roots, we set \(\text{sim}(\text{sub}(t),\text{sub}(v'))=-\infty\) for all \(v'\in F'\backslash\{t'\}\), even in the unweighted case, and similarly for \(\text{sim}(\text{sub}(v),\text{sub}(t'))\). This adjustment will not affect the algorithm we discuss, as these similarities only appear in the first column and row of some matrices we will work with. It is not difficult to see that we can compute the min/max-plus product of such matrices, in the same time as there would not be such column / row. Moreover, note that the solutions for SED on the original forests form a subset of the solutions on the new trees.

**Definition 5.1.** _Given two forests_ \(F,F'\) _and four nodes_ \(s,q\in S,s',q'\in S'\) _such that s\<q and_ \(s'<q'\)_, set_

\(B_i^\perp(s,s',q,q'):=B^\perp(\text{l}(s),\text{l}(s'),\text{l}(q),\text{l}(q')),B_i^\top(s,s',q,q'):=B^\top(\text{l}(s),\text{l}(s'),\text{l}(q),\text{l}(q')),\)<br> \(B_r^\perp(s,s',q,q'):=B^\top(\text{r}(q),\text{r}(q'),\text{r}(s),\text{r}(s')),B_r^\top(s,s',q,q'):=B^\perp(\text{r}(q),\text{r}(q'),\text{r}(s),\text{r}(s')).\)

We can interpret these sets as follows. Consider the set \([1..(2|F|+1)]\times[1..(2|F'|+1)]\). The sets \(B_i^\perp(s,s',q,q')\) and \(B_i^\top(s,s',q,q')\) are the lower left and upper right border of the subrectangle \([\text{l}(s)..\text{l}(q)]\times[\text{l}(s')..\text{l}(q')]\). On the other hand, \(B_r^\perp(s,s',q,q')\) and \(B_r^\top(s,s',q,q')\) are the upper right and lower left border of the subrectangle \([\text{r}(q)..\text{r}(s)]\times[\text{r}(q')..\text{r}(s')]\).

\(\blacktriangleleft\) **Main Theorem 3.** _Suppose there exists an algorithm computing the min-plus product of two_ \(m\times m\) _matrices in time_ T<sub>_MUL_</sub>(_m). Then, there is an algorithm for SED running in time_ O(T<sub>_MUL_</sub>(_n_)+_n_<sup>2+_o_(1)</sup>)_, where_ \(n=max(|F|,|F'|)\).

