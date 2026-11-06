macro-tree and encoding of the node \(\varepsilon_i\) in the macro-mini tree. If \(\varepsilon_i\) is in the macro-tree, then the codeword for _a<sub>i</sub>_ is the codeword for \(\varepsilon_i\). Every codeword consists of up to three components and all components of a codeword are stored in our data structure. Hence, we can generate the codeword for any symbol in _O_(1) time.

## 8.2 Proof of Lemma 1

_Proof:_ We need to show that \(\sum_{t=1}^Wlog\frac{t}{max\left(w_{a_t}^{(t-1)},1\right)}\le W\cdot H+2W\). In this sum _t_ assumes all integer values between 1 and _W_ and \(w_{a_i}^{(\cdot)}\) assumes all integer values between 1 and _w<sub>i</sub>_. Therefore we have

\(\sum_{t=1}^Wlog\frac{t}{max\left(w_{a_t}^{(t-1)},1\right)}=\sum_{t=1}^Wlogt-\sum_{j=1}^n\sum_{i=1}^{w_j}logi\le\)<br>
\(\le WlogW-\sum_{j=1}^nw_j(logw_j-2)=WlogW-\sum_{j=1}^nw_jlogw_j+2\sum_{j=1}^nw_j=H\cdot W+2W\) (1)

The inequality in the second line follows from the fact that \(\sum_{j=1}^xlogj\le xlogx\) and \(\sum_{j=1}^xlogj\ge xlogx-2x\). The former inequality is obvious. For completeness, we prove the latter. \(\sum_{j=1}^xlogj=\sum_{i=0}^lL_i\) where<tbc>

\(L_i=(log(x/2^i)+log((x/2^i)-1)+\dots+log((x/2^{i+1})+1)\)

<tbc>and _l_=log_x_. Every term in _L<sub>i</sub>_ is larger than log(_x/_2<sup>_i_+1</sup>); there are _x/_2<sup>_i_+1</sup> terms in _L<sub>i</sub>_. Hence \(L_i\ge(x/2^{i+1})(logx-(i+1))\) and

\(\sum_{i=0}^lL_i\ge\left(\sum_{i=0}^l\frac{1}{2^{i+1}}\right)xlogx-\left(\sum_{i=0}^l\frac{i+1}{2^{i+1}}\right)x\ge xlogx-2x\)

because \(\sum_{i=0}^l\frac{i+1}{2^{i+1}}\le 2\).

## 8.3 Lemma 7: Splitting and Merging Mini-Trees

It remains to describe how to split a mini-tree _T<sub>m</sub>_ in less than _O_(log<sup>2</sup>_n_) time. We consider all nodes in _T<sub>m</sub>_ of height _h_=2loglog_n_. Each subtree with the root in a height-_h_ node has at most 2log<sup>2</sup>_n_ pseudo-leaves. By definition, the height of the tree is bounded by 3loglog_n+O_(1). Hence there are _f=O_(log_n_) nodes of height _h_. We insert the \(\lfloor f/2\rfloor\) leftmost nodes into a new _k_-neighbor tree \(T'_1\). In other words, we regard the nodes of height _h_ as leaves and insert them one-by-one into a new tree \(T'_1\). The tree _T_<sub>1</sub> is obtained from \(T'_1\): suppose that a height-_h_ node _u_ in _T<sub>m</sub>_ corresponds to a leaf _u<sub>l</sub>_ in \(T'_1\); we append the subtree rooted at _u_ in _T<sub>m</sub>_ to _u<sub>l</sub>_. Every leaf is inserted into \(T'_1\) in _O_((loglog_n_)<sup>2</sup>) time and we can append a sub-tree to the corresponding leaf in _O_(1) time. Hence the mini-tree _T_<sub>1</sub> is constructed in _O_(log_n_(loglog_n_)<sup>2</sup>) time. _T_<sub>1</sub> is a _k_-neighbor tree because it satisfies conditions (1)-(3) from Section 2: All leaves of \(T'_1\) have the same depth and all sub-trees appended to leaves of \(T'_1\) have the same height. Therefore all leaves of _T_<sub>1</sub> have the same depth. All nodes in \(T'_1\) satisfy conditions (2) and (3) because \(T'_1\) is a _k_-neighbor tree. We append subtrees<tbc>

