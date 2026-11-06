bound for the CT-MSeq problem. In section 5, we present our _O(n_<sup>6</sup>)-time solution and _O(n_<sup>2</sup>)-time solution for the CT-LCS problem in the case of general ordered alphabets and binary alphabets, respectively, and quadratic conditional lower bounds for the CT-LCS problem. We conclude in Section 6.

A preliminary version of this paper appeared in \[18\]. The new materials in this full version are the following:

• Result (1): _O(nm_)-time CT-MSeq algorithm for binary alphabets.<tbc>

• Result (2): \(O((nm)^{1-\epsilon})\)-time conditional lower bound for the CT-MSeq problem.<tbc>

• Result (5): \(O(n^{2-\epsilon})\)-time conditional lower bound for the CT-LCS problem.

## 2 Preliminaries

### 2.1 Basic notations: strings and vectors

For any positive integer _i_, we define a set \[_i_\]={1_,...,i_} of _i_ integers. Let \(\Sigma\) be an _ordered alphabet_ of size \(\sigma\). For simplicity, let \(\Sigma=\{0,\dots,\sigma-1\}\). An element of \(\Sigma\) is called a _character_. A sequence of characters is called a _string_. The _length_ of string _S_ is denoted by |_S_|. The empty string \(\varepsilon\) is the string of length 0. If _S=XYZ_, then _X_, _Y_ , and _Z_ are respectively called a _prefix_, _substring_, and _suffix_ of _S_. For a string _S_, _S_\[_i_\] denotes the _i_-th character of _S_ for each _i_ with \(1\le i\le|S|\). For each _i,j_ with \(1\le i\le j\le|S|\), _S_\[_i..j_\] denotes the substring of _S_ that begins at position _i_ and ends at position _j_. For convenience, let \(S[i..j]=\varepsilon\) for _i\>j_. We write \(\mathsf{min}(S)=\mathsf{min}\{S[i]|i\in[n]\}\) for the minimum character contained in the string _S_. For any \(0\le m\le n\), let \(\mathcal{I}_m^n\) be the set consisting of all _subscript sequence_ \(I=(i_1,\dots,i_m)\in[n]^m\) in ascending order satisfying \(1\le i_1<\cdots<i_m\le n\). For subscript sequence \(I=(i_1,\dots,i_m)\in\mathcal{I}_m^n\), we denote by \(S_I=\langle S[i_1],\dots,S[i_m]\rangle\) the _subsequence_ of _S_ corresponding to _I_. For a subscript sequence _I_ and its elements \(i_s,i_t\in I\) with \(i_s\le i_t\), _I_\[_i<sub>s</sub>:i<sub>t</sub>_\] denotes the substring of _I_ that starts with _i<sub>s</sub>_ and ends with _i<sub>t</sub>_. For a sequence _T_<sub>1</sub>_,...,T<sub>k</sub>_ of strings, we define \(\prod_{i=1}^kT_i=T_1\cdots T_k\).

For a _d_-dimensional binary vector \(\alpha\in\{0,1\}^d\) and an integer \(1\le t\le d\), the _t_-th element in \(\alpha\) is denoted by \(\alpha[t]\). For two vectors \(\alpha,\beta\in\{0,1\}^d\), they are said to be _orthogonal_ if \(\sum_{i=1}^d\alpha[i]\beta[i]=0\) holds.

### 2.2 Subsequence matching and LCS under Cartesian-tree equivalence

For a string _S_, let min\_id(_S_) denote the least index _i_ such that _S_\[_i_\] is the smallest element in _S_.

**Definition 1** (Cartesian-tree) The _Cartesian-tree_ of a string _S_, denoted by CT(_S_), is the ordered binary tree recursively defined as follows: If \(S=\varepsilon\), then CT(_S_) is an empty tree, and otherwise, CT(_S_) is the tree rooted at _i_=min\_id(_S_) such that the left subtree of _i_ is CT(_S_\[1_..i_-1\]) and the right subtree of _i_ is CT(_S_\[_i_+1..|_S_|\]).

